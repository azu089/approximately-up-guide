#!/usr/bin/env node
import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const publicDir = path.join(root, "public");
const sitePath = path.join(root, "data", "site.json");
const buildSourcePath = path.join(root, "data", "build_content.py");
const generatorPath = path.join(root, "scripts", "generate.js");
const expectedPublisher = "pub-4174270222899193";
const expectedClient = `ca-${expectedPublisher}`;
const consentKey = "approximately-up-consent-v1";
const locales = ["en","zh-CN","zh-TW","ja","ko","fr","de","es","it","pl","pt-BR","ru","uk","vi"];

const filesUnder = dir => fs.readdirSync(dir, {withFileTypes:true}).flatMap(entry =>
  entry.isDirectory() ? filesUnder(path.join(dir, entry.name)) : [path.join(dir, entry.name)]).sort();
const htmlRows = () => filesUnder(publicDir).filter(file => file.endsWith(".html")).map(file => ({
  relative:path.relative(publicDir,file), html:fs.readFileSync(file,"utf8"),
}));
const count = (text, needle) => text.split(needle).length - 1;
const treeHash = () => {
  const hash=crypto.createHash("sha256");
  for(const file of filesUnder(publicDir)){hash.update(path.relative(publicDir,file));hash.update("\0");hash.update(fs.readFileSync(file));hash.update("\0");}
  return hash.digest("hex");
};
const runBuild = () => {
  const env={...process.env};delete env.APPROX_UP_ADSENSE_FIXTURE;
  const result=spawnSync(process.execPath,[generatorPath],{cwd:root,env,encoding:"utf8"});
  assert.equal(result.status,0,result.stderr||result.stdout||"generator failed");
  return result.stdout.trim();
};
const localeOf = relative => {
  const first=relative.split(path.sep)[0];
  return locales.includes(first) && first!=="en" ? first : "en";
};
const privacySection = html => (html.match(/<section class="privacy-copy"[\s\S]*?<\/section>/)||[])[0]||"";
const eagerProvider = /<script[^>]+src=["'][^"']*(?:googletagmanager\.com\/gtag\/js|effectivecpmnetwork\.com|pagead2\.googlesyndication\.com\/pagead\/js\/adsbygoogle\.js)/i;

function validateRow(row){
  const lang=localeOf(row.relative),html=row.html;
  const leaf=path.basename(row.relative);
  const eligible=!(["about.html","privacy.html","contact.html","404.html"].includes(leaf));
  assert.equal(eagerProvider.test(html),false,`eager optional provider in ${row.relative}`);
  for(const token of ["data-consent-settings","data-consent-dialog","data-consent-accept","data-consent-reject","data-consent-manage-open","data-consent-save","data-consent-withdraw"])
    assert.equal(html.includes(token),true,`${token} missing in ${row.relative}`);
  assert.equal(html.includes(`data-consent-locale="${lang}"`),true,`consent locale fallback in ${row.relative}`);
  assert.equal(html.includes(consentKey),true,`consent storage/version missing in ${row.relative}`);
  assert.equal(/rel="[^"]*\bsponsored\b/i.test(html),false,`sponsored rel pollution in ${row.relative}`);
  assert.equal(html.includes("affiliate_click"),false,`affiliate classifier pollution in ${row.relative}`);
  assert.equal(count(html,'"adsterraSrc":"https://pl30767409.effectivecpmnetwork.com/c8bf889a0dcc57e129ef61a0c31f243d/invoke.js"'),eligible?1:0,`Adsterra config count in ${row.relative}`);
  assert.equal(count(html,'<aside class="commercial-slot" data-commercial-slot="primary-display"'),eligible?1:0,`commercial wrapper count in ${row.relative}`);
  assert.equal(count(html,'"gaId":"G-YV335TQLWZ"'),1,`GA4 config count in ${row.relative}`);
  assert.equal(count(html,'"adsenseSrc":""'),1,`AdSense serving gate in ${row.relative}`);
  assert.equal(html.includes("outbound_click"),true,`outbound classifier missing in ${row.relative}`);
}

function validatePrivacy(rows){
  const bodies=new Map();
  for(const lang of locales){
    const relative=lang==="en"?"privacy.html":`${lang}/privacy.html`;
    const row=rows.find(item=>item.relative===relative);
    assert(row,`privacy page missing for ${lang}`);
    const body=privacySection(row.html);
    assert(body,`privacy body missing for ${lang}`);
    assert(body.includes(`data-privacy-locale="${lang}"`),`privacy locale fallback for ${lang}`);
    for(const marker of ["Google Analytics 4","GA4","Adsterra","effectivecpmnetwork.com","Google AdSense",consentKey,"Cloudflare","Google Fonts"])
      assert(body.includes(marker),`${marker} missing from ${lang} privacy`);
    bodies.set(lang,body.replace(/data-privacy-locale="[^"]+"/,"data-privacy-locale=LOCALE"));
  }
  assert.equal(new Set(bodies.values()).size,locales.length,"privacy English fallback or duplicate locale body detected");
  assert.notEqual(bodies.get("zh-TW"),bodies.get("zh-CN"),"zh-TW privacy reuses zh-CN body");
}

function expectFault(name, mutate, expected){
  let caught="";
  try{mutate();}catch(error){caught=String(error.message||error);}
  assert(caught.includes(expected),`${name} did not fail for intended reason: ${caught||"no failure"}`);
}

const site=JSON.parse(fs.readFileSync(sitePath,"utf8"));
assert.deepEqual(site.site.languages,locales,"fourteen-language configuration changed");
assert.equal(site.pages.length,17,"page inventory changed");
assert.equal(site.site.affiliates&&Object.keys(site.site.affiliates).length,0,"affiliate configuration must stay empty");
assert.equal(site.site.adsenseId,expectedPublisher,"AdSense publisher changed");
assert.deepEqual(site.site.adsenseServing,{enabled:false,providerReady:false,certifiedCmpReady:false},"AdSense production gates must remain false");
const buildSource=fs.readFileSync(buildSourcePath,"utf8");
assert(buildSource.includes(`"adsenseId": "${expectedPublisher}"`),"canonical build source lost publisher");
for(const gate of ["enabled","providerReady","certifiedCmpReady"])
  assert(new RegExp(`"${gate}"\\s*:\\s*False`).test(buildSource),`canonical ${gate} gate changed`);

const firstBuild=runBuild(),firstHash=treeHash(),rows=htmlRows();
assert.equal(rows.length,295,"expected 294 indexable pages plus one default-language 404");
for(const row of rows)validateRow(row);
validatePrivacy(rows);
const sitemap=fs.readFileSync(path.join(publicDir,"sitemap.xml"),"utf8");
assert.equal(count(sitemap,"<loc>"),294,"indexable URL inventory changed");
assert.equal(count(rows.map(row=>row.html).join("\n"),`<meta name="google-adsense-account" content="${expectedClient}" />`),294,"AdSense ownership metadata count changed");
assert.equal(fs.readFileSync(path.join(publicDir,"ads.txt"),"utf8"),`google.com, ${expectedPublisher}, DIRECT, f08c47fec0942fa0\n`,"ads.txt changed");

const sample=rows.find(row=>row.relative==="index.html");
expectFault("eager GA4",()=>validateRow({...sample,html:sample.html+'<script src="https://www.googletagmanager.com/gtag/js?id=fault"></script>'}),"eager optional provider");
expectFault("eager Adsterra",()=>validateRow({...sample,html:sample.html+'<script src="https://fault.effectivecpmnetwork.com/x.js"></script>'}),"eager optional provider");
expectFault("missing reject",()=>validateRow({...sample,html:sample.html.replaceAll("data-consent-reject","data-broken-reject")}),"data-consent-reject missing");
expectFault("missing settings",()=>validateRow({...sample,html:sample.html.replaceAll("data-consent-settings","data-broken-settings")}),"data-consent-settings missing");
expectFault("missing withdrawal",()=>validateRow({...sample,html:sample.html.replaceAll("data-consent-withdraw","data-broken-withdraw")}),"data-consent-withdraw missing");
expectFault("consent locale fallback",()=>validateRow({...sample,html:sample.html.replace('data-consent-locale="en"','data-consent-locale="fr"')}),"consent locale fallback");
expectFault("sponsored Steam",()=>validateRow({...sample,html:sample.html+'<a href="https://store.steampowered.com/app/000" rel="noopener sponsored">fault</a>'}),"sponsored rel pollution");
expectFault("affiliate classifier",()=>validateRow({...sample,html:sample.html.replace("outbound_click","affiliate_click")}),"affiliate classifier pollution");
const privacyFaultRows=rows.map(row=>row.relative==="fr/privacy.html"?{...row,html:row.html.replace('data-privacy-locale="fr"','data-privacy-locale="en"')}:row);
expectFault("privacy locale fallback",()=>validatePrivacy(privacyFaultRows),"privacy locale fallback");
const zhCn=privacySection(rows.find(row=>row.relative==="zh-CN/privacy.html").html);
const zhTwFault=rows.map(row=>row.relative==="zh-TW/privacy.html"?{...row,html:row.html.replace(privacySection(row.html),zhCn.replace('data-privacy-locale="zh-CN"','data-privacy-locale="zh-TW"'))}:row);
expectFault("zh-TW reuse",()=>validatePrivacy(zhTwFault),"privacy English fallback or duplicate locale body detected");

const secondBuild=runBuild(),secondHash=treeHash();
assert.equal(secondHash,firstHash,"two builds are not byte-identical");
console.log(JSON.stringify({status:"pass",locales:14,htmlPages:295,indexablePages:294,defaultOptionalProviderRequests:0,sponsoredRel:0,affiliateEvents:0,privacyFallbacks:0,negativeFaults:10,treeSha256:firstHash,builds:[firstBuild,secondBuild]},null,2));
