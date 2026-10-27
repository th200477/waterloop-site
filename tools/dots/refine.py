import numpy as np, json
from PIL import Image
from scipy import ndimage as ndi
from scipy.optimize import minimize
A=np.array(Image.open('../wlp-site/assets/c6e5b358e170921460712e745c51741bbc594628.png').convert('RGBA'))[...,3].astype(float)/255
H,W=A.shape
acc=[list(c) for c in np.load('acc.npy')]
def cov(x,y,r,x0,y0,x1,y1):
    ys,xs=np.mgrid[y0:y1,x0:x1]+0.5
    return np.clip(r-np.hypot(xs-x,ys-y)+0.5,0,1)
def win(x,y,r,p=3):
    return int(max(0,x-r-p)),int(max(0,y-r-p)),int(min(W,x+r+p+1)),int(min(H,y+r+p+1))
# spatial index
def build():
    g={}
    for i,(x,y,r) in enumerate(acc): g.setdefault((int(x//60),int(y//60)),[]).append(i)
    return g
def others(i,x0,y0,x1,y1,g):
    o=np.zeros((y1-y0,x1-x0)); x,y,_=acc[i]
    for a in (-1,0,1):
        for b in (-1,0,1):
            for j in g.get((int(x//60)+a,int(y//60)+b),[]):
                if j==i: continue
                cx,cy,cr=acc[j]
                if cx+cr<x0 or cx-cr>x1 or cy+cr<y0 or cy-cr>y1: continue
                o=np.maximum(o,cov(cx,cy,cr,x0,y0,x1,y1))
    return o
def render():
    img=np.zeros((H,W))
    for x,y,r in acc:
        x0,y0,x1,y1=win(x,y,r,2); img[y0:y1,x0:x1]=np.maximum(img[y0:y1,x0:x1],cov(x,y,r,x0,y0,x1,y1))
    return img
for it in range(3):
    g=build()
    for i in range(len(acc)):
        x,y,r=acc[i]; x0,y0,x1,y1=win(x,y,r,3)
        o=others(i,x0,y0,x1,y1,g); t=A[y0:y1,x0:x1]
        f=lambda p: ((np.maximum(o,cov(p[0],p[1],p[2],x0,y0,x1,y1))-t)**2).sum()
        res=minimize(f,[x,y,r],method='Nelder-Mead',options={'xatol':0.02,'fatol':1e-3,'maxiter':200})
        if res.fun<=f([x,y,r]) and res.x[2]>0.3: acc[i]=list(res.x)
    R=render(); resid=A-R
    print('iter',it,'mean abs',np.abs(resid).mean(),'px>0.5',(np.abs(resid)>0.5).sum(),'n',len(acc))
    # add missing
    lab,n=ndi.label(resid>0.5); added=0
    for k,sl in enumerate(ndi.find_objects(lab)):
        m=lab[sl]==k+1; area=(resid[sl]*m).sum()
        if area<3: continue
        ys,xs=np.nonzero(m); acc.append([xs.mean()+sl[1].start+0.5,ys.mean()+sl[0].start+0.5,np.sqrt(area/np.pi)]); added+=1
    # remove spurious (circle mostly over empty)
    keep=[]
    for x,y,r in acc:
        x0,y0,x1,y1=win(x,y,r,0); c=cov(x,y,r,x0,y0,x1,y1)
        keep.append((A[y0:y1,x0:x1]*c).sum()/max(c.sum(),1e-6)>0.6)
    rem=len(acc)-sum(keep); acc=[a for a,k in zip(acc,keep) if k]
    print(' added',added,'removed',rem)
R=render(); d=np.abs(A-R); print('final mean abs',d.mean(),'px>0.5',(d>0.5).sum(),'max',d.max(),'n',len(acc))
np.save('acc2.npy',np.array(acc))
Image.fromarray((d*255).astype(np.uint8)).save('diff2.png')
