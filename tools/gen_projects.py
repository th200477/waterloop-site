# プロジェクト詳細3ページ（同じ型）を書き出す
import html
IG_URL='https://www.instagram.com/water_loop_project?igsh=dWZhb2dpcjlmMnI='
FORM_URL='https://forms.gle/ctRRV2kZaHnQCKRw9'
ARROW='a207ac095b45fd81c1c1f05749896f171ba52e80'
IGB='94982e9c917fd821a2dc483dae38bd09486c4ccb'; WEBB='92fef69bc280a0360c53a2c23d84a967229ad268'
ICONS={'ig':'Instagram','fb':'Facebook','x':'X','yt':'YouTube','mc':'Mixcloud','web':'Webサイト'}
SAIJO=('西条自然学校','2012年設立のNPO法人。野生動植物の調査をベースに、自然を科学的に見る視点と身近な自然を知る楽しみを伝える活動を行い、愛媛の自然環境の把握と保全に取り組む。西条湧水調査プロジェクトや加茂川河口干潟の生物調査など、地域の水環境に根ざしたフィールドワークを継続的に実施している。',
       [('ig',IGB,'https://www.instagram.com/saijo.nature/'),('web',WEBB,'https://saijo-shizen.org')])
PAGES={
'projects-sugosugi':dict(
  title='SUGOSUGI', num='01',
  desc='石鎚山系の間伐材から生まれた、森と地域の循環を味わうクラフトビールプロジェクト',
  slides=['57bbd1df8c6138a1b83c0fa244c2f6ca87d2f478','74b42c43f253999bb72b15c3d0e1247a9fe889ba','51fae708d2e8c8ab45529ad84572dbac9fd01f50','734bfe3f69a62ff4d1fcab301d7c23facef1d824','9874a4235c509a83ac89b03804c036b3131ab53c','1ac883c5a6f5cb349701a4d29eb67c60f76a4bb6'],
  video=None, scope=['山の課題','街の課題'],
  overview=['石鎚山系の森林では、林業の衰退や担い手不足により、適切な管理が難しくなっています。間伐が行われず、森に十分な光が届きにくくなることで、下草が育ちにくくなるなど、森林環境にも少しずつ影響が生まれています。⏎一方で、間伐によって生まれる木材は、バイオマス燃料などとして活用されることもありますが、高い価値がつきにくく、地域資源としての可能性を十分に引き出しきれていない現状があります。',
            'このプロジェクトは、地域の環境と、人の消費や楽しみをもう一度接続できないか。 という問いから始まりました。'],
  highlights=['本プロジェクトでは、間伐された杉を蒸留した際に生まれる香りの水、「杉ウォーター」をクラフトビールに使用しています。',
              '仕込み水には、西条市の地下水を使用。⏎石鎚山系に降った雨が長い時間をかけて地中を巡り、街へ湧き出すこの水は、西条の暮らしや文化を支えてきた存在でもあります。',
              '森林の管理、水の循環、地域の営み。⏎本来はつながっているはずのそれらを、“飲む体験”として再編集できないか。',
              '杉の香りや空気感をビールに落とし込むことで、 普段森と接点のない人でも、地域の環境や循環に自然と触れられる入口を目指しました。',
              'また、環境問題を「学ぶもの」として伝えるのではなく、まずは「おいしい」「気になる」「また飲みたい」という感覚から関係が始まることを重視しています。'],
  hl_img=('a3bb329318059d0fc9272a0ea505110092772544','間伐材のスギの葉 × 西条の地下水',640,240,'592/222'), hl_opt=dict(mt=0,sp_w=420,sp_ar='420/158'),
  partners_text=['本プロジェクトは、森林と醸造、それぞれ異なる領域のプレイヤーが関わることで実現しました。',
                 '西条自然学校は、石鎚山系の自然環境や森林管理に関する知見を共有するとともに、間伐材の調達や杉の蒸留にも協力。 森林の現場で起きている課題を、単なる知識としてではなく、実際の素材や体験へ接続する役割を担いました。',
                 'GROUNDTAP BREWERYは、西条の地下水を仕込み水に使用するローカルブルワリーとして参加。杉を蒸留して生まれた「杉ウォーター」と地域の名水を用いながら、森の香りや土地の風景をクラフトビールとして表現しました。',
                 'WATER LOOP PROJECTは、それぞれの領域を横断しながら、地域環境・体験・カルチャーをつなぐプロジェクト全体の企画とディレクションを担当。⏎ 環境課題を「説明する」のではなく、人が自然と関わりたくなる入口として再編集することを目指しました。'],
  p_img=('5432eaee4d2f26d3cd242be5e29041263b0ade61','GROUNDTAP BREWERY × 西条自然学校 × WATER LOOP PROJECT',640,240,'592/222'), p_opt=dict(mt=16,mb=0,sp_mb=16,sp_w=340,sp_ar='340/128'),
  partners=[('GROUNDTAP BREWERY','愛媛県西条市に2023年に誕生したマイクロブルワリー。地元企業・株式会社ダイテックが、金属加工のものづくり技術を活かして参入した。ブランド名は西条の湧水「うちぬき」に由来し、名水百選に選ばれたこの地下水を全商品の仕込み水に使用。西条産米を使ったラガーをはじめ、地域の素材と文化をビールに落とし込んでいる。',
             [('ig','ab9ec683ee775ad2483cb9eb0a0878c8ada26a58','https://www.instagram.com/groundtap_brewery/'),('fb','e633b3e99e9247cb4a50557ca8e0affb8c68fd93','https://www.facebook.com/groundtap.brewery/'),('x','b8a2cde219ab8b38905270c27e29b083774c4eb9','https://x.com/gt_brewery'),('yt','536e223d284eee864e6356923e28b98b299c0dac',None),('mc','a97c8956a2f908916b047362a389243cabea6775','https://www.mixcloud.com/gtbtaproom/'),('web','5e8d31e262b0882403d2fd24f91fd71f7e4873f3','https://groundtap-brewery.com/')]),
            SAIJO],
  next=[('p','現在、WATER LOOP PROJECTでは、定期的に交流会やイベントを開催しており、SUGOSUGIをその場で試飲いただける機会を設けています。実際に飲みながら、森や地域のことをゆるやかに知ってもらう場になればと考えています。'),
        ('p','イベントや交流会のお知らせは、Instagramにて発信しています。ぜひお気軽にご参加ください。'),
        ('btn','Instagram',IG_URL,True),
        ('p','また、SUGOSUGIを取り扱っていただける販売店・飲食店さまを募集しています。ご興味のある方は、お問い合わせフォームよりご連絡ください。'),
        ('btn','お問い合わせフォーム',FORM_URL,False)]),
'projects-table0':dict(
  title='TABLE 0', num='02',
  desc='山・里・街の課題と食材をひとつのテーブルに集め、美味しくいただくフードプロジェクト',
  slides=['4dcbafc79da3543cb7fa94768d79fa34f1518adf','55a537d1f1efe0da52dd30ca4056ec4023e76da4','12ce014371f965bd051aa049e74c4d96212ad53b','7ebafad0db8478e696dbf625d08a71d576fe59c1','01dc024cb075395651d2798627b9793886055d09','9f03ce3968ca6326ff18557206ae1532aeba6b8d','7dc7c247015cd4826657605abceaa69f542eb42f','d8e7746e7a5d39804f5088af92f39f252d8f0876','8985b24543320ca7b4371ec1a4ed6c632dd3aea5','08a42db24dcb9d4f344df1d39013d0ea593111b1','3a15e7453cafdbb7edefb6f0df5aa7c61ac3d070'],
  video='https://www.youtube.com/embed/C2jLkicErGg', scope=['山の課題','里の課題','街の課題'],
  overview=['西条市は、豊かな地下水に支えられた水のまちです。市内には「うちぬき」と呼ばれる自噴井戸も点在し、その水は暮らしや文化を支えてきました。',
            '山に降った雨は、森を通り、里を潤し、やがて街へ届く。その流れの中には、農業、林業、食、暮らしなど、さまざまな人の営みが重なっています。',
            '一方で、森林管理の担い手不足、耕作放棄地の増加、野生鳥獣による被害など、⏎地域の中では少しずつ見えにくい課題も生まれています。',
            'TABLE 0は、そうした地域の背景を、“食べること”を入口に体験できないかという問いから始まったプロジェクトです。'],
  highlights=['課題と食材を、ひとつのテーブルへ。',
              'TABLE 0では、地域の課題と食材を、ひとつのコースとして再編集しています。',
              '森に手を入れることで生まれる間伐材は、切り株のテーブルボードへ。耕作放棄地に咲いたひまわりは、ドレッシングへ。地域の森で獲れた鹿や猪は、ジビエ料理へ。さらに、間伐された杉の香りを落とし込んだクラフトビールも並びます。',
              'それぞれの料理やプロダクトには、地域で起きている出来事や、人の営みが背景として存在しています。TABLE 0では、それらを味わうだけでなく、生産者や、実際に地域の現場と向き合っている人たちの話を聞きながら、食と地域課題をひとつのテーブルで体験していきます。',
              '食べるだけでは見えなかった背景を、少しずつ言葉でひらいていく。そんな体験を目指しています。'],
  hl_img=('12298c9c0cf230202f538ddf0502c12aeacbfcb7','間伐材の杉のクラフトビール、耕作放棄地のひまわり油ドレッシング、森のジビエ、間伐材の切り株ボード',640,320,'592/210'), hl_opt=dict(mt=12,sp_w=311,sp_ar='311/588',sp_src=('f631aed83c79712238cadd2d0ca1de68be14e5a6',640,960)),
  partners_text=['TABLE 0は、地域のさまざまなプレイヤーとの協力によって実現しています。',
                 'ジビエ専門店Magokoroは、地域で捕獲された鹿や猪を提供。命をいただく営みを、食の体験へとつなげています。',
                 'CREW TAMBARAは、耕作放棄地を活用して育てたひまわりから生まれた油や、地域の野菜を提供。農業と地域の風景をつなぐ取り組みを行っています。',
                 '西条自然学校は、森林整備によって生まれた間伐材を提供。地域の自然環境や水循環に関する知見を共有しています。',
                 'TRUNKは、その間伐材を加工し、切り株のテーブルボードを制作。森の素材を、実際に触れられる体験へと落とし込みました。⏎WATER LOOP PROJECTは、それぞれの領域を横断しながら、地域環境・体験・カルチャーをつなぐプロジェクト全体の企画とディレクションを担当しています。'],
  p_img=('dc1ac0e779436af104c26404b40d9f3742f0601d','ジビエ専門店Magokoro × CREW TAMBARA × 西条自然学校 × TRUNK × WATER LOOP PROJECT',640,320,'592/290'), p_opt=dict(mt=16,mb=32,sp_mb=32,sp_w=311,sp_ar='311/170'),
  partners=[('ジビエ専門店Magokoro','愛媛県西条市丹原町を拠点に、地元で捕獲されたシカやイノシシの精肉販売を行うジビエ専門店。 スタッフ全員が地元の猟師であり、捕獲から解体処理、販売までを一貫して行っている。迅速な血抜きや温度管理を徹底することで、ジビエ特有の臭みを抑え、素材本来の旨みを引き出すことを重視。 “命をいただく”という営みを、地域の自然環境や暮らしとともに伝える活動を続けている。',
             [('ig',IGB,'https://www.instagram.com/magokor_jibie/')]),
            ('CREW TAMBARA','愛媛県西条市丹原町を拠点に、耕作放棄地の増加や地域の担い手不足と向き合いながら、農業・観光・商業」をつなぐ地域プロジェクトを展開。 放棄地へひまわりを植え、採れた種からひまわり油を製造。その油を使った「たんばらドーナッツ」の開発や、景観・体験・地域産品を組み合わせた取り組みを行っている。「畑と人を近づける」をテーマに、地域の風景や営みを、食や体験を通して次世代へつないでいく活動を続けている。',
             [('ig',IGB,'https://www.instagram.com/crew_tambara/'),('web',WEBB,'https://crewtambara.theshop.jp/')]),
            SAIJO,
            ('TRUNK','Little Branchの小澤奏氏によって立ち上げられたプロダクトレーベル。チェンソー一本から始める“ミクロ林業”を背景に、自ら森に入りつつ、いつ、どこで、誰が伐ったものか分かる木材をプロダクトへ落とし込むまでを一貫して行っている。大量生産ではなく、地域の森と密接につながりながら、小さな循環を積み重ねることを重視。 木材そのものだけではなく、森林空間そのものの価値を展開していく活動によりプロダクトから森林まで導線のあるものづくりを実践している。',
             [('ig',IGB,'https://www.instagram.com/trunk_intotheforest/')])],
  next=[('p','現在TABLE 0は、単体のフードイベントとしてではなく、企業研修向けのツーリズムプログラムや、教育機関向けの地域探究プログラムの一部として開発を進めています。'),
        ('p','地域課題を知識として学ぶだけではなく、実際に食べ、対話し、現地の空気に触れることで、水や地域との関係を身体感覚として捉え直す体験を目指しています。'),
        ('p','今後は、企業・教育機関・団体向けに、地域フィールドワークやツアーと連動したプログラムとして展開予定です。'),
        ('p','ご興味のある方は、お問い合わせフォームよりお気軽にご連絡ください。'),
        ('btn','お問い合わせフォーム',FORM_URL,False)]),
'projects-saunadobadoba':dict(
  title='SAUNA DOBADOBA', num='03',
  desc='森と水の恵みを五感で味わい、自然との距離を縮めるアウトドア体験プログラム',
  slides=['7d3227555c85b4a91562a66769c1fc1e44276e91','72d254fc20b9db553c94cef9df2549974183c6c2','0d6149d0962c8b500e142d244e3f23c2618ad2f8','1c4b36f190c9baac0c4bdf6ee821e0346db1b420','f5ffb485309c29828f4bbeba3a21784b9f65e354','8606d6acd1dd11d2c08f4110432915f6a5ba530e','1894220668e457728e591190569550dde9b9fa28','ba08f6903b95c3952b82bfd3bcc25b2491651b6c','e9bbfbc719f10a5cb7f8d4f68376740c23acc2a2'],
  video='https://www.youtube.com/embed/c45kU-h8piY', scope=['山の課題','街の課題'],
  overview=['DOBADOBAでは、間伐材を燃料にした薪ストーブを使用しています。',
            '森林整備の過程で生まれた木を燃やし、その熱で身体を温める。⏎さらに、ロウリュにはスギの葉を蒸留してつくられたアロマオイルを使用し、サウナ室全体を森の香りで包み込みます。',
            '水風呂には、西条の地下水を使用。⏎年間を通して約15℃前後を保つこの水は、やわらかく澄んだ肌あたりが特徴です。',
            '森に降った雨が、長い時間をかけて街へ届く。⏎DOBADOBAでは、その循環を“ととのう体験”として再構成しています。'],
  highlights=['DOBADOBAでは、間伐材を燃料にした薪ストーブを使用しています。',
              '森林整備の過程で生まれた木を燃やし、その熱で身体を温める。⏎さらに、ロウリュにはスギの葉を蒸留してつくられたアロマオイルを使用し、サウナ室全体を森の香りで包み込みます。',
              '水風呂には、西条の地下水を使用。⏎年間を通して約15℃前後を保つこの水は、やわらかく澄んだ肌あたりが特徴です。',
              '森に降った雨が、長い時間をかけて街へ届く。⏎DOBADOBAでは、その循環を“ととのう体験”として再構成しています。'],
  hl_img=('86f0ea21423d0b724ada3fb5a0eef67899c38219','',640,280,'592/222'), hl_opt=dict(mt=12,sp_w=311,sp_ar='311/455',sp_src=('d563061fcb8e3aebf3e77c74f20d7b63131f57b4',640,800)),
  partners_text=['DOBADOBAは、地域の森林資源を活用しながら実現しているプロジェクトです。',
                 '西条自然学校は、森林整備の過程で生まれる間伐材や、スギの葉を蒸留してつくられたアロマオイルを製造。DOBADOBAでは、それらをサウナの薪やロウリュとして使用しています。',
                 'WATER LOOP PROJECTは、地域資源・体験・カルチャーを横断しながら、森と水の循環を身体感覚として体験できるプロジェクト全体の企画とディレクションを担当しています。'],
  p_img=('80a67ae80fca61977a58befd3f1b759a0f274fc5','西条自然学校 × WATER LOOP PROJECT',640,320,'592/222'), p_opt=dict(mt=0,mb=0,sp_mb=16,sp_w=340,sp_ar='340/128'),
  partners=[SAIJO],
  next=[('p','DOBADOBAは、今後定期的に開催予定の交流会にて体験いただけます。'),
        ('p','交流会では、サウナを楽しむだけでなく、地域の人たちが自然とつながり、話し合える場を目指しています。'),
        ('p','森や水のこと。地域で起きていること。これからの暮らしや遊びのこと。'),
        ('p','サウナを入口に、そんな会話がゆるやかに生まれる時間をつくっていきます。'),
        ('p','開催情報については、Instagramにてお知らせしています。⏎ ご興味のある方は、ぜひチェックしてみてください。'),
        ('btn','Instagram',IG_URL,True)]),
}
e=html.escape
def paras(ps,ind='          '): return '\n'.join(f'{ind}<p>{br(p)}</p>' for p in ps)
def br(t): return e(t).replace('⏎','<br>')
def img(t,o,cls='pj-figure'):
    h,alt,w,hh,ar=t
    st=f"--ar:{ar};--mt:{o.get('mt',0)}px;--mb:{o.get('mb',0)}px;--sp-mb:{o.get('sp_mb',o.get('mb',0))}px;--sp-w:{o['sp_w']}px;--sp-ar:{o['sp_ar']}"
    tag=f'<img src="/img/{h}.webp" alt="{e(alt)}" width="{w}" height="{hh}" loading="lazy">'
    src=''
    if o.get('sp_src'):
        sh,sw,shh=o['sp_src']; src=f'<source media="(max-width:767px)" srcset="/img/{sh}.webp" width="{sw}" height="{shh}">'
    return f'<picture class="{cls}" style="{st}">{src}{tag}</picture>'
def btn(label,url,blank):
    tb=' target="_blank" rel="noopener"' if blank else ''
    return f'<a class="pj-btn" href="{e(url)}"{tb}>{e(label)}<img src="/svg/{ARROW}.svg" alt="" width="16" height="15"></a>'
for slug,d in PAGES.items():
    slides='\n'.join(f'        <li class="pj-carousel__slide"><img src="/img/{h}.webp" alt=""{"" if i==0 else " loading=\"lazy\""}></li>' for i,h in enumerate(d['slides']))
    partners=[]
    for name,txt,links in d['partners']:
        ic=''.join((f'<a href="{e(u)}" target="_blank" rel="noopener" aria-label="{ICONS[k]}"><img src="/svg/{h}.svg" alt="" width="20" height="20"></a>' if u else f'<span aria-hidden="true"><img src="/svg/{h}.svg" alt="" width="20" height="20"></span>') for k,h,u in links)
        partners.append(f'''          <div class="pj-partner">
            <h3 class="pj-partner__name">{e(name)}</h3>
            <p class="pj-partner__text">{br(txt)}</p>
            <p class="pj-partner__links">{ic}</p>
          </div>''')
    nxt=[]
    for it in d['next']:
        if it[0]=='p': nxt.append(f'          <p>{br(it[1])}</p>')
        else: nxt.append(f'          <p class="pj-btn-wrap">{btn(*it[1:])}</p>')
    video=(f'''    <div class="pj-video"><iframe src="{d['video']}" title="{e(d['title'])}の動画" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>\n''' if d['video'] else '')
    scope=''.join(f'<li>{e(s)}</li>' for s in d['scope'])
    page=f'''<!--#title {d['title']}｜WATER LOOP PROJECT-->
<!--#desc {d['desc']}-->
<!--#head <link rel="stylesheet" href="/css/pages/project.css"><script src="/js/pages/project.js" defer></script>-->
<main class="pj">
  <section class="pj-carousel" aria-roledescription="carousel" aria-label="{e(d['title'])}の写真">
    <div class="pj-carousel__viewport">
      <ul class="pj-carousel__track">
{slides}
      </ul>
    </div>
    <button class="pj-carousel__btn pj-carousel__btn--prev hv-arrow" type="button" aria-label="前の写真"><img src="/svg/cacc5ed7e09c9c2f3056f20c4921c5bf48fc4a96.svg" alt="" width="72" height="72"></button>
    <button class="pj-carousel__btn pj-carousel__btn--next hv-arrow hv-arrow--next" type="button" aria-label="次の写真"><img src="/svg/cacc5ed7e09c9c2f3056f20c4921c5bf48fc4a96.svg" alt="" width="72" height="72"></button>
  </section>

  <article class="pj-body">
    <header class="pj-head">
      <h1 class="pj-head__title"><span class="pj-head__num">{d['num']}</span><span class="pj-head__name">{e(d['title'])}</span></h1>
      <p class="pj-head__tag">Products</p>
      <p class="pj-head__lead">{e(d['desc'])}</p>
    </header>
{video}    <div class="pj-rows">
      <section class="pj-row">
        <h2 class="pj-row__label">Scope</h2>
        <div class="pj-row__body"><ul class="pj-scope">{scope}</ul></div>
      </section>
      <section class="pj-row">
        <h2 class="pj-row__label">Overview</h2>
        <div class="pj-row__body">
{paras(d['overview'])}
        </div>
      </section>
      <section class="pj-row">
        <h2 class="pj-row__label">Highlights</h2>
        <div class="pj-row__body">
{paras(d['highlights'])}
          {img(d['hl_img'],d['hl_opt'])}
        </div>
      </section>
      <section class="pj-row">
        <h2 class="pj-row__label">Partners</h2>
        <div class="pj-row__body">
{paras(d['partners_text'])}
          {img(d['p_img'],d['p_opt'],'pj-figure pj-figure--partners')}
{chr(10).join(partners)}
        </div>
      </section>
      <section class="pj-row">
        <h2 class="pj-row__label">Next Action</h2>
        <div class="pj-row__body pj-next">
{chr(10).join(nxt)}
        </div>
      </section>
    </div>
    <p class="pj-back"><a class="pj-btn pj-btn--back" href="/projects-list">All Project<img src="/svg/f5febb17932b6c3fce114298116ffcaefaaa2604.svg" alt="" width="16" height="15"></a></p>
  </article>
</main>
'''
    open(f'/home/claude/waterloop-site/src/pages/{slug}.html','w').write(page)
    print(slug,len(page))
