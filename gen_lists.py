# 一覧の印をカードに置き換える。build.py が gen_articles.py のあとに exec で実行する。
#   <!--#list columns limit=9-->  … コラムのカード（新しい順）
#   <!--#list news limit=5-->     … お知らせのカード（新しい順）
#   variant=page を付けると一覧ページ（/blog-list, /news-list）用の見た目。付けないとトップ用。
# dist/ に書き出し済みの全HTMLを見て置き換え、カードのCSS（/css/components/cards.css）が無ければ <head> に足す。
import os, re, json, html as _html

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

def date_label(iso):
    if not iso:
        return ''
    y, m, d = iso.split('-')
    return '%s %d, %s' % (MONTHS[int(m) - 1], int(d), y)

def load_template(name):
    t = open(os.path.join(SRC, 'templates', name), encoding='utf-8').read()
    return re.sub(r'\A<!--.*?-->\n', '', t, flags=re.S)

def fill(tpl, values):
    return re.sub(r'\{\{(\w+)\}\}', lambda m: str(values.get(m.group(1), '')), tpl)

def sort_new_first(items):
    # 新しい日付が先。日付の無いもの（今のサイトで日付が空の告知）は先頭に、元の並びのまま置く。
    undated = [a for a in items if not a.get('date')]
    dated = sorted([a for a in items if a.get('date')], key=lambda a: a['date'], reverse=True)
    return undated + dated

def card_values(a):
    h = a['hero']
    return {'slug': a['slug'], 'title': _html.escape(a['title'], quote=False),
            'date_label': date_label(a.get('date')) or '​',
            'hero': h['src'], 'hero_w': h.get('w', ''), 'hero_h': h.get('h', '')}

DATA = {}
TPL = {}
def cards(kind, limit, variant):
    if kind not in DATA:
        fn = 'columns.json' if kind == 'columns' else 'news.json'
        DATA[kind] = sort_new_first(json.load(open(os.path.join(ROOT, 'data', fn), encoding='utf-8')))
        TPL[kind] = load_template('card-column.html' if kind == 'columns' else 'card-news.html')
    items = DATA[kind][:limit] if limit else DATA[kind]
    cls = 'col-cards' if kind == 'columns' else 'news-cards'
    body = '\n'.join(fill(TPL[kind], card_values(a)).strip() for a in items)
    return '<div class="%s %s--%s">\n%s\n</div>' % (cls, cls, variant, body)

MARK = re.compile(r'<!--#list\s+(columns|news)((?:\s+\w+=\w+)*)\s*-->')
LINK = '<link rel="stylesheet" href="/css/components/cards.css">'

def gen_lists():
    n = 0
    for d, _, fs in os.walk(DIST):
        for f in fs:
            if not f.endswith('.html'):
                continue
            p = os.path.join(d, f)
            s = open(p, encoding='utf-8').read()
            if '<!--#list' not in s:
                continue
            def rep(m):
                opts = dict(o.split('=') for o in m.group(2).split())
                limit = int(opts['limit']) if 'limit' in opts else None
                return cards(m.group(1), limit, opts.get('variant', 'top'))
            s2 = MARK.sub(rep, s)
            if s2 != s:
                if '/css/components/cards.css' not in s2:
                    s2 = s2.replace('</head>', LINK + '\n</head>', 1)
                open(p, 'w', encoding='utf-8').write(s2)
                n += 1
    print('lists: replaced in', n, 'pages')

gen_lists()
