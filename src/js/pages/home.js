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

  // パララックスは共通の仕組み（main.js の data-parallax）。PC の1つ目の背景 0.85、写真3枚の列 1.05（今のサイトと同じ）

  // COLUMNS の上の DOBADOBA マーク：画面の下から入ってきて、自分の高さぶん進むあいだに 1 → 1.3 倍（スマホは 1.1 倍）。
  // 今のサイトの「スクロールで変形（このレイヤーが見えたら）」と同じ計算。値が変わるたびに 0.8 秒の ease-out-back で追いかける（CSS）。
  var dob=document.querySelector('.dobadoba');
  if(dob&&!reduce){
    var pc=window.matchMedia('(min-width: 1200px)'), sp=window.matchMedia('(max-width: 767px)');
    var dt=false;
    function dobUpdate(){
      dt=false;
      var h=dob.offsetHeight, top=0, e=dob;
      while(e){ top+=e.offsetTop; e=e.offsetParent; }   // 変形を含まない位置
      if(pc.matches) top+=h/2;                           // 今のサイトの PC 版はマークの枠が上に半分ずれていて、その分だけ遅れて始まる
      var p=(window.pageYOffset+window.innerHeight-top)/h; p=Math.max(0,Math.min(1,p));
      var to=sp.matches?1.1:1.3;
      dob.style.scale=(1+(to-1)*p).toFixed(4);
    }
    window.addEventListener('scroll',function(){ if(!dt){dt=true;requestAnimationFrame(dobUpdate);} },{passive:true});
    window.addEventListener('resize',dobUpdate);
    dobUpdate();
  }

  // WATER LOOP の流れる文字：今のサイトと同じ 50px/秒 で左へ
  var mqTrack=document.querySelector('.marquee__track');
  if(mqTrack){
    function mqSpeed(){ var w=mqTrack.scrollWidth/2; if(w>0) mqTrack.style.animationDuration=(w/50).toFixed(2)+'s'; }
    mqSpeed(); window.addEventListener('resize',mqSpeed);
    if(document.fonts&&document.fonts.ready) document.fonts.ready.then(mqSpeed);
  }
})();
