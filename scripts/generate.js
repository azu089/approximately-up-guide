#!/usr/bin/env node
/**
 * Doloc Town Guide Static Site Generator — "Ruins & Roots" theme
 * 数据驱动 + 6 语言：data/site.json → node scripts/generate.js → public/
 * 语言：en（默认，根路径）/ zh-CN / zh-TW / ja / ko / es，hreflang + 语言切换器
 * 视觉：废墟田园（暖绿+琥珀+锈灰、生长卡、季节条、废土手册风）
 */
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const ROOT = path.join(__dirname, "..");
const DATA = JSON.parse(fs.readFileSync(path.join(ROOT, "data", "site.json"), "utf8"));
const OUT = path.join(ROOT, "public");
const KIT = require("./lib/site-kit");   // 共用基建：URL/图片/sitemap/lastmod
// 联盟链接：site.json 的 affiliates 没配 ID 时原样输出原链接，配了才加追踪参数 + rel="sponsored"
const AFF = KIT.createAffiliate(DATA.site.affiliates);
const esc = KIT.esc;
const clean = KIT.clean;
const LANGS = DATA.site.languages || ["en"];
const DEF = DATA.site.defaultLanguage || "en";
const CSS_V = crypto.createHash("md5").update(fs.readFileSync(path.join(ROOT,"templates","style.css"),"utf8")).digest("hex").slice(0,8);
const today = new Date().toISOString().slice(0,10);
const urlOf = KIT.createUrl({ domain: DATA.site.domain, defaultLang: DEF });
const LM = KIT.createLastmod({ manifestPath: path.join(ROOT,"data",".lastmod.json"), today });
const HERO_SET = "/images/hero-640.jpg 640w, /images/hero-1280.jpg 1280w, /images/hero.jpg 1600w";
const LANG_META = {
  "en":    { flag: "🇬🇧", name: "English",      html: "en" },
  "zh-CN": { flag: "🇨🇳", name: "简体中文",     html: "zh-CN" },
  "zh-TW": { flag: "🇹🇼", name: "繁體中文",     html: "zh-TW" },
  "ja":    { flag: "🇯🇵", name: "日本語",       html: "ja" },
  "ko":    { flag: "🇰🇷", name: "한국어",       html: "ko" },
  "fr":    { flag: "🇫🇷", name: "Français",     html: "fr" },
  "de":    { flag: "🇩🇪", name: "Deutsch",      html: "de" },
  "es":    { flag: "🇪🇸", name: "Español",      html: "es" },
  "it":    { flag: "🇮🇹", name: "Italiano",     html: "it" },
  "pl":    { flag: "🇵🇱", name: "Polski",       html: "pl" },
  "pt-BR": { flag: "🇧🇷", name: "Português (BR)", html: "pt-BR" },
  "ru":    { flag: "🇷🇺", name: "Русский",      html: "ru" },
  "uk":    { flag: "🇺🇦", name: "Українська",   html: "uk" },
  "vi":    { flag: "🇻🇳", name: "Tiếng Việt",   html: "vi" },
};
/* ---------- SVG flags (premium, render on all platforms) ---------- */
const FLAGS = {
  "en": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#012169"/><path d="M0 0 60 40M60 0 0 40" stroke="#fff" stroke-width="11"/><path d="M0 0 60 40M60 0 0 40" stroke="#C8102E" stroke-width="6"/><path d="M30 0v40M0 20h60" stroke="#fff" stroke-width="14"/><path d="M30 0v40M0 20h60" stroke="#C8102E" stroke-width="8"/></svg>',
  "zh-CN": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#EE1C25"/><g fill="#FFDE00"><path d="M12 8l1.7 3.4 3.8.5-2.8 2.7.7 3.8L12 16.7l-3.4 1.7.7-3.8-2.8-2.7 3.8-.5z"/><path d="M22 4l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3zM25 11l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3zM22 18l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3zM19 11l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3z"/></g></svg>',
  "zh-TW": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#FE0000"/><rect width="30" height="20" fill="#000095"/><g fill="#fff" stroke="#fff" stroke-width="1"><path d="M15 2l2.3 6.7 7 .1-5.6 4.2 2.1 6.7-5.8-4-5.8 4 2.1-6.7L5.7 8.8l7-.1z"/><g stroke-width=".6"><path d="M15 2v16M15 2 5.7 8.8 15 15.6M15 2l9.3 6.8L15 15.6M15 2v16M15 18.8 5.7 12 15 5.2M15 18.8l9.3-6.8L15 5.2"/></g></g></svg>',
  "ja": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><circle cx="30" cy="20" r="11" fill="#BC002D"/></svg>',
  "ko": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><g transform="translate(30 20)"><g transform="rotate(45)"><rect x="-10" y="-5" width="20" height="10" fill="#CD2E3A"/><rect x="-10" y="0" width="20" height="10" fill="#0047A0"/><circle r="6" fill="#fff"/></g><circle r="5" fill="#CD2E3A"/><path d="M0-5a5 5 0 0 1 0 10 2 2 0 0 1 0-10" fill="#0047A0"/></g><g fill="#000"><path d="M15 2h3v6h-3zM15 32h3v6h-3zM42 2h3v6h-3zM42 32h3v6h-3z"/></g></svg>',
  "es": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#AA151B"/><rect y="10" width="60" height="20" fill="#F1BF00"/><g transform="translate(30 20)"><path d="M-10 0a10 10 0 0 1 10-10 10 10 0 0 1 0 20 10 10 0 0 1-10-10z" fill="#fff" opacity=".85"/></g></svg>',
  "fr": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><rect width="20" height="40" fill="#0055A4"/><rect x="40" width="20" height="40" fill="#EF4135"/></svg>',
  "de": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#FFCE00"/><rect width="60" height="13.3" fill="#000"/><rect y="26.7" width="60" height="13.3" fill="#DD0000"/></svg>',
  "it": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><rect width="20" height="40" fill="#009246"/><rect x="40" width="20" height="40" fill="#CE2B37"/></svg>',
  "pl": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><rect width="60" height="20" fill="#DC143C"/></svg>',
  "pt-BR": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#009C3B"/><rect width="60" height="20" fill="#FFDF00"/><circle cx="30" cy="20" r="9" fill="#002776"/><path d="M30 14l5 6-5 6-5-6z" fill="#fff"/></svg>',
  "ru": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><rect y="13.3" width="60" height="13.3" fill="#0039A6"/><rect y="26.7" width="60" height="13.3" fill="#D52B1E"/></svg>',
  "uk": '<svg viewBox="0 0 60 40"><rect width="60" height="20" fill="#005BBB"/><rect y="20" width="60" height="20" fill="#FFD500"/></svg>',
  "vi": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#DA251D"/><path d="M30 8l3.3 6.7 7.3 1-5.3 5.2 1.3 7.3-6.6-3.5-6.6 3.5 1.3-7.3-5.3-5.2 7.3-1z" fill="#FFFF00"/></svg>',
};
const flagOf = lang => FLAGS[lang] || "🌐";

const metaOf = slug => (DATA.pages.find(p=>p.slug===slug)?.meta) || {};
const pageOf = (page, lang) => {
  if (lang === DEF || !page.i18n || !page.i18n[lang]) {
    return { title: page.title, metaTitle: page.metaTitle, metaDescription: page.metaDescription, intro: page.intro, sections: page.sections, heroImage: page.heroImage };
  }
  const t = page.i18n[lang];
  return { title: t.title || page.title, metaTitle: t.metaTitle || page.metaTitle, metaDescription: t.metaDescription || page.metaDescription, intro: t.intro || page.intro, sections: t.sections || page.sections, heroImage: t.heroImage || page.heroImage };
};
const siteI18n = lang => {
  const s = (DATA.site.i18n && DATA.site.i18n[lang]) || {};
  return {
    name: s.name || DATA.site.name, tagline: s.tagline || DATA.site.tagline, description: s.description || DATA.site.description,
    navHome: s.navHome || "Home", navGuides: s.navGuides || "Guides",
    navAbout: s.navAbout || "About", navPrivacy: s.navPrivacy || "Privacy", navContact: s.navContact || "Contact",
    langLabel: s.langLabel || "Language", aboutTitle: s.aboutTitle || "About", privacyTitle: s.privacyTitle || "Privacy Policy", contactTitle: s.contactTitle || "Contact",
    footerNote: s.footerNote || "Unofficial fan site — game and related assets belong to their respective owners.",
    footerSource: s.footerSource || "Information checked against the official Steam store page, official 1.0 announcement, publisher and media reports.",
    quickAnswers: s.quickAnswers || "Quick answers", guides: s.guides || "All guides", aboutGame: s.aboutGame || "About the game",
    startPlaying: s.startPlaying || "Get it on Steam", getOnSteam: s.getOnSteam || "Get it on Steam ↗", readGuide: s.readGuide || "Read the guide →",
    moreGuides: s.moreGuides || "More guides", sources: s.sources || "Sources & fact-checking",
    blueTag: s.blueTag || "BLUEPRINT", updated: s.updated || "Contents", explore: s.explore || "Build, crash, rebuild",
    latest: s.latest || "Core systems", aboutText: s.aboutText || "", aboutSources: s.aboutSources || "",
    searchPh: s.searchPh || "Search guides…", searchLabel: s.searchLabel || "Search guides", noMatch: s.noMatch || "No matching entries",
  };
};



/* ---------- SVG icons (Ruins & Roots line icons, stroke currentColor) ---------- */
const SVG = {
  logo: '<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="2" y="2" width="36" height="36" rx="10" fill="#0B1220"/><path d="M20 7l11 5v9c0 6-4.5 10.5-11 12-6.5-1.5-11-6-11-12v-9l11-5z" fill="none" stroke="#4FD1C5" stroke-width="2" stroke-linejoin="round"/><path d="M20 12l7 3v6.5c0 3.8-2.8 6.8-7 8-4.2-1.2-7-4.2-7-8V15l7-3z" fill="none" stroke="#F59E0B" stroke-width="1.6" stroke-linejoin="round"/><circle cx="20" cy="20" r="2.4" fill="#4FD1C5"/></svg>',
  "how-to-play": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M15.91 11.672a.375.375 0 010 .656l-5.603 3.113a.375.375 0 01-.557-.328V8.887c0-.286.307-.466.557-.327l5.603 3.112z"/></svg>',
  "farming": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21v-7m0 0c-3-1.5-5-4.5-5-8 4.5 0 8 3 8 8z"/><path d="M12 14c3-1 5.5-3.5 5.5-7C13 7 10.5 10 10 14z" opacity=".75"/><path d="M8 21h8"/></svg>',
  "automation": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="3.5" width="17" height="17" rx="3"/><path d="M8 17V7m8 10V7M3.5 12h17"/><circle cx="8" cy="9" r="1.2" fill="currentColor"/><circle cx="8" cy="15" r="1.2" fill="currentColor"/><circle cx="16" cy="9" r="1.2" fill="currentColor"/><circle cx="16" cy="15" r="1.2" fill="currentColor"/></svg>',
  "gene-system": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="6" r="2.5"/><circle cx="6.5" cy="17" r="2.5"/><circle cx="17.5" cy="17" r="2.5"/><path d="M12 8.5c-1 4-1 7.5-4 10.5M12 8.5c1 4 1 7.5 4 10.5M12 8.5v11M12 19.5h.01"/></svg>',
  "fishing": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h7a3 3 0 013 3v12a1.5 1.5 0 003 0V8"/><path d="M17 8l3-1.5v3L17 8z"/><path d="M4 8h4"/></svg>',
  "drone-combat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3c-2 0-3.5 1.5-3.5 3.5S10 10 12 10s3.5-1.5 3.5-3.5S14 3 12 3z"/><path d="M12 10v6"/><circle cx="12" cy="19" r="2"/><path d="M5 6.5h2M17 6.5h2"/></svg>',
  "exploration": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4 6v6c0 4.5 3.5 8 8 9 4.5-1 8-4.5 8-9V6l-8-3z"/><path d="M12 8v5m-2.5-2.5 5 0"/></svg>',
  "friendship": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20s-7-4.5-9-9c-1.2-3 1.2-6.5 4.5-6.5 2 0 3.5 1 4.5 2.5 1-1.5 2.5-2.5 4.5-2.5 3.3 0 5.7 3.5 4.5 6.5-2 4.5-9 9-9 9z"/><path d="M9 12h6M12 9v6" opacity=".7"/></svg>',
  "cooking": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 9h14v3a7 7 0 01-14 0V9z"/><path d="M9 4c0 1.5-1 2-1 3.5M12 4c0 1.5-1 2-1 3.5M15 4c0 1.5-1 2-1 3.5"/></svg>',
  "ranching": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V8l8-4 8 4v12"/><path d="M4 12h16M9 20v-4a3 3 0 016 0v4"/></svg>',
  "characters": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4.5 20c1.2-3.6 4-5.5 7.5-5.5s6.3 1.9 7.5 5.5"/></svg>',
  "story": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4 6.5 9.5 12 15l5.5-5.5L12 4z"/><path d="M6.5 9.5h11M8 15l1.5 5h5L16 15"/></svg>',
  "weather": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17a4.5 4.5 0 01-.5-9A6 6 0 0118 9.5 3.5 3.5 0 0117.5 17H7z"/><path d="M4 5.5 5 6.5M4 5.5 5 4.5M19 5.5 20 6.5M19 5.5 18 4.5" opacity=".8"/><path d="M4.5 11h-1.5M21 11h-1.5"/></svg>',
  "achievements": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8m-4-3v3m-3.5-18 1.5 2.5L9 6l1.5 1L12 5l1.5 2L15 6l-1-1.5L15.5 3H8.5z"/><path d="M9 8.5h6v1.5a3 3 0 01-6 0V8.5z"/></svg>',
  "mods": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 4-3 7.5-7 9-4-1.5-7-5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>',
  "update-log": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9 3h6"/></svg>',
  "faq": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.2a2.6 2.6 0 115.1.9c-.6 1.1-2.1 1.6-2.1 2.9M12 16.5h.01"/></svg>',
  "system-requirements": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4.5" width="18" height="12" rx="2"/><path d="M8 20h8m-4-3.5V20"/><path d="M7 8h4M7 11h7"/></svg>',
  "steam-deck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="6" width="16" height="12" rx="3"/><path d="M8.5 10h.01M12 10h.01M15.5 10h.01M9.5 13.5c.8.8 4.2.8 5 0"/></svg>',
  "where-to-buy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 002.25-2.25V6.75A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25v10.5A2.25 2.25 0 004.5 19.5z"/></svg>',
  "how-long-to-beat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>',
  "up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5m-6 6 6-6 6 6"/></svg>',
  "pin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a7 7 0 00-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 00-7-7zm0 9.5A2.5 2.5 0 1112 6a2.5 2.5 0 010 5.5z"/></svg>',
  "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="11" cy="11" r="6"/><path d="m16 16 4 4"/></svg>',
  "rocket": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 15c-1.5 1.5-2 5-2 5s3.5-.5 5-2m9-13c3 1 5 5 5 5s-1 5-5 5-6-1.5-9-4.5S7 4 7 4s3-3 5-3 4 1 5 3z"/><circle cx="14.5" cy="9.5" r="2"/><path d="M7.5 11.5c-1 3-.5 5 1 7m2.5-14.5c.5-1.5 2-3 3.5-3.5"/></svg>',
  "ship": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v3m-3 3L7 6l5 3 5-3-2 3M5 12h14l-1 7H6l-1-7z"/><path d="M6 12l1.5-3M18 12l-1.5-3"/></svg>',
  "blueprint": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 8h10M7 12h10M7 16h6"/><path d="M3 3l3 3M21 21l-3-3M3 21l3-3M21 3l-3 3" opacity=".5"/></svg>',
  "wire": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h4l2-5 4 10 2-5h4"/><circle cx="4" cy="12" r="1.3" fill="currentColor"/><circle cx="20" cy="12" r="1.3" fill="currentColor"/></svg>',
  "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 2v3m0 14v3M2 12h3m14 0h3M4.9 4.9l2.1 2.1m10 10 2.1 2.1m0-14.2-2.1 2.1m-10 10-2.1 2.1"/></svg>',
  "console": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M7 9h.01M10 9h.01M7 13h6M15 12v3m-3-1.5h6"/></svg>',
  "checklist": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9 5H5a2 2 0 00-2 2v12a2 2 0 002 2h12a2 2 0 002-2v-4"/><path d="M8 3h8v4H8zM9 12l2 2 4-4"/></svg>',
  "part": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l3 5 5 3-5 3-3 5-3-5-5-3 5-3z"/><circle cx="12" cy="10" r="1.5" fill="currentColor"/></svg>',
  "launch": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 17l6-6 4 4 6-6-2-2h-3V4l-2 2-4-4-2 2"/><path d="M3 21h18"/></svg>',
  "sprout": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21v-8"/><path d="M12 13c-3-1.5-5-4-5-7.5C11.5 5.5 15 8 12 13z"/><path d="M12 13c3-1 5.5-3.5 5.5-7C13 6 10.5 8.5 10.5 12.5" opacity=".7"/></svg>',
};

function hreflang(slug){
  const alt = LANGS.map(l => `<link rel="alternate" hreflang="${LANG_META[l]?.html || l}" href="${urlOf(slug,l)}" />`).join("\n");
  return `${alt}\n<link rel="alternate" hreflang="x-default" href="${urlOf(slug,DEF)}" />`;
}
function head(title, desc, extraLd, slug, lang, ogImage){
  const ld = JSON.stringify([siteLd(lang)].concat(extraLd || []));
  const gsc = DATA.site.gscVerification ? `<meta name="google-site-verification" content="${esc(DATA.site.gscVerification)}" />` : "";
  const adsenseMeta = DATA.site.adsenseId ? `<meta name="google-adsense-account" content="ca-${esc(DATA.site.adsenseId)}" />` : "";
  // Awin 联盟所有权验证：官方要求是「源代码里出现 Awin 字样」，没有规定 meta 名称，这里用描述性名字。
  // 值可以是任意字符串（拿到正式验证码就换成那个）；未配置时不输出。
  const awin = DATA.site.awinVerification ? `<meta name="awin-site-verification" content="${esc(DATA.site.awinVerification)}" />` : "";
  // Impact（Humble Bundle 联盟）所有权验证。
  // ⚠️ 两处刻意和本文件其它 meta 不一致，都别"顺手修正"：
  //    1. 属性名是 `value` 不是 `content`
  //    2. 单引号 + 不自闭合
  //    这是 Impact 后台给的原文格式。理论上 HTML 等价，但验证器若做字符串精确匹配就只认原样，
  //    照抄的成本是零，赌它按标准解析的成本是一轮部署 + 一次失败重试。
  //    值是 UUID（十六进制+连字符），单引号属性不会被内容破坏；仍然转义 ' 以防将来换成别的值。
  // impactVerification 支持单值或数组：Humble 主流程 + Connect channels 渠道表单会生成不同 UUID，
  // 都放上，无论 Impact 查哪个都通过。
  const _impVals = Array.isArray(DATA.site.impactVerification)
    ? DATA.site.impactVerification.filter(Boolean)
    : (DATA.site.impactVerification ? [DATA.site.impactVerification] : []);
  const impact = _impVals.map(v =>
    `<meta name='impact-site-verification' value='${esc(v).replace(/'/g, "&#39;")}'>`
  ).join("");
  const og = ogImage || DATA.site.ogImage || "/images/hero.jpg";
  const htmlLang = LANG_META[lang]?.html || lang;
  return `<!DOCTYPE html>
<html lang="${htmlLang}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>${esc(title)}</title>
<meta name="description" content="${esc(desc)}" />
<link rel="canonical" href="${urlOf(slug,lang)}" />
${hreflang(slug)}
<meta name="theme-color" content="#16211A" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />
${gsc}
${adsenseMeta}${awin}${impact}
<meta property="og:type" content="website" />
<meta property="og:site_name" content="${esc(siteI18n(lang).name)}" />
<meta property="og:title" content="${esc(title)}" />
<meta property="og:description" content="${esc(desc)}" />
<meta property="og:url" content="${urlOf(slug,lang)}" />
<meta property="og:image" content="https://${DATA.site.domain}${og}" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Zilla+Slab:wght@500;600;700&family=Inter:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/css/style.css?v=${CSS_V}" />${slug === "index" ? "\n" + KIT.heroPreload({ srcset: HERO_SET, sizes: "100vw" }) : ""}
<script type="application/ld+json">${ld}</script>
${DATA.site.gaId ? `<script async src="https://www.googletagmanager.com/gtag/js?id=${esc(DATA.site.gaId)}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','${esc(DATA.site.gaId)}');</script>` : ""}
</head>
<body>`;
}
function langSwitcher(lang, slug){
  const items = LANGS.map(l =>
    `<a href="${urlOf(slug,l)}" class="${l===lang?"active":""}"><span class="lang-flag">${flagOf(l)}</span>${LANG_META[l]?.name||l}</a>`
  ).join("");
  return `<details class="lang-dd">
    <summary><span class="lang-flag">${flagOf(lang)}</span><span class="lang-name">${LANG_META[lang]?.name||lang}</span><span class="caret">▾</span></summary>
    <div class="dd-menu dd-lang">${items}</div>
  </details>`;
}
function header(lang, active){
  const s = siteI18n(lang);
  const prefix = lang === DEF ? "" : `/${lang}`;
  const P0 = ["how-to-play","ship-building-guide","blueprints-guide","wiring-electronics","controls","multiplayer"];
  const P1 = ["best-ship-designs","system-requirements","console-release","mods","patch-notes","demo-vs-full"];
  const P2 = ["achievements","achievements-list","ships","blueprints","guides"];
  const gTitle = s.navGroup1 || "Guides", gTitle2 = s.navGroup2 || "Reference", gTitle3 = s.navGroup3 || "Index";
  const drop = (title, slugs) => `<div class="dd-group"><b class="dd-title">${esc(title)}</b>${slugs.map(slug=>{
    const p=DATA.pages.find(x=>x.slug===slug); if(!p) return "";
    const m=metaOf(slug);
    // 下拉目录显示时去掉游戏名前缀（页面 title/SEO 不动，仅目录清爽）
    const _t = pageOf(p,lang).title;
    const _disp = _t.replace(/\s*Approximately Up\s*/g," ").replace(/\s+/g," ").trim() || _t;
    return `<a href="${prefix}/${slug}" class="${slug===active?"active":""}"><span class="nav-ic">${SVG[m.icon]}</span><span>${esc(_disp)}</span></a>`;
  }).join("")}</div>`;
  const guides = `<div class="dd-menu dd-manual">${drop(gTitle, P0)}${drop(gTitle2, P1)}${drop(gTitle3, P2)}</div>`;
  const searchPh = s.searchPh || "Search guides…";
  const searchLabel = s.searchLabel || "Search guides";
  return `<header class="site-header">
  <div class="container header-inner">
    <a class="logo" href="${prefix}/"><span class="logo-badge">${SVG.logo}</span><span class="logo-txt">${esc(s.name)}</span></a>
    <nav class="nav" aria-label="Main">
      <a href="${prefix}/" class="${active===""?"active":""}">${esc(s.navHome)}</a>
      <details class="dd">
        <summary>${esc(s.navGuides)} <span class="caret">▾</span></summary>
        ${guides}
      </details>
    </nav>
    <form class="site-search" action="https://www.google.com/search" method="get" target="_blank" rel="noopener" role="search">
      <input type="search" name="q" placeholder="${searchPh}" aria-label="${searchLabel}" />
      <input type="hidden" name="as_sitesearch" value="${esc(DATA.site.domain)}" />
      <span class="search-ic" aria-hidden="true">${SVG.search}</span>
    </form>
    ${langSwitcher(lang, active || "index")}
  </div>
</header>`;
}
function footer(lang){
  const s = siteI18n(lang);
  const prefix = lang === DEF ? "" : `/${lang}`;
  // 按 header 的舱段分组（Cockpit/Engine/Cargo/Archive），避免一列 10 个长标题拉到底
  const GRPS = [
    {label:s.navGroup1||"Guides", slugs:["how-to-play","ship-building-guide","blueprints-guide","wiring-electronics","controls","multiplayer"]},
    {label:s.navGroup2||"Reference", slugs:["best-ship-designs","system-requirements","console-release","mods","patch-notes","demo-vs-full"]},
    {label:s.navGroup3||"Index", slugs:["achievements","achievements-list","ships","blueprints","guides"]},
  ];
  const footCols = GRPS.map(g=>`<nav class="footer-col"><b>${esc(g.label)}</b>${g.slugs.map(slug=>{
    const p=DATA.pages.find(x=>x.slug===slug); if(!p) return "";
    return `<a href="${prefix}/${slug}">${esc(pageOf(p,lang).title)}</a>`;
  }).join("")}</nav>`).join("");
  return `<footer class="site-footer">
  <div class="container footer-inner">
    <div class="footer-brand-row">
      <div class="footer-brand"><span class="logo-badge small">${SVG.logo}</span><span>${esc(s.name)}</span></div>
      <div class="footer-links">
        <a href="${prefix}/about">${esc(s.navAbout)}</a><a href="${prefix}/privacy">${esc(s.navPrivacy)}</a><a href="${prefix}/contact">${esc(s.navContact)}</a>
        <a href="${esc(DATA.game.steamUrl)}" target="_blank" rel="noopener">Steam ↗</a>
      </div>
    </div>
    <div class="footer-cols">${footCols}</div>
    <div class="footer-meta">
      <p>${esc(s.tagline)}</p>
      <p>${esc(s.footerNote)}</p>
      <p>${esc(s.footerSource)} · ${today}</p>
    </div>
    ${DATA.site.adsenseId ? `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${esc(DATA.site.adsenseId)}" crossorigin="anonymous"></script>` : ""}\n    ${DATA.site.adsterra ? DATA.site.adsterra : ""}
  </div>
<script>
document.addEventListener('click', function(e){
  document.querySelectorAll('details.dd[open], details.lang-dd[open]').forEach(function(d){
    if (!d.contains(e.target)) d.removeAttribute('open');
  });
});
document.addEventListener('keydown', function(e){
  if (e.key === 'Escape') document.querySelectorAll('details[open]').forEach(function(d){ d.removeAttribute('open'); });
});
document.addEventListener('DOMContentLoaded', function(){
  var obs = new IntersectionObserver(function(es){
    es.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('in'); obs.unobserve(en.target); } });
  }, {threshold:.08});
  document.querySelectorAll('.reveal').forEach(function(el){ obs.observe(el); });
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (tocLinks.length) {
    var tocTargets = tocLinks.map(function(a){ return document.querySelector(a.getAttribute('href')); });
    var tocObs = new IntersectionObserver(function(es){
      es.forEach(function(en){
        if (en.isIntersecting) {
          var id = '#' + en.target.id;
          tocLinks.forEach(function(a){ a.classList.toggle('active', a.getAttribute('href') === id); });
        }
      });
    }, {rootMargin:'-15% 0px -70% 0px', threshold:0});
    tocTargets.forEach(function(s){ if (s) tocObs.observe(s); });
  }

  /* ---- 鱼类筛选器（渐进增强：JS 没跑 = 页面完全等同于改动前）---- */
  var ff = document.querySelector('.ff');
  var rows = Array.prototype.slice.call(document.querySelectorAll('.eng-table.filterable tbody tr'));
  if (ff && rows.length) {
    ff.removeAttribute('hidden');
    /* 筛选维度不写死，从 DOM 里的 .ff-group[data-key] 读出来。
       这样鱼类（period/loc/req）和礼物（v）共用同一段代码，将来加第三个表也不用改这里。
       匹配一律用「空格分隔的多值包含」——单值属性走这条同样成立，行为与改动前一致。 */
    var keys = Array.prototype.slice.call(ff.querySelectorAll('.ff-group'))
                 .map(function(g){ return g.getAttribute('data-key'); });
    function fresh(){ var s = { q:'' }; keys.forEach(function(k){ s[k] = 'all'; }); return s; }
    var state = fresh();
    var countEl = ff.querySelector('.ff-count');
    var tpl = countEl ? countEl.getAttribute('data-tpl') : '';

    function matches(tr){
      for (var i = 0; i < keys.length; i++) {
        var k = keys[i], v = state[k];
        if (v !== 'all' && (' '+(tr.getAttribute('data-'+k)||'')+' ').indexOf(' '+v+' ') < 0) return false;
      }
      if (state.q && (tr.cells[0].textContent||'').toLowerCase().indexOf(state.q) < 0) return false;
      return true;
    }
    function apply(){
      var shown = 0;
      rows.forEach(function(tr){
        var ok = matches(tr);
        tr.hidden = !ok;
        if (ok) shown++;
      });
      // 整张表都被筛没了就收起该表、显示空态
      document.querySelectorAll('.eng-table.filterable').forEach(function(box){
        var any = Array.prototype.slice.call(box.querySelectorAll('tbody tr')).some(function(tr){ return !tr.hidden; });
        var tbl = box.querySelector('table'), empty = box.querySelector('.table-empty');
        if (tbl) tbl.hidden = !any;
        if (empty) empty.hidden = any;
      });
      if (countEl) countEl.textContent = tpl.replace('{n}', shown).replace('{t}', rows.length);
    }
    ff.addEventListener('click', function(e){
      var chip = e.target.closest('.ff-chip');
      if (chip) {
        var g = chip.closest('.ff-group');
        g.querySelectorAll('.ff-chip').forEach(function(c){ c.classList.toggle('on', c === chip); });
        state[g.getAttribute('data-key')] = chip.getAttribute('data-v');
        apply(); return;
      }
      if (e.target.closest('.ff-reset')) {
        state = fresh();
        ff.querySelectorAll('.ff-group').forEach(function(g){
          g.querySelectorAll('.ff-chip').forEach(function(c,i){ c.classList.toggle('on', i === 0); });
        });
        var inp = ff.querySelector('.ff-input'); if (inp) inp.value = '';
        apply();
      }
    });
    var input = ff.querySelector('.ff-input');
    if (input) input.addEventListener('input', function(){ state.q = this.value.trim().toLowerCase(); apply(); });
    apply();
  }
});
</script>
</footer>`;
}

/* ---------- section renderer (Space-Engineer Blueprint components — 太空工程蓝图语言, 全局独立) ---------- */
let SEC_IDX = 0;
function secId(){ SEC_IDX += 1; return "sec-" + SEC_IDX; }
function renderSection(s, lang){
  const id = secId();
  const st = siteI18n(lang);
  const tag = esc(s.tag || st.blueTag || "BLUEPRINT");
  switch(s.type){
    case "steps": {
      // 装配线步骤：纵向工位（框架→动力→逻辑→测试→发射）
      const items = (s.items||[]).map((it,i)=>{
        const phase = ["frame","power","logic","test","launch"][i%5];
        return `<li class="assy-item">
          <span class="assy-phase assy-${phase}" aria-hidden="true"><span class="assy-dot"></span></span>
          <div class="assy-body"><b>${esc(it[0])}</b>${it[1]?`<p>${esc(it[1])}</p>`:""}</div>
        </li>`;
      }).join("");
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}<ol class="assy-line">${items}</ol></section>`;
    }
    case "list": {
      // 元件清单
      const items = (s.items||[]).map(it=>`<li class="part-item"><span class="part-mark" aria-hidden="true">${SVG.part || "▣"}</span><p>${esc(it)}</p></li>`).join("");
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}<ul class="part-list">${items}</ul></section>`;
    }
    case "table": {
      // 工程数据表
      const headRow = (s.columns||[]).map(c=>`<th>${esc(c)}</th>`).join("");
      const attrsOf = i => {
        const a = (s.rowAttrs||[])[i];
        if (!a) return "";
        return " " + Object.entries(a).map(([k,v])=>`data-${k}="${esc(v)}"`).join(" ");
      };
      const rows = (s.rows||[]).map((r,i)=>`<tr${attrsOf(i)}>${r.map(c=>`<td>${esc(c)}</td>`).join("")}</tr>`).join("");
      const cls = s.rowAttrs ? "eng-table filterable" : "eng-table";
      const noMatch = s.noMatch || st.noMatch || "No matching entries";
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}<div class="${cls}"><table><thead><tr>${headRow}</tr></thead><tbody>${rows}</tbody></table><p class="table-empty" hidden>${esc(noMatch)}</p></div></section>`;
    }
    case "faq": {
      const items = (s.items||[]).map(([q,a])=>`<details class="panel-faq"><summary><span class="panel-wire" aria-hidden="true">${SVG.wire || "⏚"}</span><span>${esc(q)}</span><span class="pm">+</span></summary><div class="panel-a">${esc(a)}</div></details>`).join("");
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${items}</section>`;
    }
    case "evidence": {
      const items = (s.items||[]).map(([label,txt])=>`<div class="log-card"><span class="log-label">${esc(label)}</span><p>${esc(txt)}</p></div>`).join("");
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}<div class="log-cards">${items}</div></section>`;
    }
    case "timeline": {
      const items = (s.items||[]).map(([t,txt])=>`<li class="launch-tl"><span class="launch-tl-time">${esc(t)}</span><p>${esc(txt)}</p></li>`).join("");
      return `<section class="panel-block reveal" id="${id}"><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}<ul class="launch-timeline">${items}</ul></section>`;
    }
    case "note": {
      return `<section class="panel-block reveal mission-note" id="${id}"><div class="mission-pin" aria-hidden="true"></div><div class="panel-head"><span class="panel-tag">${tag}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="panel-lead">${esc(s.body)}</p>`:""}</section>`;
    }
    case "filter": {
      // 蓝图/材料速查筛选器（渐进增强：默认 hidden，JS 跑起来才显示）
      const u = s.ui || {};
      const group = (key, opts) => `<div class="ff-group" data-key="${key}">
        <span class="ff-label">${esc(u[key] || key)}</span>
        <div class="ff-chips">${opts.map((o,i)=>
          `<button type="button" class="ff-chip${i===0?" on":""}" data-v="${o}">${esc(u[o] || o)}</button>`
        ).join("")}</div>
      </div>`;
      return `<section class="ff reveal" id="${id}" hidden>
        <div class="ff-head"><span class="panel-tag">${esc(st.blueTag || "BLUEPRINT")}</span><h2>${esc(u.title || s.heading)}</h2></div>
        ${s.body?`<p class="ff-lead">${esc(s.body)}</p>`:""}
        <div class="ff-search"><span class="ff-search-ic" aria-hidden="true">${SVG.search || ""}</span>
          <input type="search" class="ff-input" placeholder="${esc(u.search || "Search…")}" aria-label="${esc(u.search || "Search…")}" />
        </div>
        ${(s.groups||[]).map(g=>group(g.key, g.opts)).join("")}
        <div class="ff-foot"><span class="ff-count" data-tpl="${esc(u.count || "{n}/{t}")}"></span>
          <button type="button" class="ff-reset">${esc(u.reset || "Reset")}</button></div>
      </section>`;
    }
    default: return "";
  }
}

/* ---------- home ---------- */
function renderHome(lang){
  const s = siteI18n(lang);
  const prefix = lang === DEF ? "" : `/${lang}`;
  const gname = (DATA.game.nameI18n && DATA.game.nameI18n[lang]) || DATA.game.name;
  const gintro = (DATA.game.introI18n && DATA.game.introI18n[lang]) || DATA.game.intro;
  const statsArr = (DATA.game.statsI18n && DATA.game.statsI18n[lang]) || DATA.game.stats || [];
  // 仪表盘数据：取前 5 个做成「读数行」（不是并列卡片）
  const gaugeRows = statsArr.slice(0,5).map((st,i)=>`<div class="gauge-row"><span class="gauge-idx">${String(i+1).padStart(2,"0")}</span><div class="gauge-meta"><span class="gauge-label">${esc(st.label)}</span><b class="gauge-value">${esc(st.value)}</b></div><span class="gauge-rail" aria-hidden="true"><span class="gauge-fill" style="width:${78 - i*13}%"></span></span></div>`).join("");
  const keyFactsArr = (DATA.game.keyFactsI18n && DATA.game.keyFactsI18n[lang]) || DATA.game.keyFacts || [];
  const keyFacts = keyFactsArr.map(f=>`<li class="log-line">${esc(f)}</li>`).join("");
  const aboutPointsArr = (DATA.game.aboutPointsI18n && DATA.game.aboutPointsI18n[lang]) || DATA.game.aboutPoints || [];
  // 系统舱段：按「驾驶舱/引擎/蓝图/维生/通讯/资料库」组织（游戏建造隐喻）
  const HAB = [
    {code:"COCKPIT", acc:"var(--cyan)",   label:lang==="en"?"Cockpit — start here":lang==="ja"?"コックピット":lang==="ko"?"조종석":"驾驶舱 — 从这里开始", desc:lang==="en"?"First flight, controls, and the build-crash-rebuild loop.":"", slugs:["how-to-play","controls","system-requirements","multiplayer"]},
    {code:"ENGINE",  acc:"var(--amber)",  label:lang==="en"?"Engine room — ship building":lang==="ja"?"機関室":lang==="ko"?"기관실":"引擎舱 — 飞船建造", desc:lang==="en"?"Modular ships, thrusters, wiring and blueprints.":"", slugs:["ship-building-guide","wiring-electronics","blueprints-guide","best-ship-designs"]},
    {code:"CARGO",   acc:"var(--violet)", label:lang==="en"?"Cargo bay — references":lang==="ja"?"カーゴベイ":lang==="ko"?"화물칸":"货舱 — 参考资料", desc:lang==="en"?"Console release, mods, updates and demo comparison.":"", slugs:["console-release","mods","patch-notes","demo-vs-full"]},
    {code:"ARCHIVE", acc:"#5CB8FF",       label:lang==="en"?"Archive — achievements & indexes":lang==="ja"?"資料室":lang==="ko"?"기록실":"资料库 — 成就与索引", desc:lang==="en"?"Achievements, ships index, blueprints index and guide index.":"", slugs:["achievements","achievements-list","ships","blueprints","guides"]},
  ];
  const habPanels = HAB.map((h,i)=>{
    const links = h.slugs.map(slug=>{
      const p=DATA.pages.find(x=>x.slug===slug); if(!p) return "";
      const m=metaOf(slug); const t=Object.assign(pageOf(p,lang),{slug});
      return `<a class="hab-link" href="${prefix}/${slug}" style="--hab-acc:${h.acc}"><span class="hab-ic">${SVG[m.icon]}</span><span class="hab-tx">${esc(t.title)}</span><span class="hab-go">${String(i+1)}.${h.slugs.indexOf(slug)+1} →</span></a>`;
    }).join("");
    return `<section class="hab-panel reveal" id="hab-${i+1}" style="--hab-acc:${h.acc}">
      <div class="hab-head"><span class="hab-code">${h.code}</span><h2>${esc(h.label)}</h2>${h.desc?`<p>${esc(h.desc)}</p>`:""}</div>
      <div class="hab-links">${links}</div>
    </section>`;
  }).join("");
  const heroImg = DATA.site.ogImage || "/images/hero.jpg";
  const heroCardImg = `<div class="ship-imgwrap"><img class="ship-img" src="${esc(heroImg)}" alt="${esc(gname)}" loading="eager" width="1600" height="900"></div>`;
  return `<!doctype html>
<html lang="${LANG_META[lang].html}"><head>${head(s.name, s.description, [gameLd()], "index", lang)}</head>
<body class="home">
${header(lang, "")}
<main class="flightdeck">
  <div class="fd-left">
    <div class="ship-card">
      ${heroCardImg}
      <div class="ship-id"><b>${esc(gname)}</b></div>
      <p class="ship-desc">${esc(gintro)}</p>
      <div class="gauges">${gaugeRows}</div>
    </div>
    <div class="fd-log">
      <span class="hab-code">MISSION LOG</span>
      <ul class="log-list">${keyFacts}</ul>
      <div class="fd-cta">
        <a class="btn btn-primary" href="${esc(DATA.game.steamUrl)}" rel="noopener sponsored">${esc(s.getOnSteam)}</a>
        <a class="btn btn-ghost" href="${prefix}/how-to-play">${esc(s.readGuide)}</a>
      </div>
    </div>
  </div>
  <div class="fd-right">
    <div class="fd-head">
      <span class="hab-code">HABITAT MODULES</span>
      <h1 class="fd-title">${esc(s.blueTag||"BLUEPRINT")} · ${esc(gname)}</h1>
      <p class="fd-sub">${esc(s.explore||gintro)}</p>
    </div>
    ${habPanels}
  </div>
</main>
${footer(lang)}
</body></html>`;
}




function renderFull(lang, title, desc, extraLd, slug, body, ogImage){
  const s = siteI18n(lang);
  return head(title, desc, extraLd, slug, lang, ogImage) + header(lang, slug === "index" ? "" : slug) + body + footer(lang);
}

/* ---------- article pages ---------- */
function renderPage(lang, page){
  const t = Object.assign(pageOf(page, lang), {slug: page.slug});
  const prefix = lang === DEF ? "" : `/${lang}`;
  SEC_IDX = 0;
  const toc = (t.sections||[]).filter(x=>x.heading).map((x,i)=>{
    SEC_IDX += 1;
    const n = String(SEC_IDX).padStart(2,"0");
    return `<a href="#sec-${SEC_IDX}"><span class="node-no">${n}</span><span class="node-tx">${esc(x.heading)}</span></a>`;
  }).join("");
  SEC_IDX = 0;
  const sections2 = (t.sections||[]).map(x => renderSection(x, lang)).join("");
  const srcList = page.sources || [];
  const sources = srcList.map(x=>`<li>${AFF.anchor({ url: x.url, text: (x.labels && x.labels[lang]) || x.label, suffix: " ↗" })}</li>`).join("");
  const affNote = AFF.needsDisclosure(srcList.map(x=>x.url))
    ? `<p class="aff-note">${esc(KIT.affiliateDisclosure(lang))}</p>` : "";
  const s = siteI18n(lang);
  const heroImg = t.heroImage;
  const srcsetOf = img => {
    if (!img) return null;
    const base = img.replace(/\.(jpg|jpeg|png|webp)$/i, "");
    return { srcset: `${base}-640.jpg 640w, ${base}-1280.jpg 1280w, ${img} 1600w`, sizes: "(max-width: 640px) 94vw, (max-width: 960px) 92vw, 820px" };
  };
  const pageHero = heroImg ? `<div class="dossier-img">${KIT.picture({ ...srcsetOf(heroImg), src: heroImg, attrs: `alt="${esc(t.title)}" loading="lazy" width="1600" height="900"` })}</div>` : "";
  // 相关档案（同舱段内）
  const related = DATA.pages.filter(p=>p.slug!==page.slug).slice(0,5).map((p,i)=>{
    const m = metaOf(p.slug);
    return `<a href="${prefix}/${p.slug}" class="rel-link"><span class="rel-no">${String(i+1).padStart(2,"0")}</span><span class="nav-ic">${SVG[m.icon]}</span><span>${esc(pageOf(p,lang).title)}</span></a>`;
  }).join("");
  const body = `
  <main class="dossier-page">
  <div class="dossier-wrap">
    <div class="dossier-bar">
      <span class="dossier-code">${esc(s.blueTag||"BLUEPRINT")} / ${esc(page.slug.toUpperCase())}</span>
      <span class="dossier-meta">${esc(t.title.split(":")[0].split("—")[0].trim())} · ${today}</span>
      <a class="dossier-home" href="${prefix}/">${esc(s.navHome)}</a>
    </div>
    <header class="dossier-head reveal">
      ${heroImg ? "" : `<span class="dossier-ic" aria-hidden="true">${SVG[page.meta?.icon || "rocket"]}</span>`}
      <h1>${esc(t.title)}</h1>
      <p class="dossier-lead">${esc(t.intro)}</p>
      ${pageHero}
    </header>
    <div class="dossier-body">
      <nav class="blueprint-nav reveal">
        <b class="bp-title">${esc(s.updated||"Contents")}</b>
        ${toc ? `<div class="bp-nodes">${toc}</div>` : ""}
      </nav>
      <div class="dossier-main">
        ${sections2}
        ${sources ? `<footer class="dossier-src reveal"><b>${esc(s.sources||"Sources")}</b><ul>${sources}</ul>${affNote}</footer>` : ""}
      </div>
      <aside class="dossier-side reveal">
        <div class="side-block">
          <span class="hab-code">RELATED</span>
          ${related}
        </div>
        <div class="side-block">
          <span class="hab-code">STEAM</span>
          <p>${esc(DATA.game.name)}</p>
          <a class="btn btn-primary" href="${esc(DATA.game.steamUrl)}" target="_blank" rel="noopener sponsored">${esc(s.getOnSteam)}</a>
        </div>
      </aside>
    </div>
  </div>
  </main>`;
  const extraLd = [articleLd(page, lang), breadcrumbLd(page, lang)];
  const fq = faqLd(t.sections);
  if (fq) extraLd.push(fq);
  return renderFull(lang, t.metaTitle || t.title, t.metaDescription, extraLd, page.slug, body, heroImg || DATA.site.ogImage);
}




function gnameOf(lang){ return (DATA.game.nameI18n && DATA.game.nameI18n[lang]) || DATA.game.name; }

/* ---------- static pages ---------- */
function renderStatic(lang, slug, title, body){
  const prefix = lang === DEF ? "" : `/${lang}`;
  const s = siteI18n(lang);
  const descRaw = KIT.staticDesc(slug, lang, s.name, title);
  const isCjk = lang === "zh-CN" || lang === "zh-TW" || lang === "ja" || lang === "ko";
  const desc = descRaw.length > (isCjk ? 74 : 148) ? descRaw.slice(0, (isCjk ? 73 : 147)).replace(/\s+[^\s]*$/, "") + "…" : descRaw;
  const pageTitle = `${title} — ${s.name}`;
  return renderFull(lang, pageTitle, desc, [breadcrumbLd({slug,title}, lang)], slug, `<main class="container"><div class="article-wrap single"><article><div class="page-hero reveal"><span class="evidence-tag">${esc(s.blueTag||"BLUEPRINT")} // ${esc(slug.toUpperCase())}</span><h1>${esc(title)}</h1></div>${body}</article></div></main>`);
}
function genStatic(lang){
  const s = siteI18n(lang);
  const dir = path.join(OUT, lang === DEF ? "" : lang);
  const aboutPoints = (DATA.game.aboutPointsI18n && DATA.game.aboutPointsI18n[lang]) || DATA.game.aboutPoints || [];
  const aboutBody = `<p>${esc(s.aboutText)}</p><h2 style="font-size:1.05rem;margin:18px 0 8px">${esc(s.aboutSources)}</h2><ul class="checks">${aboutPoints.map(x=>`<li>${esc(x)}</li>`).join("")}</ul>`;
  writePage(path.join(dir,"about.html"), "about", lang, renderStatic(lang,"about", s.aboutTitle,
    aboutBody + `<section class="card">` + KIT.editorialPolicy(lang, { siteName: s.name, contactEmail: `contact@${DATA.site.domain}` }) + `</section>`));
  const privacyBody = lang==="zh-CN"||lang==="zh-TW"
    ? `<p>这是游戏攻略网站，我们尊重访问者隐私。以下说明我们收集什么、如何使用。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">我们收集什么</h2><p>我们使用 Google Analytics（GA4）进行匿名流量统计：页面浏览、来源、设备类型和大致地区。我们不收集姓名、邮箱等个人身份信息，不出售数据。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Cookie</h2><p>Google Analytics 会使用 Cookie 进行会话统计。你可以在浏览器中禁用，或安装 Google Analytics 的停用插件。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">第三方服务</h2><p>字体来自 Google Fonts，站点由 Cloudflare CDN 提供服务；两者可能记录标准访问日志（IP、UA、时间）。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">联系我们</h2><p>隐私问题请邮件 <a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a>。</p><p style="margin-top:14px;opacity:.75">生效日期：${today}</p>`
    : lang==="ko"
    ? `<p>이곳은 게임 공략 사이트이며 방문자의 개인정보를 존중합니다. 수집 항목과 사용 방식을 설명합니다.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">수집하는 정보</h2><p>Google Analytics(GA4)로 익명 트래픽 통계(페이지뷰, 유입 경로, 기기 유형, 대략적 지역)를 수집합니다. 이름, 이메일 등 개인 식별 정보는 수집하지 않으며 데이터를 판매하지 않습니다.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">쿠키</h2><p>Google Analytics는 세션 통계를 위해 쿠키를 사용합니다. 브라우저에서 비활성화하거나 Google Analytics 차단 부가기능을 사용할 수 있습니다.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">제3자 서비스</h2><p>글꼴은 Google Fonts에서, 사이트는 Cloudflare CDN으로 제공됩니다. 두 서비스 모두 표준 접속 로그(IP, UA, 시간)를 기록할 수 있습니다.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">문의</h2><p>개인정보 관련 질문은 <a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a>로 보내주세요.</p><p style="margin-top:14px;opacity:.75">발효일: ${today}</p>`
    : lang==="es"
    ? `<p>Este es un sitio web de guías de juegos y respetamos la privacidad de los visitantes. Esto explica qué recopilamos y cómo se usa.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Qué recopilamos</h2><p>Usamos Google Analytics (GA4) para estadísticas de tráfico anónimas: visitas, referencias, tipos de dispositivo y regiones aproximadas. No recopilamos nombres, correos ni información personal identificable, y no vendemos datos.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Cookies</h2><p>Google Analytics usa cookies para estadísticas de sesión. Puedes desactivarlas en tu navegador o instalar el complemento de exclusión de Google Analytics.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Servicios de terceros</h2><p>Las fuentes se cargan desde Google Fonts y el sitio se sirve a través de Cloudflare CDN; ambos pueden registrar registros de acceso estándar (IP, agente de usuario, hora).</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Contacto</h2><p>Para preguntas de privacidad, escribe a <a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a>.</p><p style="margin-top:14px;opacity:.75">Fecha de entrada en vigor: ${today}</p>`
    : lang==="ja"
    ? `<p>これはゲーム攻略サイトです。訪問者のプライバシーを尊重します。以下、収集内容と利用方法を説明します。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">収集する情報</h2><p>Google Analytics（GA4）で匿名のトラフィック統計（ページビュー、参照元、端末種別、おおよその地域）を取得しています。氏名・メールアドレスなどの個人情報は収集せず、データの販売も行いません。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Cookie</h2><p>Google Analytics はセッション統計のため Cookie を使用します。ブラウザで無効化するか、Google Analytics のオプトアウトアドオンを利用できます。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">第三者サービス</h2><p>Google Fonts からフォントを、Cloudflare の CDN を利用しています。標準的なアクセスログ（IP・UA・時刻）を記録する場合があります。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">お問い合わせ</h2><p>プライバシーに関する質問は <a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a> まで。</p><p style="margin-top:14px;opacity:.75">発効日：${today}</p>`
    : `<p>This is a game guide website and we respect visitor privacy. This policy explains what we collect and how it is used.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">What we collect</h2><p>We use Google Analytics (GA4) for anonymous traffic statistics: page views, referrers, device types and approximate regions. We do not collect names, email addresses or any personally identifiable information, and we do not sell data.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Cookies</h2><p>Google Analytics sets cookies for session statistics. You can disable cookies in your browser or install the Google Analytics opt-out add-on.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Third-party services</h2><p>Fonts are loaded from Google Fonts and the site is served via Cloudflare's CDN; both may record standard access logs (IP, user agent, time). Those services follow their own privacy policies.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Contact</h2><p>For privacy questions, email <a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a>.</p><p style="margin-top:14px;opacity:.75">Effective date: ${today}</p>`;
  writePage(path.join(dir,"privacy.html"), "privacy", lang, renderStatic(lang,"privacy", s.privacyTitle, privacyBody));
  const contactPh = lang==="zh-CN"||lang==="zh-TW" ? "联系我们："
    : lang==="ja" ? "お問い合わせ："
    : lang==="ko" ? "문의하기: "
    : lang==="es" ? "Contáctanos: "
    : "Reach us at:";
  const contactReply = lang==="zh-CN"||lang==="zh-TW" ? "我们通常会在 2-3 个工作日内回复。"
    : lang==="ja" ? "通常 2〜3 営業日以内に返信します。"
    : lang==="ko" ? "보통 2~3 영업일 내에 답변드립니다."
    : lang==="es" ? "Normalmente respondemos en 2-3 días laborables."
    : "We usually reply within 2-3 business days.";
  writePage(path.join(dir,"contact.html"), "contact", lang, renderStatic(lang,"contact", s.contactTitle, `<p>${contactPh} <a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a></p><p style="margin-top:10px">${contactReply}</p>`));
}
// 404 (default lang) — function so OUT exists when called
function gen404(){
  const s404 = siteI18n(DEF);
  const pop404 = DATA.pages.filter(p=>["how-to-play","ship-building-guide","blueprints-guide","controls"].includes(p.slug)).map(p=>`<a href="/${p.slug}" style="display:inline-block;margin:6px;padding:9px 16px;border:1px solid var(--border);border-radius:10px;color:var(--muted);text-decoration:none">${esc(p.title)}</a>`).join("");
  fs.writeFileSync(path.join(OUT,"404.html"), `<!DOCTYPE html><html lang="${LANG_META[DEF].html}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>404 - ${esc(s404.name)}</title><meta name="robots" content="noindex" /><link rel="stylesheet" href="/css/style.css?v=${CSS_V}"></head><body>${header(DEF,"")}<main class="container" style="padding-top:70px;text-align:center"><section class="card grow-card" style="max-width:560px;margin:0 auto"><h1 style="font-size:3rem">404</h1><p>This page doesn't exist. Try one of these guides instead:</p><div style="margin:18px 0">${pop404}</div><p><a class="btn btn-primary" href="/">← Back to Home</a></p></section></main>${footer(DEF)}</body></html>`);
}

/* ---------- JSON-LD ---------- */
const siteLd = lang => ({"@context":"https://schema.org","@type":"WebSite",name:siteI18n(lang).name,url:urlOf("index",lang),description:siteI18n(lang).description});
function isoDate(str){
  const m=/([A-Za-z]+) (\d+), (\d+)/.exec(str||"")||[];
  const mo={Jan:1,Feb:2,Mar:3,Apr:4,May:5,Jun:6,Jul:7,Aug:8,Sep:9,Oct:10,Nov:11,Dec:12,January:1,February:2,March:3,April:4,May:5,June:6,July:7,August:8,September:9,October:10,November:11,December:12};
  return m[3] ? `${m[3]}-${String(mo[m[1]]||0).padStart(2,"0")}-${String(m[2]).padStart(2,"0")}` : today;
}
function gameLd(){
  return {"@context":"https://schema.org","@type":"VideoGame",name:DATA.game.name,description:DATA.game.intro,url:DATA.game.steamUrl,applicationCategory:"Game",operatingSystem:"Windows",genre:DATA.game.genre,datePublished:isoDate(DATA.game.releaseDate),inLanguage:"en",offers:{"@type":"Offer",price:DATA.game.price,priceCurrency:"USD",availability:"https://schema.org/InStock"}};
}
function articleLd(page, lang){
  const t = pageOf(page, lang);
  return {"@context":"https://schema.org","@type":"Article",headline:t.title,description:t.metaDescription,mainEntityOfPage:urlOf(page.slug,lang),datePublished:isoDate(DATA.game.releaseDate),dateModified:KIT.LASTMOD_TOKEN,inLanguage:LANG_META[lang]?.html||lang,publisher:{"@type":"Organization",name:siteI18n(lang).name}};
}
function faqLd(sections){
  const items = (sections||[]).filter(s=>s.type==="faq").flatMap(s=>s.items||[]);
  if (!items.length) return null;
  return {"@context":"https://schema.org","@type":"FAQPage",mainEntity:items.map(([q,a])=>({"@type":"Question",name:q,acceptedAnswer:{"@type":"Answer",text:a}}))};
}
function breadcrumbLd(page, lang){
  return {"@context":"https://schema.org","@type":"BreadcrumbList",itemListElement:[{"@type":"ListItem",position:1,name:siteI18n(lang).navHome,item:`https://${DATA.site.domain}/${lang===DEF?"":lang+"/"}`},{"@type":"ListItem",position:2,name:page.title,item:urlOf(page.slug,lang)}]};
}

/* ---------- build ---------- */
// 写页面统一走这里：按「内容是否真变了」把 lastmod 占位符换成真实日期
const writePage = (filePath, slug, lang, html) => fs.writeFileSync(filePath, LM.stamp(urlOf(slug, lang), html));
fs.rmSync(OUT, {recursive:true, force:true});

// favicon：主题图标（深空飞船），构建时生成避免 rmSync 后丢失
fs.mkdirSync(OUT, {recursive:true});
const faviconSvg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect x="2" y="2" width="60" height="60" rx="14" fill="#0B1220"/><rect x="2" y="2" width="60" height="60" rx="14" fill="none" stroke="#1E3A5F" stroke-width="2"/><path d="M32 12l16 7v14c0 8-6.5 14-16 16-9.5-2-16-8-16-16V19l16-7z" fill="none" stroke="#4FD1C5" stroke-width="3" stroke-linejoin="round"/><path d="M32 20l10 4.5v9.5c0 5.5-4 9.5-10 11-6-1.5-10-5.5-10-11v-9.5L32 20z" fill="none" stroke="#F59E0B" stroke-width="2.2" stroke-linejoin="round"/><circle cx="32" cy="32" r="3.4" fill="#4FD1C5"/></svg>`;
fs.writeFileSync(path.join(OUT, "favicon.svg"), faviconSvg);
for (const f of ["favicon-16x16.png","favicon-32x32.png","apple-touch-icon.png"]) {
  const srcFav = path.join(ROOT, "templates", "favicon", f);
  if (fs.existsSync(srcFav)) fs.copyFileSync(srcFav, path.join(OUT, f));
}
fs.mkdirSync(OUT, {recursive:true});
// assets copy
for (const f of ["favicon.svg","favicon-16x16.png","favicon-32x32.png","apple-touch-icon.png"]) {
  const src = path.join(ROOT,"assets","favicon",f);
  if (fs.existsSync(src)) fs.copyFileSync(src, path.join(OUT,f));
}
const imgDir = path.join(ROOT,"assets","images");
if (fs.existsSync(imgDir)) {
  fs.mkdirSync(path.join(OUT,"images"),{recursive:true});
  for (const f of fs.readdirSync(imgDir)) {
    if (/\.(jpg|jpeg|webp)$/i.test(f)) fs.copyFileSync(path.join(imgDir,f), path.join(OUT,"images",f));
  }
}
fs.mkdirSync(path.join(OUT,"css"),{recursive:true});
fs.writeFileSync(path.join(OUT,"css","style.css"), fs.readFileSync(path.join(ROOT,"templates","style.css"),"utf8"));

// index + pages per language
for (const lang of LANGS) {
  const dir = path.join(OUT, lang === DEF ? "" : lang);
  fs.mkdirSync(dir, {recursive:true});
  writePage(path.join(dir,"index.html"), "index", lang, renderHome(lang));
  for (const page of DATA.pages) {
    SEC_IDX = 0;
    const html = renderPage(lang, page);
    writePage(path.join(dir, page.slug + ".html"), page.slug, lang, html);
  }
  genStatic(lang);
}
gen404();

// sitemap（lastmod 走 LM：内容没变就沿用旧日期，不再每次全站标记为当天）
const urls = [];
for (const lang of LANGS) {
  urls.push({ loc: urlOf("index",lang), priority: "1.0" });
  for (const p of DATA.pages) urls.push({ loc: urlOf(p.slug,lang), priority: "0.8" });
  for (const sp of ["about","privacy","contact"]) urls.push({ loc: urlOf(sp,lang), priority: "0.3" });
}
const smN = KIT.writeSitemap(OUT, urls, LM);
KIT.writeRobots(OUT, DATA.site.domain);
KIT.writeAds(OUT, DATA.site.adsenseId);
KIT.writeHeaders(OUT);
KIT.writeIndexNowKey(OUT, DATA.site.indexNowKey);
// llms.txt：给 AI agent 的机器可读入口（不是 SEO 手段，见 site-kit 注释）
KIT.writeLlmsTxt(OUT, {
  siteName: DATA.site.name,
  domain: DATA.site.domain,
  summary: `Unofficial ${DATA.game.name} guide site. Each page answers one question players actually search for, and lists the sources it was checked against. Available in ${LANGS.length} languages: ${LANGS.join(", ")}.`,
  pages: DATA.pages.map(p => { const t = pageOf(p, DEF); return { slug: p.slug, title: t.title, desc: t.metaDescription }; }),
  notes: [
    "Facts are checked against the official Steam store page and reputable gaming media; every page lists its own sources at the bottom.",
    "Anything we could not verify is explicitly marked as unverified — gaps are left open rather than filled with generated text.",
    "Localised versions live under /<lang>/ (e.g. /ja/how-to-play) and are declared via hreflang on every page.",
    "This is an unofficial fan site, not affiliated with the game's developer or publisher."
  ]
});
const lm = LM.save();
console.log(`✓ ${LANGS.length} locales × ${1+DATA.pages.length+3} pages｜sitemap ${smN} URL｜内容有变更 ${lm.changed}/${lm.total} 页`);
