// 共通の動き：メニュー開閉、ふわっと出す。ページ固有の動きは js/pages/*.js に置く。
(function(){
  var io=('IntersectionObserver' in window)?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -10% 0px'}):null;
  document.querySelectorAll('.reveal').forEach(function(el){io?io.observe(el):el.classList.add('is-in');});
})();
