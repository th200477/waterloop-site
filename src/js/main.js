// 共通の動き：今のサイト（Figma Sites）の動きの設定値をそのまま写したもの。メニュー開閉もここ。
// ページ固有の動き（カルーセル・DOBADOBA の拡大・流れる文字など）は js/pages/*.js に置く。
//
// HTML への書き方
//   data-appear="0.7"        画面に入ったら下から出てくる。数字は時間（秒）。イージングは ease-out（CSS の --ease-out）
//     data-appear-y="50"     出てくる前のずれ（px）。省略すると 150
//     data-appear-replay     画面の外に出たら元に戻り、また入ると出直す（今のサイトの「1回だけ再生」がオフのもの）
//     data-appear-exit="0.6" 外に出たときの戻りの時間（秒）。省略すると 0.6
//     data-appear-media="(min-width:1280px)"  この幅のときだけ動かす（ほかの幅では最初から見えている）
//   data-appear-load         ページを開いたときに 1.8 秒かけて透明から出る
//   data-parallax="1.05"     スクロールに合わせて縦にずれる。ずれ = スクロール量 ×（1 − 数字）。1 より大きいと上へ、小さいと下へ
//     data-parallax-media="(min-width:1280px)"  この幅のときだけ
// 「画面に入った」は今のサイトと同じく、ずれた位置の要素が 1px でも画面に入ったとき（IntersectionObserver、しきい値 0）。
// prefers-reduced-motion のときは何も動かさない（最初から見えている）。
(function(){
  window.__motion=true;
  var root=document.documentElement;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO='IntersectionObserver' in window;
  function mq(q){return !q||!window.matchMedia||window.matchMedia(q).matches;}

  // ---- ページを開いたときに出る ----
  var loads=document.querySelectorAll('[data-appear-load]');
  requestAnimationFrame(function(){requestAnimationFrame(function(){
    for(var i=0;i<loads.length;i++) loads[i].classList.add('is-shown');
  });});

  // ---- 画面に入ったら出てくる ----
  var items=[].slice.call(document.querySelectorAll('[data-appear]'));
  if(reduce||!hasIO){ items.forEach(function(el){el.classList.add('is-static');}); }
  else {
    // 判定は今のサイトと同じく「ずれた位置の要素」が 1px でも画面に入ったとき（しきい値 0、余白なし）
    var ios={};
    function ioFor(m){
      return ios[m]||(ios[m]=new IntersectionObserver(function(es){
        es.forEach(function(e){ var st=e.target.__ap; if(st&&st.io===ios[m]) (e.isIntersecting?st.enter:st.leave)(); });
      },{rootMargin:'0px 0px '+m+'px 0px'}));
    }
    items.forEach(function(el){
      var dur=parseFloat(el.getAttribute('data-appear'))||0.6;
      var exitDur=parseFloat(el.getAttribute('data-appear-exit'));if(isNaN(exitDur))exitDur=0.6;
      var replay=el.hasAttribute('data-appear-replay');
      var media=el.getAttribute('data-appear-media');
      var y=el.getAttribute('data-appear-y'); if(y!==null) el.style.setProperty('--appear-y',y+'px');
      var shift=0;
      var visible=false, busy=false, timer=null, st={io:null};
      function watch(m){ if(st.io) st.io.unobserve(el); st.io=m===null?null:ioFor(m); if(st.io) st.io.observe(el); }
      function show(){
        busy=true; el.style.setProperty('--appear-dur',dur+'s'); el.classList.add('is-shown');
        if(!replay){ watch(null); return; }
        watch(0);
        timer=setTimeout(function(){ busy=false; if(!visible) hide(); }, dur*1000);
      }
      function hide(){
        // 外に出たら：「出たあとの状態」（見た目は同じ）へ exitDur 秒 → 一瞬で出る前の状態に戻す
        busy=true;
        timer=setTimeout(function(){
          el.style.setProperty('--appear-dur','0s'); el.classList.remove('is-shown');
          void el.offsetWidth; busy=false; visible=false;
          watch(shift);
        }, exitDur*1000);
      }
      st.enter=function(){ visible=true; if(!busy&&!el.classList.contains('is-shown')) show(); };
      st.leave=function(){ visible=false; if(replay&&!busy&&el.classList.contains('is-shown')) hide(); };
      el.__ap=st;
      function setup(){
        clearTimeout(timer); busy=false; visible=false; watch(null);
        if(mq(media)){ el.classList.remove('is-static'); el.classList.remove('is-shown'); watch(shift); }
        else { el.classList.add('is-static'); }
      }
      setup();
      if(media&&window.matchMedia){ var m=window.matchMedia(media); m.addEventListener?m.addEventListener('change',setup):m.addListener(setup); }
    });
  }

  // ---- パララックス ----
  var plx=[].slice.call(document.querySelectorAll('[data-parallax]'));
  if(plx.length&&!reduce){
    var ticking=false;
    var upd=function(){
      ticking=false;
      var sy=window.pageYOffset||root.scrollTop||0;
      for(var i=0;i<plx.length;i++){
        var el=plx[i], sp=parseFloat(el.getAttribute('data-parallax'));
        if(!mq(el.getAttribute('data-parallax-media'))){ el.style.translate=''; continue; }
        el.style.translate='0 '+(sy*(1-sp)).toFixed(2)+'px';
      }
    };
    window.addEventListener('scroll',function(){ if(!ticking){ticking=true;requestAnimationFrame(upd);} },{passive:true});
    window.addEventListener('resize',upd);
    upd();
  }
})();

// ヘッダーのロゴ色：<main data-header="dark"> なら白ロゴ（:has() が使えないブラウザ向けの保険）
(function(){
  if(document.querySelector('main[data-header="dark"]')) document.body.classList.add('is-header-dark');
})();

// メニュー開閉
(function(){
  var btn=document.querySelector('.site-header__menu');
  var menu=document.getElementById('site-menu');
  if(!btn||!menu) return;
  var root=document.documentElement;
  function setOpen(open,byKey){
    root.classList.toggle('menu-open',open);
    btn.setAttribute('aria-expanded',open?'true':'false');
    btn.setAttribute('aria-label',open?'メニューを閉じる':'メニューを開く');
    menu.setAttribute('aria-hidden',open?'false':'true');
    if(open&&byKey){var first=menu.querySelector('a');if(first)setTimeout(function(){first.focus({preventScroll:true});},50);}
  }
  // キーボードで開いたときだけ、最初のリンクに移る（指やマウスのときは枠を出さない）
  btn.addEventListener('click',function(e){setOpen(!root.classList.contains('menu-open'),e.detail===0);});
  // パネルの外（左側）を押したら閉じる
  menu.addEventListener('click',function(e){
    if(!e.target.closest('.site-menu__panel')) setOpen(false);
    else if(e.target.closest('a')) setOpen(false);
  });
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape'&&root.classList.contains('menu-open')){setOpen(false);btn.focus();}
  });
})();
