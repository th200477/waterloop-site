/**
 * waterloop.jp お問い合わせフォームの受け口（Google Apps Script）
 * サイトから送られた内容を、スプレッドシートに1行追加し、
 * info に通知メール、相手に自動返信メールを送る。
 */
var INFO = 'info@waterloop.jp';          // 受け取り先・自動返信の差出人
var FROM_NAME = 'Water Loop Project';
var SHEET_NAME = '問い合わせ';
var SHEET_ID = '1o6oFaO50FWthKbVHRKFCtfIzwip99Pme8ws3Rej2UOY'; // スプレッドシート「waterloop.jp お問い合わせ」
var MIN_MS = 3000;                       // 開いてから3秒未満の送信は機械とみなす
var HEADER = ['受付日時', '種類', 'コンテンツ', 'お名前', '会社・団体名', 'メール', '電話', '内容', '送信元ページ'];

function doPost(e) {
  var d = {};
  try { d = JSON.parse(e.postData.contents); } catch (err) { return out_('bad'); }
  if (d.website) return out_('ok');                         // 見えない欄に入力がある＝機械
  if (!d.elapsed || Number(d.elapsed) < MIN_MS) return out_('ok');
  if (!d.name || !d.email || !d.message || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(d.email)) return out_('bad');
  var f = function (k, max) { return String(d[k] || '').slice(0, max || 200); };
  var v = { type: f('type'), content: f('content'), name: f('name'), org: f('org'), email: f('email'), tel: f('tel', 40), message: f('message', 5000), page: f('page', 300) };

  var lock = LockService.getScriptLock(); lock.waitLock(10000);
  try {
    var sh = sheet_();
    sh.appendRow([new Date(), v.type, v.content, v.name, v.org, v.email, "'" + v.tel, v.message, v.page]);
  } finally { lock.releaseLock(); }

  var summary = [
    '■ 相談の種類：' + v.type,
    v.content ? '■ 相談したいコンテンツ：' + v.content : '',
    '■ お名前：' + v.name,
    v.org ? '■ 会社・団体名：' + v.org : '',
    '■ メールアドレス：' + v.email,
    v.tel ? '■ 電話番号：' + v.tel : '',
    '■ 内容：', v.message
  ].filter(String).join('\n');

  // 1) info への通知（返信すると相手に届く）
  MailApp.sendEmail({ to: INFO, subject: '【お問い合わせ】' + v.type + '｜' + v.name + '様', replyTo: v.email, name: 'waterloop.jp フォーム',
    body: 'waterloop.jp のフォームから問い合わせが届きました。\nこのメールに返信すると、' + v.name + '様に届きます。\n\n' + summary + '\n\n送信元ページ：' + v.page });

  // 2) 相手への自動返信（このスクリプトは info の Google アカウントで動くので、差出人は info になる）
  MailApp.sendEmail({ to: v.email, subject: '【Water Loop Project】お問い合わせを受け付けました', name: FROM_NAME, replyTo: INFO, body: autoReply_(v, summary) });

  return out_('ok');
}

function autoReply_(v, summary) {
  return [
    v.name + ' 様',
    '',
    'このたびは Water Loop Project にお問い合わせいただき、ありがとうございます。',
    '以下の内容で受け付けました。',
    '内容を確認のうえ、数日以内に担当者よりご連絡いたします。',
    '',
    '──────────────',
    summary,
    '──────────────',
    '',
    '※このメールは自動でお送りしています。',
    '追加のご連絡は、このメールにそのままご返信ください。',
    '※お心当たりのない場合は、お手数ですがこのメールを破棄してください。',
    '',
    'Water Loop Project',
    'https://waterloop.jp',
    INFO
  ].join('\n');
}

function sheet_() {
  var ss = SpreadsheetApp.openById(SHEET_ID);
  var sh = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);
  if (sh.getLastRow() === 0) { sh.appendRow(HEADER); sh.setFrozenRows(1); sh.getRange(1, 1, 1, HEADER.length).setFontWeight('bold'); }
  return sh;
}

function out_(s) { return ContentService.createTextOutput(JSON.stringify({ result: s })).setMimeType(ContentService.MimeType.JSON); }

// 動作確認用：エディタでこれを実行すると、自分宛てにテストが届く（サイトは使わない）
function testSend() {
  doPost({ postData: { contents: JSON.stringify({ type: 'その他', name: 'テスト', email: INFO, message: 'テスト送信です。', elapsed: 9999, page: 'test' }) } });
}
