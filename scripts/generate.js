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
const ADSENSE_FIXTURE_ENABLED = process.env.NODE_ENV === "test" && process.env.APPROX_UP_ADSENSE_FIXTURE === "enabled";
const ADSENSE_PUBLISHER_ID = /^pub-\d+$/.test(String(DATA.site.adsenseId || "").trim())
  ? String(DATA.site.adsenseId).trim()
  : "";
const ADSENSE_CLIENT_ID = ADSENSE_PUBLISHER_ID ? `ca-${ADSENSE_PUBLISHER_ID}` : "";
const ADSENSE_SERVING_ENABLED = Boolean(
  ADSENSE_CLIENT_ID && (
    ADSENSE_FIXTURE_ENABLED || (
      DATA.site.adsenseServing &&
      DATA.site.adsenseServing.enabled === true &&
      DATA.site.adsenseServing.providerReady === true &&
      DATA.site.adsenseServing.certifiedCmpReady === true
    )
  )
);
const adsenseScript = () => ADSENSE_SERVING_ENABLED
  ? `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${esc(ADSENSE_CLIENT_ID)}" crossorigin="anonymous"></script>`
  : "";
const LANGS = DATA.site.languages || ["en"];
const DEF = DATA.site.defaultLanguage || "en";
const CSS_V = crypto.createHash("md5").update(fs.readFileSync(path.join(ROOT,"templates","style.css"),"utf8")).digest("hex").slice(0,8);
const today = new Date().toISOString().slice(0,10);
const urlOf = KIT.createUrl({ domain: DATA.site.domain, defaultLang: DEF });
const LM = KIT.createLastmod({ manifestPath: path.join(ROOT,"data",".lastmod.json"), today });
const HERO_SET = "/images/hero-640.jpg 640w, /images/hero-1280.jpg 1280w, /images/hero.jpg 1600w";
const UPDATED_LABEL = { en:"Updated", "zh-CN":"更新于", "zh-TW":"更新於", ja:"更新日", ko:"업데이트", es:"Actualizado", fr:"Mis à jour", de:"Aktualisiert", it:"Aggiornato", pl:"Zaktualizowano", "pt-BR":"Atualizado", ru:"Обновлено", uk:"Оновлено", vi:"Đã cập nhật" };
const updLabel = lang => UPDATED_LABEL[lang] || "Updated";
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

const CONSENT_I18N = {
  en: { settings:"Privacy settings", title:"Privacy choices", intro:"Choose whether this site may load optional analytics and advertising.", analytics:"Analytics", analyticsHelp:"Google Analytics 4 may process device, browser, page, referrer, approximate region and network data for measurement.", ads:"Advertising", adsHelp:"Adsterra/effectivecpmnetwork may process device and network data to deliver and measure an ad. Google AdSense serving remains disabled.", accept:"Accept all", reject:"Reject", manage:"Manage options", save:"Save choices", withdraw:"Withdraw optional consent", close:"Close privacy choices" },
  "zh-CN": { settings:"隐私设置", title:"隐私选择", intro:"请选择是否允许本站加载可选的统计与广告服务。", analytics:"统计分析", analyticsHelp:"Google Analytics 4 可能为统计处理设备、浏览器、页面、来源、大致地区和网络数据。", ads:"广告", adsHelp:"Adsterra/effectivecpmnetwork 可能处理设备和网络数据以投放并衡量一则广告；Google AdSense 投放仍关闭。", accept:"全部同意", reject:"不同意", manage:"管理选项", save:"保存选择", withdraw:"撤回可选同意", close:"关闭隐私选择" },
  "zh-TW": { settings:"隱私設定", title:"隱私選擇", intro:"請選擇是否允許本站載入可選的統計與廣告服務。", analytics:"統計分析", analyticsHelp:"Google Analytics 4 可能為統計處理裝置、瀏覽器、頁面、來源、大致地區與網路資料。", ads:"廣告", adsHelp:"Adsterra/effectivecpmnetwork 可能處理裝置與網路資料以投放並衡量一則廣告；Google AdSense 投放仍關閉。", accept:"全部同意", reject:"不同意", manage:"管理選項", save:"儲存選擇", withdraw:"撤回可選同意", close:"關閉隱私選擇" },
  ja: { settings:"プライバシー設定", title:"プライバシーの選択", intro:"任意のアクセス解析と広告サービスの読み込みを許可するか選択してください。", analytics:"アクセス解析", analyticsHelp:"Google Analytics 4 は測定のため端末、ブラウザー、ページ、参照元、おおよその地域、ネットワーク情報を処理する場合があります。", ads:"広告", adsHelp:"Adsterra/effectivecpmnetwork は広告の配信・測定のため端末・ネットワーク情報を処理する場合があります。Google AdSense 配信は無効です。", accept:"すべて許可", reject:"拒否", manage:"設定を管理", save:"選択を保存", withdraw:"任意の同意を撤回", close:"プライバシー選択を閉じる" },
  ko: { settings:"개인정보 설정", title:"개인정보 선택", intro:"선택적 분석 및 광고 서비스 로드를 허용할지 선택하세요.", analytics:"분석", analyticsHelp:"Google Analytics 4는 측정을 위해 기기, 브라우저, 페이지, 유입 경로, 대략적 지역 및 네트워크 데이터를 처리할 수 있습니다.", ads:"광고", adsHelp:"Adsterra/effectivecpmnetwork는 광고 제공과 측정을 위해 기기 및 네트워크 데이터를 처리할 수 있습니다. Google AdSense 게재는 비활성 상태입니다.", accept:"모두 동의", reject:"거부", manage:"옵션 관리", save:"선택 저장", withdraw:"선택적 동의 철회", close:"개인정보 선택 닫기" },
  fr: { settings:"Réglages de confidentialité", title:"Choix de confidentialité", intro:"Choisissez si ce site peut charger l'analyse et la publicité facultatives.", analytics:"Analyse", analyticsHelp:"Google Analytics 4 peut traiter les données d'appareil, navigateur, page, référent, région approximative et réseau à des fins de mesure.", ads:"Publicité", adsHelp:"Adsterra/effectivecpmnetwork peut traiter des données d'appareil et de réseau pour diffuser et mesurer une annonce. La diffusion Google AdSense reste désactivée.", accept:"Tout accepter", reject:"Refuser", manage:"Gérer les options", save:"Enregistrer", withdraw:"Retirer le consentement facultatif", close:"Fermer les choix" },
  de: { settings:"Datenschutzeinstellungen", title:"Datenschutzauswahl", intro:"Wählen Sie, ob diese Website optionale Analyse und Werbung laden darf.", analytics:"Analyse", analyticsHelp:"Google Analytics 4 kann Geräte-, Browser-, Seiten-, Referrer-, ungefähre Regions- und Netzwerkdaten zur Messung verarbeiten.", ads:"Werbung", adsHelp:"Adsterra/effectivecpmnetwork kann Geräte- und Netzwerkdaten zur Auslieferung und Messung einer Anzeige verarbeiten. Google AdSense bleibt deaktiviert.", accept:"Alle akzeptieren", reject:"Ablehnen", manage:"Optionen verwalten", save:"Auswahl speichern", withdraw:"Optionale Einwilligung widerrufen", close:"Datenschutzauswahl schließen" },
  es: { settings:"Configuración de privacidad", title:"Opciones de privacidad", intro:"Elige si este sitio puede cargar análisis y publicidad opcionales.", analytics:"Análisis", analyticsHelp:"Google Analytics 4 puede tratar datos del dispositivo, navegador, página, referencia, región aproximada y red para medición.", ads:"Publicidad", adsHelp:"Adsterra/effectivecpmnetwork puede tratar datos del dispositivo y la red para servir y medir un anuncio. Google AdSense permanece desactivado.", accept:"Aceptar todo", reject:"Rechazar", manage:"Gestionar opciones", save:"Guardar opciones", withdraw:"Retirar consentimiento opcional", close:"Cerrar opciones" },
  it: { settings:"Impostazioni privacy", title:"Scelte sulla privacy", intro:"Scegli se il sito può caricare analisi e pubblicità facoltative.", analytics:"Analisi", analyticsHelp:"Google Analytics 4 può trattare dati su dispositivo, browser, pagina, provenienza, area approssimativa e rete per la misurazione.", ads:"Pubblicità", adsHelp:"Adsterra/effectivecpmnetwork può trattare dati del dispositivo e di rete per mostrare e misurare un annuncio. La pubblicazione Google AdSense resta disattivata.", accept:"Accetta tutto", reject:"Rifiuta", manage:"Gestisci opzioni", save:"Salva scelte", withdraw:"Revoca consenso facoltativo", close:"Chiudi le scelte" },
  pl: { settings:"Ustawienia prywatności", title:"Wybory prywatności", intro:"Wybierz, czy witryna może ładować opcjonalną analitykę i reklamy.", analytics:"Analityka", analyticsHelp:"Google Analytics 4 może przetwarzać dane urządzenia, przeglądarki, strony, odsyłacza, przybliżonego regionu i sieci do pomiarów.", ads:"Reklamy", adsHelp:"Adsterra/effectivecpmnetwork może przetwarzać dane urządzenia i sieci w celu wyświetlenia i pomiaru reklamy. Emisja Google AdSense pozostaje wyłączona.", accept:"Zaakceptuj wszystko", reject:"Odrzuć", manage:"Zarządzaj opcjami", save:"Zapisz wybór", withdraw:"Wycofaj opcjonalną zgodę", close:"Zamknij wybory" },
  "pt-BR": { settings:"Configurações de privacidade", title:"Escolhas de privacidade", intro:"Escolha se este site pode carregar análise e publicidade opcionais.", analytics:"Análise", analyticsHelp:"O Google Analytics 4 pode tratar dados de dispositivo, navegador, página, referência, região aproximada e rede para medição.", ads:"Publicidade", adsHelp:"A Adsterra/effectivecpmnetwork pode tratar dados do dispositivo e da rede para exibir e medir um anúncio. A veiculação do Google AdSense permanece desativada.", accept:"Aceitar tudo", reject:"Recusar", manage:"Gerenciar opções", save:"Salvar escolhas", withdraw:"Retirar consentimento opcional", close:"Fechar escolhas" },
  ru: { settings:"Настройки конфиденциальности", title:"Выбор конфиденциальности", intro:"Выберите, может ли сайт загружать необязательную аналитику и рекламу.", analytics:"Аналитика", analyticsHelp:"Google Analytics 4 может обрабатывать данные устройства, браузера, страницы, источника, примерного региона и сети для измерений.", ads:"Реклама", adsHelp:"Adsterra/effectivecpmnetwork может обрабатывать данные устройства и сети для показа и измерения рекламы. Показ Google AdSense остаётся отключённым.", accept:"Принять всё", reject:"Отклонить", manage:"Настроить", save:"Сохранить выбор", withdraw:"Отозвать необязательное согласие", close:"Закрыть выбор" },
  uk: { settings:"Налаштування приватності", title:"Вибір приватності", intro:"Виберіть, чи може сайт завантажувати необов’язкову аналітику та рекламу.", analytics:"Аналітика", analyticsHelp:"Google Analytics 4 може обробляти дані пристрою, браузера, сторінки, джерела, приблизного регіону й мережі для вимірювання.", ads:"Реклама", adsHelp:"Adsterra/effectivecpmnetwork може обробляти дані пристрою й мережі для показу та вимірювання реклами. Показ Google AdSense залишається вимкненим.", accept:"Прийняти все", reject:"Відхилити", manage:"Керувати параметрами", save:"Зберегти вибір", withdraw:"Відкликати необов’язкову згоду", close:"Закрити вибір" },
  vi: { settings:"Cài đặt quyền riêng tư", title:"Lựa chọn quyền riêng tư", intro:"Chọn xem trang web có thể tải phân tích và quảng cáo tùy chọn hay không.", analytics:"Phân tích", analyticsHelp:"Google Analytics 4 có thể xử lý dữ liệu thiết bị, trình duyệt, trang, nguồn giới thiệu, khu vực gần đúng và mạng để đo lường.", ads:"Quảng cáo", adsHelp:"Adsterra/effectivecpmnetwork có thể xử lý dữ liệu thiết bị và mạng để phân phối và đo lường một quảng cáo. Việc phân phối Google AdSense vẫn tắt.", accept:"Chấp nhận tất cả", reject:"Từ chối", manage:"Quản lý lựa chọn", save:"Lưu lựa chọn", withdraw:"Rút lại đồng ý tùy chọn", close:"Đóng lựa chọn" },
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
function head(title, desc, extraLd, slug, lang, ogImage, bodyClass){
  const ld = JSON.stringify([siteLd(lang)].concat(extraLd || []));
  const gsc = DATA.site.gscVerification ? `<meta name="google-site-verification" content="${esc(DATA.site.gscVerification)}" />` : "";
  const adsenseMeta = ADSENSE_CLIENT_ID ? `<meta name="google-adsense-account" content="${esc(ADSENSE_CLIENT_ID)}" />` : "";
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
	</head>
	<body${bodyClass ? ` class="${bodyClass}"` : ""}>`;
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

const AD_LABEL = {
  en:"Advertisement", "zh-CN":"广告", "zh-TW":"廣告", ja:"広告", ko:"광고", fr:"Publicité",
  de:"Werbung", es:"Publicidad", it:"Pubblicità", pl:"Reklama", "pt-BR":"Publicidade",
  ru:"Реклама", uk:"Реклама", vi:"Quảng cáo"
};
function commercialSlot(lang){
  const label = AD_LABEL[lang] || AD_LABEL.en;
  return `<aside class="commercial-slot" data-commercial-slot="primary-display" data-state="idle" aria-label="${esc(label)}" hidden>
    <div class="commercial-label">${esc(label)}</div>
    <div class="commercial-surface" data-commercial-surface></div>
  </aside>`;
}

function consentUi(lang, commercialEligible){
  const t = CONSENT_I18N[lang] || CONSENT_I18N.en;
  const rawAd = String(DATA.site.adsterra || "");
  const adsterraSrc = commercialEligible ? ((rawAd.match(/src="([^"]*effectivecpmnetwork\.com[^"]*)"/) || [])[1] || "") : "";
  const adsterraContainer = commercialEligible ? ((rawAd.match(/id="(container-[^"]+)"/) || [])[1] || "") : "";
  const adsenseSrc = ADSENSE_SERVING_ENABLED
    ? `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${ADSENSE_CLIENT_ID}`
    : "";
  const cfg = JSON.stringify({gaId:DATA.site.gaId || "",adsterraSrc,adsterraContainer,adsenseSrc});
  return `<button type="button" class="privacy-settings" data-consent-settings aria-haspopup="dialog" aria-controls="privacy-consent-dialog" aria-expanded="false">${esc(t.settings)}</button>
  <dialog id="privacy-consent-dialog" class="consent-dialog" data-consent-dialog data-consent-locale="${esc(lang)}" aria-labelledby="privacy-consent-title">
    <div class="consent-card">
      <button type="button" class="consent-close" data-consent-close aria-label="${esc(t.close)}">×</button>
      <h2 id="privacy-consent-title" tabindex="-1">${esc(t.title)}</h2><p>${esc(t.intro)}</p>
      <div class="consent-summary"><b>${esc(t.analytics)}</b><span>${esc(t.analyticsHelp)}</span><b>${esc(t.ads)}</b><span>${esc(t.adsHelp)}</span></div>
      <div class="consent-manage" data-consent-manage hidden>
        <label><input type="checkbox" data-consent-analytics> <span><b>${esc(t.analytics)}</b><small>${esc(t.analyticsHelp)}</small></span></label>
        <label><input type="checkbox" data-consent-advertising> <span><b>${esc(t.ads)}</b><small>${esc(t.adsHelp)}</small></span></label>
      </div>
      <div class="consent-actions">
        <button type="button" data-consent-accept>${esc(t.accept)}</button>
        <button type="button" data-consent-reject>${esc(t.reject)}</button>
        <button type="button" data-consent-manage-open>${esc(t.manage)}</button>
        <button type="button" data-consent-save hidden>${esc(t.save)}</button>
        <button type="button" data-consent-withdraw hidden>${esc(t.withdraw)}</button>
      </div>
    </div>
  </dialog>
  <script>
  (function(){
    var cfg=${cfg},key="approximately-up-consent-v1",dialog=document.querySelector("[data-consent-dialog]");
    var settings=document.querySelector("[data-consent-settings]"),opener=null,loaded={analytics:false,adsterra:false,adsense:false},adObserver=null;
    function read(){try{var v=JSON.parse(localStorage.getItem(key)||"null");return v&&typeof v.analytics==="boolean"&&typeof v.advertising==="boolean"?v:null;}catch(_){return null;}}
    function loadAnalytics(){if(loaded.analytics||!cfg.gaId)return;loaded.analytics=true;window.dataLayer=window.dataLayer||[];window.gtag=window.gtag||function(){dataLayer.push(arguments);};gtag("js",new Date());gtag("config",cfg.gaId);var s=document.createElement("script");s.async=true;s.src="https://www.googletagmanager.com/gtag/js?id="+encodeURIComponent(cfg.gaId);document.head.appendChild(s);}
    function removeSlot(slot,state){if(!slot)return;slot.dataset.state=state||"empty";slot.hidden=true;slot.replaceChildren();slot.remove();}
    function loadAdvertising(slot){if(!slot||!slot.isConnected||loaded.adsterra||!cfg.adsterraSrc)return;loaded.adsterra=true;slot.hidden=false;slot.dataset.state="loading";var surface=slot.querySelector("[data-commercial-surface]");if(!surface){removeSlot(slot,"error");return;}var provider=document.createElement("div");provider.setAttribute("data-commercial-provider","");if(cfg.adsterraContainer)provider.id=cfg.adsterraContainer;surface.appendChild(provider);var settled=false,stable=0,lastHeight=0,a=null;
      function providerError(e){if(!settled&&slot.dataset.state==="loading"&&(e.target===a||e.target===window||(e.filename&&e.filename.indexOf(cfg.adsterraSrc)>-1)))fail("error");}
      function finish(){if(mutation)mutation.disconnect();window.removeEventListener("error",providerError,true);}
      function fail(state){if(settled)return;settled=true;finish();removeSlot(slot,state);}
      function inspect(){if(settled||!slot.isConnected)return;var child=provider.querySelector("iframe,a,img,video,object,embed")||provider.firstElementChild;var h=child?Math.max(child.getBoundingClientRect().height,provider.getBoundingClientRect().height):0;if(h>0&&Math.abs(h-lastHeight)<1){stable+=1;}else{stable=0;lastHeight=h;}if(stable>=2){settled=true;finish();slot.style.setProperty("--commercial-filled-height",Math.ceil(h)+"px");slot.dataset.state="filled";}else requestAnimationFrame(inspect);}
      var mutation=new MutationObserver(function(){requestAnimationFrame(inspect);});mutation.observe(provider,{childList:true,subtree:true,attributes:true});a=document.createElement("script");a.async=true;a.setAttribute("data-cfasync","false");a.src=cfg.adsterraSrc;a.onerror=function(){fail("error");};window.addEventListener("error",providerError,true);surface.appendChild(a);requestAnimationFrame(inspect);setTimeout(function(){fail("empty");},2500);
    }
    function armAdvertising(){var slot=document.querySelector('[data-commercial-slot="primary-display"]');if(!slot||loaded.adsterra||!cfg.adsterraSrc)return;var target=slot.previousElementSibling||slot.parentElement;if("IntersectionObserver" in window&&target){adObserver=new IntersectionObserver(function(es){if(es.some(function(e){return e.isIntersecting;})){adObserver.disconnect();loadAdvertising(slot);}},{rootMargin:"1200px 0px",threshold:0});adObserver.observe(target);}else loadAdvertising(slot);}
    function clearAdvertising(){if(adObserver){adObserver.disconnect();adObserver=null;}var slot=document.querySelector('[data-commercial-slot="primary-display"]');if(!slot)return;if(loaded.adsterra)removeSlot(slot,"empty");else{slot.dataset.state="idle";slot.hidden=true;}}
    function apply(v){if(v&&v.analytics)loadAnalytics();if(v&&v.advertising)armAdvertising();else clearAdvertising();}
    function restoreFocus(){settings.setAttribute("aria-expanded","false");if(opener&&opener.isConnected&&opener.focus)opener.focus();opener=null;}
    function close(){if(dialog.open)dialog.close();}
    function open(source){opener=source||document.activeElement;var v=read(),manage=dialog.querySelector("[data-consent-manage]");dialog.querySelector("[data-consent-analytics]").checked=!!(v&&v.analytics);dialog.querySelector("[data-consent-advertising]").checked=!!(v&&v.advertising);manage.hidden=true;dialog.querySelector("[data-consent-save]").hidden=true;dialog.querySelector("[data-consent-withdraw]").hidden=!v;settings.setAttribute("aria-expanded","true");dialog.showModal();dialog.querySelector("#privacy-consent-title").focus();}
    function save(v){localStorage.setItem(key,JSON.stringify(v));apply(v);close();}
    settings.addEventListener("click",function(){open(settings);});
    dialog.querySelector("[data-consent-close]").addEventListener("click",close);
    dialog.querySelector("[data-consent-accept]").addEventListener("click",function(){save({analytics:true,advertising:true});});
    dialog.querySelector("[data-consent-reject]").addEventListener("click",function(){save({analytics:false,advertising:false});});
    dialog.querySelector("[data-consent-manage-open]").addEventListener("click",function(){dialog.querySelector("[data-consent-manage]").hidden=false;dialog.querySelector("[data-consent-save]").hidden=false;});
    dialog.querySelector("[data-consent-save]").addEventListener("click",function(){save({analytics:dialog.querySelector("[data-consent-analytics]").checked,advertising:dialog.querySelector("[data-consent-advertising]").checked});});
    dialog.querySelector("[data-consent-withdraw]").addEventListener("click",function(){save({analytics:false,advertising:false});});
    dialog.addEventListener("keydown",function(e){if(e.key!=="Tab")return;var f=Array.prototype.filter.call(dialog.querySelectorAll('button:not([hidden]),input:not([hidden]),[href]:not([hidden]),[tabindex]:not([tabindex="-1"]):not([hidden])'),function(el){return !el.disabled&&el.offsetParent!==null;});if(!f.length){e.preventDefault();return;}var first=f[0],last=f[f.length-1];if(e.shiftKey&&(document.activeElement===first||document.activeElement===dialog)){e.preventDefault();last.focus();}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}});
    dialog.addEventListener("cancel",function(e){e.preventDefault();close();});
    dialog.addEventListener("close",restoreFocus);
    var initial=read();if(initial)apply(initial);else setTimeout(function(){open(settings);},0);
  })();
  </script>`;
}

function decisionEventsScript(){
  return `<script>(function(){
    function send(name,params){if(typeof window.gtag==="function")window.gtag("event",name,params||{});}
    document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest("a[href]");if(a){try{var u=new URL(a.href,location.href);if(u.origin!==location.origin)send("outbound_click",{link_domain:u.hostname,link_url:u.origin+u.pathname,page_path:location.pathname});}catch(_){}}
      var root=e.target.closest&&e.target.closest(".tracker,[data-tool]");var control=e.target.closest&&e.target.closest("button,[role=button]");if(root&&control)send("tool_interaction",{tool_name:root.getAttribute("data-tool")||root.id||"interactive_tool",interaction_type:control.type||control.tagName.toLowerCase(),page_path:location.pathname});
    });
    document.addEventListener("change",function(e){var root=e.target.closest&&e.target.closest(".tracker,[data-tool]");if(root)send("tool_interaction",{tool_name:root.getAttribute("data-tool")||root.id||"interactive_tool",interaction_type:e.target.type||e.target.tagName.toLowerCase(),page_path:location.pathname});});
  })();</script>`;
}
function footer(lang, commercialEligible=false){
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
      <p>${esc(s.footerSource)} · ${updLabel(lang)} ${today}</p>
    </div>
	    ${consentUi(lang, commercialEligible)}
	  </div>
	${decisionEventsScript()}
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
// 首页系统舱段：14 语言均提供适切标签与描述（zh-TW 用繁体，非中文语言不回退简体中文）
const HAB_I18N = {
  COCKPIT: {
    en: { label: "Cockpit — start here", desc: "First flight, controls, and the build-crash-rebuild loop." },
    "zh-CN": { label: "驾驶舱 — 从这里开始", desc: "首次飞行、操作方式，以及建造-坠毁-重建的循环。" },
    "zh-TW": { label: "駕駛艙 — 從這裡開始", desc: "首次飛行、操作方式，以及建造—墜毀—重建的循環。" },
    ja: { label: "コックピット — ここから始める", desc: "初飛行、操作、そして作って・壊して・作り直すループ。" },
    ko: { label: "조종석 — 여기서 시작", desc: "첫 비행, 조작, 그리고 만들고-부수고-다시 만드는 순환." },
    fr: { label: "Poste de pilotage — commencez ici", desc: "Premier vol, commandes et le cycle construire-écraser-reconstruire." },
    de: { label: "Cockpit — hier beginnen", desc: "Erster Flug, Steuerung und der Kreislauf aus Bauen, Absturz und Neuaufbau." },
    es: { label: "Cabina — empieza aquí", desc: "Primer vuelo, controles y el ciclo construir-estrellarse-reconstruir." },
    it: { label: "Cabina di pilotaggio — inizia qui", desc: "Primo volo, comandi e il ciclo costruisci-schiantati-ricostruisci." },
    pl: { label: "Kabina — zacznij tutaj", desc: "Pierwszy lot, sterowanie i cykl buduj-rozbij-odbuduj." },
    "pt-BR": { label: "Cabine — comece aqui", desc: "Primeiro voo, controles e o ciclo construir-quebrar-reconstruir." },
    ru: { label: "Кабина — начните здесь", desc: "Первый полёт, управление и цикл «построй-разбей-перестрой»." },
    uk: { label: "Кабіна — почніть тут", desc: "Перший політ, керування та цикл «побудуй-розбий-перебудуй»." },
    vi: { label: "Buồng lái — bắt đầu tại đây", desc: "Chuyến bay đầu tiên, điều khiển và vòng lặp xây-dựng-hỏng-xây-lại." },
  },
  ENGINE: {
    en: { label: "Engine room — ship building", desc: "Modular ships, thrusters, wiring and blueprints." },
    "zh-CN": { label: "引擎舱 — 飞船建造", desc: "模块化飞船、推进器、电路与蓝图。" },
    "zh-TW": { label: "引擎艙 — 飛船建造", desc: "模組化飛船、推進器、電路與藍圖。" },
    ja: { label: "機関室 — 船の建造", desc: "モジュール式の船、スラスター、配線、ブループリント。" },
    ko: { label: "기관실 — 함선 건조", desc: "모듈식 함선, 추진기, 배선, 설계도." },
    fr: { label: "Salle des machines — construction de vaisseaux", desc: "Vaisseaux modulaires, propulseurs, câblage et plans." },
    de: { label: "Maschinenraum — Schiffbau", desc: "Modulare Schiffe, Triebwerke, Verkabelung und Baupläne." },
    es: { label: "Sala de máquinas — construcción de naves", desc: "Naves modulares, propulsores, cableado y planos." },
    it: { label: "Sala macchine — costruzione di navi", desc: "Navi modulari, propulsori, cablaggio e progetti." },
    pl: { label: "Maszynownia — budowa statków", desc: "Modułowe statki, silniki, okablowanie i plany." },
    "pt-BR": { label: "Casa de máquinas — construção de naves", desc: "Naves modulares, propulsores, fiação e projetos." },
    ru: { label: "Машинное отделение — строительство кораблей", desc: "Модульные корабли, двигатели, проводка и чертежи." },
    uk: { label: "Машинне відділення — будівництво кораблів", desc: "Модульні кораблі, двигуни, проводка та креслення." },
    vi: { label: "Phòng máy — đóng tàu", desc: "Tàu mô-đun, động cơ đẩy, hệ thống dây điện và bản thiết kế." },
  },
  CARGO: {
    en: { label: "Cargo bay — references", desc: "Console release, mods, updates and demo comparison." },
    "zh-CN": { label: "货舱 — 参考资料", desc: "主机版发售、模组、更新与试玩版对比。" },
    "zh-TW": { label: "貨艙 — 參考資料", desc: "主機版發售、模組、更新與試玩版比較。" },
    ja: { label: "カーゴベイ — リファレンス", desc: "コンソール版、MOD、アップデート、デモ比較。" },
    ko: { label: "화물칸 — 참고 자료", desc: "콘솔 출시, 모드, 업데이트, 데모 비교." },
    fr: { label: "Soute à marchandises — références", desc: "Sortie console, mods, mises à jour et comparaison de la démo." },
    de: { label: "Frachtraum — Referenzen", desc: "Konsolen-Release, Mods, Updates und Demo-Vergleich." },
    es: { label: "Bodega de carga — referencias", desc: "Lanzamiento en consolas, mods, actualizaciones y comparación de la demo." },
    it: { label: "Stiva cargo — riferimenti", desc: "Uscita console, mod, aggiornamenti e confronto con la demo." },
    pl: { label: "Ładownia — materiały", desc: "Premiera na konsole, mody, aktualizacje i porównanie wersji demo." },
    "pt-BR": { label: "Porão de carga — referências", desc: "Lançamento em consoles, mods, atualizações e comparação da demo." },
    ru: { label: "Грузовой отсек — справочники", desc: "Релиз на консолях, моды, обновления и сравнение демо." },
    uk: { label: "Вантажний відсік — довідники", desc: "Реліз на консолях, моди, оновлення та порівняння демо." },
    vi: { label: "Khoang hàng — tài liệu tham khảo", desc: "Bản console, mod, cập nhật và so sánh bản demo." },
  },
  ARCHIVE: {
    en: { label: "Archive — achievements & indexes", desc: "Achievements, ships index, blueprints index and guide index." },
    "zh-CN": { label: "资料库 — 成就与索引", desc: "成就、飞船索引、蓝图索引与攻略索引。" },
    "zh-TW": { label: "資料庫 — 成就與索引", desc: "成就、飛船索引、藍圖索引與攻略索引。" },
    ja: { label: "資料室 — 実績と索引", desc: "実績、船の索引、ブループリント索引、ガイド索引。" },
    ko: { label: "기록실 — 업적 및 색인", desc: "업적, 함선 색인, 설계도 색인, 가이드 색인." },
    fr: { label: "Archives — succès et index", desc: "Succès, index des vaisseaux, index des plans et index des guides." },
    de: { label: "Archiv — Erfolge und Verzeichnisse", desc: "Erfolge, Schiffsverzeichnis, Bauplan-Verzeichnis und Guide-Verzeichnis." },
    es: { label: "Archivo — logros e índices", desc: "Logros, índice de naves, índice de planos e índice de guías." },
    it: { label: "Archivio — obiettivi e indici", desc: "Obiettivi, indice delle navi, indice dei progetti e indice delle guide." },
    pl: { label: "Archiwum — osiągnięcia i indeksy", desc: "Osiągnięcia, indeks statków, indeks planów i indeks poradników." },
    "pt-BR": { label: "Arquivo — conquistas e índices", desc: "Conquistas, índice de naves, índice de projetos e índice de guias." },
    ru: { label: "Архив — достижения и указатели", desc: "Достижения, указатель кораблей, чертежей и гайдов." },
    uk: { label: "Архів — досягнення та покажчики", desc: "Досягнення, покажчик кораблів, креслень і гайдів." },
    vi: { label: "Kho lưu trữ — thành tựu và chỉ mục", desc: "Thành tựu, chỉ mục tàu, chỉ mục bản thiết kế và chỉ mục hướng dẫn." },
  },
};

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
    {code:"COCKPIT", acc:"var(--cyan)",   slugs:["how-to-play","controls","system-requirements","multiplayer"]},
    {code:"ENGINE",  acc:"var(--amber)",  slugs:["ship-building-guide","wiring-electronics","blueprints-guide","best-ship-designs"]},
    {code:"CARGO",   acc:"var(--violet)", slugs:["console-release","mods","patch-notes","demo-vs-full"]},
    {code:"ARCHIVE", acc:"#5CB8FF",       slugs:["achievements","achievements-list","ships","blueprints","guides"]},
  ];
  const habPanels = HAB.map((h,i)=>{
    const t = HAB_I18N[h.code][lang] || HAB_I18N[h.code].en;
    const links = h.slugs.map(slug=>{
      const p=DATA.pages.find(x=>x.slug===slug); if(!p) return "";
      const m=metaOf(slug); const t2=Object.assign(pageOf(p,lang),{slug});
      return `<a class="hab-link" href="${prefix}/${slug}" style="--hab-acc:${h.acc}"><span class="hab-ic">${SVG[m.icon]}</span><span class="hab-tx">${esc(t2.title)}</span><span class="hab-go">${String(i+1)}.${h.slugs.indexOf(slug)+1} →</span></a>`;
    }).join("");
    const panel = `<section class="hab-panel reveal" id="hab-${i+1}" style="--hab-acc:${h.acc}">
      <div class="hab-head"><span class="hab-code">${h.code}</span><h2>${esc(t.label)}</h2>${t.desc?`<p>${esc(t.desc)}</p>`:""}</div>
      <div class="hab-links">${links}</div>
    </section>`;
    return panel + (i === 1 ? commercialSlot(lang) : "");
  }).join("");
  const heroImg = DATA.site.ogImage || "/images/hero.jpg";
  const heroCardImg = `<div class="ship-imgwrap">${KIT.picture({ src: heroImg, srcset: "/images/hero-640.jpg 640w, /images/hero-1280.jpg 1280w, /images/hero.jpg 1600w", sizes: "100vw", attrs: `class="ship-img" alt="${esc(gname)}" loading="eager" width="1600" height="900"` })}</div>`;
  return head(s.name, s.description, [gameLd()], "index", lang, undefined, "home") + `
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
	        <a class="btn btn-primary" href="${esc(DATA.game.steamUrl)}" rel="noopener">${esc(s.getOnSteam)}</a>
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
${footer(lang, true)}
</body></html>`;
}




function renderFull(lang, title, desc, extraLd, slug, body, ogImage){
  const s = siteI18n(lang);
  const commercialEligible = slug === "index" || DATA.pages.some(page => page.slug === slug);
  return head(title, desc, extraLd, slug, lang, ogImage) + header(lang, slug === "index" ? "" : slug) + body + footer(lang, commercialEligible);
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
  const renderedSections = (t.sections||[]).map(x => renderSection(x, lang));
  const insertionIndex = renderedSections.length >= 3 ? 2 : renderedSections.length;
  renderedSections.splice(insertionIndex, 0, commercialSlot(lang));
  const sections2 = renderedSections.join("");
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
        ${sources ? `<footer class="dossier-src reveal"><b>${esc(s.sources||"Sources")}</b><ul>${sources}</ul>${affNote}
</footer>` : ""}
      </div>
      <aside class="dossier-side reveal">
        <div class="side-block">
          <span class="hab-code">RELATED</span>
          ${related}
        </div>
        <div class="side-block">
          <span class="hab-code">STEAM</span>
          <p>${esc(DATA.game.name)}</p>
	          <a class="btn btn-primary" href="${esc(DATA.game.steamUrl)}" target="_blank" rel="noopener">${esc(s.getOnSteam)}</a>
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
const PRIVACY_BODY = {
  en: `<p>Before you choose, this site does not request Google Analytics 4 (GA4), Adsterra/effectivecpmnetwork.com or Google AdSense ad serving.</p><h2>Optional services and data</h2><p>If you allow analytics, GA4 may process your IP address, device and browser details, visited page, referrer, approximate region, and cookies or similar identifiers for measurement. If you allow advertising, the single Adsterra/effectivecpmnetwork.com placement may process IP address and other device or network data to deliver and measure an ad. Google AdSense ownership metadata and ads.txt are configured, but its serving script remains disabled.</p><h2>Your choice</h2><p>Your choice is stored only in this browser under <code>approximately-up-consent-v1</code>. Rejecting keeps optional providers blocked. Use the persistent Privacy settings button to change or withdraw your choice; withdrawal prevents new optional-provider requests on later page loads.</p><h2>Essential infrastructure</h2><p>Google Fonts stylesheets load independently before your choice and Google may receive standard network data. Cloudflare hosting may keep standard access logs. We do not sell personal data and do not claim to use a Google-certified CMP.</p>`,
  "zh-CN": `<p>在您作出选择前，本站不会请求 Google Analytics 4（GA4）、Adsterra/effectivecpmnetwork.com 或 Google AdSense 广告投放。</p><h2>可选服务与数据</h2><p>若允许统计分析，GA4 可能为统计处理您的 IP 地址、设备与浏览器信息、访问页面、来源页面、大致地区，以及 Cookie 或类似标识符。若允许广告，唯一的 Adsterra/effectivecpmnetwork.com 广告位可能处理 IP 地址及其他设备或网络数据，以投放和衡量一则广告。Google AdSense 仅配置了所有权验证元数据与 ads.txt，投放脚本仍关闭。</p><h2>您的选择</h2><p>选择仅以 <code>approximately-up-consent-v1</code> 保存在此浏览器中。选择不同意会继续阻止可选服务。您可随时通过固定显示的“隐私设置”更改或撤回选择；撤回后，后续页面加载不会发出新的可选服务请求。</p><h2>必要基础设施</h2><p>Google Fonts 样式表会在选择前独立加载，Google 可能收到常规网络数据；Cloudflare 托管也可能保留标准访问日志。我们不出售个人数据，也不声称使用 Google 认证的 CMP。</p>`,
  "zh-TW": `<p>在您作出選擇前，本站不會請求 Google Analytics 4（GA4）、Adsterra/effectivecpmnetwork.com 或 Google AdSense 廣告投放。</p><h2>可選服務與資料</h2><p>若允許統計分析，GA4 可能為統計處理您的 IP 位址、裝置與瀏覽器資訊、瀏覽頁面、來源頁面、大致地區，以及 Cookie 或類似識別碼。若允許廣告，唯一的 Adsterra/effectivecpmnetwork.com 廣告版位可能處理 IP 位址及其他裝置或網路資料，以投放並衡量一則廣告。Google AdSense 僅設定所有權驗證後設資料與 ads.txt，投放指令碼仍關閉。</p><h2>您的選擇</h2><p>選擇只以 <code>approximately-up-consent-v1</code> 儲存在此瀏覽器中。選擇不同意會繼續阻擋可選服務。您可隨時透過固定顯示的「隱私設定」變更或撤回選擇；撤回後，後續頁面載入不會發出新的可選服務請求。</p><h2>必要基礎設施</h2><p>Google Fonts 樣式表會在選擇前獨立載入，Google 可能收到一般網路資料；Cloudflare 託管也可能保留標準存取記錄。我們不出售個人資料，也不聲稱使用 Google 認證的 CMP。</p>`,
  ja: `<p>選択前に、当サイトは Google Analytics 4（GA4）、Adsterra/effectivecpmnetwork.com、Google AdSense の広告配信を要求しません。</p><h2>任意サービスとデータ</h2><p>アクセス解析を許可すると、GA4 が測定のため IP アドレス、端末・ブラウザー情報、閲覧ページ、参照元、おおよその地域、Cookie または類似識別子を処理する場合があります。広告を許可すると、1 つの Adsterra/effectivecpmnetwork.com 広告枠が広告の配信・測定のため IP アドレスなどの端末・ネットワーク情報を処理する場合があります。Google AdSense は所有権確認メタデータと ads.txt のみ設定済みで、配信スクリプトは無効です。</p><h2>選択の管理</h2><p>選択はこのブラウザーに <code>approximately-up-consent-v1</code> としてのみ保存されます。拒否すると任意サービスはブロックされたままです。常時表示されるプライバシー設定から変更・撤回でき、撤回後のページ読み込みでは新たな任意サービス要求を防ぎます。</p><h2>必要な基盤</h2><p>Google Fonts のスタイルシートは選択前に独立して読み込まれ、Google が標準的なネットワーク情報を受け取る場合があります。Cloudflare は標準アクセスログを保持する場合があります。当サイトは個人データを販売せず、Google 認定 CMP の使用をうたいません。</p>`,
  ko: `<p>선택 전에는 Google Analytics 4(GA4), Adsterra/effectivecpmnetwork.com 또는 Google AdSense 광고 게재를 요청하지 않습니다.</p><h2>선택적 서비스와 데이터</h2><p>분석을 허용하면 GA4가 측정을 위해 IP 주소, 기기·브라우저 정보, 방문 페이지, 유입 경로, 대략적인 지역과 쿠키 또는 유사 식별자를 처리할 수 있습니다. 광고를 허용하면 하나의 Adsterra/effectivecpmnetwork.com 광고 영역이 광고 제공과 측정을 위해 IP 주소와 기타 기기·네트워크 데이터를 처리할 수 있습니다. Google AdSense는 소유권 확인 메타데이터와 ads.txt만 설정되어 있으며 게재 스크립트는 비활성 상태입니다.</p><h2>선택 관리</h2><p>선택은 이 브라우저에 <code>approximately-up-consent-v1</code>로만 저장됩니다. 거부하면 선택적 공급자가 계속 차단됩니다. 항상 표시되는 개인정보 설정에서 변경하거나 철회할 수 있으며, 철회 후 페이지를 로드할 때는 새로운 선택적 공급자 요청이 차단됩니다.</p><h2>필수 인프라</h2><p>Google Fonts 스타일시트는 선택 전에 별도로 로드되어 Google이 표준 네트워크 데이터를 받을 수 있습니다. Cloudflare 호스팅은 표준 접속 로그를 보관할 수 있습니다. 개인정보를 판매하지 않으며 Google 인증 CMP 사용을 주장하지 않습니다.</p>`,
  fr: `<p>Avant votre choix, ce site ne demande ni Google Analytics 4 (GA4), ni Adsterra/effectivecpmnetwork.com, ni diffusion Google AdSense.</p><h2>Services facultatifs et données</h2><p>Si vous autorisez l'analyse, GA4 peut traiter l'adresse IP, les informations de l'appareil et du navigateur, la page visitée, le référent, la région approximative et des cookies ou identifiants similaires pour la mesure. Si vous autorisez la publicité, l'unique emplacement Adsterra/effectivecpmnetwork.com peut traiter l'adresse IP et d'autres données d'appareil ou de réseau pour diffuser et mesurer une annonce. Seuls les métadonnées de propriété Google AdSense et ads.txt sont configurés ; son script de diffusion reste désactivé.</p><h2>Votre choix</h2><p>Votre choix est stocké uniquement dans ce navigateur sous <code>approximately-up-consent-v1</code>. Un refus maintient les services facultatifs bloqués. Le bouton permanent Réglages de confidentialité permet de modifier ou retirer votre choix ; le retrait empêche de nouvelles requêtes facultatives lors des chargements suivants.</p><h2>Infrastructure nécessaire</h2><p>Les feuilles de style Google Fonts se chargent séparément avant le choix et Google peut recevoir des données réseau standard. Cloudflare peut conserver des journaux d'accès standard. Nous ne vendons pas de données personnelles et ne prétendons pas utiliser une CMP certifiée par Google.</p>`,
  de: `<p>Vor Ihrer Auswahl fordert diese Website weder Google Analytics 4 (GA4) noch Adsterra/effectivecpmnetwork.com oder Google-AdSense-Auslieferung an.</p><h2>Optionale Dienste und Daten</h2><p>Wenn Sie Analyse erlauben, kann GA4 IP-Adresse, Geräte- und Browserdaten, besuchte Seite, Referrer, ungefähre Region sowie Cookies oder ähnliche Kennungen zur Messung verarbeiten. Wenn Sie Werbung erlauben, kann der einzelne Adsterra/effectivecpmnetwork.com-Platz IP-Adresse und weitere Geräte- oder Netzwerkdaten zur Auslieferung und Messung einer Anzeige verarbeiten. Für Google AdSense sind nur Eigentumsmetadaten und ads.txt eingerichtet; das Auslieferungsskript bleibt deaktiviert.</p><h2>Ihre Auswahl</h2><p>Ihre Auswahl wird nur in diesem Browser als <code>approximately-up-consent-v1</code> gespeichert. Ablehnen hält optionale Anbieter blockiert. Über die dauerhaft sichtbaren Datenschutzeinstellungen können Sie die Auswahl ändern oder widerrufen; der Widerruf verhindert bei späteren Seitenaufrufen neue optionale Anbieteranfragen.</p><h2>Notwendige Infrastruktur</h2><p>Google Fonts-Stylesheets werden vor der Auswahl unabhängig geladen und Google kann Standard-Netzwerkdaten erhalten. Cloudflare kann Standard-Zugriffsprotokolle führen. Wir verkaufen keine personenbezogenen Daten und behaupten nicht, eine von Google zertifizierte CMP zu verwenden.</p>`,
  es: `<p>Antes de elegir, este sitio no solicita Google Analytics 4 (GA4), Adsterra/effectivecpmnetwork.com ni la publicación de Google AdSense.</p><h2>Servicios opcionales y datos</h2><p>Si permites el análisis, GA4 puede tratar la dirección IP, datos del dispositivo y navegador, página visitada, referencia, región aproximada y cookies o identificadores similares para medición. Si permites la publicidad, el único espacio de Adsterra/effectivecpmnetwork.com puede tratar la dirección IP y otros datos del dispositivo o la red para servir y medir un anuncio. Solo están configurados los metadatos de propiedad y ads.txt de Google AdSense; su script de publicación sigue desactivado.</p><h2>Tu elección</h2><p>La elección se guarda solo en este navegador como <code>approximately-up-consent-v1</code>. Rechazar mantiene bloqueados los proveedores opcionales. El botón permanente Configuración de privacidad permite cambiar o retirar la elección; la retirada impide nuevas solicitudes opcionales en cargas posteriores.</p><h2>Infraestructura necesaria</h2><p>Las hojas de estilo de Google Fonts se cargan por separado antes de la elección y Google puede recibir datos de red estándar. Cloudflare puede conservar registros de acceso estándar. No vendemos datos personales ni afirmamos usar una CMP certificada por Google.</p>`,
  it: `<p>Prima della scelta, il sito non richiede Google Analytics 4 (GA4), Adsterra/effectivecpmnetwork.com né la pubblicazione di Google AdSense.</p><h2>Servizi facoltativi e dati</h2><p>Se consenti l'analisi, GA4 può trattare indirizzo IP, dati del dispositivo e del browser, pagina visitata, provenienza, area approssimativa e cookie o identificatori simili per la misurazione. Se consenti la pubblicità, l'unico spazio Adsterra/effectivecpmnetwork.com può trattare indirizzo IP e altri dati del dispositivo o di rete per mostrare e misurare un annuncio. Sono configurati solo i metadati di proprietà e ads.txt di Google AdSense; lo script di pubblicazione resta disattivato.</p><h2>La tua scelta</h2><p>La scelta viene salvata solo in questo browser come <code>approximately-up-consent-v1</code>. Il rifiuto mantiene bloccati i fornitori facoltativi. Il pulsante permanente Impostazioni privacy consente di cambiare o revocare la scelta; la revoca impedisce nuove richieste facoltative nei caricamenti successivi.</p><h2>Infrastruttura necessaria</h2><p>I fogli di stile Google Fonts si caricano separatamente prima della scelta e Google può ricevere normali dati di rete. Cloudflare può conservare registri di accesso standard. Non vendiamo dati personali e non dichiariamo di usare una CMP certificata da Google.</p>`,
  pl: `<p>Przed dokonaniem wyboru witryna nie wysyła żądań do Google Analytics 4 (GA4), Adsterra/effectivecpmnetwork.com ani emisji Google AdSense.</p><h2>Opcjonalne usługi i dane</h2><p>Po zezwoleniu na analitykę GA4 może przetwarzać adres IP, dane urządzenia i przeglądarki, odwiedzoną stronę, odsyłacz, przybliżony region oraz pliki cookie lub podobne identyfikatory do pomiarów. Po zezwoleniu na reklamy jeden boks Adsterra/effectivecpmnetwork.com może przetwarzać adres IP i inne dane urządzenia lub sieci w celu wyświetlenia i pomiaru reklamy. Skonfigurowano tylko metadane własności Google AdSense i ads.txt; skrypt emisji pozostaje wyłączony.</p><h2>Twój wybór</h2><p>Wybór jest przechowywany wyłącznie w tej przeglądarce jako <code>approximately-up-consent-v1</code>. Odrzucenie blokuje opcjonalnych dostawców. Stały przycisk Ustawienia prywatności umożliwia zmianę lub wycofanie wyboru; wycofanie zapobiega nowym opcjonalnym żądaniom przy kolejnych wczytaniach.</p><h2>Niezbędna infrastruktura</h2><p>Arkusze Google Fonts ładują się niezależnie przed wyborem i Google może otrzymać standardowe dane sieciowe. Cloudflare może przechowywać standardowe logi dostępu. Nie sprzedajemy danych osobowych ani nie twierdzimy, że używamy CMP certyfikowanej przez Google.</p>`,
  "pt-BR": `<p>Antes da sua escolha, o site não solicita Google Analytics 4 (GA4), Adsterra/effectivecpmnetwork.com nem veiculação do Google AdSense.</p><h2>Serviços opcionais e dados</h2><p>Se você permitir análise, o GA4 pode tratar endereço IP, dados do dispositivo e navegador, página visitada, referência, região aproximada e cookies ou identificadores semelhantes para medição. Se permitir publicidade, o único espaço Adsterra/effectivecpmnetwork.com pode tratar endereço IP e outros dados do dispositivo ou da rede para exibir e medir um anúncio. Apenas os metadados de propriedade e o ads.txt do Google AdSense estão configurados; o script de veiculação permanece desativado.</p><h2>Sua escolha</h2><p>A escolha é armazenada somente neste navegador como <code>approximately-up-consent-v1</code>. Recusar mantém fornecedores opcionais bloqueados. O botão permanente Configurações de privacidade permite alterar ou retirar a escolha; a retirada impede novas solicitações opcionais nos próximos carregamentos.</p><h2>Infraestrutura necessária</h2><p>As folhas de estilo Google Fonts carregam separadamente antes da escolha e o Google pode receber dados de rede padrão. A Cloudflare pode manter registros de acesso padrão. Não vendemos dados pessoais nem afirmamos usar uma CMP certificada pelo Google.</p>`,
  ru: `<p>До вашего выбора сайт не запрашивает Google Analytics 4 (GA4), Adsterra/effectivecpmnetwork.com или показ Google AdSense.</p><h2>Необязательные сервисы и данные</h2><p>Если разрешить аналитику, GA4 может обрабатывать IP-адрес, данные устройства и браузера, посещённую страницу, источник перехода, примерный регион, cookie или похожие идентификаторы для измерений. Если разрешить рекламу, единственный блок Adsterra/effectivecpmnetwork.com может обрабатывать IP-адрес и другие данные устройства или сети для показа и измерения рекламы. Настроены только метаданные собственности Google AdSense и ads.txt; скрипт показа остаётся отключённым.</p><h2>Ваш выбор</h2><p>Выбор хранится только в этом браузере под ключом <code>approximately-up-consent-v1</code>. Отказ блокирует необязательных поставщиков. Постоянная кнопка настроек позволяет изменить или отозвать выбор; отзыв предотвращает новые необязательные запросы при последующих загрузках.</p><h2>Необходимая инфраструктура</h2><p>Стили Google Fonts загружаются независимо до выбора, и Google может получить стандартные сетевые данные. Cloudflare может хранить стандартные журналы доступа. Мы не продаём персональные данные и не заявляем об использовании сертифицированной Google CMP.</p>`,
  uk: `<p>До вашого вибору сайт не запитує Google Analytics 4 (GA4), Adsterra/effectivecpmnetwork.com або показ Google AdSense.</p><h2>Необов’язкові сервіси й дані</h2><p>Якщо дозволити аналітику, GA4 може обробляти IP-адресу, дані пристрою та браузера, відвідану сторінку, джерело переходу, приблизний регіон, cookie або подібні ідентифікатори для вимірювання. Якщо дозволити рекламу, єдиний блок Adsterra/effectivecpmnetwork.com може обробляти IP-адресу та інші дані пристрою або мережі для показу й вимірювання реклами. Налаштовано лише метадані власності Google AdSense та ads.txt; скрипт показу залишається вимкненим.</p><h2>Ваш вибір</h2><p>Вибір зберігається лише в цьому браузері як <code>approximately-up-consent-v1</code>. Відмова блокує необов’язкових постачальників. Постійна кнопка налаштувань дозволяє змінити або відкликати вибір; відкликання запобігає новим необов’язковим запитам під час наступних завантажень.</p><h2>Необхідна інфраструктура</h2><p>Стилі Google Fonts завантажуються незалежно до вибору, і Google може отримати стандартні мережеві дані. Cloudflare може зберігати стандартні журнали доступу. Ми не продаємо персональні дані й не заявляємо про використання сертифікованої Google CMP.</p>`,
  vi: `<p>Trước khi bạn lựa chọn, trang web không yêu cầu Google Analytics 4 (GA4), Adsterra/effectivecpmnetwork.com hoặc phân phối quảng cáo Google AdSense.</p><h2>Dịch vụ tùy chọn và dữ liệu</h2><p>Nếu cho phép phân tích, GA4 có thể xử lý địa chỉ IP, thông tin thiết bị và trình duyệt, trang đã xem, nguồn giới thiệu, khu vực gần đúng và cookie hoặc mã nhận dạng tương tự để đo lường. Nếu cho phép quảng cáo, vị trí Adsterra/effectivecpmnetwork.com duy nhất có thể xử lý địa chỉ IP và dữ liệu thiết bị hoặc mạng khác để phân phối và đo lường một quảng cáo. Chỉ siêu dữ liệu xác minh quyền sở hữu và ads.txt của Google AdSense được cấu hình; tập lệnh phân phối vẫn tắt.</p><h2>Lựa chọn của bạn</h2><p>Lựa chọn chỉ được lưu trong trình duyệt này với khóa <code>approximately-up-consent-v1</code>. Từ chối sẽ tiếp tục chặn nhà cung cấp tùy chọn. Nút Cài đặt quyền riêng tư luôn hiển thị cho phép thay đổi hoặc rút lại lựa chọn; việc rút lại ngăn yêu cầu tùy chọn mới trong các lần tải trang sau.</p><h2>Hạ tầng cần thiết</h2><p>Biểu định kiểu Google Fonts tải độc lập trước lựa chọn và Google có thể nhận dữ liệu mạng tiêu chuẩn. Cloudflare có thể lưu nhật ký truy cập tiêu chuẩn. Chúng tôi không bán dữ liệu cá nhân và không tuyên bố sử dụng CMP được Google chứng nhận.</p>`,
};

function renderStatic(lang, slug, title, body, descOverride){
  const prefix = lang === DEF ? "" : `/${lang}`;
  const s = siteI18n(lang);
  const descRaw = descOverride || KIT.staticDesc(slug, lang, s.name, title);
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
	  const privacyBody = `<section class="privacy-copy" data-privacy-locale="${esc(lang)}">${PRIVACY_BODY[lang] || ""}<h2>${esc(s.contactTitle)}</h2><p><a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a></p><p class="privacy-date">${today}</p></section>`;
  writePage(path.join(dir,"privacy.html"), "privacy", lang, renderStatic(lang,"privacy", s.privacyTitle, privacyBody));
  const contactI18n = {
    en: { ph: "Reach us at:", reply: "We usually reply within 2-3 business days." },
    "zh-CN": { ph: "联系我们：", reply: "我们通常会在 2-3 个工作日内回复。" },
    "zh-TW": { ph: "聯絡我們：", reply: "我們通常會在 2-3 個工作日內回覆。" },
    ja: { ph: "お問い合わせ：", reply: "通常 2〜3 営業日以内に返信します。" },
    ko: { ph: "문의하기: ", reply: "보통 2~3 영업일 내에 답변드립니다." },
    fr: { ph: "Contactez-nous : ", reply: "Nous répondons généralement sous 2 à 3 jours ouvrés." },
    de: { ph: "Kontaktieren Sie uns: ", reply: "Wir antworten in der Regel innerhalb von 2–3 Werktagen." },
    es: { ph: "Contáctanos: ", reply: "Normalmente respondemos en 2-3 días laborables." },
    it: { ph: "Contattaci: ", reply: "Di solito rispondiamo entro 2-3 giorni lavorativi." },
    pl: { ph: "Skontaktuj się z nami: ", reply: "Zwykle odpowiadamy w ciągu 2–3 dni roboczych." },
    "pt-BR": { ph: "Fale conosco: ", reply: "Normalmente respondemos em 2-3 dias úteis." },
    ru: { ph: "Свяжитесь с нами: ", reply: "Обычно мы отвечаем в течение 2–3 рабочих дней." },
    uk: { ph: "Зв'яжіться з нами: ", reply: "Зазвичай ми відповідаємо протягом 2–3 робочих днів." },
    vi: { ph: "Liên hệ với chúng tôi: ", reply: "Chúng tôi thường trả lời trong vòng 2-3 ngày làm việc." },
  };
  const contact = contactI18n[lang] || contactI18n.en;
  writePage(path.join(dir,"contact.html"), "contact", lang, renderStatic(lang,"contact", s.contactTitle,
    `<p>${contact.ph} <a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a></p><p style="margin-top:10px">${contact.reply}</p>`,
    `${s.name} — ${contact.reply}`));
}
// 404 (default lang) — function so OUT exists when called
function gen404(){
  const s404 = siteI18n(DEF);
  const pop404 = DATA.pages.filter(p=>["how-to-play","ship-building-guide","blueprints-guide","controls"].includes(p.slug)).map(p=>`<a href="/${p.slug}" style="display:inline-block;margin:6px;padding:9px 16px;border:1px solid var(--border);border-radius:10px;color:var(--muted);text-decoration:none">${esc(p.title)}</a>`).join("");
  fs.writeFileSync(path.join(OUT,"404.html"), `<!DOCTYPE html><html lang="${LANG_META[DEF].html}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>404 - ${esc(s404.name)}</title><meta name="robots" content="noindex" /><link rel="icon" type="image/svg+xml" href="/favicon.svg" /><link rel="apple-touch-icon" href="/apple-touch-icon.png" /><link rel="stylesheet" href="/css/style.css?v=${CSS_V}"></head><body>${header(DEF,"")}<main class="container" style="padding-top:70px;text-align:center"><section class="card grow-card" style="max-width:560px;margin:0 auto"><h1 style="font-size:3rem">404</h1><p>This page doesn't exist. Try one of these guides instead:</p><div style="margin:18px 0">${pop404}</div><p><a class="btn btn-primary" href="/">← Back to Home</a></p></section></main>${footer(DEF, false)}</body></html>`);
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
