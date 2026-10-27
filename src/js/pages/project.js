// プロジェクト詳細：上の写真のカルーセル（前へ・次へ、スワイプ、端でつながる）
(function(){
  document.querySelectorAll('.pj-carousel').forEach(function(root){
    var track=root.querySelector('.pj-carousel__track');
    var orig=Array.prototype.slice.call(track.children);
    var n=orig.length; if(n<2) return;
    // 端でも左右に写真が見えるよう、前後に複製を置く
    orig.forEach(function(li){var c=li.cloneNode(true);c.setAttribute('aria-hidden','true');track.appendChild(c);});
    orig.slice().reverse().forEach(function(li){var c=li.cloneNode(true);c.setAttribute('aria-hidden','true');track.insertBefore(c,track.firstChild);});
    track.querySelectorAll('img').forEach(function(img){img.removeAttribute('loading');});
    var idx=n, busy=false;
    function slideW(){return track.children[0].getBoundingClientRect().width;}
    function place(anim){
      var w=slideW(), off=(root.clientWidth-w)/2-idx*w;
      track.classList.toggle('is-anim',!!anim);
      track.style.transform='translate3d('+off+'px,0,0)';
    }
    var timer=null;
    function settle(){
      clearTimeout(timer);
      if(idx>=2*n) idx-=n; else if(idx<n) idx+=n;
      place(false); busy=false;
    }
    function go(d){
      if(busy) return; busy=true; idx+=d; place(true);
      timer=setTimeout(settle,800); // transitionend が来ない場合の保険
    }
    track.addEventListener('transitionend',function(e){ if(e.target===track) settle(); });
    root.querySelector('.pj-carousel__btn--prev').addEventListener('click',function(){go(-1);});
    root.querySelector('.pj-carousel__btn--next').addEventListener('click',function(){go(1);});
    // スワイプ
    var sx=null;
    root.addEventListener('touchstart',function(e){sx=e.touches[0].clientX;},{passive:true});
    root.addEventListener('touchend',function(e){
      if(sx===null) return; var dx=e.changedTouches[0].clientX-sx; sx=null;
      if(Math.abs(dx)>40) go(dx<0?1:-1);
    });
    window.addEventListener('resize',function(){place(false);});
    place(false);
  });
})();
