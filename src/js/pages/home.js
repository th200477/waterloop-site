// トップページの動き：ヒーロー動画、再生ボタンのポップアップ、プロジェクトのカルーセル、パララックス
(function(){
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ヒーローの背景動画（PC・タブレットだけ読み込む。スマホは写真）
  var hv=document.querySelector('.hero__video');
  var wide=window.matchMedia('(min-width: 768px)');
  function loadHero(){
    if(!hv||!wide.matches||hv.dataset.loaded) return;
    hv.dataset.loaded='1';
    [['webm','video/webm'],['mp4','video/mp4']].forEach(function(t){
      var s=document.createElement('source');s.src=(window.__BASE__||'')+hv.dataset['src'+t[0].charAt(0).toUpperCase()+t[0].slice(1)];s.type=t[1];hv.appendChild(s);
    });
    hv.load();
    if(!reduce){var p=hv.play();if(p&&p.catch)p.catch(function(){});}
  }
  loadHero();
  if(wide.addEventListener) wide.addEventListener('change',loadHero);

  // 再生ボタン → 動画のポップアップ
  var play=document.querySelector('.hero-play');
  var modal=document.getElementById('video-modal');
  if(play&&modal){
    var mv=modal.querySelector('video'), closeBtn=modal.querySelector('.video-modal__close');
    function open(){mv.src=play.dataset.video;modal.hidden=false;var p=mv.play();if(p&&p.catch)p.catch(function(){});setTimeout(function(){closeBtn.focus();},0);}
    function close(){mv.pause();mv.removeAttribute('src');mv.load();modal.hidden=true;play.focus();}
    play.addEventListener('click',open);
    closeBtn.addEventListener('click',close);
    modal.addEventListener('click',function(e){if(e.target===modal) close();});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!modal.hidden) close();});
  }

  // プロジェクトのカルーセル（左右ボタンで1枚ずつ送る。端はつながってぐるっと回る）
  document.querySelectorAll('[data-carousel]').forEach(function(root){
    var cards=[].slice.call(root.querySelectorAll('.pcar__card'));
    var n=cards.length, cur=0, prevD=[];
    function step(){
      var cs=getComputedStyle(root);
      return cards[0].getBoundingClientRect().width+parseFloat(cs.getPropertyValue('--gap'));
    }
    function render(animate){
      var s=step();
      cards.forEach(function(c,i){
        var d=((i-cur)%n+n)%n; if(d>n/2) d-=n;           // -3..2 の範囲に
        var jump=prevD[i]!==undefined&&Math.abs(d-prevD[i])>1; // 反対側へ回り込むカードはアニメなし
        c.style.transition=(!animate||jump||reduce)?'none':'';
        c.style.transform='translateX('+(d*s)+'px)';
        c.setAttribute('aria-hidden',d===0?'false':'true');
        prevD[i]=d;
      });
    }
    function go(k){cur=(cur+k+n)%n;render(true);}
    root.querySelector('.pcar__btn--prev').addEventListener('click',function(){go(-1);});
    root.querySelector('.pcar__btn--next').addEventListener('click',function(){go(1);});
    // スワイプ
    var sx=null,sy=null;
    root.addEventListener('touchstart',function(e){sx=e.touches[0].clientX;sy=e.touches[0].clientY;},{passive:true});
    root.addEventListener('touchend',function(e){
      if(sx===null) return;
      var dx=e.changedTouches[0].clientX-sx, dy=e.changedTouches[0].clientY-sy;
      if(Math.abs(dx)>40&&Math.abs(dx)>Math.abs(dy)) go(dx<0?1:-1);
      sx=null;
    },{passive:true});
    render(false);
    window.addEventListener('resize',function(){render(false);});
  });

  // パララックス（背景と小さい写真がスクロールに合わせて少しずれる）
  var plx=[].slice.call(document.querySelectorAll('.plx'));
  if(plx.length&&!reduce){
    var ticking=false;
    function update(){
      ticking=false;
      var vh=window.innerHeight;
      plx.forEach(function(sec){
        var r=sec.getBoundingClientRect();
        if(r.bottom<-200||r.top>vh+200) return;
        // -1（画面の下）〜 1（画面の上）
        var p=((r.top+r.height/2)-vh/2)/((vh+r.height)/2);
        p=Math.max(-1,Math.min(1,p));
        sec.querySelector('.plx__bg').style.transform='translate3d(0,'+(p*110).toFixed(1)+'px,0)';
        sec.querySelectorAll('.plx__item img').forEach(function(img){
          img.style.transform='translate3d(0,'+(-p*10).toFixed(1)+'px,0)';
        });
      });
    }
    window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(update);}},{passive:true});
    window.addEventListener('resize',update);
    update();
  }
})();
