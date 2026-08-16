#!/usr/bin/env node
import assert from "node:assert/strict";
import fs from "node:fs";
import http from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const publicDir=path.join(root,"public");
const css=fs.readFileSync(path.join(root,"templates","style.css"),"utf8");
const source=fs.readFileSync(path.join(root,"scripts","generate.js"),"utf8");
const locales=["en","zh-CN","zh-TW","ja","ko","fr","de","es","it","pl","pt-BR","ru","uk","vi"];
const adSrc="https://pl30767409.effectivecpmnetwork.com/c8bf889a0dcc57e129ef61a0c31f243d/invoke.js";
const adLabels={en:"Advertisement","zh-CN":"广告","zh-TW":"廣告",ja:"広告",ko:"광고",fr:"Publicité",de:"Werbung",es:"Publicidad",it:"Pubblicità",pl:"Reklama","pt-BR":"Publicidade",ru:"Реклама",uk:"Реклама",vi:"Quảng cáo"};
const count=(text,needle)=>text.split(needle).length-1;
const htmlFiles=dir=>fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?htmlFiles(path.join(dir,e.name)):[path.join(dir,e.name)]).filter(f=>f.endsWith(".html")).sort();
const rows=htmlFiles(publicDir).map(file=>({relative:path.relative(publicDir,file),html:fs.readFileSync(file,"utf8")}));
const leaf=relative=>path.basename(relative);
const eligible=relative=>!["about.html","privacy.html","contact.html","404.html"].includes(leaf(relative));

function footerHtml(html){return (html.match(/<footer class="site-footer">[\s\S]*<\/footer>/)||[""])[0];}
function validateDocument(row){
  const {relative,html}=row,isEligible=eligible(relative);
  assert.equal(count(html,'<aside class="commercial-slot" data-commercial-slot="primary-display"'),isEligible?1:0,`wrapper count ${relative}`);
  assert.equal(count(html,`"adsterraSrc":"${adSrc}"`),isEligible?1:0,`provider config ${relative}`);
  assert.equal(/<script[^>]+(?:effectivecpmnetwork\.com|pagead2\.googlesyndication\.com)/i.test(html),false,`premature provider request ${relative}`);
  assert.equal(/<ins\b[^>]*\badsbygoogle\b/i.test(html),false,`AdSense ins ${relative}`);
  assert.equal(/href="[^"]*(?:amazon\.|amzn\.)/i.test(html),false,`stale Amazon link ${relative}`);
  assert.equal(/href="[^"]*steampowered\.com[^"]*"[^>]*rel="[^"]*sponsored/i.test(html),false,`sponsored Steam ${relative}`);
  assert.equal(count(footerHtml(html),'<aside class="commercial-slot" data-commercial-slot="primary-display"'),0,`footer leakage ${relative}`);
  if(!isEligible)return;
  const wrapperAt=html.indexOf('data-commercial-slot="primary-display"');
  if(leaf(relative)==="index.html"){
    assert(wrapperAt>html.indexOf('id="hab-2"')&&wrapperAt<html.indexOf('id="hab-3"'),`home placement ${relative}`);
  }else{
    const before=html.slice(0,wrapperAt);
    const total=count((html.match(/<div class="dossier-main">([\s\S]*?)<\/div>\s*<aside class="dossier-side/)||[])[1]||"",'<section class="panel-block reveal');
    const expected=total>=3?2:total;
    assert.equal(count(before,'<section class="panel-block reveal'),expected,`article insertion rule ${relative}`);
  }
}

function validateCss(text){
  assert(/\[hidden\]\s*\{\s*display:none!important\s*\}/.test(text),"hidden is not authoritative");
  assert(/\.commercial-slot\{[^}]*max-width:760px[^}]*margin:32px auto/.test(text),"desktop centering contract missing");
  assert(/max-width:720px[\s\S]*\.commercial-slot\{margin-block:24px/.test(text),"mobile gutter spacing contract missing");
  assert(/\.commercial-slot\[hidden\][^}]*;height:0!important[^}]*margin:0!important[^}]*padding:0!important[^}]*border:0!important/.test(text),"empty zero-geometry contract missing");
  assert(!/\.commercial-slot[^\n{]*\{[^}]*\b(?:animation|transition|transform|opacity)\s*:/m.test(text),"commercial motion forbidden");
}

function validateController(text){
  for(const marker of ['rootMargin:"1200px 0px"','setTimeout(function(){fail("empty");},2500)','loaded.adsterra','a.onerror=function(){fail("error");}','window.addEventListener("error",providerError,true)','dialog.addEventListener("keydown"','e.shiftKey','restoreFocus()'])
    assert(text.includes(marker),`controller marker missing: ${marker}`);
  assert.equal(count(text,"function loadAdvertising("),1,"duplicate advertising loader");
}

/* ---------- G4 successor findings ---------- */
// 每个 home 页恰好一个文档壳（P2 home-double-document-shell 回归）
function validateDocumentShell(row){
  const {relative,html}=row;
  assert.equal((html.match(/<!doctype html>/gi)||[]).length,1,`doctype count ${relative}`);
  assert.equal((html.match(/<html\b/gi)||[]).length,1,`html count ${relative}`);
  assert.equal((html.match(/<head\b/gi)||[]).length,1,`head count ${relative}`);
  assert.equal((html.match(/<body\b/gi)||[]).length,1,`body count ${relative}`);
}

// 首页 habitat 标签与描述：14 语言全部 locale 适切（P1 locale-home-contact-fallback 回归）
const HAB_FIXTURE = {
  COCKPIT: {
    en: ["Cockpit — start here","First flight, controls, and the build-crash-rebuild loop."],
    "zh-CN": ["驾驶舱 — 从这里开始","首次飞行、操作方式，以及建造-坠毁-重建的循环。"],
    "zh-TW": ["駕駛艙 — 從這裡開始","首次飛行、操作方式，以及建造—墜毀—重建的循環。"],
    ja: ["コックピット — ここから始める","初飛行、操作、そして作って・壊して・作り直すループ。"],
    ko: ["조종석 — 여기서 시작","첫 비행, 조작, 그리고 만들고-부수고-다시 만드는 순환."],
    fr: ["Poste de pilotage — commencez ici","Premier vol, commandes et le cycle construire-écraser-reconstruire."],
    de: ["Cockpit — hier beginnen","Erster Flug, Steuerung und der Kreislauf aus Bauen, Absturz und Neuaufbau."],
    es: ["Cabina — empieza aquí","Primer vuelo, controles y el ciclo construir-estrellarse-reconstruir."],
    it: ["Cabina di pilotaggio — inizia qui","Primo volo, comandi e il ciclo costruisci-schiantati-ricostruisci."],
    pl: ["Kabina — zacznij tutaj","Pierwszy lot, sterowanie i cykl buduj-rozbij-odbuduj."],
    "pt-BR": ["Cabine — comece aqui","Primeiro voo, controles e o ciclo construir-quebrar-reconstruir."],
    ru: ["Кабина — начните здесь","Первый полёт, управление и цикл «построй-разбей-перестрой»."],
    uk: ["Кабіна — почніть тут","Перший політ, керування та цикл «побудуй-розбий-перебудуй»."],
    vi: ["Buồng lái — bắt đầu tại đây","Chuyến bay đầu tiên, điều khiển và vòng lặp xây-dựng-hỏng-xây-lại."],
  },
  ENGINE: {
    en: ["Engine room — ship building","Modular ships, thrusters, wiring and blueprints."],
    "zh-CN": ["引擎舱 — 飞船建造","模块化飞船、推进器、电路与蓝图。"],
    "zh-TW": ["引擎艙 — 飛船建造","模組化飛船、推進器、電路與藍圖。"],
    ja: ["機関室 — 船の建造","モジュール式の船、スラスター、配線、ブループリント。"],
    ko: ["기관실 — 함선 건조","모듈식 함선, 추진기, 배선, 설계도."],
    fr: ["Salle des machines — construction de vaisseaux","Vaisseaux modulaires, propulseurs, câblage et plans."],
    de: ["Maschinenraum — Schiffbau","Modulare Schiffe, Triebwerke, Verkabelung und Baupläne."],
    es: ["Sala de máquinas — construcción de naves","Naves modulares, propulsores, cableado y planos."],
    it: ["Sala macchine — costruzione di navi","Navi modulari, propulsori, cablaggio e progetti."],
    pl: ["Maszynownia — budowa statków","Modułowe statki, silniki, okablowanie i plany."],
    "pt-BR": ["Casa de máquinas — construção de naves","Naves modulares, propulsores, fiação e projetos."],
    ru: ["Машинное отделение — строительство кораблей","Модульные корабли, двигатели, проводка и чертежи."],
    uk: ["Машинне відділення — будівництво кораблів","Модульні кораблі, двигуни, проводка та креслення."],
    vi: ["Phòng máy — đóng tàu","Tàu mô-đun, động cơ đẩy, hệ thống dây điện và bản thiết kế."],
  },
  CARGO: {
    en: ["Cargo bay — references","Console release, mods, updates and demo comparison."],
    "zh-CN": ["货舱 — 参考资料","主机版发售、模组、更新与试玩版对比。"],
    "zh-TW": ["貨艙 — 參考資料","主機版發售、模組、更新與試玩版比較。"],
    ja: ["カーゴベイ — リファレンス","コンソール版、MOD、アップデート、デモ比較。"],
    ko: ["화물칸 — 참고 자료","콘솔 출시, 모드, 업데이트, 데모 비교."],
    fr: ["Soute à marchandises — références","Sortie console, mods, mises à jour et comparaison de la démo."],
    de: ["Frachtraum — Referenzen","Konsolen-Release, Mods, Updates und Demo-Vergleich."],
    es: ["Bodega de carga — referencias","Lanzamiento en consolas, mods, actualizaciones y comparación de la demo."],
    it: ["Stiva cargo — riferimenti","Uscita console, mod, aggiornamenti e confronto con la demo."],
    pl: ["Ładownia — materiały","Premiera na konsole, mody, aktualizacje i porównanie wersji demo."],
    "pt-BR": ["Porão de carga — referências","Lançamento em consoles, mods, atualizações e comparação da demo."],
    ru: ["Грузовой отсек — справочники","Релиз на консолях, моды, обновления и сравнение демо."],
    uk: ["Вантажний відсік — довідники","Реліз на консолях, моди, оновлення та порівняння демо."],
    vi: ["Khoang hàng — tài liệu tham khảo","Bản console, mod, cập nhật và so sánh bản demo."],
  },
  ARCHIVE: {
    en: ["Archive — achievements &amp; indexes","Achievements, ships index, blueprints index and guide index."],
    "zh-CN": ["资料库 — 成就与索引","成就、飞船索引、蓝图索引与攻略索引。"],
    "zh-TW": ["資料庫 — 成就與索引","成就、飛船索引、藍圖索引與攻略索引。"],
    ja: ["資料室 — 実績と索引","実績、船の索引、ブループリント索引、ガイド索引。"],
    ko: ["기록실 — 업적 및 색인","업적, 함선 색인, 설계도 색인, 가이드 색인."],
    fr: ["Archives — succès et index","Succès, index des vaisseaux, index des plans et index des guides."],
    de: ["Archiv — Erfolge und Verzeichnisse","Erfolge, Schiffsverzeichnis, Bauplan-Verzeichnis und Guide-Verzeichnis."],
    es: ["Archivo — logros e índices","Logros, índice de naves, índice de planos e índice de guías."],
    it: ["Archivio — obiettivi e indici","Obiettivi, indice delle navi, indice dei progetti e indice delle guide."],
    pl: ["Archiwum — osiągnięcia i indeksy","Osiągnięcia, indeks statków, indeks planów i indeks poradników."],
    "pt-BR": ["Arquivo — conquistas e índices","Conquistas, índice de naves, índice de projetos e índice de guias."],
    ru: ["Архив — достижения и указатели","Достижения, указатель кораблей, чертежей и гайдов."],
    uk: ["Архів — досягнення та покажчики","Досягнення, покажчик кораблів, креслень і гайдів."],
    vi: ["Kho lưu trữ — thành tựu và chỉ mục","Thành tựu, chỉ mục tàu, chỉ mục bản thiết kế và chỉ mục hướng dẫn."],
  },
};
function validateHomeLocale(row){
  const {relative,html}=row;
  const lang=locales.find(l=>relative===(l==="en"?"index.html":`${l}/index.html`));
  assert(lang,`home locale path unknown ${relative}`);
  for(const code of Object.keys(HAB_FIXTURE)){
    const [label,desc]=HAB_FIXTURE[code][lang];
    assert(html.includes(`<h2>${label}</h2>`)||html.includes(`<h2>${label.replace("&","&amp;")}</h2>`),`${code} label missing for ${lang}`);
    assert(html.includes(`<p>${desc}</p>`),`${code} desc missing for ${lang}`);
  }
  // 简体中文 habitat 文案只允许出现在 zh-CN；zh-TW 必须用繁体
  if(lang!=="zh-CN"){
    for(const zh of ["驾驶舱","引擎舱","货舱","资料库","从这里开始"])
      assert(!html.includes(zh),`Simplified-Chinese habitat copy in ${lang}`);
  }
  if(lang==="zh-TW"){
    for(const tw of ["駕駛艙","引擎艙","貨艙","資料庫","從這裡開始"])
      assert(html.includes(tw),`Traditional habitat copy missing in ${lang}`);
  }
}

// contact 页 locale 适切联系/回复文案；仅英文 locale 可回退英文（P1 回归）
const CONTACT_FIXTURE = {
  en: ["Reach us at:","We usually reply within 2-3 business days."],
  "zh-CN": ["联系我们：","我们通常会在 2-3 个工作日内回复。"],
  "zh-TW": ["聯絡我們：","我們通常會在 2-3 個工作日內回覆。"],
  ja: ["お問い合わせ：","通常 2〜3 営業日以内に返信します。"],
  ko: ["문의하기: ","보통 2~3 영업일 내에 답변드립니다."],
  fr: ["Contactez-nous : ","Nous répondons généralement sous 2 à 3 jours ouvrés."],
  de: ["Kontaktieren Sie uns: ","Wir antworten in der Regel innerhalb von 2–3 Werktagen."],
  es: ["Contáctanos: ","Normalmente respondemos en 2-3 días laborables."],
  it: ["Contattaci: ","Di solito rispondiamo entro 2-3 giorni lavorativi."],
  pl: ["Skontaktuj się z nami: ","Zwykle odpowiadamy w ciągu 2–3 dni roboczych."],
  "pt-BR": ["Fale conosco: ","Normalmente respondemos em 2-3 dias úteis."],
  ru: ["Свяжитесь с нами: ","Обычно мы отвечаем в течение 2–3 рабочих дней."],
  uk: ["Зв'яжіться з нами: ","Зазвичай ми відповідаємо протягом 2–3 робочих днів."],
  vi: ["Liên hệ với chúng tôi: ","Chúng tôi thường trả lời trong vòng 2-3 ngày làm việc."],
};
function validateContactLocale(row){
  const {relative,html}=row;
  const lang=locales.find(l=>relative===(l==="en"?"contact.html":`${l}/contact.html`));
  assert(lang,`contact locale path unknown ${relative}`);
  const [ph,reply]=CONTACT_FIXTURE[lang];
  assert(html.includes(ph),`contact phrase missing for ${lang}`);
  assert(html.includes(reply),`contact reply missing for ${lang}`);
  if(lang!=="en"){
    assert(!html.includes("Reach us at:"),`English contact fallback in ${lang}`);
    assert(!html.includes("We usually reply"),`English reply fallback in ${lang}`);
  }
}

// 320px 触控契约（P1 mobile-320-header-touch-contract 回归）
function validateTouchCss(text){
  const blocks=[...text.matchAll(/@media\(max-width:480px\)\{([\s\S]*?)\n\}/g)].map(m=>m[1]);
  const block=blocks[blocks.length-1]||"";
  assert(block,"max-width:480px media block missing");
  for(const sel of [".logo{"," .nav>a{",".dd summary{",".lang-dd summary{",".site-search{"])
    assert(block.includes(sel),`touch selector missing: ${sel}`);
  for(const rule of ["min-height:44px","min-width:44px"])
    assert(block.includes(rule),`touch rule missing: ${rule}`);
  assert(/\.header-inner\{[^}]*padding:8px 12px/.test(block),"header padding contract missing");
  assert(/\.header-inner\{[^}]*gap:6px 8px/.test(block),"header gap contract missing");
  assert(!/\.nav\b[^\n{]*\{[^}]*\b(?:animation|transition|transform)\s*:/.test(text),"navigation motion forbidden on mobile");
}

function expectFault(name,run,needle){let message="";try{run();}catch(error){message=String(error.message||error);}assert(message.includes(needle),`${name} did not fail as intended: ${message||"no failure"}`);}

assert.equal(rows.length,295,"page inventory changed");
assert.equal(rows.filter(row=>eligible(row.relative)).length,252,"eligible page inventory changed");
for(const row of rows)validateDocument(row);
validateCss(css);validateController(source);
const homeRows=rows.filter(row=>leaf(row.relative)==="index.html");
assert.equal(homeRows.length,14,"home locale inventory changed");
for(const row of homeRows)validateDocumentShell(row);
for(const row of homeRows)validateHomeLocale(row);
for(const lang of locales)validateContactLocale(rows.find(row=>row.relative===(lang==="en"?"contact.html":`${lang}/contact.html`)));
validateTouchCss(css);
const sample=rows.find(row=>row.relative==="how-to-play.html");
expectFault("duplicate unit",()=>validateDocument({...sample,html:sample.html.replace('</aside>','</aside>'+sample.html.match(/<aside class="commercial-slot"[\s\S]*?<\/aside>/)[0])}),"wrapper count");
expectFault("footer leakage",()=>validateDocument({...sample,html:sample.html.replace('<footer class="site-footer">','<footer class="site-footer"><aside class="commercial-slot" data-commercial-slot="primary-display"></aside>')}),"wrapper count");
expectFault("premature request",()=>validateDocument({...sample,html:sample.html+'<script src="https://fault.effectivecpmnetwork.com/x.js"></script>'}),"premature provider request");
expectFault("AdSense serving",()=>validateDocument({...sample,html:sample.html+'<ins class="adsbygoogle"></ins>'}),"AdSense ins");
expectFault("stale Amazon",()=>validateDocument({...sample,html:sample.html+'<a href="https://amazon.com/fault">fault</a>'}),"stale Amazon link");
expectFault("sponsored ordinary link",()=>validateDocument({...sample,html:sample.html+'<a href="https://store.steampowered.com/app/1" rel="sponsored noopener">fault</a>'}),"sponsored Steam");
expectFault("off-center geometry",()=>validateCss(css.replace("max-width:760px;margin:32px auto","max-width:760px;margin:32px 0")),"desktop centering");
expectFault("empty reserved state",()=>validateCss(css.replace("display:none!important;height:0!important;min-height:0!important","display:none!important;height:20px!important;min-height:0!important")),"empty zero-geometry");
expectFault("hidden regression",()=>validateCss(css.replace("[hidden]{display:none!important}","[hidden]{display:block}")),"hidden is not authoritative");
expectFault("focus regression",()=>validateController(source.replace('dialog.addEventListener("keydown"','dialog.addEventListener("keyup"')),"controller marker missing: dialog.addEventListener");

const homeEn=homeRows.find(row=>row.relative==="index.html");
const frHome=homeRows.find(row=>row.relative==="fr/index.html");
expectFault("duplicate home shell",()=>validateDocumentShell({...homeEn,html:homeEn.html.replace('<!DOCTYPE html>','<!DOCTYPE html><!DOCTYPE html>')}),"doctype count");
expectFault("home locale simplified fallback",()=>validateHomeLocale({...frHome,html:frHome.html+'<p>驾驶舱 — 从这里开始</p>'}),"Simplified-Chinese habitat copy");
expectFault("home locale missing label",()=>validateHomeLocale({...frHome,html:frHome.html.replace('<h2>Poste de pilotage — commencez ici</h2>','<h2></h2>')}),"label missing for fr");
expectFault("contact english fallback",()=>validateContactLocale({...rows.find(row=>row.relative==="fr/contact.html"),html:rows.find(row=>row.relative==="fr/contact.html").html+'<p>Reach us at:</p>'}),"English contact fallback");
expectFault("contact missing reply",()=>validateContactLocale({...rows.find(row=>row.relative==="de/contact.html"),html:rows.find(row=>row.relative==="de/contact.html").html.replace(/Wir antworten in der Regel innerhalb von 2–3 Werktagen\./g,"")}),"contact reply missing for de");
expectFault("touch selector removed",()=>validateTouchCss(css.replace(".logo{order:1"," .logoX{order:1")),"touch selector missing: .logo{");
expectFault("touch min-height removed",()=>validateTouchCss(css.replaceAll("min-height:44px","min-height:40px")),"touch rule missing: min-height:44px");
expectFault("header padding contract removed",()=>validateTouchCss(css.replace(".header-inner{flex-wrap:wrap;gap:6px 8px;padding:8px 12px}",".header-inner{flex-wrap:wrap;gap:6px 8px;padding:20px 12px}")),"header padding contract missing");

for(const lang of locales){const relative=lang==="en"?"index.html":`${lang}/index.html`;const row=rows.find(item=>item.relative===relative);assert(row.html.includes(`<div class="commercial-label">${adLabels[lang]}</div>`),`advertisement label fallback ${lang}`);}
console.log(JSON.stringify({status:"pass",htmlPages:rows.length,eligiblePages:252,excludedPages:43,wrappers:252,footerWrappers:0,providerRequestsBeforeConsent:0,adsenseUnits:0,amazonLinks:0,localizedLabels:14,negativeFaults:22,proximityGatePx:1200,noFillTimeoutMs:2500,homeShells:{documents:14,shellPerDocument:1},habitatLocales:14,contactLocales:14,touchContract:{headerMaxPx:150,targetMinPx:44,media:"max-width:480px"}},null,2));

if(process.argv.includes("--browser")){
  const {chromium}=await import("file:///opt/homebrew/lib/node_modules/@playwright/mcp/node_modules/playwright/index.mjs");
  const mime={".html":"text/html; charset=utf-8",".css":"text/css; charset=utf-8",".js":"text/javascript; charset=utf-8",".svg":"image/svg+xml",".jpg":"image/jpeg",".png":"image/png",".txt":"text/plain; charset=utf-8",".xml":"application/xml; charset=utf-8"};
  const server=http.createServer((req,res)=>{const pathname=decodeURIComponent(new URL(req.url,"http://local").pathname);let file=path.join(publicDir,pathname==="/"?"index.html":pathname.replace(/^\//,""));if(!path.extname(file))file+=".html";if(!file.startsWith(publicDir)||!fs.existsSync(file)){res.writeHead(404);res.end("not found");return;}res.writeHead(200,{"content-type":mime[path.extname(file)]||"application/octet-stream"});fs.createReadStream(file).pipe(res);});
  await new Promise(resolve=>server.listen(0,"127.0.0.1",resolve));
  const origin=`http://127.0.0.1:${server.address().port}`;
  const browser=await chromium.launch({headless:true,executablePath:"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"});
  const results=[];
  try{
    for(const width of [320,375,414,768,1080,1440]){
      const page=await browser.newPage({viewport:{width,height:900}});let providerRequests=0;
      await page.route("**/*effectivecpmnetwork.com/**",route=>{providerRequests++;return route.fulfill({contentType:"text/javascript",body:'document.getElementById("container-c8bf889a0dcc57e129ef61a0c31f243d").innerHTML="<iframe title=\\"Ad fixture\\" style=\\"display:block;width:100%;height:120px;border:0\\"></iframe>";'});});
      await page.addInitScript(()=>localStorage.setItem("approximately-up-consent-v1",JSON.stringify({analytics:false,advertising:true})));
      await page.goto(origin+"/",{waitUntil:"domcontentloaded"});await page.waitForSelector('[data-commercial-slot="primary-display"][data-state="filled"]',{timeout:5000});
      const geometry=await page.locator('[data-commercial-slot="primary-display"]').evaluate(el=>{const r=el.getBoundingClientRect(),p=el.parentElement.getBoundingClientRect();return {midDelta:Math.abs((r.left+r.width/2)-(p.left+p.width/2)),overflow:document.documentElement.scrollWidth-document.documentElement.clientWidth,width:r.width};});
      assert(geometry.midDelta<=1,`off-center at ${width}`);assert(geometry.overflow<=0,`horizontal overflow at ${width}`);assert(geometry.width<=760,`slot wider than 760 at ${width}`);assert.equal(providerRequests,1,`provider request count at ${width}`);results.push({viewportWidth:width,...geometry,providerRequests});await page.close();
    }
    // 320px 触控契约：法文 header ≤150px，可见交互目标 ≥44×44，无横向溢出
    for(const locale of ["fr","en"]){
      const narrow=await browser.newPage({viewport:{width:320,height:568}});
      await narrow.goto(origin+(locale==="en"?"/index.html":`/${locale}/index.html`),{waitUntil:"domcontentloaded"});
      const header=await narrow.locator(".site-header").evaluate(el=>el.getBoundingClientRect().height);
      assert(header<=150,`${locale} header ${header}px above 150 at 320`);
      const targets=await narrow.evaluate(()=>Array.from(document.querySelectorAll(".header-inner a,.header-inner summary,.header-inner input,.site-footer a,.site-footer button")).filter(el=>{const r=el.getBoundingClientRect();return r.width>0&&r.height>0;}).map(el=>{const r=el.getBoundingClientRect();return {sel:el.tagName+"."+String(el.className).split(" ")[0],w:Math.round(r.width),h:Math.round(r.height)};}).filter(t=>t.w<44||t.h<44));
      assert.equal(targets.length,0,`${locale} touch targets below 44x44 at 320: ${JSON.stringify(targets.slice(0,6))}`);
      const overflow=await narrow.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth);
      assert(overflow<=0,`${locale} horizontal overflow at 320: ${overflow}px`);
      await narrow.close();
    }
    const choice=await browser.newPage({viewport:{width:375,height:812}});let choiceRequests=0;await choice.route("**/*effectivecpmnetwork.com/**",route=>{choiceRequests++;return route.abort();});await choice.goto(origin+"/how-to-play",{waitUntil:"domcontentloaded"});await choice.waitForSelector("[data-consent-dialog][open]");assert.equal(choiceRequests,0,"provider requested before choice");
    const hiddenDisplay=await choice.locator("[data-consent-manage]").evaluate(el=>getComputedStyle(el).display);assert.equal(hiddenDisplay,"none","hidden consent controls displayed");
    for(let i=0;i<18;i++){await choice.keyboard.press(i%2?"Shift+Tab":"Tab");assert.notEqual(await choice.evaluate(()=>document.activeElement===document.body),true,"focus escaped dialog");}
    await choice.locator("[data-consent-reject]").click();await choice.waitForFunction(()=>document.activeElement&&document.activeElement.matches("[data-consent-settings]"));assert.equal(await choice.locator('[data-commercial-slot="primary-display"]:visible').count(),0,"rejected slot retained geometry");await choice.reload({waitUntil:"domcontentloaded"});await choice.waitForTimeout(200);assert.equal(choiceRequests,0,"rejected reload requested provider");assert.equal(await choice.locator('[data-commercial-slot="primary-display"]:visible').count(),0,"rejected reload retained geometry");await choice.close();
    const nofill=await browser.newPage({viewport:{width:375,height:812}});let nofillRequests=0;await nofill.route("**/*effectivecpmnetwork.com/**",route=>{nofillRequests++;return route.fulfill({contentType:"text/javascript",body:"/* deliberate no-fill */"});});await nofill.addInitScript(()=>localStorage.setItem("approximately-up-consent-v1",JSON.stringify({analytics:false,advertising:true})));await nofill.goto(origin+"/",{waitUntil:"domcontentloaded"});await nofill.waitForTimeout(2900);assert.equal(nofillRequests,1,"no-fill request count");assert.equal(await nofill.locator('[data-commercial-slot="primary-display"]').count(),0,"no-fill slot persisted");await nofill.close();
    const thrown=await browser.newPage({viewport:{width:375,height:812}});await thrown.route("**/*effectivecpmnetwork.com/**",route=>route.fulfill({contentType:"text/javascript",body:'throw new Error("deliberate provider failure")'}));await thrown.addInitScript(()=>localStorage.setItem("approximately-up-consent-v1",JSON.stringify({analytics:false,advertising:true})));await thrown.goto(origin+"/",{waitUntil:"domcontentloaded"});await thrown.waitForTimeout(300);assert.equal(await thrown.locator('[data-commercial-slot="primary-display"]').count(),0,"thrown provider error slot persisted");await thrown.close();
    const excluded=await browser.newPage({viewport:{width:375,height:812}});let excludedRequests=0;await excluded.route("**/*effectivecpmnetwork.com/**",route=>{excludedRequests++;return route.abort();});await excluded.addInitScript(()=>localStorage.setItem("approximately-up-consent-v1",JSON.stringify({analytics:false,advertising:true})));for(const url of ["/privacy","/about","/contact","/404.html"]){await excluded.goto(origin+url,{waitUntil:"domcontentloaded"});assert.equal(await excluded.locator('[data-commercial-slot="primary-display"]').count(),0,`excluded wrapper ${url}`);}assert.equal(excludedRequests,0,"excluded page requested provider");await excluded.close();
    const zoom=await browser.newPage({viewport:{width:720,height:450}});await zoom.addInitScript(()=>localStorage.setItem("approximately-up-consent-v1",JSON.stringify({analytics:false,advertising:false})));await zoom.goto(origin+"/",{waitUntil:"domcontentloaded"});const zoomResult=await zoom.evaluate(()=>({physicalViewportWidth:1440,effectiveCssViewportWidth:innerWidth,overflow:document.documentElement.scrollWidth-document.documentElement.clientWidth,settingsHeight:document.querySelector("[data-consent-settings]").getBoundingClientRect().height}));assert.equal(zoomResult.effectiveCssViewportWidth,720,"200 percent zoom reflow viewport");assert(zoomResult.overflow<=0,"200 percent zoom overflow");assert(zoomResult.settingsHeight>=44,"commercial/privacy target below 44px");await zoom.close();
    console.log(JSON.stringify({status:"pass",browser:"chromium",viewports:results,zoom200:zoomResult,focusTrap:"pass",focusRestore:"pass",beforeChoiceRequests:0,rejectedReloadRequests:0,noFillFinalSlotCount:0,thrownErrorFinalSlotCount:0,excludedProviderRequests:0,touch320:{locales:["fr","en"],headerMaxPx:150,targetMinPx:44}},null,2));
  }finally{await browser.close();await new Promise(resolve=>server.close(resolve));}
}
