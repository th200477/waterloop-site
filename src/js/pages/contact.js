// /contact
// 1) 「お問い合わせフォームを開く」でフォームを開閉する（JSが無いときはフォームが最初から見えている）。
// 2) 送信は form の action（FORM_ENDPOINT を実際のURLに差し替える）へ fetch で送り、成功したら data-thanks（/contact/thanks）へ移る。
//    JSが無いときは通常のPOSTになる（その場合の移動先は送信先サービスの設定、または hidden の _next で指定）。
(function(){
  var btn=document.querySelector('[data-contact-open]');
  var form=document.getElementById('contact-form');
  if(!form) return;
  if(btn){
    form.hidden=true;
    btn.addEventListener('click',function(e){
      e.preventDefault();
      var open=form.hidden;
      form.hidden=!open;
      btn.setAttribute('aria-expanded',open?'true':'false');
      if(open){var f=form.querySelector('input:not([type=hidden]):not([name=bot-field])');if(f)f.focus({preventScroll:true});form.scrollIntoView({behavior:'smooth',block:'start'});}
    });
  }
  var submit=form.querySelector('[type=submit]');
  var status=form.querySelector('[data-status]');
  function say(msg){ if(status){ status.textContent=msg; } }
  form.addEventListener('submit',function(e){
    if(!window.fetch||!window.FormData) return; // 古いブラウザは通常のPOST
    e.preventDefault();
    var thanks=(window.__BASE__||'')+(form.getAttribute('data-thanks')||'/contact/thanks');
    var bot=form.querySelector('[name=bot-field]');
    if(bot&&bot.value){ location.href=thanks; return; } // ボットらしい送信は送らない
    var endpoint=form.getAttribute('action')||'';
    if(!endpoint||endpoint==='FORM_ENDPOINT'){ say('送信先が設定されていません。お手数ですが info@waterloop.jp までご連絡ください。'); return; }
    var data=new FormData(form); data.delete('bot-field');
    if(submit){ submit.disabled=true; }
    say('送信しています…');
    fetch(endpoint,{method:'POST',body:data,headers:{'Accept':'application/json'}})
      .then(function(r){ if(!r.ok) throw new Error(r.status); location.href=thanks; })
      .catch(function(){ if(submit){ submit.disabled=false; } say('送信できませんでした。時間をおいて再度お試しいただくか、info@waterloop.jp までご連絡ください。'); });
  });
})();
