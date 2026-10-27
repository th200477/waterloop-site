#!/usr/bin/env python3
"""waterloop.jp の静的サイトを組み立てる。
src/pages/**.html を dist/ に書き出す。URLは /issue → dist/issue/index.html。
ページ内の <!--#include name--> を src/partials/name.html に置き換える。
<!--#title ...--> <!--#desc ...--> はheadに入る。
記事（コラム・お知らせ）は data/*.json と src/templates/*.html から作る（build_articles.py）。
"""
import os, re, shutil, glob, json, html
ROOT=os.path.dirname(os.path.abspath(__file__))
SRC=os.path.join(ROOT,'src'); DIST=os.path.join(ROOT,'dist')
def partial(name):
    return open(os.path.join(SRC,'partials',name+'.html'),encoding='utf-8').read()
def render(body, title, desc, path, extra_head=''):
    head=partial('head').replace('{{title}}',html.escape(title)).replace('{{desc}}',html.escape(desc)).replace('{{path}}',path).replace('{{extra_head}}',extra_head)
    out=head+body+partial('tail')
    for _ in range(3):
        out=re.sub(r'<!--#include ([\w-]+)-->', lambda m: partial(m.group(1)), out)
    return out
def write(path, content):
    d=os.path.join(DIST, path.strip('/'))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(content)
def meta(src, key, default=''):
    m=re.search(r'<!--#'+key+r' (.*?)-->', src, re.S)
    return m.group(1).strip() if m else default
def rebase(base):
    # 仮のURL（github.io/waterloop-site/）で見るときだけ、/ で始まるサイト内リンクに base を付ける
    pat=re.compile(r'((?:href|src|action|poster|content|srcset)=")/(?!/)')
    for dp,_,fs in os.walk(DIST):
        for f in fs:
            p=os.path.join(dp,f)
            if f.endswith('.html'):
                s=open(p,encoding='utf-8').read()
                s=pat.sub(lambda m: m.group(1)+base+'/', s)
                s=re.sub(r'url\((["\']?)/(?!/)', lambda m: 'url('+m.group(1)+base+'/', s)
                open(p,'w',encoding='utf-8').write(s)
            elif f.endswith(('.css','.js')):
                s=open(p,encoding='utf-8').read()
                s=re.sub(r'url\((["\']?)/(?!/)', lambda m: 'url('+m.group(1)+base+'/', s)
                if f.endswith('.js'): s="window.__BASE__='"+base+"';\n"+s
                open(p,'w',encoding='utf-8').write(s)
def main():
    if os.path.exists(DIST): shutil.rmtree(DIST)
    os.makedirs(DIST)
    for d in ('css','js','img','svg','fonts','video'):
        if os.path.exists(os.path.join(SRC,d)): shutil.copytree(os.path.join(SRC,d), os.path.join(DIST,d))
    for f in glob.glob(os.path.join(SRC,'pages','**','*.html'), recursive=True):
        rel=os.path.relpath(f, os.path.join(SRC,'pages'))[:-5]
        path='/' if rel=='index' else '/'+rel.replace(os.sep,'/')
        src=open(f,encoding='utf-8').read()
        body=re.sub(r'<!--#(title|desc|head) .*?-->','',src,flags=re.S)
        write(path, render(body, meta(src,'title','WATER LOOP PROJECT'), meta(src,'desc',''), path, meta(src,'head','')))
    # 記事などの生成ページ
    for g in sorted(glob.glob(os.path.join(ROOT,'gen_*.py'))):
        ns={'render':render,'write':write,'ROOT':ROOT,'SRC':SRC,'DIST':DIST}
        exec(open(g,encoding='utf-8').read(), ns)
    for f in ('_redirects','_headers','robots.txt','favicon.png'):
        p=os.path.join(SRC,f)
        if os.path.exists(p): shutil.copy(p, DIST)
    base=os.environ.get('BASE_PATH','').rstrip('/')
    if base: rebase(base)
    open(os.path.join(DIST,'.nojekyll'),'w').close()
    print('built', sum(len(fs) for _,_,fs in os.walk(DIST)), 'files')
if __name__=='__main__': main()
