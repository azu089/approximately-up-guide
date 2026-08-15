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

function expectFault(name,run,needle){let message="";try{run();}catch(error){message=String(error.message||error);}assert(message.includes(needle),`${name} did not fail as intended: ${message||"no failure"}`);}

assert.equal(rows.length,295,"page inventory changed");
assert.equal(rows.filter(row=>eligible(row.relative)).length,252,"eligible page inventory changed");
for(const row of rows)validateDocument(row);
validateCss(css);validateController(source);
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

for(const lang of locales){const relative=lang==="en"?"index.html":`${lang}/index.html`;const row=rows.find(item=>item.relative===relative);assert(row.html.includes(`<div class="commercial-label">${adLabels[lang]}</div>`),`advertisement label fallback ${lang}`);}
console.log(JSON.stringify({status:"pass",htmlPages:rows.length,eligiblePages:252,excludedPages:43,wrappers:252,footerWrappers:0,providerRequestsBeforeConsent:0,adsenseUnits:0,amazonLinks:0,localizedLabels:14,negativeFaults:10,proximityGatePx:1200,noFillTimeoutMs:2500},null,2));

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
    const choice=await browser.newPage({viewport:{width:375,height:812}});let choiceRequests=0;await choice.route("**/*effectivecpmnetwork.com/**",route=>{choiceRequests++;return route.abort();});await choice.goto(origin+"/how-to-play",{waitUntil:"domcontentloaded"});await choice.waitForSelector("[data-consent-dialog][open]");assert.equal(choiceRequests,0,"provider requested before choice");
    const hiddenDisplay=await choice.locator("[data-consent-manage]").evaluate(el=>getComputedStyle(el).display);assert.equal(hiddenDisplay,"none","hidden consent controls displayed");
    for(let i=0;i<18;i++){await choice.keyboard.press(i%2?"Shift+Tab":"Tab");assert.notEqual(await choice.evaluate(()=>document.activeElement===document.body),true,"focus escaped dialog");}
    await choice.locator("[data-consent-reject]").click();await choice.waitForFunction(()=>document.activeElement&&document.activeElement.matches("[data-consent-settings]"));assert.equal(await choice.locator('[data-commercial-slot="primary-display"]:visible').count(),0,"rejected slot retained geometry");await choice.reload({waitUntil:"domcontentloaded"});await choice.waitForTimeout(200);assert.equal(choiceRequests,0,"rejected reload requested provider");assert.equal(await choice.locator('[data-commercial-slot="primary-display"]:visible').count(),0,"rejected reload retained geometry");await choice.close();
    const nofill=await browser.newPage({viewport:{width:375,height:812}});let nofillRequests=0;await nofill.route("**/*effectivecpmnetwork.com/**",route=>{nofillRequests++;return route.fulfill({contentType:"text/javascript",body:"/* deliberate no-fill */"});});await nofill.addInitScript(()=>localStorage.setItem("approximately-up-consent-v1",JSON.stringify({analytics:false,advertising:true})));await nofill.goto(origin+"/",{waitUntil:"domcontentloaded"});await nofill.waitForTimeout(2900);assert.equal(nofillRequests,1,"no-fill request count");assert.equal(await nofill.locator('[data-commercial-slot="primary-display"]').count(),0,"no-fill slot persisted");await nofill.close();
    const thrown=await browser.newPage({viewport:{width:375,height:812}});await thrown.route("**/*effectivecpmnetwork.com/**",route=>route.fulfill({contentType:"text/javascript",body:'throw new Error("deliberate provider failure")'}));await thrown.addInitScript(()=>localStorage.setItem("approximately-up-consent-v1",JSON.stringify({analytics:false,advertising:true})));await thrown.goto(origin+"/",{waitUntil:"domcontentloaded"});await thrown.waitForTimeout(300);assert.equal(await thrown.locator('[data-commercial-slot="primary-display"]').count(),0,"thrown provider error slot persisted");await thrown.close();
    const excluded=await browser.newPage({viewport:{width:375,height:812}});let excludedRequests=0;await excluded.route("**/*effectivecpmnetwork.com/**",route=>{excludedRequests++;return route.abort();});await excluded.addInitScript(()=>localStorage.setItem("approximately-up-consent-v1",JSON.stringify({analytics:false,advertising:true})));for(const url of ["/privacy","/about","/contact","/404.html"]){await excluded.goto(origin+url,{waitUntil:"domcontentloaded"});assert.equal(await excluded.locator('[data-commercial-slot="primary-display"]').count(),0,`excluded wrapper ${url}`);}assert.equal(excludedRequests,0,"excluded page requested provider");await excluded.close();
    const zoom=await browser.newPage({viewport:{width:720,height:450}});await zoom.addInitScript(()=>localStorage.setItem("approximately-up-consent-v1",JSON.stringify({analytics:false,advertising:false})));await zoom.goto(origin+"/",{waitUntil:"domcontentloaded"});const zoomResult=await zoom.evaluate(()=>({physicalViewportWidth:1440,effectiveCssViewportWidth:innerWidth,overflow:document.documentElement.scrollWidth-document.documentElement.clientWidth,settingsHeight:document.querySelector("[data-consent-settings]").getBoundingClientRect().height}));assert.equal(zoomResult.effectiveCssViewportWidth,720,"200 percent zoom reflow viewport");assert(zoomResult.overflow<=0,"200 percent zoom overflow");assert(zoomResult.settingsHeight>=44,"commercial/privacy target below 44px");await zoom.close();
    console.log(JSON.stringify({status:"pass",browser:"chromium",viewports:results,zoom200:zoomResult,focusTrap:"pass",focusRestore:"pass",beforeChoiceRequests:0,rejectedReloadRequests:0,noFillFinalSlotCount:0,thrownErrorFinalSlotCount:0,excludedProviderRequests:0},null,2));
  }finally{await browser.close();await new Promise(resolve=>server.close(resolve));}
}
