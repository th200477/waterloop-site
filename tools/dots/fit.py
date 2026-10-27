import numpy as np, json
from PIL import Image
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
A=np.array(Image.open('../wlp-site/assets/c6e5b358e170921460712e745c51741bbc594628.png').convert('RGBA'))[...,3].astype(float)/255
H,W=A.shape
M=A>0.5
DT=ndi.distance_transform_edt(M)
# subpixel-ish: DT at pixel centers; real radius ≈ DT+0.5
pk=peak_local_max(DT,min_distance=1,threshold_abs=0.9,exclude_border=False)
cands=sorted([(DT[y,x],x,y) for y,x in pk],reverse=True)
acc=[]
from scipy.spatial import cKDTree
def ok(x,y,r):
    for (ax,ay,ar) in acc_near(x,y):
        d=np.hypot(ax-x,ay-y)
        if d<max(ar,r)*0.75: return False
    return True
grid={}
def acc_near(x,y):
    gx,gy=int(x//40),int(y//40)
    for i in (-1,0,1):
        for j in (-1,0,1):
            yield from grid.get((gx+i,gy+j),[])
for r,x,y in cands:
    if ok(x,y,r):
        c=(x+0.5,y+0.5,r+0.5); acc.append(c); grid.setdefault((int(x//40),int(y//40)),[]).append(c)
print('circles',len(acc))
def render(circ,ss=1):
    img=np.zeros((H,W))
    for x,y,r in circ:
        x0,x1=int(max(0,x-r-2)),int(min(W,x+r+2)); y0,y1=int(max(0,y-r-2)),int(min(H,y+r+2))
        ys,xs=np.mgrid[y0:y1,x0:x1]+0.5
        d=np.hypot(xs-x,ys-y)
        cov=np.clip(r-d+0.5,0,1)
        img[y0:y1,x0:x1]=np.maximum(img[y0:y1,x0:x1],cov)
    return img
R=render(acc)
diff=np.abs(R-A); print('mean abs diff',diff.mean(),'pixels >0.5',(diff>0.5).sum())
np.save('acc.npy',np.array(acc))
Image.fromarray((np.clip(diff,0,1)*255).astype(np.uint8)).save('diff.png')
