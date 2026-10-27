# 作業メモ（共通ルール）

## 場所
- リポジトリ: /home/claude/waterloop-site（ここで作業。git の commit/push はしない。まとめ役が行う）
- 取得済みの今のサイト: /tmp/claude-0/-home-claude/15b76929-41bb-5676-95cc-81ecf0ec316c/scratchpad/wlp-site/raw/*.html（ファイル名はURLの / を _ にしたもの。index.html がトップ）
- 今のサイトの画像の元ファイル: .../scratchpad/wlp-site/assets/（<hash>.png / <hash>.svg）
- https://waterloop.jp には curl / Playwright で接続できる（Playwright は chromium.launch({proxy:{server:process.env.HTTPS_PROXY}}) と ignoreHTTPSErrors:true）

## Figma
- fileKey: 3nEhZQqKuCof7ZjXfAEFSP（ファイル名 WLP_NEW）、sessionId: 804bccf9-b680-4826-b1d3-85027f4f5005
- get_design_context の前に skill://figma/figma-design-to-code/SKILL.md を読む（get_figma_skill）。use_figma の前に skill://figma/figma-use/SKILL.md。このファイルは読み取りだけ。Figmaのデザインを書き換えない。
- get_design_context は1ページ丸ごとだと出力が切れる。セクション単位（子ノードID）で呼ぶ。
- Figmaの一時アセットURL（figma.com/api/mcp/asset/...）はこの環境からダウンロードできない。使わない。
- 画像: Figma の imageHash がそのままファイル名。src/img/<imageHash>.webp にある（最大幅2000px）。ノードの imageHash は use_figma で fills を読んで調べる。
- SVG（ロゴ・アイコン・波線など）: src/svg/<hash>.svg（今のサイトの _assets と同じ名前）。どれがどこかは raw/*.html の <img src="/_assets/v11/xxx.svg"> の位置で照合する。見つからない装飾は、get_design_context の中身から同じ形を描かない。分からなければ報告する。
- フォント: Manrope / Noto Sans JP / Zen Old Mincho（Google Fonts。headで読込済み）

## ページのフレーム（Desktop 1280 / Tablet 800 / Mobile 375）
| URL | Desktop | Tablet | Mobile |
|---|---|---|---|
| / | 1:895 | 1:955 | 1:1015 |
| /issue | 3:2972 | 3:3083 | 3:3194 |
| /projects-list | 3:4208 | 3:4231 | 3:4254 |
| /blog-list | 3:4686 | 3:4709 | 3:4732 |
| /blog/*（記事の型） | 4:5100 | 4:5325 | 4:5550 |
| /news-list | 4:5939 | 4:5971 | 4:6003 |
| /news-2/*（記事の型） | 4:6664 | 4:6697 | 4:6730 |
| /contact | 4:6918 | 4:6935 | 4:6952 |
| /privacy-policy | 4:7131 | 4:7182 | 4:7233 |
| /terms-of-use | 4:7468 | 4:7524 | 4:7580 |
| /projects-sugosugi | 4:7969 | 4:8071 | 4:8173 |
| /projects-table0 | 4:9303 | 4:9443 | 4:9583 |
| /projects-saunadobadoba | 4:9725 | 4:9808 | 4:9891 |
| /fam-tour | 4:11215 | 4:11394 | 4:11573 |

## 作り方
- ページは src/pages/<URL>.html（例 src/pages/issue.html、src/pages/projects-sugosugi.html）。中身は <main>…</main> だけ書く。ヘッダー・フッター・head は自動で付く。
- 先頭に <!--#title ページ名｜WATER LOOP PROJECT--> <!--#desc 説明--> <!--#head <link rel="stylesheet" href="/css/pages/xxx.css">--> を書ける。
- ページ固有のCSSは src/css/pages/<名前>.css、JSは src/js/pages/<名前>.js（<!--#head <script src=... defer>--> で読む）。
- src/css/base.css のトークン（--blue など）、.btn-pill、.sec-title、.reveal（ふわっと出す）を使う。base.css を書き換えてよいのは担当A（ヘッダー・フッター・トップ）だけ。足りないものは自分のページCSSに書く。
- 幅の区切り: スマホ 〜799px／タブレット 800〜1279px／PC 1280px〜（今のサイトと同じ区切り）。Figmaの3つのフレームを見て、それぞれの幅で合わせる。絶対配置の羅列にせず、flex/grid で組む。
- 文言は Figma と今のサイトから一字一句そのまま写す。作文しない。Figma と今のサイトで違う場合は、今のサイト（raw/*.html）を正とし、報告する。
- サイト内リンクは /issue のような絶対パス。外部リンクは今のサイトと同じURL。
- 確認: `python3 build.py` のあと dist/ を `python3 -m http.server` などで出し、Playwright で 1280 / 800 / 375 の幅でスクリーンショットを撮り、Figma の get_screenshot と見比べて直す。
- 終わったら、作ったファイル、残った違い、分からなかったことを短く報告する。

## 追記（公開先の変更）
- 公開先は GitHub Pages。確認用のURLは https://th200477.github.io/waterloop-site/ になるため、ビルド時に BASE_PATH=/waterloop-site を付けると、HTMLの href/src/action/srcset と CSS/JS の url(/...) に自動で /waterloop-site が付く。
- そのため、サイト内リンクと画像は必ず「/」で始まる絶対パスで、HTML属性かCSSのurl()に書く。JSの中でURLを組み立てる場合は (window.__BASE__||'') + '/img/...' のようにする。
- Netlify 固有の機能（Netlify Forms、_redirects）は使わない。
