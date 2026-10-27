// 共通の動き：メニュー開閉、ふわっと出す。ページ固有の動きは js/pages/*.js に置く。
(function(){
  var io=('IntersectionObserver' in window)?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -10% 0px'}):null;
  document.querySelectorAll('.reveal').forEach(function(el){io?io.observe(el):el.classList.add('is-in');});
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
  function setOpen(open){
    root.classList.toggle('menu-open',open);
    btn.setAttribute('aria-expanded',open?'true':'false');
    btn.setAttribute('aria-label',open?'メニューを閉じる':'メニューを開く');
    menu.setAttribute('aria-hidden',open?'false':'true');
    if(open){var first=menu.querySelector('a');if(first)setTimeout(function(){first.focus({preventScroll:true});},50);}
  }
  btn.addEventListener('click',function(){setOpen(!root.classList.contains('menu-open'));});
  // パネルの外（左側）を押したら閉じる
  menu.addEventListener('click',function(e){
    if(!e.target.closest('.site-menu__panel')) setOpen(false);
    else if(e.target.closest('a')) setOpen(false);
  });
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape'&&root.classList.contains('menu-open')){setOpen(false);btn.focus();}
  });
})();
