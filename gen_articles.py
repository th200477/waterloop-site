# コラム（/blog/<slug>）とお知らせ（/news-2/<slug>）の記事ページを data/*.json と src/templates/*.html から書き出す。
# build.py が exec で実行する（render, write, ROOT, SRC, DIST が渡される）。単体でも python3 gen_articles.py で動く（dist/ へ書くだけ）。
import os, re, json, html as _html

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

def date_label(iso):
    """2026-07-10 → July 10, 2026（今のサイトの表記）。日付が無いときは空。"""
    if not iso:
        return ''
    y, m, d = iso.split('-')
    return '%s %d, %s' % (MONTHS[int(m) - 1], int(d), y)

def load_template(name):
    t = open(os.path.join(SRC, 'templates', name), encoding='utf-8').read()
    return re.sub(r'\A<!--.*?-->\n', '', t, flags=re.S)  # 先頭の説明コメントは出さない

def fill(tpl, values):
    return re.sub(r'\{\{(\w+)\}\}', lambda m: str(values.get(m.group(1), '')), tpl)

def block_html(b):
    """本文の1ブロックをHTMLにする。html は抽出時にエスケープ済み（<strong> <a> <br> のみ）。"""
    t = b['t']
    if t == 'p':
        return '<p>%s</p>' % b['html']
    if t == 'space':  # 今のサイトで余白に使っている空の段落
        size = b.get('size')
        return '<p class="rt-space%s" aria-hidden="true"></p>' % (' rt-space--' + size if size else '')
    if t in ('h2', 'h3', 'h4'):
        cls = ' class="rt-en"' if b.get('style') == 'en' else ''
        return '<%s%s>%s</%s>' % (t, cls, b['html'], t)
    if t == 'img':
        alt = _html.escape(b.get('alt', ''))
        wh = ' width="%d" height="%d"' % (b['w'], b['h']) if 'w' in b else ''
        return '<p class="rt-img"><img src="/img/%s.webp" alt="%s"%s loading="lazy"></p>' % (b['src'], alt, wh)
    if t in ('ul', 'ol'):
        return '<%s>%s</%s>' % (t, ''.join('<li>%s</li>' % i for i in b['items']), t)
    raise ValueError('unknown block: %r' % t)

HEADINGS = ('h2', 'h3', 'h4')

def drop_heading_spaces(blocks):
    """見出しの直前・直後の空き段落（space）を外す。見出しの前後の間隔は CSS（article.css の .rt h2 など）で一定にする。
    今のサイトから写した記事は、見出しの前の空き段落が 0〜4 個、後ろが 0〜1 個とまちまちだったため。"""
    out = []
    for i, b in enumerate(blocks):
        if b['t'] == 'space':
            j = i
            while j < len(blocks) and blocks[j]['t'] == 'space':
                j += 1
            k = i
            while k >= 0 and blocks[k]['t'] == 'space':
                k -= 1
            if (j < len(blocks) and blocks[j]['t'] in HEADINGS) or (k >= 0 and blocks[k]['t'] in HEADINGS):
                continue
        out.append(b)
    return out

def blocks_html(blocks):
    return '\n'.join('        ' + block_html(b) for b in drop_heading_spaces(blocks))

def plain(blocks, n=110):
    """説明文（meta description）用に本文の先頭を文字だけにする。"""
    out = ''
    for b in blocks:
        if b['t'] == 'p':
            s = _html.unescape(re.sub(r'<br>', ' ', re.sub(r'<(?!br>)[^>]+>', '', b['html']))).strip()
            if s and not set(s) <= set('ー－-—　 '):
                out += s + ' '
        if len(out) >= n:
            break
    out = re.sub(r'\s+', ' ', out).strip()
    return out[:n] + ('…' if len(out) > n else '')

def article_values(a):
    hero = a['hero']
    return {
        'slug': a['slug'],
        'title': _html.escape(a['title'], quote=False),
        'date_label': date_label(a.get('date')) or '​',
        'hero': hero['src'], 'hero_alt': _html.escape(hero.get('alt', '')),
        'hero_w': hero.get('w', ''), 'hero_h': hero.get('h', ''),
    }

HEAD = '<link rel="stylesheet" href="/css/pages/article.css">'

def gen_articles():
    tpl_col = load_template('column.html')
    tpl_news = load_template('news.html')
    cols = json.load(open(os.path.join(ROOT, 'data', 'columns.json'), encoding='utf-8'))
    news = json.load(open(os.path.join(ROOT, 'data', 'news.json'), encoding='utf-8'))
    for a in cols:
        v = article_values(a)
        v['profile'] = blocks_html(a['profile'])
        v['body'] = blocks_html(a['body'])
        path = '/blog/' + a['slug']
        write(path, render(fill(tpl_col, v), a['title'] + '｜WATER LOOP PROJECT', plain(a['body']), path, HEAD))
    for a in news:
        v = article_values(a)
        v['body'] = blocks_html(a['body'])
        path = '/news-2/' + a['slug']
        write(path, render(fill(tpl_news, v), a['title'] + '｜WATER LOOP PROJECT', plain(a['body']), path, HEAD))
    print('articles:', len(cols), 'columns,', len(news), 'news')

gen_articles()
