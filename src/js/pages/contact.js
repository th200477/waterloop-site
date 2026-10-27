// /contact：「お問い合わせフォームを開く」でフォームを開閉する。JSが無いときはフォームが最初から見えている。
(function(){
  var btn=document.querySelector('[data-contact-open]');
  var form=document.getElementById('contact-form');
  if(!btn||!form) return;
  form.hidden=true;
  btn.addEventListener('click',function(e){
    e.preventDefault();
    var open=form.hidden;
    form.hidden=!open;
    btn.setAttribute('aria-expanded',open?'true':'false');
    if(open){var f=form.querySelector('input:not([type=hidden]):not([name=bot-field])');if(f)f.focus({preventScroll:true});form.scrollIntoView({behavior:'smooth',block:'start'});}
  });
})();
