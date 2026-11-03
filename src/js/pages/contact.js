// /contact のフォーム：入力 → 確認 → 送信完了。送信先は Google Apps Script（tools/contact_gas）。
(function(){
  // GASを公開したら、そのURLに書き換える。仮のままだと送ったことにして完了画面を出す（確認用）。
  var GAS_URL = 'https://script.google.com/macros/s/AKfycbwk_FzL0PN-tHVqNijr4qn69r9t6C9TI8A1KJ1ckeLqLlO66d-28KgKio8-_oDgFdTm/exec';
  var MIN_MS = 3000;
  var form = document.getElementById('cf'); if(!form) return;
  var confirmBox = document.getElementById('cf-confirm'), doneBox = document.getElementById('cf-done');
  var list = document.getElementById('cf-confirm-list'), err = document.getElementById('cf-error'), sendErr = document.getElementById('cf-send-error');
  var sendBtn = document.getElementById('cf-send'), steps = document.querySelectorAll('.cf-steps li');
  var loadedAt = Date.now();
  var TYPES = {trip:'旅行・研修に組み込みたい', make:'一緒に商品やサービスをつくりたい', press:'取材・講演の依頼', other:'その他'};
  var FIELDS = [['type','相談の種類'],['content','相談したいコンテンツ'],['name','お名前'],['org','会社・団体名'],['email','メールアドレス'],['tel','電話番号'],['message','内容']];

  // CONTENTS詳細の「相談する」から来たとき：?c=<slug>&t=trip|make
  var q = new URLSearchParams(location.search), names = window.CONTENT_NAMES || {};
  var c = q.get('c'), t = q.get('t');
  if(c){ var row = document.getElementById('cf-content-row'); row.hidden = false; form.content.value = names[c] || c; }
  if(t && TYPES[t]) form.type.value = t;

  function step(name){
    steps.forEach(function(li){ li.classList.toggle('is-on', li.dataset.step === name); });
    form.hidden = name !== 'input'; confirmBox.hidden = name !== 'confirm'; doneBox.hidden = name !== 'done';
    var top = document.querySelector('.cf-steps').getBoundingClientRect().top + scrollY - 120;
    scrollTo({top: Math.max(0, top), behavior: 'smooth'});
  }
  function val(k){ return (form[k] && form[k].value || '').trim(); }

  form.addEventListener('submit', function(e){
    e.preventDefault(); err.textContent = '';
    var bad = [];
    [['type','相談の種類'],['name','お名前'],['email','メールアドレス'],['message','内容']].forEach(function(f){
      var el = form[f[0]], ng = !val(f[0]) || (f[0] === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val('email')));
      el.setAttribute('aria-invalid', ng ? 'true' : 'false'); if(ng) bad.push(f[1]);
    });
    if(bad.length){ err.textContent = bad.join('・') + 'を入力してください。'; return; }
    if(!form.agree.checked){ err.textContent = 'プライバシーポリシーへの同意をお願いします。'; return; }
    list.innerHTML = '';
    FIELDS.forEach(function(f){
      var v = f[0] === 'type' ? TYPES[val('type')] : val(f[0]); if(!v) return;
      var d = document.createElement('div'), dt = document.createElement('dt'), dd = document.createElement('dd');
      dt.textContent = f[1]; dd.textContent = v; d.appendChild(dt); d.appendChild(dd); list.appendChild(d);
    });
    step('confirm');
  });
  document.getElementById('cf-back').addEventListener('click', function(){ sendErr.textContent = ''; step('input'); });

  sendBtn.addEventListener('click', function(){
    sendErr.textContent = '';
    if(val('website')) { step('done'); return; }            // 機械の送信は黙って捨てる
    if(Date.now() - loadedAt < MIN_MS){ sendErr.textContent = '少し時間をおいて、もう一度お試しください。'; return; }
    var data = {type: TYPES[val('type')], content: val('content'), name: val('name'), org: val('org'), email: val('email'), tel: val('tel'), message: val('message'), website: val('website'), elapsed: Date.now() - loadedAt, page: location.href};
    sendBtn.disabled = true; sendBtn.textContent = '送信しています…';
    var done = function(){ sendBtn.disabled = false; sendBtn.textContent = 'この内容で送信する'; form.reset(); step('done'); doneBox.focus({preventScroll:true}); };
    if(GAS_URL.indexOf('REPLACE') === 0){ setTimeout(done, 600); return; }
    fetch(GAS_URL, {method:'POST', mode:'no-cors', headers:{'Content-Type':'text/plain;charset=utf-8'}, body: JSON.stringify(data)})
      .then(done)
      .catch(function(){ sendBtn.disabled = false; sendBtn.textContent = 'この内容で送信する'; sendErr.textContent = '送信できませんでした。通信の状態をご確認のうえ、もう一度お試しください。'; });
  });
})();
