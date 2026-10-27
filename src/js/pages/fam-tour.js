// /fam-tour：研修コンテンツのカルーセル（前へ・次へ、端まで行ったら反対側へ戻る、横スワイプ対応）
(function(){
  document.querySelectorAll('[data-carousel]').forEach(function(root){
    var track=root.querySelector('[data-track]');
    var slides=track.children, n=slides.length, i=0;
    function go(k){
      i=(k+n)%n;
      track.style.transform='translateX('+(-100*i)+'%)';
      for(var j=0;j<n;j++){ slides[j].setAttribute('aria-hidden', j===i?'false':'true'); slides[j].inert = j!==i; }
    }
    root.querySelector('[data-prev]').addEventListener('click',function(){go(i-1);});
    root.querySelector('[data-next]').addEventListener('click',function(){go(i+1);});
    var x0=null;
    track.addEventListener('touchstart',function(e){x0=e.touches[0].clientX;},{passive:true});
    track.addEventListener('touchend',function(e){ if(x0===null)return; var dx=e.changedTouches[0].clientX-x0; if(Math.abs(dx)>40) go(i+(dx<0?1:-1)); x0=null; });
    go(0);
  });
})();
