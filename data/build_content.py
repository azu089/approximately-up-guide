# -*- coding: utf-8 -*-
"""Approximately Up guide site.json 重建：14 语言全量 (en/zh-CN/zh-TW/ja/ko/fr/de/es/it/pl/pt-BR/ru/uk/vi)
+ 17 内容页全量翻译（zh-TW 由 zh-CN 经 OpenCC s2tw 自动生成）。
事实口径：仅使用 docs/approximately-up-research.md 的 L0 事实（官方 Steam 页/官方视频/官方链接/社区线索）；
未核实的数值、名称、机制一律标「待补」（各语言本地化写法），禁止编造。
生成器：sites/approximately-up/scripts/generate.js（data/site.json → public/）。
"""
import json, copy
from pathlib import Path
import opencc

ROOT = Path(__file__).parent
cc = opencc.OpenCC("s2tw")

LANGS = ["en", "zh-CN", "zh-TW", "ja", "ko", "fr", "de", "es", "it", "pl", "pt-BR", "ru", "uk", "vi"]
# 需手写翻译的语言（zh-TW 自动生成；en 是基准内容）
TRANS_LANGS = [l for l in LANGS if l not in ("en", "zh-TW")]

# 页面 slug 全量（与 generate.js 的 header P0/P1/P2 及页面矩阵一致）
PAGE_SLUGS = [
    "how-to-play", "ship-building-guide", "blueprints-guide", "wiring-electronics",
    "controls", "multiplayer", "best-ship-designs", "system-requirements",
    "console-release", "mods", "patch-notes", "demo-vs-full",
    "achievements-list", "ships", "blueprints", "guides", "achievements",
]

# =====================================================================
# 站点级配置（site）与 14 语 site.i18n
# =====================================================================
SITE = {
    "name": "Approximately Up Guide",
    "domain": "approximatelyupguides.com",
    "tagline": "Build, Crash, Rebuild — Guides for Ships, Blueprints & Multiplayer",
    "description": "The best Approximately Up guides: how to play, ship building, controls, multiplayer, console release status, mods, patch notes and achievements — in 14 languages.",
    "language": "en",
    "gaId": "G-YV335TQLWZ",
    "gscVerification": "",
    "adsenseId": "pub-4174270222899193",
    "indexNowKey": "1d3c9081af5f6615482e53da0c46918f",
    "ogImage": "/images/hero.jpg",
    "awinVerification": "",
    "impactVerification": [],
    "affiliates": {},
    "adsterra": '<script async="async" data-cfasync="false" src="https://pl30767409.effectivecpmnetwork.com/c8bf889a0dcc57e129ef61a0c31f243d/invoke.js"></script> <div id="container-c8bf889a0dcc57e129ef61a0c31f243d"></div>',
}

SITE_I18N = {
    "en": {
        "name": "Approximately Up Guide",
        "tagline": "Build, Crash, Rebuild — Guides for Ships, Blueprints & Multiplayer",
        "description": "The best Approximately Up guides: how to play, ship building, controls, multiplayer, console release status, mods, patch notes and achievements — in 14 languages.",
        "navHome": "Home", "navGuides": "Guides", "navAbout": "About", "navPrivacy": "Privacy", "navContact": "Contact",
        "langLabel": "Language", "aboutTitle": "About this site", "privacyTitle": "Privacy Policy", "contactTitle": "Contact",
        "footerNote": "Unofficial fan site — game and related assets belong to their respective owners.",
        "footerSource": "Information checked against the official Steam store page, official videos and official links; unverified details are marked.",
        "quickAnswers": "Quick answers", "guides": "All guides", "aboutGame": "About the game",
        "startPlaying": "Get it on Steam", "getOnSteam": "Get it on Steam ↗", "readGuide": "Read the guide →",
        "moreGuides": "More guides", "sources": "Sources & fact-checking",
        "aboutText": "Approximately Up Guide is an unofficial fan resource. We research each page against the official Steam store page, official videos and official links, and clearly mark anything still being verified. We aim for accurate, useful guides for the global community.",
        "aboutSources": "Where our information comes from",
        "navGroup1": "Guides", "navGroup2": "Reference", "navGroup3": "Index",
        "searchPh": "Search guides…", "searchLabel": "Search guides",
        "plotTag": "FLIGHT LOG", "growTag": "BUILD", "seasonTag": "MISSION", "updated": "Contents",
        "explore": "Build, crash, rebuild", "latest": "Latest guides", "harvest": "REBUILD", "seedTag": "PART",
    },
    "zh-CN": {
        "name": "Approximately Up 攻略站",
        "tagline": "建造、坠毁、重建——飞船、蓝图与多人联机攻略",
        "description": "最好的 Approximately Up 攻略：怎么玩、飞船建造、控制、多人联机、主机版状态、模组、更新日志与成就——14 种语言。",
        "navHome": "首页", "navGuides": "攻略", "navAbout": "关于", "navPrivacy": "隐私", "navContact": "联系",
        "langLabel": "语言", "aboutTitle": "关于本站", "privacyTitle": "隐私政策", "contactTitle": "联系我们",
        "footerNote": "非官方粉丝站——游戏及相关资产归其所有者所有。",
        "footerSource": "信息核对自 Steam 官方商店页、官方视频与官方链接；未核实的内容已明确标注。",
        "quickAnswers": "常见问题速答", "guides": "全部攻略", "aboutGame": "关于这款游戏",
        "startPlaying": "在 Steam 获取", "getOnSteam": "在 Steam 获取 ↗", "readGuide": "阅读攻略 →",
        "moreGuides": "更多攻略", "sources": "来源与事实核对",
        "aboutText": "Approximately Up 攻略站是非官方粉丝资源站。我们针对 Steam 官方商店页、官方视频与官方链接逐页核对信息，并将仍在验证中的内容明确标注「待补」。目标是给全球玩家提供准确、实用的攻略。",
        "aboutSources": "我们的信息来源",
        "navGroup1": "攻略", "navGroup2": "参考资料", "navGroup3": "索引",
        "searchPh": "搜索攻略…", "searchLabel": "搜索攻略",
        "plotTag": "飞行日志", "growTag": "建造", "seasonTag": "任务", "updated": "目录",
        "explore": "建造、坠毁、重建", "latest": "最新攻略", "harvest": "重建", "seedTag": "部件",
    },
    "ja": {
        "name": "Approximately Up 攻略ガイド",
        "tagline": "作って、墜ちて、作り直す——宇宙船・設計図・マルチプレイ攻略",
        "description": "Approximately Up の攻略まとめ：遊び方、宇宙船の建造、操作、マルチプレイ、コンソール版、Mod、パッチノート、実績——14言語対応。",
        "navHome": "ホーム", "navGuides": "攻略", "navAbout": "このサイト", "navPrivacy": "プライバシー", "navContact": "お問い合わせ",
        "langLabel": "言語", "aboutTitle": "このサイトについて", "privacyTitle": "プライバシーポリシー", "contactTitle": "お問い合わせ",
        "footerNote": "非公式ファンサイトです。ゲームおよび関連アセットは各権利者に帰属します。",
        "footerSource": "情報は Steam 公式ストア・公式動画・公式リンクで確認しています。未検証の内容は明記しています。",
        "quickAnswers": "よくある質問", "guides": "攻略一覧", "aboutGame": "このゲームについて",
        "startPlaying": "Steam で入手", "getOnSteam": "Steam で入手 ↗", "readGuide": "攻略を読む →",
        "moreGuides": "その他の攻略", "sources": "出典とファクトチェック",
        "aboutText": "Approximately Up 攻略ガイドは非公式のファンリソースです。各ページを Steam 公式ストア・公式動画・公式リンクで確認し、未検証の内容は明記しています。世界のプレイヤーに役立つ正確な攻略を目指します。",
        "aboutSources": "情報の出典",
        "navGroup1": "攻略", "navGroup2": "リファレンス", "navGroup3": "索引",
        "searchPh": "攻略を検索…", "searchLabel": "攻略を検索",
        "plotTag": "フライトログ", "growTag": "建造", "seasonTag": "ミッション", "updated": "目次",
        "explore": "作って、墜ちて、作り直す", "latest": "最新攻略", "harvest": "再建造", "seedTag": "パーツ",
    },
    "ko": {
        "name": "Approximately Up 가이드",
        "tagline": "만들고, 추락하고, 다시 만든다 — 우주선·설계도·멀티플레이 가이드",
        "description": "Approximately Up 최고의 가이드: 플레이 방법, 우주선 제작, 조작, 멀티플레이, 콘솔 출시 현황, 모드, 패치 노트, 업적 — 14개 언어.",
        "navHome": "홈", "navGuides": "가이드", "navAbout": "소개", "navPrivacy": "개인정보", "navContact": "문의",
        "langLabel": "언어", "aboutTitle": "이 사이트 소개", "privacyTitle": "개인정보 처리방침", "contactTitle": "문의하기",
        "footerNote": "비공식 팬 사이트입니다. 게임 및 관련 자산은 각 소유자에게 있습니다.",
        "footerSource": "정보는 Steam 공식 스토어, 공식 영상, 공식 링크에서 확인했습니다. 미확인 내용은 명확히 표시합니다.",
        "quickAnswers": "빠른 답변", "guides": "전체 가이드", "aboutGame": "게임 소개",
        "startPlaying": "Steam에서 받기", "getOnSteam": "Steam에서 받기 ↗", "readGuide": "가이드 읽기 →",
        "moreGuides": "더 많은 가이드", "sources": "출처 및 사실 확인",
        "aboutText": "Approximately Up 가이드는 비공식 팬 리소스입니다. 각 페이지를 Steam 공식 스토어, 공식 영상, 공식 링크로 확인하고, 아직 확인되지 않은 내용은 명확히 표시합니다. 전 세계 플레이어에게 정확하고 유용한 가이드를 목표로 합니다.",
        "aboutSources": "정보 출처",
        "navGroup1": "가이드", "navGroup2": "참고 자료", "navGroup3": "색인",
        "searchPh": "가이드 검색…", "searchLabel": "가이드 검색",
        "plotTag": "비행 기록", "growTag": "제작", "seasonTag": "임무", "updated": "목차",
        "explore": "만들고, 추락하고, 다시 만들기", "latest": "최신 가이드", "harvest": "재건", "seedTag": "부품",
    },
    "fr": {
        "name": "Guide Approximately Up",
        "tagline": "Construire, s'écraser, reconstruire — guides vaisseaux, plans et multijoueur",
        "description": "Les meilleurs guides Approximately Up : comment jouer, construction de vaisseaux, contrôles, multijoueur, statut console, mods, notes de mise à jour et succès — en 14 langues.",
        "navHome": "Accueil", "navGuides": "Guides", "navAbout": "À propos", "navPrivacy": "Confidentialité", "navContact": "Contact",
        "langLabel": "Langue", "aboutTitle": "À propos de ce site", "privacyTitle": "Politique de confidentialité", "contactTitle": "Contact",
        "footerNote": "Site de fans non officiel — le jeu et ses ressources appartiennent à leurs propriétaires.",
        "footerSource": "Informations vérifiées sur la page Steam officielle, les vidéos officielles et les liens officiels ; les éléments non vérifiés sont signalés.",
        "quickAnswers": "Réponses rapides", "guides": "Tous les guides", "aboutGame": "À propos du jeu",
        "startPlaying": "Obtenir sur Steam", "getOnSteam": "Obtenir sur Steam ↗", "readGuide": "Lire le guide →",
        "moreGuides": "Plus de guides", "sources": "Sources et vérification",
        "aboutText": "Guide Approximately Up est une ressource de fans non officielle. Nous vérifions chaque page sur la page Steam officielle, les vidéos officielles et les liens officiels, et signalons clairement ce qui reste à vérifier. Notre objectif : des guides précis et utiles pour la communauté mondiale.",
        "aboutSources": "D'où viennent nos informations",
        "navGroup1": "Guides", "navGroup2": "Référence", "navGroup3": "Index",
        "searchPh": "Rechercher des guides…", "searchLabel": "Rechercher des guides",
        "plotTag": "JOURNAL DE VOL", "growTag": "CONSTRUCTION", "seasonTag": "MISSION", "updated": "Sommaire",
        "explore": "Construire, s'écraser, reconstruire", "latest": "Guides récents", "harvest": "RECONSTRUIRE", "seedTag": "PIÈCE",
    },
    "de": {
        "name": "Approximately Up Spielanleitung",
        "tagline": "Bauen, abstürzen, neu bauen — Guides zu Schiffen, Bauplänen & Mehrspieler",
        "description": "Die besten Approximately Up-Guides: Spielanleitung, Schiffsbau, Steuerung, Mehrspieler, Konsolen-Status, Mods, Patchnotes und Erfolge — in 14 Sprachen.",
        "navHome": "Start", "navGuides": "Guides", "navAbout": "Über", "navPrivacy": "Datenschutz", "navContact": "Kontakt",
        "langLabel": "Sprache", "aboutTitle": "Über diese Seite", "privacyTitle": "Datenschutzerklärung", "contactTitle": "Kontakt",
        "footerNote": "Inoffizielle Fan-Seite — Spiel und zugehörige Assets gehören ihren jeweiligen Eigentümern.",
        "footerSource": "Informationen geprüft gegen die offizielle Steam-Seite, offizielle Videos und offizielle Links; nicht verifizierte Details sind gekennzeichnet.",
        "quickAnswers": "Schnelle Antworten", "guides": "Alle Guides", "aboutGame": "Über das Spiel",
        "startPlaying": "Auf Steam holen", "getOnSteam": "Auf Steam holen ↗", "readGuide": "Guide lesen →",
        "moreGuides": "Weitere Guides", "sources": "Quellen & Faktencheck",
        "aboutText": "Approximately Up Guide ist eine inoffizielle Fan-Ressource. Wir prüfen jede Seite gegen die offizielle Steam-Seite, offizielle Videos und offizielle Links und kennzeichnen alles, was noch offen ist. Unser Ziel sind präzise, nützliche Guides für die globale Community.",
        "aboutSources": "Woher unsere Informationen stammen",
        "navGroup1": "Guides", "navGroup2": "Referenz", "navGroup3": "Index",
        "searchPh": "Guides suchen…", "searchLabel": "Guides suchen",
        "plotTag": "FLUGPROTOKOLL", "growTag": "BAU", "seasonTag": "MISSION", "updated": "Inhalt",
        "explore": "Bauen, abstürzen, neu bauen", "latest": "Neueste Guides", "harvest": "NEUBAU", "seedTag": "TEIL",
    },
    "es": {
        "name": "Guía de Approximately Up",
        "tagline": "Construye, choca, reconstruye — guías de naves, planos y multijugador",
        "description": "Las mejores guías de Approximately Up: cómo jugar, construcción de naves, controles, multijugador, estado en consolas, mods, notas de parche y logros — en 14 idiomas.",
        "navHome": "Inicio", "navGuides": "Guías", "navAbout": "Acerca de", "navPrivacy": "Privacidad", "navContact": "Contacto",
        "langLabel": "Idioma", "aboutTitle": "Acerca de este sitio", "privacyTitle": "Política de privacidad", "contactTitle": "Contacto",
        "footerNote": "Sitio de fans no oficial: el juego y sus recursos pertenecen a sus propietarios.",
        "footerSource": "Información verificada con la página oficial de Steam, los vídeos oficiales y los enlaces oficiales; lo no verificado está marcado.",
        "quickAnswers": "Respuestas rápidas", "guides": "Todas las guías", "aboutGame": "Sobre el juego",
        "startPlaying": "Consíguelo en Steam", "getOnSteam": "Consíguelo en Steam ↗", "readGuide": "Leer la guía →",
        "moreGuides": "Más guías", "sources": "Fuentes y verificación",
        "aboutText": "Guía de Approximately Up es un recurso de fans no oficial. Verificamos cada página con la página oficial de Steam, los vídeos oficiales y los enlaces oficiales, y marcamos claramente lo que aún está en verificación. Buscamos guías precisas y útiles para la comunidad global.",
        "aboutSources": "De dónde proviene nuestra información",
        "navGroup1": "Guías", "navGroup2": "Referencia", "navGroup3": "Índice",
        "searchPh": "Buscar guías…", "searchLabel": "Buscar guías",
        "plotTag": "BITÁCORA", "growTag": "CONSTRUCCIÓN", "seasonTag": "MISIÓN", "updated": "Contenidos",
        "explore": "Construye, choca, reconstruye", "latest": "Guías recientes", "harvest": "RECONSTRUIR", "seedTag": "PIEZA",
    },
    "it": {
        "name": "Guida Approximately Up",
        "tagline": "Costruisci, schianta, ricostruisci — guide su navi, progetti e multiplayer",
        "description": "Le migliori guide su Approximately Up: come si gioca, costruzione delle navi, controlli, multiplayer, stato su console, mod, note di patch e obiettivi — in 14 lingue.",
        "navHome": "Home", "navGuides": "Guide", "navAbout": "Info", "navPrivacy": "Privacy", "navContact": "Contatti",
        "langLabel": "Lingua", "aboutTitle": "Informazioni su questo sito", "privacyTitle": "Informativa sulla privacy", "contactTitle": "Contatti",
        "footerNote": "Sito di fan non ufficiale: il gioco e le risorse associate appartengono ai rispettivi proprietari.",
        "footerSource": "Informazioni verificate sulla pagina Steam ufficiale, sui video ufficiali e sui link ufficiali; i dettagli non verificati sono contrassegnati.",
        "quickAnswers": "Risposte rapide", "guides": "Tutte le guide", "aboutGame": "Informazioni sul gioco",
        "startPlaying": "Ottienilo su Steam", "getOnSteam": "Ottienilo su Steam ↗", "readGuide": "Leggi la guida →",
        "moreGuides": "Altre guide", "sources": "Fonti e verifica dei fatti",
        "aboutText": "Guida di Approximately Up è una risorsa di fan non ufficiale. Verifichiamo ogni pagina sulla pagina Steam ufficiale, sui video ufficiali e sui link ufficiali, e contrassegniamo chiaramente ciò che è ancora da verificare. Il nostro obiettivo sono guide precise e utili per la comunità globale.",
        "aboutSources": "Da dove provengono le nostre informazioni",
        "navGroup1": "Guide", "navGroup2": "Riferimento", "navGroup3": "Indice",
        "searchPh": "Cerca guide…", "searchLabel": "Cerca guide",
        "plotTag": "DIARIO DI VOLO", "growTag": "COSTRUZIONE", "seasonTag": "MISSIONE", "updated": "Contenuti",
        "explore": "Costruisci, schianta, ricostruisci", "latest": "Guide recenti", "harvest": "RICOSTRUZIONE", "seedTag": "PEZZO",
    },
    "pl": {
        "name": "Poradnik Approximately Up",
        "tagline": "Buduj, rozbijaj, buduj od nowa — poradniki o statkach, planach i trybie wieloosobowym",
        "description": "Najlepsze poradniki do Approximately Up: jak grać, budowa statków, sterowanie, tryb wieloosobowy, status na konsole, mody, noty aktualizacji i osiągnięcia — w 14 językach.",
        "navHome": "Start", "navGuides": "Poradniki", "navAbout": "O nas", "navPrivacy": "Prywatność", "navContact": "Kontakt",
        "langLabel": "Język", "aboutTitle": "O tej stronie", "privacyTitle": "Polityka prywatności", "contactTitle": "Kontakt",
        "footerNote": "Nieoficjalna strona fanowska — gra i powiązane zasoby należą do ich właścicieli.",
        "footerSource": "Informacje sprawdzane na oficjalnej stronie Steam, oficjalnych filmach i oficjalnych linkach; nieweryfikowane elementy są oznaczone.",
        "quickAnswers": "Szybkie odpowiedzi", "guides": "Wszystkie poradniki", "aboutGame": "O grze",
        "startPlaying": "Pobierz na Steam", "getOnSteam": "Pobierz na Steam ↗", "readGuide": "Czytaj poradnik →",
        "moreGuides": "Więcej poradników", "sources": "Źródła i weryfikacja",
        "aboutText": "Poradnik Approximately Up to nieoficjalny zasób fanowski. Każdą stronę sprawdzamy na oficjalnej stronie Steam, oficjalnych filmach i oficjalnych linkach, a wszystko, co pozostaje nieweryfikowane, wyraźnie oznaczamy. Celem są dokładne i przydatne poradniki dla globalnej społeczności.",
        "aboutSources": "Skąd pochodzą nasze informacje",
        "navGroup1": "Poradniki", "navGroup2": "Informacje", "navGroup3": "Indeks",
        "searchPh": "Szukaj poradników…", "searchLabel": "Szukaj poradników",
        "plotTag": "DZIENNIK LOTU", "growTag": "BUDOWA", "seasonTag": "MISJA", "updated": "Spis treści",
        "explore": "Buduj, rozbijaj, buduj od nowa", "latest": "Najnowsze poradniki", "harvest": "ODBUDOWA", "seedTag": "CZĘŚĆ",
    },
    "pt-BR": {
        "name": "Guia Approximately Up",
        "tagline": "Construa, caia, reconstrua — guias de naves, plantas e multiplayer",
        "description": "Os melhores guias de Approximately Up: como jogar, construção de naves, controles, multiplayer, status nos consoles, mods, notas de atualização e conquistas — em 14 idiomas.",
        "navHome": "Início", "navGuides": "Guias", "navAbout": "Sobre", "navPrivacy": "Privacidade", "navContact": "Contato",
        "langLabel": "Idioma", "aboutTitle": "Sobre este site", "privacyTitle": "Política de privacidade", "contactTitle": "Contato",
        "footerNote": "Site de fãs não oficial — o jogo e os recursos relacionados pertencem aos seus respectivos donos.",
        "footerSource": "Informações verificadas na página oficial da Steam, nos vídeos oficiais e nos links oficiais; detalhes não verificados são marcados.",
        "quickAnswers": "Respostas rápidas", "guides": "Todos os guias", "aboutGame": "Sobre o jogo",
        "startPlaying": "Obter na Steam", "getOnSteam": "Obter na Steam ↗", "readGuide": "Ler o guia →",
        "moreGuides": "Mais guias", "sources": "Fontes e verificação",
        "aboutText": "Guia de Approximately Up é um recurso de fãs não oficial. Verificamos cada página na página oficial da Steam, nos vídeos oficiais e nos links oficiais, e marcamos claramente o que ainda está em verificação. Nosso objetivo são guias precisos e úteis para a comunidade global.",
        "aboutSources": "De onde vêm nossas informações",
        "navGroup1": "Guias", "navGroup2": "Referência", "navGroup3": "Índice",
        "searchPh": "Pesquisar guias…", "searchLabel": "Pesquisar guias",
        "plotTag": "DIÁRIO DE VOO", "growTag": "CONSTRUÇÃO", "seasonTag": "MISSÃO", "updated": "Conteúdo",
        "explore": "Construa, caia, reconstrua", "latest": "Guias recentes", "harvest": "RECONSTRUIR", "seedTag": "PEÇA",
    },
    "ru": {
        "name": "Гайд Approximately Up",
        "tagline": "Строй, разбивай, строй заново — гайды по кораблям, чертежам и мультиплееру",
        "description": "Лучшие гайды по Approximately Up: как играть, строительство кораблей, управление, мультиплеер, статус на консолях, моды, патчноуты и достижения — на 14 языках.",
        "navHome": "Главная", "navGuides": "Гайды", "navAbout": "О сайте", "navPrivacy": "Конфиденциальность", "navContact": "Контакты",
        "langLabel": "Язык", "aboutTitle": "О сайте", "privacyTitle": "Политика конфиденциальности", "contactTitle": "Контакты",
        "footerNote": "Неофициальный фанатский сайт — игра и связанные материалы принадлежат их владельцам.",
        "footerSource": "Информация проверена по официальной странице Steam, официальным видео и официальным ссылкам; непроверенные детали помечены.",
        "quickAnswers": "Быстрые ответы", "guides": "Все гайды", "aboutGame": "Об игре",
        "startPlaying": "В Steam", "getOnSteam": "В Steam ↗", "readGuide": "Читать гайд →",
        "moreGuides": "Ещё гайды", "sources": "Источники и проверка фактов",
        "aboutText": "Гайд по Approximately Up — неофициальный фанатский ресурс. Мы проверяем каждую страницу по официальной странице Steam, официальным видео и официальным ссылкам и явно помечаем всё, что ещё не подтверждено. Наша цель — точные и полезные гайды для мирового сообщества.",
        "aboutSources": "Откуда мы берём информацию",
        "navGroup1": "Гайды", "navGroup2": "Справочник", "navGroup3": "Индекс",
        "searchPh": "Поиск гайдов…", "searchLabel": "Поиск гайдов",
        "plotTag": "БОРТЖУРНАЛ", "growTag": "СТРОЙКА", "seasonTag": "МИССИЯ", "updated": "Содержание",
        "explore": "Строй, разбивай, строй заново", "latest": "Новые гайды", "harvest": "ПЕРЕСТРОЙКА", "seedTag": "ДЕТАЛЬ",
    },
    "uk": {
        "name": "Посібник Approximately Up",
        "tagline": "Будуй, розбивай, будуй заново — гайди про кораблі, креслення та мультиплеєр",
        "description": "Найкращі гайди з Approximately Up: як грати, будівництво кораблів, керування, мультиплеєр, статус на консолях, моди, патчноути та досягнення — 14 мовами.",
        "navHome": "Головна", "navGuides": "Гайди", "navAbout": "Про сайт", "navPrivacy": "Конфіденційність", "navContact": "Контакти",
        "langLabel": "Мова", "aboutTitle": "Про цей сайт", "privacyTitle": "Політика конфіденційності", "contactTitle": "Контакти",
        "footerNote": "Неофіційний фан-сайт — гра та пов'язані матеріали належать їхнім власникам.",
        "footerSource": "Інформацію звірено з офіційною сторінкою Steam, офіційними відео та офіційними посиланнями; неперевірені деталі позначено.",
        "quickAnswers": "Швидкі відповіді", "guides": "Усі гайди", "aboutGame": "Про гру",
        "startPlaying": "У Steam", "getOnSteam": "У Steam ↗", "readGuide": "Читати гайд →",
        "moreGuides": "Більше гайдів", "sources": "Джерела та перевірка",
        "aboutText": "Гайд з Approximately Up — неофіційний фан-ресурс. Ми звіряємо кожну сторінку з офіційною сторінкою Steam, офіційними відео та офіційними посиланнями й чітко позначаємо все, що ще не підтверджено. Наша мета — точні та корисні гайди для світової спільноти.",
        "aboutSources": "Звідки ми беремо інформацію",
        "navGroup1": "Гайди", "navGroup2": "Довідник", "navGroup3": "Індекс",
        "searchPh": "Пошук гайдів…", "searchLabel": "Пошук гайдів",
        "plotTag": "БОРТЖУРНАЛ", "growTag": "БУДІВНИЦТВО", "seasonTag": "МІСІЯ", "updated": "Зміст",
        "explore": "Будуй, розбивай, будуй заново", "latest": "Нові гайди", "harvest": "ПЕРЕБУДОВА", "seedTag": "ДЕТАЛЬ",
    },
    "vi": {
        "name": "Hướng dẫn Approximately Up",
        "tagline": "Xây, rơi, xây lại — hướng dẫn về tàu, bản thiết kế và chơi mạng",
        "description": "Hướng dẫn Approximately Up hay nhất: cách chơi, chế tạo tàu, điều khiển, chơi mạng, tình trạng máy console, mod, ghi chú bản vá và thành tựu — bằng 14 ngôn ngữ.",
        "navHome": "Trang chủ", "navGuides": "Hướng dẫn", "navAbout": "Giới thiệu", "navPrivacy": "Quyền riêng tư", "navContact": "Liên hệ",
        "langLabel": "Ngôn ngữ", "aboutTitle": "Giới thiệu trang này", "privacyTitle": "Chính sách quyền riêng tư", "contactTitle": "Liên hệ",
        "footerNote": "Trang fan không chính thức — trò chơi và tài sản liên quan thuộc về chủ sở hữu của chúng.",
        "footerSource": "Thông tin được đối chiếu với trang Steam chính thức, video chính thức và liên kết chính thức; nội dung chưa xác minh được đánh dấu.",
        "quickAnswers": "Trả lời nhanh", "guides": "Tất cả hướng dẫn", "aboutGame": "Về trò chơi",
        "startPlaying": "Tải trên Steam", "getOnSteam": "Tải trên Steam ↗", "readGuide": "Đọc hướng dẫn →",
        "moreGuides": "Hướng dẫn khác", "sources": "Nguồn và kiểm chứng",
        "aboutText": "Hướng dẫn Approximately Up là tài nguyên fan không chính thức. Chúng tôi đối chiếu từng trang với trang Steam chính thức, video chính thức và liên kết chính thức, đồng thời đánh dấu rõ nội dung chưa xác minh. Mục tiêu là những hướng dẫn chính xác, hữu ích cho cộng đồng toàn cầu.",
        "aboutSources": "Nguồn thông tin của chúng tôi",
        "navGroup1": "Hướng dẫn", "navGroup2": "Tham khảo", "navGroup3": "Chỉ mục",
        "searchPh": "Tìm hướng dẫn…", "searchLabel": "Tìm hướng dẫn",
        "plotTag": "NHẬT KÝ BAY", "growTag": "CHẾ TẠO", "seasonTag": "NHIỆM VỤ", "updated": "Mục lục",
        "explore": "Xây, rơi, xây lại", "latest": "Hướng dẫn mới", "harvest": "TÁI CHẾ TẠO", "seedTag": "BỘ PHẬN",
    },
}

# =====================================================================
# 游戏级配置（game）与 14 语 game.*I18n
# =====================================================================
GAME = {
    "name": "Approximately Up",
    "releaseDate": "2026-08-06",
    "platforms": ["PC (Steam)"],
    "genre": "Adventure / Indie / Simulation",
    "price": "$24.99",
    "steamUrl": "https://store.steampowered.com/app/3904850/",
    "officialSite": "https://approximatelyup.com",
    "intro": "Approximately Up is a space sandbox builder by Approximately Games. Build a fully modular spaceship from whatever bolts together long enough to fly, crash, and rebuild. Explore new planets in co-op multiplayer, mount giant thrusters and annoying cables, complete wild missions, and face the dangers of space. Released on Steam on August 6, 2026, with 14 languages, 22 achievements and Steam Workshop support.",
    "keyFacts": [
        "Released August 6, 2026 on Steam ($19.99 at launch, was $24.99)",
        "Build, crash, rebuild — fully modular spaceships",
        "Single-player + online co-op multiplayer",
        "14 languages and 22 Steam achievements",
        "Steam Workshop support",
        "Self-published by Approximately Games (developer & publisher)",
    ],
    "stats": [
        {"value": "Aug 6", "label": "Release date"},
        {"value": "14", "label": "Languages"},
        {"value": "22", "label": "Achievements"},
        {"value": "Solo + Co-op", "label": "Modes"},
        {"value": "$19.99", "label": "On Steam (20% off)"},
        {"value": "TBD", "label": "Steam rating"},
    ],
    "aboutPoints": [
        "Approximately Up is developed and published by Approximately Games (self-published indie).",
        "It released on Steam on August 6, 2026; a demo predates the full release.",
        "This site fact-checks every page against the official Steam store page, official videos and official links; community-sourced details are marked as unverified until confirmed.",
        "Official channels: approximatelyup.com, Discord, TikTok @approximatelyup and YouTube @ApproximatelyUp.",
    ],
}

GAME_I18N = {
    "zh-CN": {
        "name": "Approximately Up",
        "intro": "《Approximately Up》是 Approximately Games 出品的太空沙盒建造游戏。用任何「能拼到能飞」的部件组装全模块化飞船，坠毁后再重建。在多人合作中探索新星球、安装巨型推进器与恼人的缆线、完成疯狂任务，直面太空的危险。游戏于 2026 年 8 月 6 日在 Steam 发售，支持 14 种语言、22 项成就与 Steam 创意工坊。",
        "keyFacts": [
            "2026 年 8 月 6 日在 Steam 发售（$19.99，原价 $24.99，20% 折扣）",
            "建造、坠毁、重建——全模块化飞船",
            "单人 + 在线合作多人",
            "14 种语言、22 项 Steam 成就",
            "支持 Steam 创意工坊",
            "由 Approximately Games 自研自发（开发者兼发行商）",
        ],
        "stats": [
            {"value": "8月6日", "label": "发售日"},
            {"value": "14", "label": "语言"},
            {"value": "22", "label": "成就"},
            {"value": "单人+联机", "label": "模式"},
            {"value": "$19.99", "label": "Steam 售价（8折）"},
            {"value": "待补", "label": "Steam 好评"},
        ],
        "aboutPoints": [
            "《Approximately Up》由 Approximately Games 开发并发行（自研自发独立游戏）。",
            "2026 年 8 月 6 日在 Steam 正式发售；Demo 版更早推出。",
            "本站每页信息都核对自 Steam 官方商店页、官方视频与官方链接；社区来源的内容在确认前会明确标注「待补」。",
            "官方渠道：approximatelyup.com、Discord、TikTok @approximatelyup、YouTube @ApproximatelyUp。",
        ],
    },
    "ja": {
        "name": "Approximately Up",
        "intro": "『Approximately Up』は Approximately Games による宇宙サンドボックス建造ゲーム。飛ぶのに十分なだけ繋ぎ合わせた部品で完全モジュラー式の宇宙船を作り、墜ちて、作り直す。オンライン協力で新惑星を探索し、巨大スラスターや鬱陶しいケーブルを取り付け、ワイルドなミッションをこなし、宇宙の危険に立ち向かおう。2026年8月6日に Steam でリリース。14言語、22実績、Steam ワークショップ対応。",
        "keyFacts": [
            "2026年8月6日に Steam でリリース（$19.99、通常 $24.99、20%オフ）",
            "作って、墜ちて、作り直す——完全モジュラー式宇宙船",
            "シングルプレイ＋オンライン協力マルチプレイ",
            "14言語、22の Steam 実績",
            "Steam ワークショップ対応",
            "Approximately Games が開発・パブリッシング（インディー）",
        ],
        "stats": [
            {"value": "8/6", "label": "リリース日"},
            {"value": "14", "label": "言語"},
            {"value": "22", "label": "実績"},
            {"value": "ソロ+協力", "label": "モード"},
            {"value": "$19.99", "label": "Steam（20%オフ）"},
            {"value": "未検証", "label": "Steam 評価"},
        ],
        "aboutPoints": [
            "『Approximately Up』は Approximately Games が開発・パブリッシング（自社パブリッシングのインディー）。",
            "2026年8月6日に Steam で正式リリース。Demo 版はそれより前に公開。",
            "このサイトは各ページを Steam 公式ストア・公式動画・公式リンクで確認し、コミュニティ由来の情報は確認できるまで「未検証」と明記します。",
            "公式チャンネル：approximatelyup.com、Discord、TikTok @approximatelyup、YouTube @ApproximatelyUp。",
        ],
    },
    "ko": {
        "name": "Approximately Up",
        "intro": "Approximately Up은 Approximately Games가 만든 우주 샌드박스 건설 게임입니다. 날기에 충분할 만큼 볼트로 조인 부품으로 완전 모듈식 우주선을 만들고, 추락하고, 다시 만듭니다. 온라인 협동으로 새 행성을 탐험하고, 거대한 추진기와 성가신 케이블을 달고, 엉뚱한 임무를 완수하며 우주의 위험에 맞서세요. 2026년 8월 6일 Steam 출시, 14개 언어, 22개 업적, Steam 창작마당 지원.",
        "keyFacts": [
            "2026년 8월 6일 Steam 출시 ($19.99, 정가 $24.99, 20% 할인)",
            "만들고, 추락하고, 다시 만들기 — 완전 모듈식 우주선",
            "싱글플레이 + 온라인 협동 멀티플레이",
            "14개 언어, 22개 Steam 업적",
            "Steam 창작마당 지원",
            "Approximately Games 자체 개발·배급 (인디)",
        ],
        "stats": [
            {"value": "8월 6일", "label": "출시일"},
            {"value": "14", "label": "언어"},
            {"value": "22", "label": "업적"},
            {"value": "솔로+협동", "label": "모드"},
            {"value": "$19.99", "label": "Steam 가격 (20% 할인)"},
            {"value": "미확인", "label": "Steam 평가"},
        ],
        "aboutPoints": [
            "Approximately Up은 Approximately Games가 개발하고 배급합니다 (자체 배급 인디).",
            "2026년 8월 6일 Steam에 정식 출시됐으며, 데모는 그보다 먼저 공개됐습니다.",
            "이 사이트는 각 페이지를 Steam 공식 스토어, 공식 영상, 공식 링크로 확인하며, 커뮤니티 출처 내용은 확인 전까지 '미확인'으로 표시합니다.",
            "공식 채널: approximatelyup.com, Discord, TikTok @approximatelyup, YouTube @ApproximatelyUp.",
        ],
    },
    "fr": {
        "name": "Approximately Up",
        "intro": "Approximately Up est un jeu de construction sandbox spatial de Approximately Games. Construisez un vaisseau entièrement modulaire à partir de tout ce qui se boulonne assez longtemps pour voler, écrasez-vous et reconstruisez. Explorez de nouvelles planètes en multijoueur coopératif, montez d'énormes propulseurs et des câbles agaçants, accomplissez de folles missions et affrontez les dangers de l'espace. Sorti sur Steam le 6 août 2026, avec 14 langues, 22 succès et le support du Steam Workshop.",
        "keyFacts": [
            "Sorti le 6 août 2026 sur Steam (19,99 $, au lieu de 24,99 $, -20 %)",
            "Construire, s'écraser, reconstruire — vaisseaux entièrement modulaires",
            "Solo + multijoueur coopératif en ligne",
            "14 langues et 22 succès Steam",
            "Support du Steam Workshop",
            "Auto-édité par Approximately Games (développeur et éditeur)",
        ],
        "stats": [
            {"value": "6 août", "label": "Date de sortie"},
            {"value": "14", "label": "Langues"},
            {"value": "22", "label": "Succès"},
            {"value": "Solo + Coop", "label": "Modes"},
            {"value": "$19.99", "label": "Sur Steam (-20 %)"},
            {"value": "à vérifier", "label": "Note Steam"},
        ],
        "aboutPoints": [
            "Approximately Up est développé et édité par Approximately Games (indépendant auto-édité).",
            "Le jeu est sorti sur Steam le 6 août 2026 ; une démo l'a précédé.",
            "Ce site vérifie chaque page sur la page Steam officielle, les vidéos officielles et les liens officiels ; les éléments issus de la communauté sont marqués comme non vérifiés jusqu'à confirmation.",
            "Canaux officiels : approximatelyup.com, Discord, TikTok @approximatelyup et YouTube @ApproximatelyUp.",
        ],
    },
    "de": {
        "name": "Approximately Up",
        "intro": "Approximately Up ist ein Weltraum-Sandbox-Bauspiel von Approximately Games. Baue ein vollständig modulares Raumschiff aus allem, was sich lange genug zusammenschrauben lässt, um zu fliegen, stürze ab und baue neu. Erkunde neue Planeten im Online-Koop, montiere riesige Triebwerke und nervige Kabel, meistere wilde Missionen und stelle dich den Gefahren des Weltraums. Erschienen am 6. August 2026 auf Steam, mit 14 Sprachen, 22 Erfolgen und Steam-Workshop-Support.",
        "keyFacts": [
            "Erschienen am 6. August 2026 auf Steam (19,99 $, statt 24,99 $, 20 % Rabatt)",
            "Bauen, abstürzen, neu bauen — vollständig modulare Raumschiffe",
            "Einzelspieler + Online-Koop-Mehrspieler",
            "14 Sprachen und 22 Steam-Erfolge",
            "Steam-Workshop-Support",
            "Selbst veröffentlicht von Approximately Games (Entwickler & Publisher)",
        ],
        "stats": [
            {"value": "6. Aug.", "label": "Veröffentlichung"},
            {"value": "14", "label": "Sprachen"},
            {"value": "22", "label": "Erfolge"},
            {"value": "Solo + Co-op", "label": "Modi"},
            {"value": "$19.99", "label": "Auf Steam (20 % Rabatt)"},
            {"value": "unbestätigt", "label": "Steam-Bewertung"},
        ],
        "aboutPoints": [
            "Approximately Up wird von Approximately Games entwickelt und veröffentlicht (selbstverlegtes Indie-Spiel).",
            "Erschienen am 6. August 2026 auf Steam; eine Demo erschien früher.",
            "Diese Seite prüft jede Seite gegen die offizielle Steam-Seite, offizielle Videos und offizielle Links; Community-Informationen werden bis zur Bestätigung als unbestätigt markiert.",
            "Offizielle Kanäle: approximatelyup.com, Discord, TikTok @approximatelyup und YouTube @ApproximatelyUp.",
        ],
    },
    "es": {
        "name": "Approximately Up",
        "intro": "Approximately Up es un juego de construcción sandbox espacial de Approximately Games. Construye una nave totalmente modular con lo que sea que se pueda atornillar el tiempo suficiente para volar, choca y reconstruye. Explora nuevos planetas en multijugador cooperativo, monta propulsores gigantes y cables molestos, completa misiones locas y enfréntate a los peligros del espacio. Lanzado en Steam el 6 de agosto de 2026, con 14 idiomas, 22 logros y soporte del Steam Workshop.",
        "keyFacts": [
            "Lanzado el 6 de agosto de 2026 en Steam (19,99 $, antes 24,99 $, -20 %)",
            "Construye, choca, reconstruye — naves totalmente modulares",
            "Un jugador + multijugador cooperativo en línea",
            "14 idiomas y 22 logros de Steam",
            "Soporte del Steam Workshop",
            "Autopublicado por Approximately Games (desarrollador y editor)",
        ],
        "stats": [
            {"value": "6 ago", "label": "Fecha de lanzamiento"},
            {"value": "14", "label": "Idiomas"},
            {"value": "22", "label": "Logros"},
            {"value": "Solo + Cooperativo", "label": "Modos"},
            {"value": "$19.99", "label": "En Steam (-20 %)"},
            {"value": "por verificar", "label": "Valoración en Steam"},
        ],
        "aboutPoints": [
            "Approximately Up está desarrollado y publicado por Approximately Games (independiente autopublicado).",
            "Se lanzó en Steam el 6 de agosto de 2026; una demo lo precedió.",
            "Este sitio verifica cada página con la página oficial de Steam, los vídeos oficiales y los enlaces oficiales; el contenido de la comunidad se marca como no verificado hasta confirmarlo.",
            "Canales oficiales: approximatelyup.com, Discord, TikTok @approximatelyup y YouTube @ApproximatelyUp.",
        ],
    },
    "it": {
        "name": "Approximately Up",
        "intro": "Approximately Up è un gioco di costruzione sandbox spaziale di Approximately Games. Costruisci un'astronave completamente modulare con qualsiasi cosa si possa imbullonare abbastanza a lungo da volare, schiantati e ricostruisci. Esplora nuovi pianeti in multigiocatore cooperativo online, monta propulsori giganti e cavi fastidiosi, completa missioni assurde e affronta i pericoli dello spazio. Uscito su Steam il 6 agosto 2026, con 14 lingue, 22 obiettivi e supporto al Workshop di Steam.",
        "keyFacts": [
            "Uscito il 6 agosto 2026 su Steam (19,99 $, invece di 24,99 $, -20 %)",
            "Costruisci, schianta, ricostruisci — astronavi completamente modulari",
            "Giocatore singolo + multigiocatore cooperativo online",
            "14 lingue e 22 obiettivi Steam",
            "Supporto al Workshop di Steam",
            "Autopubblicato da Approximately Games (sviluppatore ed editore)",
        ],
        "stats": [
            {"value": "6 ago", "label": "Data di uscita"},
            {"value": "14", "label": "Lingue"},
            {"value": "22", "label": "Obiettivi"},
            {"value": "Solo + Co-op", "label": "Modalità"},
            {"value": "$19.99", "label": "Su Steam (-20 %)"},
            {"value": "da verificare", "label": "Valutazione Steam"},
        ],
        "aboutPoints": [
            "Approximately Up è sviluppato e pubblicato da Approximately Games (indie autopubblicato).",
            "È uscito su Steam il 6 agosto 2026; una demo l'ha preceduto.",
            "Questo sito verifica ogni pagina sulla pagina Steam ufficiale, sui video ufficiali e sui link ufficiali; i contenuti della community sono contrassegnati come non verificati fino a conferma.",
            "Canali ufficiali: approximatelyup.com, Discord, TikTok @approximatelyup e YouTube @ApproximatelyUp.",
        ],
    },
    "pl": {
        "name": "Approximately Up",
        "intro": "Approximately Up to kosmiczna gra sandboxowa o budowaniu od Approximately Games. Zbuduj w pełni modułowy statek z czegokolwiek, co da się skręcić na tyle długo, by polecieć, rozbij się i zbuduj od nowa. Eksploruj nowe planety w trybie kooperacji online, montuj ogromne silniki i irytujące kable, wykonuj zwariowane misje i stawiaj czoła zagrożeniom kosmosu. Premiera na Steam 6 sierpnia 2026, 14 języków, 22 osiągnięcia i wsparcie Steam Workshop.",
        "keyFacts": [
            "Premiera 6 sierpnia 2026 na Steam (19,99 $, zamiast 24,99 $, -20 %)",
            "Buduj, rozbijaj, buduj od nowa — w pełni modułowe statki",
            "Tryb jednoosobowy + kooperacja online",
            "14 języków i 22 osiągnięcia Steam",
            "Wsparcie Steam Workshop",
            "Samodzielne wydawnictwo Approximately Games (deweloper i wydawca)",
        ],
        "stats": [
            {"value": "6 sie", "label": "Data premiery"},
            {"value": "14", "label": "Języki"},
            {"value": "22", "label": "Osiągnięcia"},
            {"value": "Solo + Koop", "label": "Tryby"},
            {"value": "$19.99", "label": "Na Steam (-20 %)"},
            {"value": "do potwierdzenia", "label": "Ocena Steam"},
        ],
        "aboutPoints": [
            "Approximately Up jest tworzone i wydawane przez Approximately Games (niezależne, self-publishing).",
            "Gra ukazała się na Steam 6 sierpnia 2026; demo pojawiło się wcześniej.",
            "Ta strona weryfikuje każdą podstronę na oficjalnej stronie Steam, oficjalnych filmach i oficjalnych linkach; treści ze społeczności są oznaczane jako niepotwierdzone do czasu weryfikacji.",
            "Oficjalne kanały: approximatelyup.com, Discord, TikTok @approximatelyup i YouTube @ApproximatelyUp.",
        ],
    },
    "pt-BR": {
        "name": "Approximately Up",
        "intro": "Approximately Up é um jogo de construção sandbox espacial da Approximately Games. Construa uma nave totalmente modular com qualquer coisa que se parafuse por tempo suficiente para voar, caia e reconstrua. Explore novos planetas em multijogador cooperativo, monte propulsores gigantes e cabos irritantes, complete missões malucas e enfrente os perigos do espaço. Lançado na Steam em 6 de agosto de 2026, com 14 idiomas, 22 conquistas e suporte à Oficina da Steam.",
        "keyFacts": [
            "Lançado em 6 de agosto de 2026 na Steam (US$ 19,99, antes US$ 24,99, -20 %)",
            "Construa, caia, reconstrua — naves totalmente modulares",
            "Um jogador + multijogador cooperativo online",
            "14 idiomas e 22 conquistas na Steam",
            "Suporte à Oficina da Steam",
            "Autopublicado pela Approximately Games (desenvolvedora e publicadora)",
        ],
        "stats": [
            {"value": "6 ago", "label": "Data de lançamento"},
            {"value": "14", "label": "Idiomas"},
            {"value": "22", "label": "Conquistas"},
            {"value": "Solo + Cooperativo", "label": "Modos"},
            {"value": "$19.99", "label": "Na Steam (-20 %)"},
            {"value": "a verificar", "label": "Avaliação na Steam"},
        ],
        "aboutPoints": [
            "Approximately Up é desenvolvido e publicado pela Approximately Games (indie autopublicado).",
            "Foi lançado na Steam em 6 de agosto de 2026; uma demo veio antes.",
            "Este site verifica cada página na página oficial da Steam, nos vídeos oficiais e nos links oficiais; conteúdo da comunidade é marcado como não verificado até confirmação.",
            "Canais oficiais: approximatelyup.com, Discord, TikTok @approximatelyup e YouTube @ApproximatelyUp.",
        ],
    },
    "ru": {
        "name": "Approximately Up",
        "intro": "Approximately Up — космическая песочница о строительстве от Approximately Games. Собирайте полностью модульный корабль из всего, что можно скрутить достаточно надолго, чтобы взлететь, разбивайтесь и стройте заново. Исследуйте новые планеты в кооперативном мультиплеере, устанавливайте гигантские двигатели и надоедливые кабели, выполняйте безумные миссии и встречайте опасности космоса. Релиз в Steam — 6 августа 2026 года, 14 языков, 22 достижения и поддержка Мастерской Steam.",
        "keyFacts": [
            "Релиз 6 августа 2026 года в Steam (19,99 $, вместо 24,99 $, скидка 20 %)",
            "Строй, разбивай, строй заново — полностью модульные корабли",
            "Одиночный режим + онлайн-кооператив",
            "14 языков и 22 достижения Steam",
            "Поддержка Мастерской Steam",
            "Самиздат Approximately Games (разработчик и издатель)",
        ],
        "stats": [
            {"value": "6 авг", "label": "Дата релиза"},
            {"value": "14", "label": "Языки"},
            {"value": "22", "label": "Достижения"},
            {"value": "Соло + Кооп", "label": "Режимы"},
            {"value": "$19.99", "label": "В Steam (-20 %)"},
            {"value": "не подтверждено", "label": "Оценка в Steam"},
        ],
        "aboutPoints": [
            "Approximately Up разработана и издана Approximately Games (независимый самиздат).",
            "Релиз в Steam состоялся 6 августа 2026 года; демо вышло раньше.",
            "Этот сайт сверяет каждую страницу с официальной страницей Steam, официальными видео и официальными ссылками; материалы сообщества помечаются как непроверенные до подтверждения.",
            "Официальные каналы: approximatelyup.com, Discord, TikTok @approximatelyup и YouTube @ApproximatelyUp.",
        ],
    },
    "uk": {
        "name": "Approximately Up",
        "intro": "Approximately Up — космічна пісочниця про будівництво від Approximately Games. Зберіть повністю модульний корабель з усього, що можна скрутити достатньо довго, щоб злетіти, розбийтеся й будуйте заново. Досліджуйте нові планети в кооперативному мультиплеєрі, встановлюйте гігантські двигуни й набридливі кабелі, виконуйте божевільні місії та зустрічайте небезпеки космосу. Реліз у Steam — 6 серпня 2026 року, 14 мов, 22 досягнення та підтримка Майстерні Steam.",
        "keyFacts": [
            "Реліз 6 серпня 2026 року в Steam (19,99 $, замість 24,99 $, знижка 20 %)",
            "Будуй, розбивай, будуй заново — повністю модульні кораблі",
            "Одиночний режим + онлайн-кооператив",
            "14 мов і 22 досягнення Steam",
            "Підтримка Майстерні Steam",
            "Самвидав Approximately Games (розробник і видавець)",
        ],
        "stats": [
            {"value": "6 серп", "label": "Дата релізу"},
            {"value": "14", "label": "Мови"},
            {"value": "22", "label": "Досягнення"},
            {"value": "Соло + Кооп", "label": "Режими"},
            {"value": "$19.99", "label": "У Steam (-20 %)"},
            {"value": "не підтверджено", "label": "Оцінка в Steam"},
        ],
        "aboutPoints": [
            "Approximately Up розроблена й видана Approximately Games (незалежний самвидав).",
            "Реліз у Steam відбувся 6 серпня 2026 року; демо вийшло раніше.",
            "Цей сайт звіряє кожну сторінку з офіційною сторінкою Steam, офіційними відео та офіційними посиланнями; матеріали спільноти позначаються як неперевірені до підтвердження.",
            "Офіційні канали: approximatelyup.com, Discord, TikTok @approximatelyup і YouTube @ApproximatelyUp.",
        ],
    },
    "vi": {
        "name": "Approximately Up",
        "intro": "Approximately Up là trò chơi xây dựng hộp cát không gian của Approximately Games. Hãy lắp một con tàu hoàn toàn mô-đun từ bất cứ thứ gì bắt vít đủ lâu để bay, rơi xuống và xây lại. Khám phá hành tinh mới trong chế độ chơi mạng hợp tác, gắn động cơ đẩy khổng lồ và dây cáp phiền phức, hoàn thành các nhiệm vụ điên rồ và đối mặt với hiểm nguy ngoài không gian. Phát hành trên Steam ngày 6 tháng 8 năm 2026, với 14 ngôn ngữ, 22 thành tựu và hỗ trợ Steam Workshop.",
        "keyFacts": [
            "Phát hành ngày 6 tháng 8 năm 2026 trên Steam (19,99 $, thay vì 24,99 $, giảm 20%)",
            "Xây, rơi, xây lại — tàu hoàn toàn mô-đun",
            "Chơi đơn + chơi mạng hợp tác trực tuyến",
            "14 ngôn ngữ và 22 thành tựu Steam",
            "Hỗ trợ Steam Workshop",
            "Tự phát hành bởi Approximately Games (nhà phát triển kiêm phát hành)",
        ],
        "stats": [
            {"value": "6/8", "label": "Ngày phát hành"},
            {"value": "14", "label": "Ngôn ngữ"},
            {"value": "22", "label": "Thành tựu"},
            {"value": "Đơn + Hợp tác", "label": "Chế độ"},
            {"value": "$19.99", "label": "Trên Steam (-20%)"},
            {"value": "chưa xác minh", "label": "Đánh giá Steam"},
        ],
        "aboutPoints": [
            "Approximately Up được phát triển và phát hành bởi Approximately Games (indie tự phát hành).",
            "Trò chơi phát hành trên Steam ngày 6 tháng 8 năm 2026; bản demo ra mắt sớm hơn.",
            "Trang này đối chiếu từng trang với trang Steam chính thức, video chính thức và liên kết chính thức; nội dung từ cộng đồng được đánh dấu là chưa xác minh cho đến khi xác nhận.",
            "Kênh chính thức: approximatelyup.com, Discord, TikTok @approximatelyup và YouTube @ApproximatelyUp.",
        ],
    },
}

# =====================================================================
# 来源池（页面 → 来源映射取自 research.md；label 全 14 语，避免英文混排）
# =====================================================================
def _src(label, url, labels):
    """labels: {en, zh-CN, ja, ko, fr, de, es, it, pl, pt-BR, ru, uk, vi}；zh-TW 自动由 zh-CN 转换。"""
    d = {"label": label, "url": url, "labels": dict(labels)}
    d["labels"]["zh-TW"] = cc.convert(d["labels"]["zh-CN"])
    return d

SRC_STEAM = _src("Official Steam page", "https://store.steampowered.com/app/3904850/", {
    "en": "Official Steam page", "zh-CN": "Steam 官方商店页",
    "ja": "Steam 公式ストア", "ko": "Steam 공식 스토어", "fr": "Page Steam officielle",
    "de": "Offizielle Steam-Seite", "es": "Página oficial de Steam", "it": "Pagina Steam ufficiale",
    "pl": "Oficjalna strona Steam", "pt-BR": "Página oficial na Steam", "ru": "Официальная страница Steam",
    "uk": "Офіційна сторінка Steam", "vi": "Trang Steam chính thức",
})
SRC_TRAILER = _src("Gameplay Trailer (official)", "https://www.youtube.com/watch?v=1vhwtXETc1w", {
    "en": "Gameplay Trailer (official)", "zh-CN": "官方实机预告片",
    "ja": "公式ゲームプレイトレーラー", "ko": "공식 게임플레이 트레일러", "fr": "Bande-annonce de gameplay (officielle)",
    "de": "Offizieller Gameplay-Trailer", "es": "Tráiler de gameplay (oficial)", "it": "Trailer di gameplay (ufficiale)",
    "pl": "Oficjalny zwiastun rozgrywki", "pt-BR": "Trailer de gameplay (oficial)", "ru": "Официальный геймплейный трейлер",
    "uk": "Офіційний трейлер геймплею", "vi": "Trailer gameplay (chính thức)",
})
SRC_REVEAL = _src("Reveal Trailer (official)", "https://www.youtube.com/watch?v=gc6rN0HiH90", {
    "en": "Reveal Trailer (official)", "zh-CN": "官方公布预告片",
    "ja": "公式リビールトレーラー", "ko": "공식 리빌 트레일러", "fr": "Bande-annonce de révélation (officielle)",
    "de": "Offizieller Enthüllungs-Trailer", "es": "Tráiler de presentación (oficial)", "it": "Trailer di annuncio (ufficiale)",
    "pl": "Oficjalny zwiastun zapowiedzi", "pt-BR": "Trailer de anúncio (oficial)", "ru": "Официальный анонс-трейлер",
    "uk": "Офіційний анонс-трейлер", "vi": "Trailer công bố (chính thức)",
})
SRC_SITE = _src("Official website", "https://approximatelyup.com", {
    "en": "Official website", "zh-CN": "官方网站",
    "ja": "公式サイト", "ko": "공식 웹사이트", "fr": "Site officiel",
    "de": "Offizielle Website", "es": "Sitio web oficial", "it": "Sito ufficiale",
    "pl": "Oficjalna strona", "pt-BR": "Site oficial", "ru": "Официальный сайт",
    "uk": "Офіційний сайт", "vi": "Trang web chính thức",
})
SRC_DISCORD = _src("Official Discord", "https://discord.gg/approximatelyup", {
    "en": "Official Discord", "zh-CN": "官方 Discord",
    "ja": "公式 Discord", "ko": "공식 Discord", "fr": "Discord officiel",
    "de": "Offizieller Discord", "es": "Discord oficial", "it": "Discord ufficiale",
    "pl": "Oficjalny Discord", "pt-BR": "Discord oficial", "ru": "Официальный Discord",
    "uk": "Офіційний Discord", "vi": "Discord chính thức",
})
SRC_COMMUNITY = _src("Steam Community discussions", "https://steamcommunity.com/app/3904850/", {
    "en": "Steam Community discussions", "zh-CN": "Steam 社区讨论",
    "ja": "Steam コミュニティの議論", "ko": "Steam 커뮤니티 토론", "fr": "Discussions de la communauté Steam",
    "de": "Steam-Community-Diskussionen", "es": "Discusiones de la comunidad de Steam", "it": "Discussioni della community Steam",
    "pl": "Dyskusje społeczności Steam", "pt-BR": "Discussões da comunidade Steam", "ru": "Обсуждения в сообществе Steam",
    "uk": "Обговорення в спільноті Steam", "vi": "Thảo luận cộng đồng Steam",
})
SRC_WORKSHOP = _src("Steam Workshop", "https://steamcommunity.com/app/3904850/workshop/", {
    "en": "Steam Workshop", "zh-CN": "Steam 创意工坊",
    "ja": "Steam ワークショップ", "ko": "Steam 창작마당", "fr": "Steam Workshop",
    "de": "Steam Workshop", "es": "Steam Workshop", "it": "Steam Workshop",
    "pl": "Steam Workshop", "pt-BR": "Steam Workshop", "ru": "Мастерская Steam",
    "uk": "Майстерня Steam", "vi": "Steam Workshop",
})
SRC_NEWS = _src("Steam Announcements (patch notes)", "https://store.steampowered.com/news/app/3904850", {
    "en": "Steam Announcements (patch notes)", "zh-CN": "Steam 官方公告（更新日志）",
    "ja": "Steam 公式アナウンス（パッチノート）", "ko": "Steam 공지 (패치 노트)", "fr": "Annonces Steam (notes de mise à jour)",
    "de": "Steam-Ankündigungen (Patch-Notizen)", "es": "Anuncios de Steam (notas del parche)", "it": "Annunci Steam (note di patch)",
    "pl": "Ogłoszenia Steam (noty aktualizacji)", "pt-BR": "Anúncios da Steam (notas de atualização)", "ru": "Анонсы Steam (примечания к обновлениям)",
    "uk": "Анонси Steam (примітки до оновлень)", "vi": "Thông báo Steam (ghi chú bản vá)",
})
SRC_STEAMDB = _src("SteamDB (to verify)", "https://steamdb.info/app/3904850/achievements/", {
    "en": "SteamDB (to verify)", "zh-CN": "SteamDB（待核）",
    "ja": "SteamDB（要確認）", "ko": "SteamDB (확인 필요)", "fr": "SteamDB (à vérifier)",
    "de": "SteamDB (zu prüfen)", "es": "SteamDB (por verificar)", "it": "SteamDB (da verificare)",
    "pl": "SteamDB (do sprawdzenia)", "pt-BR": "SteamDB (a verificar)", "ru": "SteamDB (проверить)",
    "uk": "SteamDB (перевірити)", "vi": "SteamDB (cần xác minh)",
})
SRC_PCGW = _src("PCGamingWiki (to verify)", "https://www.pcgamingwiki.com/wiki/Approximately_Up", {
    "en": "PCGamingWiki (to verify)", "zh-CN": "PCGamingWiki（待核）",
    "ja": "PCGamingWiki（要確認）", "ko": "PCGamingWiki (확인 필요)", "fr": "PCGamingWiki (à vérifier)",
    "de": "PCGamingWiki (zu prüfen)", "es": "PCGamingWiki (por verificar)", "it": "PCGamingWiki (da verificare)",
    "pl": "PCGamingWiki (do sprawdzenia)", "pt-BR": "PCGamingWiki (a verificar)", "ru": "PCGamingWiki (проверить)",
    "uk": "PCGamingWiki (перевірити)", "vi": "PCGamingWiki (cần xác minh)",
})

# =====================================================================
# 英文页面（en 为基准；sources 的 labels 已全语言覆盖）
# 注意：heroImage 暂不填（配图生成后由 gen_images.py / 后续填充），生成器会用 meta.icon 渲染。
# =====================================================================
def _page(slug, title, meta_title, meta_desc, intro, sections, sources, icon):
    return {
        "slug": slug, "title": title, "metaTitle": meta_title, "metaDescription": meta_desc,
        "intro": intro, "sections": sections, "sources": sources,
        "meta": {"icon": icon},
    }

PAGES = []

PAGES.append(_page(
    "how-to-play",
    "How to Play Approximately Up",
    "How to Play Approximately Up: Complete Beginner's Guide",
    "New to Approximately Up? Learn the build-crash-rebuild loop, modular ships, co-op multiplayer and planet exploration in this beginner's guide.",
    "Approximately Up is a space sandbox builder about bolting parts together, taking off, crashing, and rebuilding better. Here is the core loop and what to know before your first launch.",
    [
        {"type": "steps", "heading": "The core loop: build, crash, rebuild",
         "body": "The official description sums up the loop in three words — build, crash, rebuild. Everything else follows from it.",
         "items": [
            ["Start small", "Assemble a ship from whatever parts bolt together long enough to fly. You do not need a perfect design to begin — you need something that lifts off."],
            ["Mount thrusters and cables", "Giant thrusters get you moving; cables and every part in between connect your build. Expect the layout to be messy at first."],
            ["Test fly", "Take off and see what holds. The first flights are experiments, not polished flights."],
            ["Crash (it happens)", "Crashes are part of the loop. The official pitch treats them as expected — debris is a lesson, not a failure."],
            ["Rebuild smarter", "Use what you learned to rebuild. Each iteration teaches you which parts hold and which combinations fly."],
         ]},
        {"type": "list", "heading": "What the game officially promises",
         "body": "From the official Steam description:",
         "items": [
            "Explore new planets in co-op multiplayer with your fully modular spaceship.",
            "Mount giant thrusters, annoying cables, and everything in between.",
            "Complete wild missions and face the dangers of space.",
            "Play solo or with a crew — and argue with your crew, as the official pitch puts it.",
         ]},
        {"type": "faq", "heading": "Beginner FAQ",
         "items": [
            ["Is Approximately Up multiplayer?", "Yes — the official store page lists single-player and online co-op multiplayer."],
            ["Do I need to know engineering to play?", "No. The game is built around trial and error: bolt parts on, fly, crash, learn."],
            ["Is there a demo?", "Yes — the official store page lists a demo that predates the full release (August 6, 2026)."],
            ["Can I play on Steam Deck?", "Compatibility is not yet confirmed. Players are asking about it on the Steam forums; we mark this as unverified until an official answer."],
         ]},
        {"type": "note", "heading": "What we still need to verify",
         "body": "Specific planet names, mission names and detailed mechanic guides (blueprints, wiring, radar, time rewind) are not yet verified against official sources. We mark them as unverified and update this page as official information becomes available."},
    ],
    [SRC_STEAM, SRC_TRAILER],
    "how-to-play",
))

PAGES.append(_page(
    "ship-building-guide",
    "Approximately Up Ship Building Guide",
    "Approximately Up Ship Building Guide: First Ship to Big Builds",
    "Learn to build ships in Approximately Up: the modular build-crash-rebuild process, thrusters and cables, plus community needs like moon trips and radar.",
    "Ship building is the heart of Approximately Up. The official pitch is simple: bolt parts together until they fly, then rebuild smarter. This guide walks the process without inventing part stats that are still unverified.",
    [
        {"type": "steps", "heading": "Build your first ship",
         "body": "Based on the official description (modular parts, thrusters, cables, build-crash-rebuild), here is the flow:",
         "items": [
            ["Gather parts", "Collect whatever parts are available and bolt them together. The official pitch says any build 'bolts together long enough to fly' — start there."],
            ["Add thrusters", "Mount thrusters to get moving. The official description highlights 'giant thrusters' as a core part of the fantasy."],
            ["Run cables", "Connect your build with cables — 'annoying cables' are part of the experience. Expect messy wiring."],
            ["Test flight", "Take off. Your first ship does not need to be pretty; it needs to teach you what holds."],
            ["Crash and iterate", "Rebuild with what you learned. The loop is build → crash → rebuild."],
         ]},
        {"type": "list", "heading": "Design principles (official-aligned)",
         "items": [
            "Fully modular ship: everything can be re-arranged between flights.",
            "Balance weight vs thrust — heavier ships need more thrust (specific numbers unverified).",
            "Keep spare parts: crashes are expected.",
            "Plan for co-op: if you play with a crew, agree on roles (pilot, builder, engineer).",
         ]},
        {"type": "evidence", "heading": "Community tutorials being requested",
         "items": [
            ["How can I go to the moon", "A real Steam forum thread — players want a moon-trip guide. Specific moon mechanics are unverified."],
            ["Beginning Radar Monitor / Device", "A real Steam forum thread — players want a radar device tutorial. Radar mechanics are unverified."],
         ]},
        {"type": "note", "heading": "What is still unverified",
         "body": "Specific part names, stats, recipes, planet destinations and mission names are not yet verified. This guide uses only the official description plus marked community questions; we will deepen it as verified information arrives."},
    ],
    [SRC_TRAILER, SRC_STEAM],
    "automation",
))

PAGES.append(_page(
    "blueprints-guide",
    "Approximately Up Blueprints Guide",
    "Approximately Up Blueprints: Download, Share & Use",
    "Approximately Up blueprints: what we know about finding and using blueprints, Steam Workshop support, and what is still unverified.",
    "Blueprints are one of the most-searched Approximately Up topics. Official blueprint mechanics (import, export, sharing) are not yet verified, so this page covers what is confirmed and what is unverified.",
    [
        {"type": "note", "heading": "Blueprint details: unverified",
         "body": "Blueprint import, export and sharing mechanics are on our unverified list — we have not confirmed them against an official source. This page will be expanded as soon as reliable information is verified."},
        {"type": "steps", "heading": "Finding ship designs today",
         "body": "While official blueprint tools are unverified, the Steam Workshop is the confirmed place where community content lives:",
         "items": [
            ["Open the Steam Workshop for Approximately Up", "Community-uploaded content is hosted there (Workshop support is confirmed on the store page)."],
            ["Browse ships and builds", "Look for ship designs shared by other players."],
            ["Subscribe", "Subscribe to save content to your library."],
            ["Check in-game", "See how subscribed items appear in the game — exact steps unverified."],
         ]},
        {"type": "faq", "heading": "Blueprints FAQ",
         "items": [
            ["Can I download blueprints in Approximately Up?", "Unverified. Workshop content is the closest confirmed channel today."],
            ["Can I share my ship designs?", "Unverified. We will confirm the exact sharing workflow once verified."],
            ["Are blueprints the same as Workshop items?", "Not necessarily — the relationship between in-game blueprints and Workshop items is unverified."],
         ]},
        {"type": "note", "heading": "Sources to watch",
         "body": "We will verify blueprint mechanics against official channels (Steam announcements, official site, Discord) and update this page. Nothing here invents mechanics."},
    ],
    [SRC_STEAM, SRC_WORKSHOP],
    "how-to-play",
))

PAGES.append(_page(
    "wiring-electronics",
    "Approximately Up Wiring & Electronics Guide",
    "Approximately Up Wiring & Electronics: What We Know",
    "Approximately Up wiring and electronics: cables in builds, community questions about the vacuum tube era and the Remapper — with unverified details marked.",
    "Wiring and electronics are a big community topic — but official details are thin. This page collects what is verified and what players are asking, with everything unverified clearly marked.",
    [
        {"type": "note", "heading": "Official information is limited",
         "body": "The official description mentions cables as part of the modular build ('annoying cables, and everything in between'), but detailed wiring and circuit mechanics are not yet verified in our knowledge base. We mark them as unverified."},
        {"type": "evidence", "heading": "Community threads (real questions from players)",
         "items": [
            ["Can we move beyond the Vacuum Tube era of electronics please?", "A Steam forum thread asking about the electronics progression/era of parts — suggests an early-era electronics theme; exact mechanics unverified."],
            ["Can't set values in Remapper", "A Steam forum thread reporting trouble setting values in the Remapper/Constant — the exact workflow is unverified."],
         ]},
        {"type": "list", "heading": "What we can say safely",
         "items": [
            "Cables are an official part of the modular shipbuilding fantasy.",
            "Electronics appear to be a progression area (community mentions an early 'vacuum tube era').",
            "Parameter/value setting tools exist in-game (Remapper), but exact usage is unverified.",
         ]},
        {"type": "faq", "heading": "Wiring & electronics FAQ",
         "items": [
            ["How does wiring work in Approximately Up?", "Unverified. We will publish a guide once official or reliably cross-checked information exists."],
            ["What are the electronics tiers?", "A community thread mentions a 'Vacuum Tube era'; exact tiers and unlocks are unverified."],
            ["Why can't I set values in the Remapper?", "A community thread reports this issue; the official workflow is unverified."],
         ]},
    ],
    [SRC_COMMUNITY, SRC_STEAM],
    "gene-system",
))

PAGES.append(_page(
    "controls",
    "Approximately Up Controls",
    "Approximately Up Controls: Keyboard, Mouse & Controller Status",
    "Approximately Up control guide: what we know about keyboard and mouse, controller support, and the in-game remapper — plus what is still unverified.",
    "Controller support is one of the most-asked questions in the Steam community right after launch. Here is what we can confirm, what players are asking, and what is still unverified.",
    [
        {"type": "evidence", "heading": "What we know (verified)",
         "items": [
            ["Platform", "The game is on PC (Steam). Keyboard and mouse are the default input."],
            ["Controller support", "Not yet confirmed by the developer. A Steam forum thread asks 'Controller Support in the Future?', which suggests full controller support is not confirmed at launch."],
            ["In-game remapper", "Players are discussing the Remapper — a community thread reports trouble setting values in it. We mark the exact mapping workflow as unverified."],
         ]},
        {"type": "list", "heading": "How to set up controls right now",
         "items": [
            "Open the in-game settings and check the input / controls section for the current key mapping.",
            "Use the in-game Remapper to rebind keys; if values do not apply, check the Steam community thread and developer notes.",
            "For controller support updates, follow the official Discord and Steam announcements.",
         ]},
        {"type": "note", "heading": "Unverified: full key map",
         "body": "The complete official key mapping (movement, camera, build menu, thruster control) is not yet verified against an official source. We mark it as unverified and will publish the table once confirmed."},
        {"type": "faq", "heading": "Controls FAQ",
         "items": [
            ["Does Approximately Up support controllers?", "Not confirmed yet. The community is asking; we mark this unverified until the developer or an official source confirms."],
            ["Can I rebind keys?", "There is an in-game Remapper. Some players report issues setting values; the exact workflow is unverified."],
            ["Is there a Steam Deck control layout?", "Steam Deck compatibility itself is still an open question in the community — the control layout is unverified."],
         ]},
    ],
    [SRC_STEAM, SRC_COMMUNITY],
    "steam-deck",
))

PAGES.append(_page(
    "multiplayer",
    "Approximately Up Multiplayer Guide",
    "Approximately Up Multiplayer: Co-op, Player Count & Crossplay",
    "Approximately Up multiplayer explained: online co-op, how many players, whether there is asynchronous multiplayer, and what is still unverified.",
    "Approximately Up is officially a single-player and online co-op game. This page answers the multiplayer questions players are actually asking, and marks what we cannot verify yet.",
    [
        {"type": "note", "heading": "Official status",
         "body": "The official Steam store page lists 'Single-player' and 'Online Co-op' as supported modes. The game's pitch is built around a crew exploring planets together in a modular ship."},
        {"type": "faq", "heading": "Multiplayer FAQ",
         "items": [
            ["How many players can play together?", "The exact player count is not verified in our knowledge base — we mark it as unverified."],
            ["Is there online co-op?", "Yes — online co-op multiplayer is listed on the official Steam store page."],
            ["Is there cross-platform multiplayer?", "Unverified. The game is currently on PC (Steam); console versions are not announced, so crossplay is unverified."],
            ["Is there asynchronous multiplayer?", "Not confirmed. A Steam forum thread asks about 'Asynchronous Multiplayer', which suggests it is not an official feature yet — we mark it as unverified."],
            ["Can I play solo?", "Yes — single-player is listed as a supported mode."],
         ]},
        {"type": "list", "heading": "What the community is asking",
         "items": [
            "Asynchronous Multiplayer — whether players can expect an async mode.",
            "Player count / 'how many players' is a top search need; we will publish the verified number when available.",
         ]},
        {"type": "note", "heading": "What is still unverified",
         "body": "Exact player cap, invite flow, hosting details and crossplay are not yet verified against official sources. We update this page as soon as they are confirmed."},
    ],
    [SRC_STEAM, SRC_COMMUNITY],
    "characters",
))

PAGES.append(_page(
    "best-ship-designs",
    "Approximately Up Best Ship Designs",
    "Approximately Up Ship Ideas & Best Designs",
    "Approximately Up ship design ideas: starting points for your own builds, community design questions, and where to find more designs.",
    "Looking for ship ideas? This page collects design starting points based on the official build-crash-rebuild fantasy, plus community questions that shape what players want to build.",
    [
        {"type": "list", "heading": "Design starting points (inspiration, not official specs)",
         "items": [
            "Thruster-heavy speedster: mount giant thrusters and accept that control comes later.",
            "Utility hauler: favor cargo and mission parts over speed — missions need capacity (details unverified).",
            "Co-op crew ship: design with space for a crew exploring planets together.",
            "Messy cable build: embrace 'annoying cables' — wiring is part of the charm (wiring mechanics unverified).",
         ]},
        {"type": "evidence", "heading": "Community design questions",
         "items": [
            ["Trajectory Curvature Meter", "A Steam forum thread about a trajectory tool — players want better flight tools; official status unverified."],
            ["mods to make multiple ships?", "A Steam forum thread about controlling more than one ship — unverified."],
         ]},
        {"type": "list", "heading": "Where to find more designs",
         "items": [
            "Steam Workshop for Approximately Up (confirmed supported).",
            "The game's official YouTube channel for trailer builds.",
            "Steam community discussions for player screenshots and ideas.",
         ]},
        {"type": "note", "heading": "What is still unverified",
         "body": "Specific part stats, blueprints of named designs and any 'best' tier lists are not verified. We keep this page as inspiration plus verified sources, and mark everything else as unverified."},
    ],
    [SRC_WORKSHOP, SRC_COMMUNITY],
    "story",
))

PAGES.append(_page(
    "system-requirements",
    "Approximately Up System Requirements",
    "Approximately Up System Requirements (PC)",
    "Approximately Up PC system requirements: minimum and recommended specs are not yet verified — here is what we know and how to check compatibility.",
    "Players want a straight answer on whether their PC can run Approximately Up. The official minimum and recommended specs are still unverified in our knowledge base, so this page tells you what we know and what is unverified.",
    [
        {"type": "note", "heading": "Official specs: unverified",
         "body": "We have not yet verified official minimum and recommended system requirements from an official source. Instead of inventing numbers, we mark the spec table as unverified and will fill it as soon as it is confirmed (Steam store page or official site)."},
        {"type": "table", "heading": "Spec table (unverified)",
         "columns": ["Spec", "Minimum", "Recommended"],
         "rows": [
            ["OS", "unverified", "unverified"],
            ["Processor", "unverified", "unverified"],
            ["Memory", "unverified", "unverified"],
            ["Graphics", "unverified", "unverified"],
            ["Storage", "unverified", "unverified"],
            ["DirectX", "unverified", "unverified"],
         ]},
        {"type": "list", "heading": "How to check your own PC",
         "items": [
            "Open Steam and check the game's store page — system requirements usually appear there once published.",
            "Compare your CPU/GPU/RAM against the official numbers once we publish them.",
            "For Steam Deck: compatibility is an open community question ('Playable on Deck?'); we mark it unverified.",
         ]},
        {"type": "faq", "heading": "System requirements FAQ",
         "items": [
            ["Can my PC run Approximately Up?", "We cannot confirm yet — official minimum/recommended specs are unverified. Check the Steam store page when the developer publishes them."],
            ["Is Approximately Up on Steam Deck?", "Not confirmed. A Steam forum thread asks 'Playable on Deck?' — compatibility is unverified until an official answer."],
            ["Is it demanding?", "The game is a space sandbox builder with modular physics-based ships; we will report verified numbers as soon as they are available."],
         ]},
    ],
    [SRC_STEAM, SRC_PCGW],
    "system-requirements",
))

PAGES.append(_page(
    "console-release",
    "Approximately Up Console Release: PS5, Xbox & Switch Status",
    "Approximately Up Console Release Date (PS5, Xbox, Switch)",
    "Is Approximately Up coming to PS5, Xbox or Switch? No official announcement yet — here is the console release status and how to follow official news.",
    "'Approximately Up PS5 release date', 'Xbox release' and 'Switch release' are searches the game's own wiki does not answer. The honest answer today: no official console announcement is verified — here is the status page.",
    [
        {"type": "evidence", "heading": "Console status (as of 2026-08-09)",
         "items": [
            ["Current platforms", "PC (Steam) only. The game released on August 6, 2026 on Steam."],
            ["PS5", "unverified — no verified official announcement of a PlayStation 5 version."],
            ["Xbox", "unverified — no verified official announcement of an Xbox version."],
            ["Nintendo Switch", "unverified — no verified official announcement of a Switch version."],
            ["Official statement", "We have not verified an official developer statement about console plans; we mark this unverified and will update as soon as one exists."],
         ]},
        {"type": "list", "heading": "How to stay informed",
         "items": [
            "Follow the official site approximatelyup.com and the official Discord (discord.gg/approximatelyup).",
            "Watch the developer's YouTube channel (@ApproximatelyUp) and TikTok (@approximatelyup) for announcements.",
            "Check the Steam store page — console news is usually announced there first.",
         ]},
        {"type": "faq", "heading": "Console FAQ",
         "items": [
            ["Is Approximately Up on PS5?", "Not announced — we mark this unverified. No verified official statement exists yet."],
            ["Is Approximately Up on Xbox?", "Not announced — unverified."],
            ["Is Approximately Up on Nintendo Switch?", "Not announced — unverified."],
            ["When is the console release date?", "No date exists yet. This page will be updated the moment an official announcement is verified."],
         ]},
        {"type": "note", "heading": "Why this page exists",
         "body": "Console release is one of the highest-intent questions for this game, but no reliable source has answered it. This page gives the verified status (PC only) and tracks future announcements instead of inventing a date."},
    ],
    [SRC_SITE, SRC_STEAM],
    "steam-deck",
))

PAGES.append(_page(
    "mods",
    "Approximately Up Mods Guide",
    "Approximately Up Mods: Steam Workshop, Install & Mod Questions",
    "Approximately Up mods explained: Steam Workshop support, how to subscribe to mods, and community mod questions like multiple ships.",
    "Approximately Up supports the Steam Workshop, which makes finding and installing mods straightforward. Here is what is confirmed and what players are asking for.",
    [
        {"type": "steps", "heading": "Getting mods from the Steam Workshop",
         "body": "Workshop support is confirmed on the official store page. The standard flow:",
         "items": [
            ["Open the Workshop", "From the game's Steam store page, open the Workshop tab (or visit the Workshop community hub)."],
            ["Browse and subscribe", "Find a mod or item you like and press Subscribe — Steam downloads it automatically."],
            ["Launch the game", "Open Approximately Up and check the game's mod/content menu to see subscribed items."],
            ["Enable what you want", "Turn on the mods you want to use. Details of the in-game mod menu are unverified."],
         ]},
        {"type": "list", "heading": "What the community is asking",
         "items": [
            "mods to make multiple ships? — a real Steam forum thread; multi-ship support via mods is unverified.",
            "Cheat-engine related searches exist for many games; we do not provide cheats, only verified mod information.",
         ]},
        {"type": "faq", "heading": "Mods FAQ",
         "items": [
            ["Does Approximately Up support mods?", "Officially it supports Steam Workshop (per the store page). Full modding documentation is unverified."],
            ["How do I install mods?", "Subscribe via the Steam Workshop; Steam handles installation. In-game steps are unverified."],
            ["Can mods let me control multiple ships?", "A community thread asks for this; no verified mod provides it yet — unverified."],
         ]},
        {"type": "note", "heading": "What is still unverified",
         "body": "Exact Workshop features, mod guidelines, and whether mods affect achievements or multiplayer are not yet verified. We will update this page when official documentation is confirmed."},
    ],
    [SRC_STEAM, SRC_WORKSHOP],
    "mods",
))

PAGES.append(_page(
    "patch-notes",
    "Approximately Up Patch Notes",
    "Approximately Up Patch Notes & Update History",
    "Approximately Up patch notes and update history: launch info, verified official update timeline (1.0.006\u20131.0.010) and where updates are posted.",
    "Approximately Up released on August 6, 2026. This page tracks official patch notes and updates, verified from Steam announcements.",
    [
        {"type": "evidence", "heading": "Launch facts (verified)",
         "items": [
            ["Release date", "August 6, 2026 (Steam full release)."],
            ["Demo", "A demo predates the full release."],
            ["Price", "$19.99 at launch (20% off; list $24.99)."],
         ]},
        {"type": "timeline", "heading": "Update timeline (verified from Steam)",
         "body": "Patch notes verified from official Steam announcements (August 2026):",
         "items": [
            ["2026-08-12", "1.0.010 — Fixed Workshop \'Most Popular\' sorting filter, page loading and missing results; improved search clarity."],
            ["2026-08-11", "1.0.009 — Improved Frame Quarter With Ports (ports mirror across the frame chain, A\u2013D labels stay consistent); fixed Middle Window, Small Switch and Small Button geometry."],
            ["2026-08-10", "1.0.008 — Fixed Axis Rotometer hitbox and remaining issues; Plasma Cables now paintable; Autohemisphere Solar Panels return to position after Fly Mode; cable holders now paintable."],
            ["2026-08-09", "1.0.007 — Fixed Metal device compatibility; corrected default keybind (middle mouse for \'pick component\'); fixed pipe description typo; added more hints."],
            ["2026-08-08", "1.0.006 — Fixed Fuse Box power-on; Axis Rotometer outputs signed local-axis values; fixed Large Disposable Battery preview; added credits, startup screen and objectives completion tracking."],
            ["2026-08-06", "Full release (verified)."],
         ]},
        {"type": "list", "heading": "Where official updates are posted",
         "items": [
            "Steam Announcements for the game (news feed on the store page).",
            "The official site approximatelyup.com and official Discord.",
            "Developer YouTube channel for feature announcements.",
         ]},
        {"type": "note", "heading": "What is still unverified",
         "body": "Patch notes above are verified from official Steam announcements. Details of pre-release builds and unannounced changes remain unverified."},
    ],
    [SRC_STEAM, SRC_NEWS],
    "update-log",
))

PAGES.append(_page(
    "demo-vs-full",
    "Approximately Up Demo vs Full Game",
    "Approximately Up Demo vs Full Game: What's the Difference?",
    "Approximately Up demo vs full version: release dates, price, Workshop and achievements — and what content differences are still unverified.",
    "The Approximately Up demo came before the full release on August 6, 2026. Here is the verified comparison, with content differences clearly marked unverified.",
    [
        {"type": "table", "heading": "Verified comparison",
         "columns": ["Aspect", "Demo", "Full game"],
         "rows": [
            ["Availability", "Demo (released earlier, per store page)", "Full release August 6, 2026"],
            ["Price", "unverified", "$19.99 (20% launch discount; list $24.99)"],
            ["Steam Workshop", "unverified", "Supported (per store page)"],
            ["Achievements", "unverified", "22 Steam achievements (per store page)"],
            ["Co-op multiplayer", "unverified", "Single-player + online co-op (per store page)"],
         ]},
        {"type": "faq", "heading": "Demo vs full FAQ",
         "items": [
            ["Is the demo free?", "We have not verified the demo's price/model — unverified."],
            ["Does demo progress carry over to the full game?", "Unverified."],
            ["What content is only in the full game?", "Unverified — official comparison details are pending. The full game adds Workshop support and 22 achievements per the store page."],
            ["Should I try the demo first?", "For most space sandbox builders, trying the demo is a good way to feel the build-crash-rebuild loop before buying — but exact demo content limits are unverified."],
         ]},
        {"type": "note", "heading": "What is still unverified",
         "body": "Exact demo content, progress transfer and feature differences are not verified against an official source. We update this table as soon as they are confirmed."},
    ],
    [SRC_STEAM, SRC_COMMUNITY],
    "faq",
))

PAGES.append(_page(
    "achievements-list",
    "Approximately Up Achievements List",
    "Approximately Up Achievements: Full List (22)",
    "Approximately Up has 22 Steam achievements. The full list of names is still being verified — here is what is confirmed.",
    "The official Steam store page confirms 22 achievements. The exact names and unlock conditions are not yet verified in our knowledge base, so this page tracks the confirmed count and marks the list as unverified.",
    [
        {"type": "note", "heading": "Confirmed: 22 achievements",
         "body": "The Steam store page lists 22 achievements for Approximately Up. We have not yet verified each achievement's name, icon and unlock condition — that part is unverified."},
        {"type": "table", "heading": "Achievement list (unverified)",
         "columns": ["Achievement", "Condition"],
         "rows": [
            ["Achievement 1–22", "unverified — names and conditions are being verified against the official list."],
         ]},
        {"type": "list", "heading": "How to track achievements",
         "items": [
            "Use the Steam overlay in-game to see your progress.",
            "Follow the official Steam announcements — achievement lists sometimes ship with patch notes.",
            "We will publish the full verified list here when confirmed.",
         ]},
        {"type": "faq", "heading": "Achievements FAQ",
         "items": [
            ["How many achievements does Approximately Up have?", "22, confirmed on the official Steam store page."],
            ["What are the achievement names?", "unverified — we are verifying the official list and will publish it when confirmed."],
            ["Can I get all achievements in single-player?", "Unverified — some may require co-op, but we do not know until the list is confirmed."],
         ]},
    ],
    [SRC_STEAM, SRC_STEAMDB],
    "achievements",
))

PAGES.append(_page(
    "ships",
    "Approximately Up Ships",
    "Approximately Up Ships: Builds, Ideas & Designs",
    "Index of Approximately Up ship content: building guide, ship designs, blueprints and the modular shipbuilding basics.",
    "Everything about Approximately Up ships in one place — from your first build to community design ideas.",
    [
        {"type": "list", "heading": "Ship guides",
         "items": [
            "Ship Building Guide — learn the build-crash-rebuild process.",
            "Best Ship Designs — design starting points and community ideas.",
            "Blueprints Guide — what we know about blueprints and Workshop content.",
            "Mods — Workshop support and mod questions.",
         ]},
        {"type": "faq", "heading": "Ships FAQ",
         "items": [
            ["What kind of ships can I build?", "Ships are fully modular — you bolt parts together however they fit (official description). Specific part lists are unverified."],
            ["Can I fly to the moon?", "A community thread asks how; moon mechanics are unverified."],
            ["Can I control multiple ships?", "A community thread asks about this; unverified."],
         ]},
    ],
    [SRC_STEAM, SRC_TRAILER],
    "exploration",
))

PAGES.append(_page(
    "blueprints",
    "Approximately Up Blueprints",
    "Approximately Up Blueprints: Downloads & Library",
    "Index of Approximately Up blueprint content: how to use blueprints, where to find ship designs, and the Steam Workshop.",
    "The blueprint library index — find ship designs, learn the (unverified) blueprint workflow, and browse the Workshop.",
    [
        {"type": "list", "heading": "Blueprint content",
         "items": [
            "Blueprints Guide — what is confirmed and what is unverified about blueprints.",
            "Best Ship Designs — design ideas and where to find more.",
            "Steam Workshop — the confirmed home of community content.",
         ]},
        {"type": "faq", "heading": "Blueprints index FAQ",
         "items": [
            ["Where can I download blueprints?", "Steam Workshop is the confirmed channel for community content; in-game blueprint download mechanics are unverified."],
            ["How do I import a blueprint?", "Unverified."],
            ["Can I share my designs?", "Unverified."],
         ]},
    ],
    [SRC_WORKSHOP, SRC_STEAM],
    "faq",
))

PAGES.append(_page(
    "guides",
    "Approximately Up Guides",
    "Approximately Up Guides: All Pages",
    "All Approximately Up guides in one index: how to play, ship building, controls, multiplayer, mods, achievements and more.",
    "The complete guide index for Approximately Up. Every page answers one question players actually search for, and marks anything unverified.",
    [
        {"type": "list", "heading": "All guides",
         "items": [
            "How to Play — the build-crash-rebuild loop for beginners.",
            "Controls — keyboard/mouse, controller status and remapper notes.",
            "System Requirements — spec status and how to check your PC.",
            "Multiplayer — online co-op, player count and async questions.",
            "Console Release — PS5/Xbox/Switch status.",
            "Mods — Steam Workshop and mod questions.",
            "Patch Notes — launch facts and update tracking.",
            "Demo vs Full — verified comparison.",
            "Ship Building Guide — first ship to big builds.",
            "Wiring & Electronics — what is known, what is unverified.",
            "Blueprints Guide — blueprint status and Workshop.",
            "Best Ship Designs — ideas and community designs.",
            "Achievements List — 22 achievements, list unverified.",
            "Ships / Blueprints / Achievements — index pages.",
         ]},
        {"type": "note", "heading": "How we work",
         "body": "Every page lists 1–2 reliable sources and marks anything not verified as unverified. We do not invent numbers, names or mechanics."},
    ],
    [SRC_STEAM, SRC_SITE],
    "faq",
))

PAGES.append(_page(
    "achievements",
    "Approximately Up Achievements",
    "Approximately Up Achievements: Overview",
    "Approximately Up achievements overview: 22 Steam achievements confirmed, full list being verified, and how to track progress.",
    "The achievements hub for Approximately Up — confirmed count, current list status, and links to the full tracker page.",
    [
        {"type": "note", "heading": "22 achievements confirmed",
         "body": "The Steam store page confirms 22 achievements. The full list of names and conditions is unverified."},
        {"type": "list", "heading": "Achievements content",
         "items": [
            "Achievements List — the dedicated page for the full (unverified) list.",
            "Steam — check the store page's achievement section.",
         ]},
        {"type": "faq", "heading": "Achievements overview FAQ",
         "items": [
            ["How many achievements are there?", "22 (confirmed on the Steam store page)."],
            ["Where is the full list?", "unverified — we are verifying the official list."],
         ]},
    ],
    [SRC_STEAM],
    "achievements",
))

# =====================================================================
# 页面翻译（结构按 en sections 索引对齐；zh-TW 由 zh-CN 经 OpenCC 自动生成）
# 未核实内容在各语言统一用「待补」本地化写法标注（zh: 待补 / ja: 未検証 / ko: 미확인 / en: unverified …）
# =====================================================================
TR_ZH = {
    "how-to-play": {
        "title": "Approximately Up 怎么玩：新手指南",
        "metaTitle": "Approximately Up 怎么玩：完整新手入门指南",
        "metaDescription": "刚接触 Approximately Up？这篇新手指南讲清「建造—坠毁—重建」循环、模块化飞船、多人合作与星球探索。",
        "intro": "《Approximately Up》是一款太空沙盒建造游戏，核心是把零件拼起来、起飞、坠毁、再重建得更好。这是你第一次起飞前需要知道的完整循环。",
        "sections": [
            {"heading": "核心循环：建造、坠毁、重建", "body": "官方描述把循环概括为三个词——建造、坠毁、重建。其余一切都由此展开。",
             "items": [
                ["从小做起", "用任何「能拼到能飞」的零件组装飞船。开局不需要完美设计——你需要的是能起飞的船。"],
                ["安装推进器与缆线", "巨型推进器让飞船动起来；缆线以及中间的各种零件把整艘船连在一起。一开始布局乱很正常。"],
                ["试飞", "起飞看看哪些部件撑得住。最初的飞行是实验，不是漂亮的航线。"],
                ["坠毁（这很正常）", "坠毁是循环的一部分。官方定位就是预期中的事——残骸是经验，不是失败。"],
                ["重建得更聪明", "用学到的经验重建。每次迭代都会告诉你哪些零件可靠、哪些组合能飞。"],
             ]},
            {"heading": "游戏官方承诺的内容", "body": "来自 Steam 官方描述：",
             "items": [
                "用完全模块化的飞船，在多人合作中探索新星球。",
                "安装巨型推进器、恼人的缆线，以及介于两者之间的一切。",
                "完成疯狂的任务，直面太空的危险。",
                "可以单人玩，也可以和队友一起——正如官方所说，还要和队友吵嘴。",
             ]},
            {"heading": "新手常见问题",
             "items": [
                ["Approximately Up 可以多人玩吗？", "可以——官方商店页标明支持单人 + 在线合作多人。"],
                ["需要懂工程学才能玩吗？", "不需要。游戏的核心就是试错：拼零件、起飞、坠毁、学习。"],
                ["有 Demo 吗？", "有——官方商店页列出了先于正式版（2026 年 8 月 6 日）推出的 Demo。"],
                ["能在 Steam Deck 上玩吗？", "兼容性尚未确认。Steam 论坛上已有玩家在问；在官方给出答复前，我们标为「待补」。"],
             ]},
            {"heading": "仍需核实的内容", "body": "具体星球名、任务名，以及蓝图、布线、雷达、时间倒流等机制细节，尚未与官方来源核实。我们会标注「待补」，并在官方信息可用后更新本页。"},
        ],
    },
    "ship-building-guide": {
        "title": "Approximately Up 飞船建造指南",
        "metaTitle": "Approximately Up 飞船建造指南：从第一艘船到大型建造",
        "metaDescription": "学会在 Approximately Up 中建造飞船：模块化的建造—坠毁—重建流程、推进器与缆线，以及登月、雷达等社区需求。",
        "intro": "飞船建造是《Approximately Up》的核心。官方定位很简单：把零件拼到能飞，然后重建得更聪明。本指南讲解流程，但不会编造尚未核实的零件数值。",
        "sections": [
            {"heading": "建造你的第一艘船", "body": "基于官方描述（模块化零件、推进器、缆线、建造—坠毁—重建），流程如下：",
             "items": [
                ["收集零件", "收集手头可用的零件并拼起来。官方说任何建造「能拼到能飞」就行——从这里开始。"],
                ["安装推进器", "装上推进器让飞船动起来。官方描述把「巨型推进器」作为核心玩法之一。"],
                ["布设缆线", "用缆线连接整艘船——「恼人的缆线」也是体验的一部分。布线乱很正常。"],
                ["试飞", "起飞。第一艘船不需要好看，它只需要教会你什么部件靠得住。"],
                ["坠毁并迭代", "用学到的经验重建。循环就是建造 → 坠毁 → 重建。"],
             ]},
            {"heading": "设计原则（对齐官方）",
             "items": [
                "完全模块化飞船：每次飞行之间都可以重新布置一切。",
                "平衡重量与推力——更重的船需要更大推力（具体数值待补）。",
                "多备零件：坠毁是意料之中的事。",
                "为合作预留空间：和队友玩就分工明确（驾驶员、建造师、工程师）。",
             ]},
            {"heading": "社区在求的教程",
             "items": [
                ["怎么去月球", "Steam 论坛真实帖——玩家想要登月教程。月球的具体机制待补。"],
                ["入门雷达监视器 / 设备", "Steam 论坛真实帖——玩家想要雷达设备教程。雷达机制待补。"],
             ]},
            {"heading": "仍待核实的内容", "body": "以上补丁说明已从 Steam 官方公告核实。预发布版本的细节和未公布的改动仍待核实。"}
        ],
    },
    "blueprints-guide": {
        "title": "Approximately Up 蓝图指南",
        "metaTitle": "Approximately Up 蓝图：下载、分享与使用",
        "metaDescription": "Approximately Up 蓝图：我们已知的查找与使用蓝图的信息、Steam 创意工坊支持，以及仍待核实的内容。",
        "intro": "蓝图是 Approximately Up 搜索量最高的话题之一。官方蓝图机制（导入、导出、分享）尚未核实，因此本页只写已确认内容并标注「待补」。",
        "sections": [
            {"heading": "蓝图细节：待补", "body": "蓝图导入、导出与分享机制在我们的待补清单上——尚未与官方来源核实。可靠信息确认后，本页会立即扩充。"},
            {"heading": "现在如何找飞船设计", "body": "虽然官方蓝图工具待补，但 Steam 创意工坊是已确认的社区内容所在地：",
             "items": [
                ["打开 Approximately Up 的 Steam 创意工坊", "社区上传的内容都在这里（商店页已确认支持创意工坊）。"],
                ["浏览飞船与建造", "找其他玩家分享的飞船设计。"],
                ["订阅", "订阅即可把内容保存到你的库中。"],
                ["到游戏里查看", "看看订阅内容在游戏内如何显示——具体步骤待补。"],
             ]},
            {"heading": "蓝图常见问题",
             "items": [
                ["能在 Approximately Up 里下载蓝图吗？", "待补。创意工坊内容是当前最接近已确认的渠道。"],
                ["能分享我的飞船设计吗？", "待补。确认后会补充确切的分享流程。"],
                ["蓝图和创意工坊物品是一回事吗？", "不一定——游戏内蓝图与创意工坊物品的关系待补。"],
             ]},
            {"heading": "值得关注的来源", "body": "我们会对照官方渠道（Steam 公告、官网、Discord）核实蓝图机制并更新本页。这里不会编造任何机制。"},
        ],
    },
    "wiring-electronics": {
        "title": "Approximately Up 布线与电路指南",
        "metaTitle": "Approximately Up 布线与电路：目前已知的信息",
        "metaDescription": "Approximately Up 的布线与电路：建造中的缆线、社区关于电子管时代与 Remapper 的问题——未核实内容已标注。",
        "intro": "布线与电路是社区的热门话题——但官方信息很少。本页汇总已核实内容与玩家在问的问题，未核实的都明确标注。",
        "sections": [
            {"heading": "官方信息有限", "body": "官方描述提到缆线是模块化建造的一部分（「恼人的缆线，以及介于两者之间的一切」），但详细的布线/电路机制尚未在我们知识库中核实，标注为「待补」。"},
            {"heading": "社区帖子（玩家的真实提问）",
             "items": [
                ["能不能别再停留在电子管时代的电子元件？", "Steam 论坛帖，在问电子元件的阶段/等级——暗示早期电子时代主题；具体机制待补。"],
                ["Remapper 里设置不了数值", "Steam 论坛帖，反映在 Remapper/Constant 里设置数值有问题——具体操作流程待补。"],
             ]},
            {"heading": "我们可以安全说的内容",
             "items": [
                "缆线是官方模块化飞船玩法的一部分。",
                "电子元件看起来是进阶方向（社区提到早期「电子管时代」）。",
                "游戏内存在参数/数值设置工具（Remapper），但具体用法未核实。",
             ]},
            {"heading": "布线与电路常见问题",
             "items": [
                ["Approximately Up 里布线怎么运作？", "待补。等官方或可靠交叉验证的信息出现后，我们会发布指南。"],
                ["电子元件分几个阶段？", "社区帖子提到「电子管时代」；具体阶段与解锁条件待补。"],
                ["为什么我在 Remapper 里设置不了数值？", "社区帖子反映了这个问题；官方流程待补。"],
             ]},
        ],
    },
    "controls": {
        "title": "Approximately Up 操作说明",
        "metaTitle": "Approximately Up 操作说明：键鼠与手柄支持状态",
        "metaDescription": "Approximately Up 操作指南：我们已知的键鼠信息、手柄支持与游戏内重映射——以及仍待核实的内容。",
        "intro": "手柄支持是发售后 Steam 社区问得最多的问题之一。这里写我们能确认的、玩家在问的，以及仍待核实的内容。",
        "sections": [
            {"heading": "我们已核实的信息",
             "items": [
                ["平台", "游戏在 PC（Steam）上。键盘鼠标是默认输入方式。"],
                ["手柄支持", "开发者尚未确认。Steam 论坛有帖子问「以后支持手柄吗？」，说明首发时完整手柄支持尚未确认。"],
                ["游戏内重映射器", "玩家在讨论 Remapper——社区帖子反映在其中设置数值有困难。确切的重映射流程标注为待补。"],
             ]},
            {"heading": "现在如何设置操作",
             "items": [
                "打开游戏内设置，查看输入/操作部分获取当前按键映射。",
                "用游戏内 Remapper 重绑按键；如果数值不生效，去 Steam 社区帖和开发者说明里查。",
                "想跟进手柄支持更新，关注官方 Discord 和 Steam 公告。",
             ]},
            {"heading": "待补：完整键位表", "body": "完整的官方键位映射（移动、视角、建造菜单、推进器控制）尚未与官方来源核实。我们标为「待补」，确认后发布表格。"},
            {"heading": "操作常见问题",
             "items": [
                ["Approximately Up 支持手柄吗？", "尚未确认。社区在问；在开发者或官方来源确认前，我们标为「待补」。"],
                ["可以重绑按键吗？", "有游戏内 Remapper。部分玩家反映设置数值有问题；确切流程待补。"],
                ["有 Steam Deck 操作布局吗？", "Steam Deck 兼容性本身在社区仍是开放问题——操作布局待补。"],
             ]},
        ],
    },
    "multiplayer": {
        "title": "Approximately Up 多人联机指南",
        "metaTitle": "Approximately Up 多人联机：合作、人数与跨平台",
        "metaDescription": "Approximately Up 多人联机详解：在线合作、最多几人、有没有异步多人——以及仍待核实的内容。",
        "intro": "《Approximately Up》官方定位是单人 + 在线合作游戏。本页回答玩家真正在问的联机问题，并标注尚未核实的内容。",
        "sections": [
            {"heading": "官方状态", "body": "Steam 官方商店页标明支持「单人」与「在线合作」两种模式。游戏的核心卖点就是一支队伍乘模块化飞船一起探索星球。"},
            {"heading": "多人联机常见问题",
             "items": [
                ["最多几个人一起玩？", "确切人数尚未在我们知识库中核实——标为「待补」。"],
                ["有在线合作吗？", "有——Steam 官方商店页列出在线合作多人。"],
                ["有跨平台联机吗？", "待补。游戏目前只有 PC（Steam）；主机版尚未公布，因此跨平台待补。"],
                ["有异步多人吗？", "未确认。Steam 论坛有帖子问「异步多人」，说明它可能还不是官方功能——标为「待补」。"],
                ["能单人玩吗？", "能——单人模式在支持列表里。"],
             ]},
            {"heading": "社区在问什么",
             "items": [
                "异步多人——玩家是否期待异步模式。",
                "人数/「几个人一起玩」是热门搜索需求；确认后会公布准确数字。",
             ]},
            {"heading": "仍待核实的内容", "body": "确切人数上限、邀请流程、主机细节与跨平台尚未与官方来源核实。确认后我们会立即更新本页。"},
        ],
    },
    "best-ship-designs": {
        "title": "Approximately Up 最佳飞船设计",
        "metaTitle": "Approximately Up 飞船创意与最佳设计",
        "metaDescription": "Approximately Up 飞船设计灵感：你自己的建造起点、社区设计问题，以及去哪找更多设计。",
        "intro": "找飞船创意？本页基于官方「建造—坠毁—重建」玩法整理设计起点，并汇总塑造玩家建造需求的社区问题。",
        "sections": [
            {"heading": "设计起点（灵感，非官方规格）",
             "items": [
                "推力狂魔速度型：装上巨型推进器，先接受操控性差一点。",
                "实用运输型：优先载货与任务部件而不是速度——任务需要运力（细节待补）。",
                "合作船员船：为一起探索星球的队伍留出空间。",
                "乱线风：拥抱「恼人的缆线」——布线也是魅力的一部分（布线机制待补）。",
             ]},
            {"heading": "社区设计问题",
             "items": [
                ["轨迹曲率仪表", "Steam 论坛关于轨迹工具的帖子——玩家想要更好的飞行工具；官方状态待补。"],
                ["能造多艘船的模组？", "Steam 论坛关于操控多艘船的帖子——待补。"],
             ]},
            {"heading": "去哪找更多设计",
             "items": [
                "Approximately Up 的 Steam 创意工坊（已确认支持）。",
                "官方 YouTube 频道上的预告片建造。",
                "Steam 社区讨论里的玩家截图与创意。",
             ]},
            {"heading": "仍待核实的内容", "body": "具体零件数值、具名设计的蓝图以及任何「最强」排行榜都未核实。本页只做灵感 + 已核实来源，其余标注「待补」。"},
        ],
    },
    "system-requirements": {
        "title": "Approximately Up 系统配置要求",
        "metaTitle": "Approximately Up 系统配置要求（PC）",
        "metaDescription": "Approximately Up PC 配置要求：最低/推荐配置尚未核实——这里写我们已知的信息与自查方法。",
        "intro": "玩家想要一个直接答案：自己的电脑能不能跑《Approximately Up》。官方最低与推荐配置在我们知识库中仍未核实，因此本页写已知信息与「待补」项。",
        "sections": [
            {"heading": "官方配置：待补", "body": "我们尚未从官方来源核实最低与推荐系统配置。与其编造数字，我们先把配置表标为「待补」，待官方确认（Steam 商店页或官网）后立即填写。"},
            {"heading": "配置表（待补）",
             "columns": ["项目", "最低配置", "推荐配置"],
             "rows": [
                ["操作系统", "待补", "待补"],
                ["处理器", "待补", "待补"],
                ["内存", "待补", "待补"],
                ["显卡", "待补", "待补"],
                ["存储空间", "待补", "待补"],
                ["DirectX", "待补", "待补"],
             ]},
            {"heading": "如何自查电脑",
             "items": [
                "打开 Steam 查看游戏商店页——系统要求发布后通常出现在那里。",
                "等我们发布官方数字后，对照你的 CPU/GPU/内存。",
                "Steam Deck：兼容性是社区开放问题（「Playable on Deck?」）；我们标为「待补」。",
             ]},
            {"heading": "配置常见问题",
             "items": [
                ["我的电脑能跑 Approximately Up 吗？", "目前无法确认——官方最低/推荐配置待补。开发者发布后去 Steam 商店页查看。"],
                ["Approximately Up 支持 Steam Deck 吗？", "未确认。Steam 论坛有帖子问「Playable on Deck?」——官方答复前兼容性待补。"],
                ["配置要求高吗？", "这是一款带模块化物理飞船的太空沙盒建造游戏；拿到核实数字后我们会第一时间发布。"],
             ]},
        ],
    },
    "console-release": {
        "title": "Approximately Up 主机版：PS5、Xbox 与 Switch 状态",
        "metaTitle": "Approximately Up 主机版发售日期（PS5、Xbox、Switch）",
        "metaDescription": "Approximately Up 会出 PS5、Xbox 或 Switch 版吗？目前没有官方公告——这里是主机版状态与官方新闻关注方式。",
        "intro": "「Approximately Up PS5 发售日期」「Xbox 版」「Switch 版」是游戏自己的 wiki 也没回答的搜索。今天诚实的答案是：没有核实的官方主机公告——这里是状态页。",
        "sections": [
            {"heading": "主机版状态（截至 2026-08-09）",
             "items": [
                ["当前平台", "仅 PC（Steam）。游戏于 2026 年 8 月 6 日在 Steam 发售。"],
                ["PS5", "待补——没有核实的 PlayStation 5 版官方公告。"],
                ["Xbox", "待补——没有核实的 Xbox 版官方公告。"],
                ["Nintendo Switch", "待补——没有核实的 Switch 版官方公告。"],
                ["官方声明", "我们尚未核实到开发者关于主机计划的官方声明；标为「待补」，一旦有就更新。"],
             ]},
            {"heading": "如何保持关注",
             "items": [
                "关注官网 approximatelyup.com 与官方 Discord（discord.gg/approximatelyup）。",
                "留意开发者 YouTube 频道（@ApproximatelyUp）与 TikTok（@approximatelyup）的公告。",
                "查看 Steam 商店页——主机消息通常会先在那里公布。",
             ]},
            {"heading": "主机版常见问题",
             "items": [
                ["Approximately Up 有 PS5 版吗？", "尚未公布——标为「待补」。目前没有核实的官方声明。"],
                ["Approximately Up 有 Xbox 版吗？", "尚未公布——待补。"],
                ["Approximately Up 有 Switch 版吗？", "尚未公布——待补。"],
                ["主机版什么时候发售？", "目前还没有日期。官方公告一经核实，本页立即更新。"],
             ]},
            {"heading": "为什么做这个页面", "body": "主机版是这款游戏搜索意图最高的问题之一，但没有任何可靠来源回答。本页给出已核实状态（仅 PC）并追踪未来公告，而不是编造一个日期。"},
        ],
    },
    "mods": {
        "title": "Approximately Up 模组指南",
        "metaTitle": "Approximately Up 模组：Steam 创意工坊、安装与模组问题",
        "metaDescription": "Approximately Up 模组详解：Steam 创意工坊支持、如何订阅模组，以及多船等社区模组问题。",
        "intro": "《Approximately Up》支持 Steam 创意工坊，查找与安装模组都很直接。这里写已确认的内容与玩家在求的东西。",
        "sections": [
            {"heading": "从 Steam 创意工坊获取模组", "body": "官方商店页已确认支持创意工坊。标准流程：",
             "items": [
                ["打开创意工坊", "在游戏的 Steam 商店页打开创意工坊标签（或访问创意工坊社区中心）。"],
                ["浏览并订阅", "找到喜欢的模组或物品，点订阅——Steam 会自动下载。"],
                ["启动游戏", "打开 Approximately Up，在游戏的模组/内容菜单里查看已订阅物品。"],
                ["启用想要的模组", "打开要用的模组。游戏内模组菜单的细节待补。"],
             ]},
            {"heading": "社区在问什么",
             "items": [
                "「能造多艘船的模组？」——Steam 论坛真实帖；通过模组支持多船尚未核实。",
                "很多游戏都有作弊引擎相关搜索；我们不提供作弊，只提供已核实的模组信息。",
             ]},
            {"heading": "模组常见问题",
             "items": [
                ["Approximately Up 支持模组吗？", "官方层面支持 Steam 创意工坊（见商店页）。完整模组文档待补。"],
                ["怎么安装模组？", "通过 Steam 创意工坊订阅；Steam 负责安装。游戏内步骤待补。"],
                ["模组能让我操控多艘船吗？", "社区有帖子在求；目前没有已核实的模组做到——待补。"],
             ]},
            {"heading": "仍待核实的内容", "body": "创意工坊的具体功能、模组规范，以及模组是否影响成就或多人，均未核实。官方文档确认后我们会更新本页。"},
        ],
    },
    "patch-notes": {
        "title": "Approximately Up 更新日志",
        "metaTitle": "Approximately Up 更新日志与版本历史",
        "metaDescription": "Approximately Up 更新日志与版本历史：发售信息、官方更新发布位置，以及我们跟踪的变更记录（未核实项已标注）。",
        "intro": "《Approximately Up》于 2026 年 8 月 6 日发售。本页跟踪官方补丁说明与更新——未核实内容都会明确标注。",
        "sections": [
            {"heading": "发售事实（已核实）",
             "items": [
                ["发售日", "2026 年 8 月 6 日（Steam 正式版）。"],
                ["Demo", "先于正式版推出的 Demo。"],
                ["价格", "发售时 $19.99（20% 折扣，原价 $24.99）。"],
             ]},
            {"heading": "更新时间线（已从 Steam 核实）", "body": "以下更新说明已从 Steam 官方公告核实（2026 年 8 月）：",
             "items": [
                ["2026-08-12", "1.0.010 — 修复了创意工坊「最热门」排序筛选、页面加载和结果缺失问题；优化了搜索清晰度。"],
                ["2026-08-11", "1.0.009 — 改进了 Frame Quarter With Ports（连接线缆后对面端口会同步出现，A–D 标签保持一致）；修复了 Middle Window、Small Switch 和 Small Button 的几何形状。"],
                ["2026-08-10", "1.0.008 — 修复了 Axis Rotometer 判定框及剩余问题；Plasma Cables 现在可涂色；Autohemisphere Solar Panels 在 Fly 模式后恢复原位；线缆支架可涂色。"],
                ["2026-08-09", "1.0.007 — 修复了 Metal 设备兼容性；修正了默认按键（「拾取组件」改为鼠标中键）；修复了管道描述错字；增加了更多提示。"],
                ["2026-08-08", "1.0.006 — 修复了 Fuse Box 无法重新开启；Axis Rotometer 现在输出正确的本地轴带符号数值；修复了 Large Disposable Battery 预览；增加了制作人员名单、启动画面和目标完成度追踪。"],
             ]},
            {"heading": "官方更新发布位置",
             "items": [
                "游戏的 Steam 公告（商店页的新闻流）。",
                "官网 approximatelyup.com 与官方 Discord。",
                "开发者 YouTube 频道的功能公告。",
             ]},
            {"heading": "仍待核实的内容", "body": "具体补丁内容（平衡调整、修复、新部件）未核实。我们宁可全部标「待补」也不猜测。"},
        ],
    },
    "demo-vs-full": {
        "title": "Approximately Up Demo 与正式版对比",
        "metaTitle": "Approximately Up Demo 与正式版：有什么区别？",
        "metaDescription": "Approximately Up Demo 与正式版对比：发售日期、价格、创意工坊与成就——以及仍待核实的内容差异。",
        "intro": "《Approximately Up》的 Demo 先于 2026 年 8 月 6 日的正式版推出。这里给出已核实的对比，内容差异部分明确标注「待补」。",
        "sections": [
            {"heading": "已核实的对比",
             "columns": ["项目", "Demo", "正式版"],
             "rows": [
                ["可用性", "Demo（据商店页更早推出）", "2026 年 8 月 6 日正式发售"],
                ["价格", "待补", "$19.99（20% 首发折扣，原价 $24.99）"],
                ["Steam 创意工坊", "待补", "支持（据商店页）"],
                ["成就", "待补", "22 项 Steam 成就（据商店页）"],
                ["合作多人", "待补", "单人 + 在线合作（据商店页）"],
             ]},
            {"heading": "Demo 与正式版常见问题",
             "items": [
                ["Demo 免费吗？", "Demo 的价格/模式尚未核实——待补。"],
                ["Demo 进度能继承到正式版吗？", "待补。"],
                ["哪些内容只在正式版里？", "待补——官方对比细节尚未公布。据商店页，正式版包含创意工坊支持与 22 项成就。"],
                ["该先试试 Demo 吗？", "对多数太空沙盒建造游戏来说，先玩 Demo 能感受「建造—坠毁—重建」循环再决定买不买——但 Demo 的具体内容范围待补。"],
             ]},
            {"heading": "仍待核实的内容", "body": "Demo 的确切内容、进度转移与功能差异尚未与官方来源核实。确认后我们会更新此表。"},
        ],
    },
    "achievements-list": {
        "title": "Approximately Up 成就列表",
        "metaTitle": "Approximately Up 成就：完整列表（22 项）",
        "metaDescription": "Approximately Up 有 22 项 Steam 成就。完整名称列表仍在核实中——这里写已确认的内容。",
        "intro": "Steam 官方商店页确认有 22 项成就。确切名称与解锁条件尚未在我们知识库中核实，因此本页跟踪已确认数量，并把列表标为「待补」。",
        "sections": [
            {"heading": "已确认：22 项成就", "body": "Steam 商店页列出 Approximately Up 有 22 项成就。我们尚未核实每项成就的名称、图标与解锁条件——这一部分待补。"},
            {"heading": "成就列表（待补）",
             "columns": ["成就", "解锁条件"],
             "rows": [
                ["成就 1–22", "待补——名称与条件正在对照官方列表核实。"],
             ]},
            {"heading": "如何跟踪成就进度",
             "items": [
                "游戏内用 Steam 浮层查看进度。",
                "关注 Steam 官方公告——成就列表有时随补丁说明发布。",
                "核实后我们会在这里发布完整列表。",
             ]},
            {"heading": "成就常见问题",
             "items": [
                ["Approximately Up 有多少项成就？", "22 项，已在 Steam 官方商店页确认。"],
                ["成就名称是什么？", "待补——我们正在核实官方列表，确认后发布。"],
                ["单人模式能拿全成就吗？", "待补——部分可能要求合作，列表确认前无法确定。"],
             ]},
        ],
    },
    "ships": {
        "title": "Approximately Up 飞船",
        "metaTitle": "Approximately Up 飞船：建造、创意与设计",
        "metaDescription": "Approximately Up 飞船内容索引：建造指南、飞船设计、蓝图与模块化建造基础。",
        "intro": "关于 Approximately Up 飞船的一切都在这——从你的第一艘船到社区设计创意。",
        "sections": [
            {"heading": "飞船指南",
             "items": [
                "飞船建造指南——学会「建造—坠毁—重建」流程。",
                "最佳飞船设计——设计起点与社区创意。",
                "蓝图指南——我们已知的蓝图与创意工坊内容。",
                "模组——创意工坊支持与模组问题。",
             ]},
            {"heading": "飞船常见问题",
             "items": [
                ["能造什么样的飞船？", "飞船完全模块化——怎么拼都行（官方描述）。具体零件清单待补。"],
                ["能飞到月球吗？", "社区有帖子在问怎么去；月球机制待补。"],
                ["能操控多艘飞船吗？", "社区有帖子在问；待补。"],
             ]},
        ],
    },
    "blueprints": {
        "title": "Approximately Up 蓝图",
        "metaTitle": "Approximately Up 蓝图：下载与图库",
        "metaDescription": "Approximately Up 蓝图内容索引：如何使用蓝图、去哪找飞船设计，以及 Steam 创意工坊。",
        "intro": "蓝图库索引——找飞船设计、了解（待补的）蓝图流程，并浏览创意工坊。",
        "sections": [
            {"heading": "蓝图内容",
             "items": [
                "蓝图指南——蓝图方面已确认与待补的内容。",
                "最佳飞船设计——设计创意与更多来源。",
                "Steam 创意工坊——社区内容的已确认阵地。",
             ]},
            {"heading": "蓝图索引常见问题",
             "items": [
                ["在哪下载蓝图？", "Steam 创意工坊是已确认的社区内容渠道；游戏内蓝图下载机制待补。"],
                ["怎么导入蓝图？", "待补。"],
                ["能分享我的设计吗？", "待补。"],
             ]},
        ],
    },
    "guides": {
        "title": "Approximately Up 攻略",
        "metaTitle": "Approximately Up 攻略：全部页面",
        "metaDescription": "Approximately Up 全攻略索引：怎么玩、飞船建造、操作、多人联机、模组、成就等。",
        "intro": "Approximately Up 完整攻略索引。每一页回答一个玩家真正搜索的问题，未核实的都会标注。",
        "sections": [
            {"heading": "全部攻略",
             "items": [
                "怎么玩——新手必看的「建造—坠毁—重建」循环。",
                "操作说明——键鼠、手柄状态与重映射笔记。",
                "系统配置要求——配置状态与自查方法。",
                "多人联机——在线合作、人数与异步问题。",
                "主机版——PS5/Xbox/Switch 状态。",
                "模组——Steam 创意工坊与模组问题。",
                "更新日志——发售事实与更新跟踪。",
                "Demo 与正式版——已核实的对比。",
                "飞船建造指南——从第一艘船到大型建造。",
                "布线与电路——已知内容与待补内容。",
                "蓝图指南——蓝图状态与创意工坊。",
                "最佳飞船设计——创意与社区设计。",
                "成就列表——22 项成就，列表待补。",
                "飞船 / 蓝图 / 成就——索引页。",
             ]},
            {"heading": "我们的工作方式", "body": "每页列出 1–2 个可靠来源，未核实的都标「待补」。我们不会编造数字、名称或机制。"},
        ],
    },
    "achievements": {
        "title": "Approximately Up 成就",
        "metaTitle": "Approximately Up 成就：总览",
        "metaDescription": "Approximately Up 成就总览：已确认 22 项 Steam 成就、列表核实中，以及如何跟踪进度。",
        "intro": "Approximately Up 的成就中心——已确认数量、当前列表状态，以及完整跟踪页链接。",
        "sections": [
            {"heading": "已确认 22 项成就", "body": "Steam 商店页确认有 22 项成就。完整名称与条件列表待补。"},
            {"heading": "成就内容",
             "items": [
                "成就列表——完整（待补）列表的专属页面。",
                "Steam——查看商店页的成就板块。",
             ]},
            {"heading": "成就总览常见问题",
             "items": [
                ["有多少项成就？", "22 项（Steam 商店页已确认）。"],
                ["完整列表在哪？", "待补——我们正在核实官方列表。"],
             ]},
        ],
    },
}

TR_JA = {
    "how-to-play": {
        "title": "Approximately Up の遊び方：初心者ガイド",
        "metaTitle": "Approximately Up の遊び方：完全初心者ガイド",
        "metaDescription": "Approximately Up を始めたばかりの方へ。「作って、墜ちて、作り直す」ループ、モジュラー宇宙船、協力マルチ、惑星探索を解説する初心者ガイド。",
        "intro": "『Approximately Up』は、部品を組み合わせ、飛ばし、墜ちて、より良く作り直す宇宙サンドボックス建造ゲーム。初めて飛ばす前に知っておきたいコアループを解説します。",
        "sections": [
            {"heading": "コアループ：作って、墜ちて、作り直す", "body": "公式説明はループを三つの言葉に要約しています——作る、墜ちる、作り直す。すべてはここから始まります。",
             "items": [
                ["小さく始める", "飛ぶのに十分なだけ繋ぎ合わせた部品で船を組む。完璧な設計は不要——浮き上がるものが最初の一歩。"],
                ["スラスターとケーブルを取り付ける", "巨大スラスターで動きを作り、ケーブルとその間のすべての部品で船をつなぐ。最初は乱雑で当然。"],
                ["テスト飛行", "飛ばして何が持つかを見る。最初の飛行は実験であり、華麗なフライトではない。"],
                ["墜ちる（それでいい）", "墜落はループの一部。公式の売り文句もそれを前提にしています——残骸は失敗ではなく教訓。"],
                ["賢く作り直す", "学んだことを生かして再建造。繰り返すほど、どの部品が持ち、どの組み合わせが飛ぶか分かる。"],
             ]},
            {"heading": "公式が約束している内容", "body": "Steam 公式説明より：",
             "items": [
                "完全モジュラー式の宇宙船で、協力マルチプレイで新しい惑星を探索。",
                "巨大スラスター、鬱陶しいケーブル、その間にあるすべてを取り付ける。",
                "ワイルドなミッションを完了し、宇宙の危険に立ち向かう。",
                "ソロでもクルーとでもプレイ可能——公式の言う通り、クルーと言い争うのも一興。",
             ]},
            {"heading": "初心者 FAQ",
             "items": [
                ["Approximately Up はマルチプレイ対応？", "はい——公式ストアはシングルプレイ＋オンライン協力マルチを掲載しています。"],
                ["工学知識は必要？", "不要。試行錯誤が本質：部品を付け、飛ばし、墜ち、学ぶ。"],
                ["デモはある？", "あります——公式ストアに正式版（2026年8月6日）より前のデモが掲載されています。"],
                ["Steam Deck で遊べる？", "互換性は未確認。Steam フォーラムでも質問が出ています。公式回答までは「未検証」とします。"],
             ]},
            {"heading": "今後検証が必要な内容", "body": "具体的な惑星名・ミッション名、および設計図・配線・レーダー・タイムリワインドなどの詳細メカニクスは未検証。明記した上で、公式情報が入り次第更新します。"},
        ],
    },
    "ship-building-guide": {
        "title": "Approximately Up 宇宙船建造ガイド",
        "metaTitle": "Approximately Up 宇宙船建造ガイド：最初の船から大型建造まで",
        "metaDescription": "Approximately Up での宇宙船の作り方：モジュール式の「作る→墜ちる→作り直す」流れ、スラスターとケーブル、月やレーダーなどのコミュニティニーズ。",
        "intro": "宇宙船建造は『Approximately Up』の核心。公式の売り文句はシンプルです：部品を飛ぶまで繋ぎ、賢く作り直す。本ガイドは未検証の部品性能を捏造せずに手順を解説します。",
        "sections": [
            {"heading": "最初の宇宙船を作る", "body": "公式説明（モジュール部品・スラスター・ケーブル・作る→墜ちる→作り直す）に基づく手順：",
             "items": [
                ["部品を集める", "手に入る部品を集めて繋ぎ合わせる。公式は「飛ぶのに十分なだけ繋がる」船を出発点にしています。"],
                ["スラスターを付ける", "動き出すためにスラスターを取り付ける。公式説明は「巨大スラスター」を核の魅力としています。"],
                ["ケーブルを配線する", "ケーブルで船をつなぐ——「鬱陶しいケーブル」も体験の一部。配線が汚くても大丈夫。"],
                ["テスト飛行", "飛ばす。最初の船は美しくなくていい。何が持つかを教えてくれれば十分。"],
                ["墜ちて反復する", "学んだことを生かして作り直す。ループは「作る→墜ちる→作り直す」。"],
             ]},
            {"heading": "設計の原則（公式に沿う）",
             "items": [
                "完全モジュール式：飛行のたびにすべてを組み直せる。",
                "重量と推力を天秤に——重い船にはより大きな推力が必要（具体的数値は未検証）。",
                "予備パーツを確保：墜落は想定内。",
                "協力プレイを想定：クルーと遊ぶなら役割（操縦・建造・エンジニア）を決める。",
             ]},
            {"heading": "コミュニティが求めているチュートリアル",
             "items": [
                ["月へはどう行く？", "Steam フォーラムの実在スレッド——月旅行ガイドを求めています。月の具体的メカニクスは未検証。"],
                ["初心者向けレーダーモニター／デバイス", "Steam フォーラムの実在スレッド——レーダー装置のチュートリアルを求めています。レーダー機構は未検証。"],
             ]},
            {"heading": "まだ未検証の内容", "body": "上記のパッチノートは Steam 公式アナウンスで検証済みです。リリース前ビルドの詳細と未発表の変更は未検証のままです。"}
        ],
    },
    "blueprints-guide": {
        "title": "Approximately Up 設計図ガイド",
        "metaTitle": "Approximately Up 設計図の使い方：DL・共有・活用",
        "metaDescription": "Approximately Up の設計図：見つけ方・使い方で分かっていること、Steam ワークショップ対応、そして未検証の内容。",
        "intro": "設計図は Approximately Up で最も検索される話題の一つ。公式の設計図機構（インポート・エクスポート・共有）は未検証なので、本ページは確認済みの内容と「未検証」を示します。",
        "sections": [
            {"heading": "設計図の詳細：未検証", "body": "設計図のインポート・エクスポート・共有の仕組みは未検証リストにあります——公式ソースで確認できていません。信頼できる情報が確認され次第、本ページを拡充します。"},
            {"heading": "今すぐ船の設計を探す方法", "body": "公式の設計図ツールは未検証ですが、Steam ワークショップは確認済みのコミュニティコンテンツの置き場です：",
             "items": [
                ["Approximately Up の Steam ワークショップを開く", "コミュニティ投稿のコンテンツはここにあります（ストアでワークショップ対応を確認済み）。"],
                ["船や建造物を閲覧", "他のプレイヤーが共有した船の設計を探す。"],
                ["購読する", "購読するとライブラリに保存される。"],
                ["ゲーム内で確認", "購読アイテムがゲーム内でどう表示されるか——正確な手順は未検証。"],
             ]},
            {"heading": "設計図 FAQ",
             "items": [
                ["Approximately Up で設計図をダウンロードできる？", "未検証。現在、最も確認に近いチャネルはワークショップのコンテンツ。"],
                ["自分の船の設計を共有できる？", "未検証。正確な共有手順は確認後に追記します。"],
                ["設計図とワークショップアイテムは同じ？", "同じとは限りません——ゲーム内設計図とワークショップアイテムの関係は未検証。"],
             ]},
            {"heading": "注目すべき情報源", "body": "設計図の仕組みは公式チャネル（Steam アナウンス・公式サイト・Discord）で確認し、本ページを更新します。ここでは機構を捏造しません。"},
        ],
    },
    "wiring-electronics": {
        "title": "Approximately Up 配線・電子機器ガイド",
        "metaTitle": "Approximately Up 配線・電子機器：現在わかっていること",
        "metaDescription": "Approximately Up の配線と電子機器：建造のケーブル、真空管時代と Remapper に関するコミュニティの質問——未検証の内容も明記。",
        "intro": "配線と電子機器はコミュニティの大きな話題ですが、公式情報は薄い。本ページは検証済みの内容とプレイヤーの質問をまとめ、未検証のものを明確に示します。",
        "sections": [
            {"heading": "公式情報は限定的", "body": "公式説明はケーブルをモジュール建造の一部として言及していますが（「鬱陶しいケーブル、その間にあるすべて」）、配線・回路の詳細機構は未検証です。未検証と明記します。"},
            {"heading": "コミュニティのスレッド（プレイヤーの実質問）",
             "items": [
                ["電子機器の真空管時代から進めませんか？", "部品の電子機器の段階／時代を問う Steam フォーラムのスレッド——初期の電子機器テーマを示唆。正確な機構は未検証。"],
                ["Remapper で値を設定できない", "Remapper／Constant で値を設定できないという Steam フォーラムのスレッド——正確な手順は未検証。"],
             ]},
            {"heading": "安全に言えること",
             "items": [
                "ケーブルはモジュール式宇宙船建造の公式な一部。",
                "電子機器は成長領域のように見える（コミュニティは初期の「真空管時代」に言及）。",
                "ゲーム内にパラメータ／値設定ツール（Remapper）は存在するが、正確な使い方は未検証。",
             ]},
            {"heading": "配線・電子機器 FAQ",
             "items": [
                ["Approximately Up の配線はどう機能する？", "未検証。公式または信頼できる相互検証情報が出たらガイドを公開します。"],
                ["電子機器の段階は？", "コミュニティスレッドは「真空管時代」に言及。正確な段階と解放条件は未検証。"],
                ["Remapper で値が設定できないのはなぜ？", "コミュニティスレッドで報告されています。公式の手順は未検証。"],
             ]},
        ],
    },
    "controls": {
        "title": "Approximately Up 操作",
        "metaTitle": "Approximately Up 操作：キーボード・マウス・コントローラー対応状況",
        "metaDescription": "Approximately Up 操作ガイド：キーボード・マウスの既知情報、コントローラー対応、ゲーム内リマッパー——未検証の内容も含む。",
        "intro": "コントローラー対応は発売直後、Steam コミュニティで最も質問が多い話題の一つ。確認できること、プレイヤーの質問、未検証の内容をまとめます。",
        "sections": [
            {"heading": "確認済みの情報",
             "items": [
                ["プラットフォーム", "ゲームは PC（Steam）。キーボード＋マウスが標準入力。"],
                ["コントローラー対応", "開発者は未確認。Steam フォーラムに「今後のコントローラー対応は？」というスレッドがあり、発売時点での完全対応は未確認と示唆。"],
                ["ゲーム内リマッパー", "プレイヤーが Remapper を話題に——値の設定に問題があるとのスレッドあり。正確なマッピング手順は未検証。"],
             ]},
            {"heading": "今すぐ操作を設定する方法",
             "items": [
                "ゲーム内設定を開き、入力／操作セクションで現在のキーマッピングを確認する。",
                "ゲーム内 Remapper でキーを再割り当て。値が反映されない場合は Steam コミュニティスレッドと開発者ノートを確認。",
                "コントローラー対応の更新は公式 Discord と Steam アナウンスをフォロー。",
             ]},
            {"heading": "未検証：完全なキーマップ", "body": "完全な公式キーマッピング（移動・カメラ・建造メニュー・スラスター操作）は公式ソースで未確認。未検証とし、確認次第表を公開します。"},
            {"heading": "操作 FAQ",
             "items": [
                ["Approximately Up はコントローラー対応？", "まだ未確認。コミュニティが質問中。開発者または公式ソースが確認するまで未検証とします。"],
                ["キーを再割り当てできる？", "ゲーム内 Remapper あり。値の設定に問題があるとの報告も。正確な手順は未検証。"],
                ["Steam Deck 用の操作レイアウトは？", "Steam Deck 互換性自体がコミュニティで未解決——操作レイアウトも未検証。"],
             ]},
        ],
    },
    "multiplayer": {
        "title": "Approximately Up マルチプレイガイド",
        "metaTitle": "Approximately Up マルチプレイ：協力・人数・クロスプレイ",
        "metaDescription": "Approximately Up のマルチプレイを解説：オンライン協力、人数、非同期マルチの有無、そして未検証の内容。",
        "intro": "『Approximately Up』は公式にシングルプレイ＋オンライン協力のゲーム。本ページはプレイヤーが実際に尋ねるマルチプレイの質問に答え、検証できない部分を明記します。",
        "sections": [
            {"heading": "公式ステータス", "body": "Steam 公式ストアは「シングルプレイ」と「オンライン協力」を対応モードとして記載。ゲームの売りは、クルーがモジュール船で一緒に惑星を探索することです。"},
            {"heading": "マルチプレイ FAQ",
             "items": [
                ["何人まで一緒にプレイできる？", "正確な人数は知識ベースで未確認——「未検証」とします。"],
                ["オンライン協力はある？", "あります——Steam 公式ストアにオンライン協力マルチが記載。"],
                ["クロスプラットフォームは？", "未検証。現在は PC（Steam）のみ。コンソール版も未発表のため、クロスプレイは未検証。"],
                ["非同期マルチはある？", "未確認。Steam フォーラムに「非同期マルチプレイ」を問うスレッドがあり、公式機能ではない可能性——未検証とします。"],
                ["ソロで遊べる？", "できます——シングルプレイが対応モードとして記載。"],
             ]},
            {"heading": "コミュニティの質問",
             "items": [
                "非同期マルチ——非同期モードを期待しているか。",
                "人数／「何人まで」は上位の検索ニーズ。確認でき次第、検証済みの数字を公開します。",
             ]},
            {"heading": "まだ未検証の内容", "body": "正確な人数上限・招待の流れ・ホストの詳細・クロスプレイは公式ソースで未確認。確認され次第、本ページを更新します。"},
        ],
    },
    "best-ship-designs": {
        "title": "Approximately Up 最強の宇宙船デザイン",
        "metaTitle": "Approximately Up 宇宙船のアイデアとベストデザイン",
        "metaDescription": "Approximately Up の宇宙船デザインのアイデア：自作の出発点、コミュニティの設計質問、さらにデザインを探す場所。",
        "intro": "宇宙船のアイデアを探していますか？ 本ページは公式の「作る→墜ちる→作り直す」に基づく設計の出発点と、プレイヤーが作りたいものを形作るコミュニティ質問をまとめます。",
        "sections": [
            {"heading": "設計の出発点（インスピレーションであり、公式仕様ではない）",
             "items": [
                "推力特化スピードスター：巨大スラスターを載せ、操縦性は後回し。",
                "実用輸送型：速度より貨物とミッション部品——ミッションには容量が必要（詳細は未検証）。",
                "協力クルー船：一緒に惑星を探索するクルーのための空間を設計。",
                "乱雑ケーブル建造：「鬱陶しいケーブル」を受け入れる——配線も魅力の一部（配線機構は未検証）。",
             ]},
            {"heading": "コミュニティの設計質問",
             "items": [
                ["軌道曲率メーター", "軌道ツールに関する Steam フォーラムのスレッド——より良い飛行ツールを求める声。公式ステータスは未検証。"],
                ["複数の船を作る Mod？", "複数の船を操作したいという Steam フォーラムのスレッド——未検証。"],
             ]},
            {"heading": "さらにデザインを探す場所",
             "items": [
                "Approximately Up の Steam ワークショップ（対応確認済み）。",
                "公式 YouTube チャンネルのトレーラー内の船。",
                "Steam コミュニティ討論でのプレイヤーのスクリーンショットやアイデア。",
             ]},
            {"heading": "まだ未検証の内容", "body": "具体的な部品性能・名称付き設計の設計図・「最強」ランキングは未検証。本ページはインスピレーション＋検証済みソースに留め、他は未検証とします。"},
        ],
    },
    "system-requirements": {
        "title": "Approximately Up 動作環境",
        "metaTitle": "Approximately Up 動作環境（PC）",
        "metaDescription": "Approximately Up の PC 動作環境：最低／推奨スペックは未検証——わかっていることと互換性の確認方法。",
        "intro": "プレイヤーは自分の PC で動くかどうかの明確な答えを求めています。公式の最低・推奨スペックは未検証のため、本ページは判明していることと「未検証」を明記します。",
        "sections": [
            {"heading": "公式スペック：未検証", "body": "公式の最低・推奨システム要件を公式ソースで確認できていません。数値を捏造せず、スペック表は「未検証」とし、確認（Steam ストアまたは公式サイト）次第すぐ埋めます。"},
            {"heading": "スペック表（未検証）",
             "columns": ["項目", "最低", "推奨"],
             "rows": [
                ["OS", "未検証", "未検証"],
                ["CPU", "未検証", "未検証"],
                ["メモリ", "未検証", "未検証"],
                ["GPU", "未検証", "未検証"],
                ["ストレージ", "未検証", "未検証"],
                ["DirectX", "未検証", "未検証"],
             ]},
            {"heading": "自分の PC を確認する方法",
             "items": [
                "Steam でゲームのストアページを開く——公開されれば通常ここに動作環境が表示されます。",
                "公開後に、公式数値と自分の CPU／GPU／RAM を比較する。",
                "Steam Deck：互換性はコミュニティの未解決質問（「Playable on Deck?」）——未検証とします。",
             ]},
            {"heading": "動作環境 FAQ",
             "items": [
                ["私の PC で動く？", "現時点では確認不可——公式の最低／推奨スペックは未検証。開発者が公開したらストアページで確認を。"],
                ["Steam Deck 対応？", "未確認。Steam フォーラムに「Playable on Deck?」というスレッドあり——公式回答まで未検証。"],
                ["要求は高い？", "モジュール式物理船の宇宙サンドボックス建造ゲーム。検証済みの数値が入り次第報告します。"],
             ]},
        ],
    },
    "console-release": {
        "title": "Approximately Up コンソール版：PS5・Xbox・Switch の状況",
        "metaTitle": "Approximately Up コンソール版発売日（PS5・Xbox・Switch）",
        "metaDescription": "Approximately Up は PS5・Xbox・Switch に出る？ まだ公式発表なし——コンソール版の状況と公式ニュースの追い方を紹介。",
        "intro": "「Approximately Up PS5 発売日」「Xbox 版」「Switch 版」は、ゲーム自身の wiki も答えていない検索。今日の正直な答え：検証済みの公式コンソール発表はなし——ここがステータスページです。",
        "sections": [
            {"heading": "コンソール版の状況（2026-08-09 現在）",
             "items": [
                ["現在のプラットフォーム", "PC（Steam）のみ。2026年8月6日に Steam でリリース。"],
                ["PS5", "未検証——PlayStation 5 版の検証済み公式発表なし。"],
                ["Xbox", "未検証——Xbox 版の検証済み公式発表なし。"],
                ["Nintendo Switch", "未検証——Switch 版の検証済み公式発表なし。"],
                ["公式声明", "コンソール計画に関する開発者の公式声明は未確認——未検証とし、出次第更新。"],
             ]},
            {"heading": "情報を追う方法",
             "items": [
                "公式サイト approximatelyup.com と公式 Discord（discord.gg/approximatelyup）をフォロー。",
                "開発者の YouTube チャンネル（@ApproximatelyUp）と TikTok（@approximatelyup）で発表をチェック。",
                "Steam ストアページを確認——コンソール情報はたいてい最初にここで発表されます。",
             ]},
            {"heading": "コンソール版 FAQ",
             "items": [
                ["PS5 版は出る？", "未発表——未検証とします。検証済みの公式声明はまだありません。"],
                ["Xbox 版は出る？", "未発表——未検証。"],
                ["Switch 版は出る？", "未発表——未検証。"],
                ["コンソール版の発売日は？", "まだ日付はありません。公式発表が検証された時点で本ページを更新します。"],
             ]},
            {"heading": "このページがある理由", "body": "コンソール版はこのゲームで検索意図が最も高い質問の一つですが、信頼できる情報源は答えていません。本ページは検証済みステータス（PC のみ）を示し、日付を捏造せずに今後の発表を追跡します。"},
        ],
    },
    "mods": {
        "title": "Approximately Up Mod ガイド",
        "metaTitle": "Approximately Up Mod：Steam ワークショップ・導入・Mod の疑問",
        "metaDescription": "Approximately Up の Mod を解説：Steam ワークショップ対応、Mod の購読方法、複数船などのコミュニティの Mod 質問。",
        "intro": "『Approximately Up』は Steam ワークショップに対応しており、Mod の検索と導入は簡単です。ここでは確認済みの内容とプレイヤーが求めているものを紹介します。",
        "sections": [
            {"heading": "Steam ワークショップから Mod を入手", "body": "ワークショップ対応は公式ストアで確認済み。標準的な流れ：",
             "items": [
                ["ワークショップを開く", "ゲームの Steam ストアページからワークショップタブを開く（またはワークショップコミュニティハブへ）。"],
                ["閲覧して購読", "気に入った Mod やアイテムを見つけて「購読」——Steam が自動でダウンロード。"],
                ["ゲームを起動", "Approximately Up を開き、ゲーム内の Mod／コンテンツメニューで購読アイテムを確認。"],
                ["使いたいものを有効化", "使いたい Mod をオンに。ゲーム内 Mod メニューの詳細は未検証。"],
             ]},
            {"heading": "コミュニティの質問",
             "items": [
                "「複数の船を作る Mod？」——Steam フォーラムの実在スレッド。Mod による複数船対応は未検証。",
                "多くのゲームに cheat engine 関連の検索がありますが、当サイトはチートを提供せず検証済みの Mod 情報のみ扱います。",
             ]},
            {"heading": "Mod FAQ",
             "items": [
                ["Approximately Up は Mod 対応？", "公式には Steam ワークショップ対応（ストアページ）。完全な Mod ドキュメントは未検証。"],
                ["Mod の入れ方は？", "Steam ワークショップで購読——導入は Steam が処理。ゲーム内手順は未検証。"],
                ["Mod で複数の船を操作できる？", "コミュニティスレッドで要望あり。検証済みの Mod はまだなし——未検証。"],
             ]},
            {"heading": "まだ未検証の内容", "body": "ワークショップの正確な機能・Mod ガイドライン・Mod が実績やマルチに影響するかは未検証。公式ドキュメント確認後に本ページを更新します。"},
        ],
    },
    "patch-notes": {
        "title": "Approximately Up パッチノート",
        "metaTitle": "Approximately Up パッチノートとアップデート履歴",
        "metaDescription": "Approximately Up のパッチノートと更新履歴：発売情報、公式アップデートの掲載場所、追跡中の変更履歴（未検証は明記）。",
        "intro": "『Approximately Up』は2026年8月6日にリリース。本ページは公式パッチノートとアップデートを追跡し、未検証のものは明確に示します。",
        "sections": [
            {"heading": "発売の事実（検証済み）",
             "items": [
                ["リリース日", "2026年8月6日（Steam 正式版）。"],
                ["デモ", "正式版より前にデモが公開。"],
                ["価格", "発売時 $19.99（20% オフ、通常 $24.99）。"],
             ]},
            {"heading": "アップデートのタイムライン（Steam で検証済み）", "body": "以下の更新情報は Steam 公式アナウンスで確認済み（2026年8月）：",
             "items": [
                ["2026-08-12", "1.0.010 — ワークショップの「人気順」ソートフィルター、ページ読み込み、結果欠落を修正。検索の分かりやすさを改善。"],
                ["2026-08-11", "1.0.009 — Frame Quarter With Ports を改善（ケーブル接続で反対側にもポートが反映、A–D ラベルも一致）。Middle Window、Small Switch、Small Button の形状を修正。"],
                ["2026-08-10", "1.0.008 — Axis Rotometer の当たり判定と残りの問題を修正。Plasma Cables が塗装可能に。Autohemisphere Solar Panels が Fly モード後に元の位置へ。ケーブルホルダーの塗装に対応。"],
                ["2026-08-09", "1.0.007 — Metal デバイスとの互換性を修正。デフォルトキーバインドを修正（「部品を拾う」をマウス中ボタンに）。パイプ説明の誤字を修正。ヒントを追加。"],
                ["2026-08-08", "1.0.006 — Fuse Box が再びオンにできない問題を修正。Axis Rotometer がローカル軸の符号付き値を出力するよう修正。Large Disposable Battery のプレビューを修正。クレジット、起動画面、目標達成率トラッキングを追加。"],
             ]},
            {"heading": "公式アップデートの掲載場所",
             "items": [
                "ゲームの Steam アナウンス（ストアページのニュースフィード）。",
                "公式サイト approximatelyup.com と公式 Discord。",
                "開発者 YouTube チャンネルの機能発表。",
             ]},
            {"heading": "まだ未検証の内容", "body": "具体的なパッチ内容（バランス調整・修正・新パーツ）は未検証。推測せず、すべて未検証とします。"},
        ],
    },
    "demo-vs-full": {
        "title": "Approximately Up デモと製品版の比較",
        "metaTitle": "Approximately Up デモと製品版：違いは？",
        "metaDescription": "Approximately Up のデモと製品版を比較：リリース日・価格・ワークショップ・実績——そして未検証の内容差。",
        "intro": "『Approximately Up』のデモは2026年8月6日の製品版より先に公開されました。検証済みの比較を示し、内容差は明確に「未検証」とします。",
        "sections": [
            {"heading": "検証済みの比較",
             "columns": ["項目", "デモ", "製品版"],
             "rows": [
                ["入手方法", "デモ（ストア記載どおり先に公開）", "2026年8月6日正式リリース"],
                ["価格", "未検証", "$19.99（ローンチ20%オフ、通常 $24.99）"],
                ["Steam ワークショップ", "未検証", "対応（ストア記載）"],
                ["実績", "未検証", "Steam 実績22個（ストア記載）"],
                ["協力マルチ", "未検証", "シングル＋オンライン協力（ストア記載）"],
             ]},
            {"heading": "デモと製品版 FAQ",
             "items": [
                ["デモは無料？", "デモの価格・形態は未確認——未検証。"],
                ["デモの進行は製品版に引き継がれる？", "未検証。"],
                ["製品版だけのコンテンツは？", "未検証——公式比較の詳細は未発表。ストア記載どおり、製品版にはワークショップ対応と22実績があります。"],
                ["先にデモを試すべき？", "多くの宇宙サンドボックス建造ゲームでは、購入前に「作る→墜ちる→作り直す」を体感できるデモがおすすめ——ただしデモの正確な範囲は未検証。"],
             ]},
            {"heading": "まだ未検証の内容", "body": "デモの正確な内容・進行の引き継ぎ・機能差は公式ソースで未確認。確認され次第、この表を更新します。"},
        ],
    },
    "achievements-list": {
        "title": "Approximately Up 実績リスト",
        "metaTitle": "Approximately Up 実績：完全リスト（22個）",
        "metaDescription": "Approximately Up には Steam 実績が22個。名称の完全リストは検証中——確認済みの内容をここに示します。",
        "intro": "Steam 公式ストアは実績22個を確認。正確な名称と解放条件は未検証のため、本ページは確認済みの数と「未検証」を示します。",
        "sections": [
            {"heading": "確認済み：実績22個", "body": "Steam ストアは Approximately Up の実績を22個と記載。各実績の名称・アイコン・解放条件は未確認——その部分は未検証です。"},
            {"heading": "実績リスト（未検証）",
             "columns": ["実績", "解放条件"],
             "rows": [
                ["実績 1–22", "未検証——名称と条件を公式リストと照合中。"],
             ]},
            {"heading": "実績の進捗を確認する方法",
             "items": [
                "ゲーム内の Steam オーバーレイで進捗を確認する。",
                "Steam 公式アナウンスをフォロー——実績リストがパッチノートに同梱されることもあります。",
                "確認でき次第、検証済みの完全リストをここで公開します。",
             ]},
            {"heading": "実績 FAQ",
             "items": [
                ["Approximately Up の実績はいくつ？", "22個——Steam 公式ストアで確認済み。"],
                ["実績の名称は？", "未検証——公式リストを確認中で、確認後に公開します。"],
                ["シングルプレイで全部取れる？", "未検証——一部は協力が必要かもしれませんが、リスト確認まで不明です。"],
             ]},
        ],
    },
    "ships": {
        "title": "Approximately Up の宇宙船",
        "metaTitle": "Approximately Up の宇宙船：建造・アイデア・デザイン",
        "metaDescription": "Approximately Up の宇宙船コンテンツ索引：建造ガイド、船のデザイン、設計図、モジュール建造の基本。",
        "intro": "Approximately Up の宇宙船に関するすべてを一箇所に——最初の建造からコミュニティのデザインアイデアまで。",
        "sections": [
            {"heading": "宇宙船ガイド",
             "items": [
                "宇宙船建造ガイド——「作る→墜ちる→作り直す」の流れを学ぶ。",
                "最強の宇宙船デザイン——設計の出発点とコミュニティのアイデア。",
                "設計図ガイド——設計図とワークショップ内容の既知情報。",
                "Mod——ワークショップ対応と Mod の質問。",
             ]},
            {"heading": "宇宙船 FAQ",
             "items": [
                ["どんな船を作れる？", "完全モジュール式——部品を自由に繋げます（公式説明）。具体的な部品リストは未検証。"],
                ["月へ飛べる？", "コミュニティスレッドで方法を質問中。月の機構は未検証。"],
                ["複数の船を操作できる？", "コミュニティスレッドで質問あり——未検証。"],
             ]},
        ],
    },
    "blueprints": {
        "title": "Approximately Up 設計図",
        "metaTitle": "Approximately Up 設計図一覧：DL とライブラリ",
        "metaDescription": "Approximately Up の設計図コンテンツ索引：設計図の使い方、船の設計の探し方、Steam ワークショップ。",
        "intro": "設計図ライブラリの索引——船の設計を見つけ、（未検証の）設計図ワークフローを学び、ワークショップを閲覧。",
        "sections": [
            {"heading": "設計図コンテンツ",
             "items": [
                "設計図ガイド——設計図で確認済み・未検証の内容。",
                "最強の宇宙船デザイン——設計のアイデアとさらに探す場所。",
                "Steam ワークショップ——コミュニティコンテンツの確認済みの置き場。",
             ]},
            {"heading": "設計図索引 FAQ",
             "items": [
                ["設計図はどこでダウンロード？", "Steam ワークショップが確認済みのコミュニティチャネル。ゲーム内の設計図ダウンロード機構は未検証。"],
                ["設計図のインポート方法は？", "未検証。"],
                ["自分のデザインを共有できる？", "未検証。"],
             ]},
        ],
    },
    "guides": {
        "title": "Approximately Up 攻略",
        "metaTitle": "Approximately Up 攻略：全ページ",
        "metaDescription": "Approximately Up の全攻略索引：遊び方、宇宙船建造、操作、マルチプレイ、Mod、実績など。",
        "intro": "Approximately Up の完全な攻略索引。各ページはプレイヤーが実際に検索する質問に答え、未検証のものはすべて明記します。",
        "sections": [
            {"heading": "全攻略",
             "items": [
                "遊び方——初心者のための「作る→墜ちる→作り直す」ループ。",
                "操作——キーボード・マウス、コントローラー状況、リマッパーのメモ。",
                "動作環境——スペック状況と PC の確認方法。",
                "マルチプレイ——オンライン協力、人数、非同期の質問。",
                "コンソール版——PS5／Xbox／Switch の状況。",
                "Mod——Steam ワークショップと Mod の質問。",
                "パッチノート——発売の事実と更新の追跡。",
                "デモと製品版——検証済みの比較。",
                "宇宙船建造ガイド——最初の船から大型建造まで。",
                "配線・電子機器——既知の内容と未検証の内容。",
                "設計図ガイド——設計図の状況とワークショップ。",
                "最強の宇宙船デザイン——アイデアとコミュニティデザイン。",
                "実績リスト——22個の実績、リストは未検証。",
                "宇宙船／設計図／実績——索引ページ。",
             ]},
            {"heading": "私たちの進め方", "body": "各ページは1〜2の信頼できる情報源を挙げ、未検証のものは「未検証」と明記します。数字・名称・機構は捏造しません。"},
        ],
    },
    "achievements": {
        "title": "Approximately Up 実績",
        "metaTitle": "Approximately Up 実績：概要",
        "metaDescription": "Approximately Up の実績概要：Steam 実績22個を確認済み、完全リストを検証中、進捗の追い方。",
        "intro": "Approximately Up の実績ハブ——確認済みの数、現在のリスト状況、完全トラッカーページへのリンク。",
        "sections": [
            {"heading": "実績22個を確認済み", "body": "Steam ストアは実績22個を確認。完全な名称と条件のリストは未検証。"},
            {"heading": "実績コンテンツ",
             "items": [
                "実績リスト——完全（未検証）リストの専用ページ。",
                "Steam——ストアページの実績セクションを確認。",
             ]},
            {"heading": "実績概要 FAQ",
             "items": [
                ["実績はいくつ？", "22個（Steam ストアで確認済み）。"],
                ["完全リストはどこ？", "未検証——公式リストを確認中。"],
             ]},
        ],
    },
}

TR_KO = {
    "how-to-play": {
        "title": "Approximately Up 플레이 방법: 초보자 가이드",
        "metaTitle": "Approximately Up 플레이 방법: 완전 초보자 가이드",
        "metaDescription": "Approximately Up이 처음인가요? 만들고-추락하고-다시 만들기 루프, 모듈식 우주선, 협동 멀티플레이, 행성 탐험을 설명하는 초보자 가이드.",
        "intro": "Approximately Up은 부품을 조립하고, 날리고, 추락하고, 더 잘 다시 만드는 우주 샌드박스 건설 게임입니다. 첫 비행 전에 알아야 할 핵심 루프를 소개합니다.",
        "sections": [
            {"heading": "핵심 루프: 만들고, 추락하고, 다시 만들기", "body": "공식 설명은 루프를 세 단어로 요약합니다 — 만들고, 추락하고, 다시 만들기. 나머지는 모두 여기서 시작됩니다.",
             "items": [
                ["작게 시작하기", "날기에 충분할 만큼 볼트로 조인 부품으로 우주선을 조립하세요. 완벽한 설계는 필요 없습니다 — 떠오를 수 있는 것이면 충분합니다."],
                ["추진기와 케이블 달기", "거대한 추진기로 움직임을 만들고, 케이블과 그 사이의 모든 부품으로 배를 연결하세요. 처음에는 어수선한 것이 정상입니다."],
                ["시험 비행", "이륙해서 무엇이 견디는지 확인하세요. 첫 비행은 실험이지, 완성된 비행이 아닙니다."],
                ["추락하기 (그럴 수 있음)", "추락은 루프의 일부입니다. 공식 소개도 당연한 일로 여깁니다 — 잔해는 실패가 아니라 교훈입니다."],
                ["더 똑똑하게 다시 만들기", "배운 것을 활용해 다시 만드세요. 반복할수록 어떤 부품이 견디고 어떤 조합이 나는지 알게 됩니다."],
             ]},
            {"heading": "게임이 공식적으로 약속한 것", "body": "Steam 공식 설명에서:",
             "items": [
                "완전 모듈식 우주선으로 협동 멀티플레이에서 새로운 행성을 탐험하세요.",
                "거대한 추진기, 성가신 케이블, 그 사이의 모든 것을 장착하세요.",
                "엉뚱한 임무를 완수하고 우주의 위험에 맞서세요.",
                "솔로로 또는 크루와 함께 플레이하세요 — 공식 소개대로, 크루와 말다툼도 하게 됩니다.",
             ]},
            {"heading": "초보자 FAQ",
             "items": [
                ["Approximately Up은 멀티플레이가 가능한가요?", "네 — 공식 스토어에 싱글플레이와 온라인 협동 멀티플레이가 명시되어 있습니다."],
                ["공학 지식이 필요한가요?", "아니요. 게임은 시행착오 중심입니다: 부품을 붙이고, 날고, 추락하고, 배우면 됩니다."],
                ["데모가 있나요?", "네 — 공식 스토어에 정식 출시(2026년 8월 6일)보다 먼저 나온 데모가 명시되어 있습니다."],
                ["Steam Deck에서 플레이할 수 있나요?", "호환성은 아직 확인되지 않았습니다. Steam 포럼에서도 질문이 나오고 있으며, 공식 답변 전까지 '미확인'으로 표시합니다."],
             ]},
            {"heading": "아직 확인이 필요한 내용", "body": "구체적인 행성 이름, 임무 이름, 그리고 설계도·배선·레이더·타임 리와인드 같은 상세 메커니즘은 공식 소스로 확인되지 않았습니다. '미확인'으로 표시하고, 공식 정보가 나오면 업데이트합니다."},
        ],
    },
    "ship-building-guide": {
        "title": "Approximately Up 우주선 제작 가이드",
        "metaTitle": "Approximately Up 우주선 제작 가이드: 첫 우주선부터 대형 제작까지",
        "metaDescription": "Approximately Up에서 우주선 만드는 법: 모듈식 만들고-추락하고-다시 만들기 과정, 추진기와 케이블, 달 여행·레이더 같은 커뮤니티 니즈.",
        "intro": "우주선 제작은 Approximately Up의 핵심입니다. 공식 소개는 단순합니다: 부품을 날 수 있을 만큼 조립하고, 더 똑똑하게 다시 만들기. 이 가이드는 아직 확인되지 않은 부품 수치를 지어내지 않고 과정을 안내합니다.",
        "sections": [
            {"heading": "첫 우주선 만들기", "body": "공식 설명(모듈 부품, 추진기, 케이블, 만들고-추락하고-다시 만들기)에 기반한 과정:",
             "items": [
                ["부품 모으기", "손에 있는 부품을 모아 볼트로 조이세요. 공식 소개는 '날기에 충분할 만큼 조인' 배를 출발점으로 삼습니다."],
                ["추진기 달기", "움직이기 위해 추진기를 장착하세요. 공식 설명은 '거대한 추진기'를 핵심 매력으로 꼽습니다."],
                ["케이블 배선하기", "케이블로 배를 연결하세요 — '성가신 케이블'도 경험의 일부입니다. 배선이 지저분해도 괜찮습니다."],
                ["시험 비행", "이륙하세요. 첫 우주선은 예쁠 필요가 없습니다. 무엇이 견디는지 알려주면 충분합니다."],
                ["추락하고 반복하기", "배운 것을 활용해 다시 만드세요. 루프는 만들기 → 추락 → 다시 만들기입니다."],
             ]},
            {"heading": "설계 원칙 (공식에 부합)",
             "items": [
                "완전 모듈식 우주선: 비행 사이에 모든 것을 다시 배치할 수 있습니다.",
                "무게와 추력의 균형 — 무거운 배는 더 큰 추력이 필요합니다(구체적 수치는 미확인).",
                "예비 부품 확보: 추락은 예상된 일입니다.",
                "협동 플레이 대비: 크루와 플레이한다면 역할(조종사, 건축가, 엔지니어)을 정하세요.",
             ]},
            {"heading": "커뮤니티가 요청한 튜토리얼",
             "items": [
                ["달에는 어떻게 가나요?", "Steam 포럼의 실제 스레드 — 달 여행 가이드를 원합니다. 달의 구체적 메커니즘은 미확인."],
                ["초보용 레이더 모니터/장치", "Steam 포럼의 실제 스레드 — 레이더 장치 튜토리얼을 원합니다. 레이더 메커니즘은 미확인."],
             ]},
            {"heading": "아직 미확인인 내용", "body": "위 패치 노트는 Steam 공식 발표로 검증되었습니다. 출시 전 빌드의 세부 사항과 미공개 변경 사항은 아직 미확인입니다."}
        ],
    },
    "blueprints-guide": {
        "title": "Approximately Up 설계도 가이드",
        "metaTitle": "Approximately Up 설계도 사용법: 다운로드, 공유",
        "metaDescription": "Approximately Up 설계도: 설계도 찾기와 사용에 대해 아는 것, Steam 창작마당 지원, 그리고 아직 미확인인 내용.",
        "intro": "설계도는 Approximately Up에서 가장 많이 검색되는 주제 중 하나입니다. 공식 설계도 메커니즘(가져오기, 내보내기, 공유)은 아직 확인되지 않았으므로, 이 페이지는 확인된 내용과 '미확인'을 다룹니다.",
        "sections": [
            {"heading": "설계도 세부 사항: 미확인", "body": "설계도 가져오기·내보내기·공유 메커니즘은 미확인 목록에 있습니다 — 공식 소스로 확인하지 못했습니다. 신뢰할 수 있는 정보가 확인되는 대로 이 페이지를 확장하겠습니다."},
            {"heading": "지금 우주선 설계를 찾는 방법", "body": "공식 설계도 도구는 미확인이지만, Steam 창작마당은 커뮤니티 콘텐츠가 있는 확인된 공간입니다:",
             "items": [
                ["Approximately Up의 Steam 창작마당 열기", "커뮤니티 업로드 콘텐츠가 여기 있습니다(스토어에서 창작마당 지원 확인됨)."],
                ["우주선과 제작물 둘러보기", "다른 플레이어가 공유한 우주선 설계를 찾아보세요."],
                ["구독하기", "구독하면 라이브러리에 저장됩니다."],
                ["게임에서 확인하기", "구독 항목이 게임에서 어떻게 표시되는지 — 정확한 단계는 미확인."],
             ]},
            {"heading": "설계도 FAQ",
             "items": [
                ["Approximately Up에서 설계도를 다운로드할 수 있나요?", "미확인. 창작마당 콘텐츠가 현재 가장 확인된 채널입니다."],
                ["우주선 설계를 공유할 수 있나요?", "미확인. 정확한 공유 절차는 확인 후 알려드리겠습니다."],
                ["설계도와 창작마당 아이템은 같은 건가요?", "같지 않을 수 있습니다 — 게임 내 설계도와 창작마당 아이템의 관계는 미확인."],
             ]},
            {"heading": "주목할 소스", "body": "설계도 메커니즘을 공식 채널(Steam 공지, 공식 사이트, Discord)에서 확인하고 이 페이지를 업데이트하겠습니다. 여기서 메커니즘을 지어내지 않습니다."},
        ],
    },
    "wiring-electronics": {
        "title": "Approximately Up 배선 & 전자기기 가이드",
        "metaTitle": "Approximately Up 배선 & 전자기기: 현재 알려진 것",
        "metaDescription": "Approximately Up의 배선과 전자기기: 제작의 케이블, 진공관 시대와 Remapper에 대한 커뮤니티 질문 — 미확인 내용 표시.",
        "intro": "배선과 전자기기는 커뮤니티의 큰 주제이지만 공식 정보는 빈약합니다. 이 페이지는 확인된 내용과 플레이어들이 묻는 질문을 모으고, 미확인된 것은 모두 명확히 표시합니다.",
        "sections": [
            {"heading": "공식 정보는 제한적", "body": "공식 설명은 케이블을 모듈식 제작의 일부로 언급하지만('성가신 케이블, 그 사이의 모든 것'), 상세한 배선·회로 메커니즘은 아직 지식 베이스에서 확인되지 않았습니다. '미확인'으로 표시합니다."},
            {"heading": "커뮤니티 스레드 (플레이어들의 실제 질문)",
             "items": [
                ["전자기기의 진공관 시대를 넘어설 수 없나요?", "부품의 전자기기 단계/시대를 묻는 Steam 포럼 스레드 — 초기 전자기기 테마를 시사합니다. 정확한 메커니즘은 미확인."],
                ["Remapper에서 값을 설정할 수 없음", "Remapper/Constant에서 값을 설정하는 데 문제가 있다는 Steam 포럼 스레드 — 정확한 절차는 미확인."],
             ]},
            {"heading": "안전하게 말할 수 있는 내용",
             "items": [
                "케이블은 모듈식 우주선 제작 판타지의 공식적인 일부입니다.",
                "전자기기는 성장 영역으로 보입니다(커뮤니티는 초기 '진공관 시대'를 언급).",
                "게임 내에 매개변수/값 설정 도구(Remapper)가 있지만 정확한 사용법은 미확인입니다.",
             ]},
            {"heading": "배선 & 전자기기 FAQ",
             "items": [
                ["Approximately Up에서 배선은 어떻게 작동하나요?", "미확인. 공식 또는 신뢰할 수 있는 교차 검증 정보가 나오면 가이드를 게시하겠습니다."],
                ["전자기기 단계는 무엇인가요?", "커뮤니티 스레드가 '진공관 시대'를 언급합니다. 정확한 단계와 해금은 미확인."],
                ["Remapper에서 값을 설정할 수 없는 이유는?", "커뮤니티 스레드가 이 문제를 보고합니다. 공식 절차는 미확인."],
             ]},
        ],
    },
    "controls": {
        "title": "Approximately Up 조작법",
        "metaTitle": "Approximately Up 조작법: 키보드·마우스 & 컨트롤러 지원 현황",
        "metaDescription": "Approximately Up 조작 가이드: 키보드·마우스에 대해 아는 것, 컨트롤러 지원, 게임 내 리매퍼 — 그리고 아직 미확인인 내용.",
        "intro": "컨트롤러 지원은 출시 직후 Steam 커뮤니티에서 가장 많이 묻는 질문 중 하나입니다. 여기서는 확인할 수 있는 것, 플레이어들이 묻는 것, 그리고 미확인인 것을 다룹니다.",
        "sections": [
            {"heading": "확인된 정보",
             "items": [
                ["플랫폼", "게임은 PC(Steam)에 있습니다. 키보드+마우스가 기본 입력입니다."],
                ["컨트롤러 지원", "개발자가 아직 확인하지 않았습니다. Steam 포럼에 '향후 컨트롤러 지원?'이라는 스레드가 있어, 출시 시점의 완전한 지원은 미확인임을 시사합니다."],
                ["게임 내 리매퍼", "플레이어들이 Remapper를 논의 중 — 값 설정에 문제가 있다는 스레드가 있습니다. 정확한 매핑 절차는 미확인으로 표시합니다."],
             ]},
            {"heading": "지금 조작을 설정하는 방법",
             "items": [
                "게임 내 설정을 열고 입력/조작 섹션에서 현재 키 매핑을 확인하세요.",
                "게임 내 Remapper로 키를 다시 지정하세요. 값이 적용되지 않으면 Steam 커뮤니티 스레드와 개발자 노트를 확인하세요.",
                "컨트롤러 지원 업데이트는 공식 Discord와 Steam 공지를 팔로우하세요.",
             ]},
            {"heading": "미확인: 전체 키맵", "body": "완전한 공식 키 매핑(이동, 카메라, 제작 메뉴, 추진기 조작)은 공식 소스로 아직 확인되지 않았습니다. '미확인'으로 표시하고, 확인되면 표를 게시하겠습니다."},
            {"heading": "조작 FAQ",
             "items": [
                ["Approximately Up이 컨트롤러를 지원하나요?", "아직 미확인입니다. 커뮤니티가 묻고 있으며, 개발자나 공식 소스가 확인하기 전까지 '미확인'으로 표시합니다."],
                ["키를 다시 지정할 수 있나요?", "게임 내 Remapper가 있습니다. 일부 플레이어가 값 설정 문제를 보고합니다. 정확한 절차는 미확인."],
                ["Steam Deck 조작 레이아웃이 있나요?", "Steam Deck 호환성 자체가 커뮤니티에서 열린 질문입니다 — 조작 레이아웃도 미확인."],
             ]},
        ],
    },
    "multiplayer": {
        "title": "Approximately Up 멀티플레이 가이드",
        "metaTitle": "Approximately Up 멀티플레이: 협동, 인원수 & 크로스플레이",
        "metaDescription": "Approximately Up 멀티플레이 설명: 온라인 협동, 몇 명까지, 비동기 멀티 여부 — 그리고 아직 미확인인 내용.",
        "intro": "Approximately Up은 공식적으로 싱글플레이 + 온라인 협동 게임입니다. 이 페이지는 플레이어들이 실제로 묻는 멀티플레이 질문에 답하고, 아직 확인할 수 없는 것을 표시합니다.",
        "sections": [
            {"heading": "공식 현황", "body": "Steam 공식 스토어는 '싱글플레이'와 '온라인 협동'을 지원 모드로 명시합니다. 이 게임의 핵심은 크루가 모듈식 우주선을 타고 함께 행성을 탐험하는 것입니다."},
            {"heading": "멀티플레이 FAQ",
             "items": [
                ["몇 명까지 함께 플레이할 수 있나요?", "정확한 인원수는 지식 베이스에서 확인되지 않았습니다 — '미확인'으로 표시합니다."],
                ["온라인 협동이 있나요?", "네 — Steam 공식 스토어에 온라인 협동 멀티플레이가 명시되어 있습니다."],
                ["크로스플랫폼 멀티가 있나요?", "미확인. 현재 PC(Steam)뿐이고 콘솔 버전도 발표되지 않아 크로스플레이도 미확인입니다."],
                ["비동기 멀티가 있나요?", "확인되지 않았습니다. Steam 포럼에 '비동기 멀티플레이'를 묻는 스레드가 있어 아직 공식 기능이 아닐 가능성이 큽니다 — '미확인'으로 표시합니다."],
                ["혼자 플레이할 수 있나요?", "네 — 싱글플레이가 지원 모드로 명시되어 있습니다."],
             ]},
            {"heading": "커뮤니티가 묻는 것",
             "items": [
                "비동기 멀티 — 비동기 모드를 기대하는지 여부.",
                "인원수/'몇 명까지'는 최상위 검색 니즈입니다. 확인되면 검증된 숫자를 공개하겠습니다.",
             ]},
            {"heading": "아직 미확인인 내용", "body": "정확한 인원 상한, 초대流程, 호스팅 세부 사항, 크로스플레이는 공식 소스로 확인되지 않았습니다. 확인되는 대로 이 페이지를 업데이트합니다."},
        ],
    },
    "best-ship-designs": {
        "title": "Approximately Up 최고의 우주선 설계",
        "metaTitle": "Approximately Up 우주선 아이디어 & 최고의 설계",
        "metaDescription": "Approximately Up 우주선 설계 아이디어: 직접 만들기 위한 출발점, 커뮤니티 설계 질문, 더 많은 설계를 찾는 곳.",
        "intro": "우주선 아이디어를 찾고 있나요? 이 페이지는 공식 '만들고-추락하고-다시 만들기' 판타지에 기반한 설계 출발점과, 플레이어들이 만들고 싶어 하는 것을 형성하는 커뮤니티 질문을 모읍니다.",
        "sections": [
            {"heading": "설계 출발점 (영감이지 공식 사양이 아님)",
             "items": [
                "추진기 중심 스피드스터: 거대한 추진기를 달고, 조종성은 나중에 감수하세요.",
                "실용 운반선: 속도보다 화물과 임무 부품 — 임무에는 적재량이 필요합니다(세부 사항 미확인).",
                "협동 크루선: 함께 행성을 탐험할 크루를 위한 공간을 설계하세요.",
                "지저분한 케이블 제작: '성가신 케이블'을 받아들이세요 — 배선도 매력의 일부입니다(배선 메커니즘 미확인).",
             ]},
            {"heading": "커뮤니티 설계 질문",
             "items": [
                ["궤적 곡률 계측기", "궤적 도구에 대한 Steam 포럼 스레드 — 더 나은 비행 도구를 원합니다. 공식 상태는 미확인."],
                ["여러 우주선을 만드는 모드?", "우주선을 여러 대 조종하는 것에 대한 Steam 포럼 스레드 — 미확인."],
             ]},
            {"heading": "더 많은 설계를 찾는 곳",
             "items": [
                "Approximately Up의 Steam 창작마당(지원 확인됨).",
                "공식 YouTube 채널의 트레일러 제작물.",
                "Steam 커뮤니티 토론의 플레이어 스크린샷과 아이디어.",
             ]},
            {"heading": "아직 미확인인 내용", "body": "구체적인 부품 수치, 이름 붙은 설계의 설계도, 어떤 '최고' 티어 목록도 확인되지 않았습니다. 이 페이지는 영감 + 검증된 소스로 유지하고, 나머지는 미확인으로 표시합니다."},
        ],
    },
    "system-requirements": {
        "title": "Approximately Up 시스템 요구 사항",
        "metaTitle": "Approximately Up 시스템 요구 사항 (PC)",
        "metaDescription": "Approximately Up PC 시스템 요구 사항: 최소/권장 사양은 아직 미확인 — 아는 것과 호환성 확인 방법.",
        "intro": "플레이어들은 자신의 PC로 실행 가능한지에 대한 명확한 답을 원합니다. 공식 최소·권장 사양은 아직 지식 베이스에서 확인되지 않았으므로, 이 페이지는 아는 것과 미확인 항목을 알려드립니다.",
        "sections": [
            {"heading": "공식 사양: 미확인", "body": "공식 소스에서 최소·권장 시스템 요구 사항을 아직 확인하지 못했습니다. 숫자를 지어내는 대신 사양 표를 '미확인'으로 표시하고, 확인(Steam 스토어 또는 공식 사이트)되는 대로 채우겠습니다."},
            {"heading": "사양 표 (미확인)",
             "columns": ["항목", "최소", "권장"],
             "rows": [
                ["OS", "미확인", "미확인"],
                ["프로세서", "미확인", "미확인"],
                ["메모리", "미확인", "미확인"],
                ["그래픽", "미확인", "미확인"],
                ["저장 공간", "미확인", "미확인"],
                ["DirectX", "미확인", "미확인"],
             ]},
            {"heading": "내 PC 확인 방법",
             "items": [
                "Steam에서 게임 스토어 페이지를 열어보세요 — 시스템 요구 사항은 보통 공개되면 여기에 표시됩니다.",
                "공식 숫자가 나오면 CPU/GPU/RAM과 비교하세요.",
                "Steam Deck: 호환성은 커뮤니티의 열린 질문('Playable on Deck?')입니다 — 미확인으로 표시합니다.",
             ]},
            {"heading": "시스템 요구 사항 FAQ",
             "items": [
                ["내 PC로 Approximately Up을 실행할 수 있나요?", "아직 확인할 수 없습니다 — 공식 최소/권장 사양이 미확인입니다. 개발자가 공개하면 Steam 스토어 페이지를 확인하세요."],
                ["Steam Deck에서 되나요?", "확인되지 않았습니다. Steam 포럼에 'Playable on Deck?' 스레드가 있습니다 — 공식 답변 전까지 호환성은 미확인."],
                ["사양이 높은가요?", "모듈식 물리 기반 우주선의 우주 샌드박스 건설 게임입니다. 검증된 숫자가 나오는 대로 보고하겠습니다."],
             ]},
        ],
    },
    "console-release": {
        "title": "Approximately Up 콘솔 출시: PS5·Xbox·Switch 현황",
        "metaTitle": "Approximately Up 콘솔 출시일 (PS5, Xbox, Switch)",
        "metaDescription": "Approximately Up이 PS5, Xbox, Switch로 나오나요? 아직 공식 발표 없음 — 콘솔 출시 현황과 공식 뉴스 확인 방법.",
        "intro": "'Approximately Up PS5 출시일', 'Xbox 출시', 'Switch 출시'는 게임 자체 위키도 답하지 못하는 검색입니다. 오늘의 정직한 답: 검증된 공식 콘솔 발표는 없습니다 — 여기가 현황 페이지입니다.",
        "sections": [
            {"heading": "콘솔 현황 (2026-08-09 기준)",
             "items": [
                ["현재 플랫폼", "PC(Steam)뿐입니다. 2026년 8월 6일 Steam으로 출시됐습니다."],
                ["PS5", "미확인 — PlayStation 5 버전에 대한 검증된 공식 발표 없음."],
                ["Xbox", "미확인 — Xbox 버전에 대한 검증된 공식 발표 없음."],
                ["Nintendo Switch", "미확인 — Switch 버전에 대한 검증된 공식 발표 없음."],
                ["공식 성명", "콘솔 계획에 대한 개발자의 공식 성명을 확인하지 못했습니다 — 미확인으로 표시하고, 나오는 대로 업데이트합니다."],
             ]},
            {"heading": "정보를 받아보는 방법",
             "items": [
                "공식 사이트 approximatelyup.com과 공식 Discord(discord.gg/approximatelyup)를 팔로우하세요.",
                "개발자 YouTube 채널(@ApproximatelyUp)과 TikTok(@approximatelyup)에서 발표를 확인하세요.",
                "Steam 스토어 페이지를 확인하세요 — 콘솔 소식은 보통 여기서 먼저 발표됩니다.",
             ]},
            {"heading": "콘솔 FAQ",
             "items": [
                ["Approximately Up이 PS5로 나오나요?", "발표되지 않았습니다 — 미확인으로 표시합니다. 검증된 공식 성명이 아직 없습니다."],
                ["Xbox로 나오나요?", "발표되지 않았습니다 — 미확인."],
                ["Nintendo Switch로 나오나요?", "발표되지 않았습니다 — 미확인."],
                ["콘솔 출시일은 언제인가요?", "아직 날짜가 없습니다. 공식 발표가 검증되는 즉시 이 페이지를 업데이트합니다."],
             ]},
            {"heading": "이 페이지가 존재하는 이유", "body": "콘솔 출시는 이 게임에서 검색 의도가 가장 높은 질문 중 하나이지만, 신뢰할 수 있는 소스가 답하지 않았습니다. 이 페이지는 검증된 현황(PC만)을 제공하고 날짜를 지어내는 대신 향후 발표를 추적합니다."},
        ],
    },
    "mods": {
        "title": "Approximately Up 모드 가이드",
        "metaTitle": "Approximately Up 모드: Steam 창작마당, 설치 & 모드 질문",
        "metaDescription": "Approximately Up 모드 설명: Steam 창작마당 지원, 모드 구독 방법, 여러 우주선 같은 커뮤니티 모드 질문.",
        "intro": "Approximately Up은 Steam 창작마당을 지원해서 모드 찾기와 설치가 간단합니다. 여기서는 확인된 내용과 플레이어들이 요구하는 것을 다룹니다.",
        "sections": [
            {"heading": "Steam 창작마당에서 모드 받기", "body": "창작마당 지원은 공식 스토어에서 확인됐습니다. 표준 절차:",
             "items": [
                ["창작마당 열기", "게임의 Steam 스토어 페이지에서 창작마당 탭을 열거나 창작마당 커뮤니티 허브로 이동하세요."],
                ["둘러보고 구독하기", "마음에 드는 모드나 아이템을 찾아 구독을 누르세요 — Steam이 자동으로 다운로드합니다."],
                ["게임 실행하기", "Approximately Up을 열고 게임의 모드/콘텐츠 메뉴에서 구독 항목을 확인하세요."],
                ["원하는 것 활성화하기", "사용할 모드를 켜세요. 게임 내 모드 메뉴의 세부 사항은 미확인입니다."],
             ]},
            {"heading": "커뮤니티가 묻는 것",
             "items": [
                "'여러 우주선을 만드는 모드?' — Steam 포럼의 실제 스레드. 모드로 다중 우주선 지원은 미확인.",
                "많은 게임에 치트 엔진 관련 검색이 있지만, 우리는 치트를 제공하지 않고 검증된 모드 정보만 제공합니다.",
             ]},
            {"heading": "모드 FAQ",
             "items": [
                ["Approximately Up이 모드를 지원하나요?", "공식적으로 Steam 창작마당을 지원합니다(스토어 기준). 완전한 모딩 문서는 미확인."],
                ["모드는 어떻게 설치하나요?", "Steam 창작마당에서 구독하면 설치를 Steam이 처리합니다. 게임 내 단계는 미확인."],
                ["모드로 여러 우주선을 조종할 수 있나요?", "커뮤니티 스레드가 요청 중입니다. 검증된 모드는 아직 없습니다 — 미확인."],
             ]},
            {"heading": "아직 미확인인 내용", "body": "정확한 창작마당 기능, 모드 가이드라인, 모드가 업적이나 멀티에 영향을 주는지는 아직 확인되지 않았습니다. 공식 문서가 확인되면 이 페이지를 업데이트합니다."},
        ],
    },
    "patch-notes": {
        "title": "Approximately Up 패치 노트",
        "metaTitle": "Approximately Up 패치 노트 & 업데이트 기록",
        "metaDescription": "Approximately Up 패치 노트와 업데이트 기록: 출시 정보, 공식 업데이트 게시 위치, 추적 중인 변경 기록(미확인 항목 표시).",
        "intro": "Approximately Up은 2026년 8월 6일에 출시됐습니다. 이 페이지는 공식 패치 노트와 업데이트를 추적하며, 미확인된 것은 모두 명확히 표시합니다.",
        "sections": [
            {"heading": "출시 사실 (검증됨)",
             "items": [
                ["출시일", "2026년 8월 6일 (Steam 정식 출시)."],
                ["데모", "정식 출시보다 먼저 나온 데모."],
                ["가격", "출시가 $19.99 (20% 할인, 정가 $24.99)."],
             ]},
            {"heading": "업데이트 타임라인 (Steam에서 검증됨)", "body": "다음 업데이트 내역은 Steam 공식 발표로 확인되었습니다 (2026년 8월):",
             "items": [
                ["2026-08-12", "1.0.010 — 워크숍 '인기순' 정렬 필터, 페이지 로딩, 결과 누락 문제를 수정하고 검색 명확성을 개선했습니다."],
                ["2026-08-11", "1.0.009 — Frame Quarter With Ports 개선(케이블 연결 시 반대쪽 포트도 동기화, A–D 라벨 일치). Middle Window, Small Switch, Small Button 기하 구조를 수정했습니다."],
                ["2026-08-10", "1.0.008 — Axis Rotometer 히트박스 및 남은 문제를 수정하고, Plasma Cables 페인팅 지원, Fly 모드 후 Autohemisphere Solar Panels 복귀, 케이블 홀더 페인팅을 추가했습니다."],
                ["2026-08-09", "1.0.007 — Metal 기기 호환성 수정, 기본 키바인드 수정(부품 집기를 마우스 가운데 버튼으로), 파이프 설명 오타 수정, 힌트 추가."],
                ["2026-08-08", "1.0.006 — Fuse Box 재시작 불가 문제 수정, Axis Rotometer의 부호 있는 로컬 축 값 출력 수정, Large Disposable Battery 미리보기 수정, 크레딧·시작 화면·목표 완료율 추적 추가."],
             ]},
            {"heading": "공식 업데이트 게시 위치",
             "items": [
                "게임의 Steam 공지(스토어 페이지의 뉴스 피드).",
                "공식 사이트 approximatelyup.com과 공식 Discord.",
                "개발자 YouTube 채널의 기능 발표.",
             ]},
            {"heading": "아직 미확인인 내용", "body": "구체적인 패치 내용(밸런스 변경, 수정 사항, 새 부품)은 확인되지 않았습니다. 추측 대신 모든 것을 미확인으로 표시합니다."},
        ],
    },
    "demo-vs-full": {
        "title": "Approximately Up 데모 vs 정식 게임",
        "metaTitle": "Approximately Up 데모 vs 정식: 차이점은?",
        "metaDescription": "Approximately Up 데모와 정식 버전 비교: 출시일, 가격, 창작마당과 업적 — 그리고 아직 미확인인 콘텐츠 차이.",
        "intro": "Approximately Up 데모는 2026년 8월 6일 정식 출시보다 먼저 나왔습니다. 검증된 비교를 제공하고, 콘텐츠 차이는 명확히 '미확인'으로 표시합니다.",
        "sections": [
            {"heading": "검증된 비교",
             "columns": ["항목", "데모", "정식 게임"],
             "rows": [
                ["이용 가능 여부", "데모 (스토어 기준 더 먼저 출시)", "2026년 8월 6일 정식 출시"],
                ["가격", "미확인", "$19.99 (출시 20% 할인, 정가 $24.99)"],
                ["Steam 창작마당", "미확인", "지원 (스토어 기준)"],
                ["업적", "미확인", "Steam 업적 22개 (스토어 기준)"],
                ["협동 멀티플레이", "미확인", "싱글플레이 + 온라인 협동 (스토어 기준)"],
             ]},
            {"heading": "데모 vs 정식 FAQ",
             "items": [
                ["데모는 무료인가요?", "데모의 가격/형태를 확인하지 못했습니다 — 미확인."],
                ["데모 진행 상황이 정식 게임으로 이어지나요?", "미확인."],
                ["정식 게임에만 있는 콘텐츠는?", "미확인 — 공식 비교 세부 사항이 아직 없습니다. 스토어 기준 정식 게임에는 창작마당 지원과 22개 업적이 있습니다."],
                ["데모를 먼저 해봐야 하나요?", "대부분의 우주 샌드박스 건설 게임에서 데모는 구매 전 '만들고-추락하고-다시 만들기'를 느끼기 좋은 방법입니다 — 다만 데모의 정확한 콘텐츠 범위는 미확인."],
             ]},
            {"heading": "아직 미확인인 내용", "body": "정확한 데모 콘텐츠, 진행 이전, 기능 차이는 공식 소스로 확인되지 않았습니다. 확인되는 대로 이 표를 업데이트합니다."},
        ],
    },
    "achievements-list": {
        "title": "Approximately Up 업적 목록",
        "metaTitle": "Approximately Up 업적: 전체 목록 (22개)",
        "metaDescription": "Approximately Up에는 Steam 업적 22개가 있습니다. 이름 전체 목록은 아직 확인 중 — 확인된 내용을 여기에 안내합니다.",
        "intro": "Steam 공식 스토어가 업적 22개를 확인했습니다. 정확한 이름과 해금 조건은 아직 지식 베이스에서 확인되지 않았으므로, 이 페이지는 확인된 수를 추적하고 목록을 '미확인'으로 표시합니다.",
        "sections": [
            {"heading": "확인됨: 업적 22개", "body": "Steam 스토어는 Approximately Up의 업적을 22개로 명시합니다. 각 업적의 이름, 아이콘, 해금 조건은 아직 확인하지 못했습니다 — 그 부분은 미확인입니다."},
            {"heading": "업적 목록 (미확인)",
             "columns": ["업적", "해금 조건"],
             "rows": [
                ["업적 1–22", "미확인 — 이름과 조건을 공식 목록과 대조 중입니다."],
             ]},
            {"heading": "업적 진행 상황 확인 방법",
             "items": [
                "게임 내 Steam 오버레이로 진행 상황을 확인하세요.",
                "Steam 공식 공지를 팔로우하세요 — 업적 목록이 패치 노트와 함께 나오기도 합니다.",
                "확인되는 대로 검증된 전체 목록을 여기에 게시하겠습니다.",
             ]},
            {"heading": "업적 FAQ",
             "items": [
                ["Approximately Up 업적은 몇 개인가요?", "22개 — Steam 공식 스토어에서 확인됨."],
                ["업적 이름은 무엇인가요?", "미확인 — 공식 목록을 확인 중이며, 확인되면 게시하겠습니다."],
                ["싱글플레이로 모든 업적을 얻을 수 있나요?", "미확인 — 일부는 협동이 필요할 수 있지만 목록이 확인되기 전까지 알 수 없습니다."],
             ]},
        ],
    },
    "ships": {
        "title": "Approximately Up 우주선",
        "metaTitle": "Approximately Up 우주선: 제작, 아이디어 & 설계",
        "metaDescription": "Approximately Up 우주선 콘텐츠 색인: 제작 가이드, 우주선 설계, 설계도, 모듈식 제작 기본.",
        "intro": "Approximately Up 우주선에 관한 모든 것을 한곳에 — 첫 제작부터 커뮤니티 설계 아이디어까지.",
        "sections": [
            {"heading": "우주선 가이드",
             "items": [
                "우주선 제작 가이드 — 만들고-추락하고-다시 만들기 과정 배우기.",
                "최고의 우주선 설계 — 설계 출발점과 커뮤니티 아이디어.",
                "설계도 가이드 — 설계도와 창작마당 콘텐츠에 대해 아는 것.",
                "모드 — 창작마당 지원과 모드 질문.",
             ]},
            {"heading": "우주선 FAQ",
             "items": [
                ["어떤 우주선을 만들 수 있나요?", "완전 모듈식입니다 — 부품을 원하는 대로 조립하세요(공식 설명). 구체적인 부품 목록은 미확인."],
                ["달까지 날아갈 수 있나요?", "커뮤니티 스레드가 방법을 묻습니다. 달 메커니즘은 미확인."],
                ["여러 우주선을 조종할 수 있나요?", "커뮤니티 스레드가 묻고 있습니다 — 미확인."],
             ]},
        ],
    },
    "blueprints": {
        "title": "Approximately Up 설계도",
        "metaTitle": "Approximately Up 설계도 모음: 다운로드, 라이브러리",
        "metaDescription": "Approximately Up 설계도 콘텐츠 색인: 설계도 사용법, 우주선 설계를 찾는 곳, Steam 창작마당.",
        "intro": "설계도 라이브러리 색인 — 우주선 설계를 찾고, (미확인인) 설계도 절차를 배우고, 창작마당을 둘러보세요.",
        "sections": [
            {"heading": "설계도 콘텐츠",
             "items": [
                "설계도 가이드 — 설계도에서 확인된 것과 미확인인 것.",
                "최고의 우주선 설계 — 설계 아이디어와 더 찾는 곳.",
                "Steam 창작마당 — 커뮤니티 콘텐츠의 확인된 공간.",
             ]},
            {"heading": "설계도 색인 FAQ",
             "items": [
                ["설계도는 어디서 다운로드하나요?", "Steam 창작마당이 확인된 커뮤니티 채널입니다. 게임 내 설계도 다운로드 메커니즘은 미확인."],
                ["설계도를 어떻게 가져오나요?", "미확인."],
                ["내 설계를 공유할 수 있나요?", "미확인."],
             ]},
        ],
    },
    "guides": {
        "title": "Approximately Up 가이드",
        "metaTitle": "Approximately Up 가이드: 전체 페이지",
        "metaDescription": "Approximately Up 전체 가이드 색인: 플레이 방법, 우주선 제작, 조작, 멀티플레이, 모드, 업적 등.",
        "intro": "Approximately Up 완전 가이드 색인. 각 페이지는 플레이어들이 실제로 검색하는 질문 하나에 답하며, 미확인된 것은 모두 표시합니다.",
        "sections": [
            {"heading": "전체 가이드",
             "items": [
                "플레이 방법 — 초보자를 위한 만들고-추락하고-다시 만들기 루프.",
                "조작법 — 키보드/마우스, 컨트롤러 현황, 리매퍼 메모.",
                "시스템 요구 사항 — 사양 현황과 PC 확인 방법.",
                "멀티플레이 — 온라인 협동, 인원수, 비동기 질문.",
                "콘솔 출시 — PS5/Xbox/Switch 현황.",
                "모드 — Steam 창작마당과 모드 질문.",
                "패치 노트 — 출시 사실과 업데이트 추적.",
                "데모 vs 정식 — 검증된 비교.",
                "우주선 제작 가이드 — 첫 우주선부터 대형 제작까지.",
                "배선 & 전자기기 — 알려진 것, 미확인인 것.",
                "설계도 가이드 — 설계도 현황과 창작마당.",
                "최고의 우주선 설계 — 아이디어와 커뮤니티 설계.",
                "업적 목록 — 업적 22개, 목록 미확인.",
                "우주선 / 설계도 / 업적 — 색인 페이지.",
             ]},
            {"heading": "우리의 작업 방식", "body": "각 페이지는 1–2개의 신뢰할 수 있는 소스를 나열하고, 확인되지 않은 것은 미확인으로 표시합니다. 숫자, 이름, 메커니즘을 지어내지 않습니다."},
        ],
    },
    "achievements": {
        "title": "Approximately Up 업적",
        "metaTitle": "Approximately Up 업적: 개요",
        "metaDescription": "Approximately Up 업적 개요: Steam 업적 22개 확인, 전체 목록 확인 중, 진행 상황 추적 방법.",
        "intro": "Approximately Up 업적 허브 — 확인된 수, 현재 목록 상태, 전체 추적 페이지 링크.",
        "sections": [
            {"heading": "업적 22개 확인됨", "body": "Steam 스토어가 업적 22개를 확인합니다. 전체 이름과 조건 목록은 미확인입니다."},
            {"heading": "업적 콘텐츠",
             "items": [
                "업적 목록 — 전체(미확인) 목록 전용 페이지.",
                "Steam — 스토어 페이지의 업적 섹션 확인.",
             ]},
            {"heading": "업적 개요 FAQ",
             "items": [
                ["업적이 몇 개인가요?", "22개 (Steam 스토어에서 확인됨)."],
                ["전체 목록은 어디에 있나요?", "미확인 — 공식 목록을 확인 중입니다."],
             ]},
        ],
    },
}

TR_FR = {
    "how-to-play": {
        "title": "Comment jouer à Approximately Up",
        "metaTitle": "Comment jouer à Approximately Up : guide du débutant complet",
        "metaDescription": "Nouveau sur Approximately Up ? Découvrez la boucle construire-s'écraser-reconstruire, les vaisseaux modulaires, le multijoueur coopératif et l'exploration de planètes.",
        "intro": "Approximately Up est un jeu de construction sandbox spatial où l'on boulonne des pièces, décolle, s'écrase et reconstruit mieux. Voici la boucle principale et ce qu'il faut savoir avant votre premier lancement.",
        "sections": [
            {"heading": "La boucle principale : construire, s'écraser, reconstruire", "body": "La description officielle résume la boucle en trois mots — construire, s'écraser, reconstruire. Tout le reste en découle.",
             "items": [
                ["Commencez petit", "Assemblez un vaisseau avec tout ce qui se boulonne assez longtemps pour voler. Pas besoin d'un design parfait pour commencer — il faut juste quelque chose qui décolle."],
                ["Montez propulseurs et câbles", "Les propulseurs géants font avancer ; les câbles et tout le reste relient votre construction. Attendez-vous à un agencement chaotique au début."],
                ["Vol d'essai", "Décollez et voyez ce qui tient. Les premiers vols sont des expériences, pas des vols maîtrisés."],
                ["Écraser (ça arrive)", "Les crashs font partie de la boucle. Le discours officiel les considère comme normaux — les débris sont une leçon, pas un échec."],
                ["Reconstruire plus malin", "Servez-vous de ce que vous avez appris. Chaque itération vous apprend quelles pièces tiennent et quelles combinaisons volent."],
             ]},
            {"heading": "Ce que le jeu promet officiellement", "body": "D'après la description officielle Steam :",
             "items": [
                "Explorez de nouvelles planètes en multijoueur coopératif avec votre vaisseau entièrement modulaire.",
                "Montez d'énormes propulseurs, des câbles agaçants, et tout le reste.",
                "Accomplissez de folles missions et affrontez les dangers de l'espace.",
                "Jouez en solo ou avec un équipage — et disputez-vous avec lui, comme le dit le pitch officiel.",
             ]},
            {"heading": "FAQ du débutant",
             "items": [
                ["Approximately Up est-il multijoueur ?", "Oui — la page Steam officielle liste le solo et le multijoueur coopératif en ligne."],
                ["Faut-il des connaissances en ingénierie ?", "Non. Le jeu repose sur l'essai-erreur : boulonner, voler, s'écraser, apprendre."],
                ["Y a-t-il une démo ?", "Oui — la page Steam officielle liste une démo antérieure à la sortie complète (6 août 2026)."],
                ["Puis-je jouer sur Steam Deck ?", "La compatibilité n'est pas encore confirmée. Les joueurs posent la question sur les forums Steam ; nous marquons cela comme non vérifié en attendant une réponse officielle."],
             ]},
            {"heading": "Ce qu'il reste à vérifier", "body": "Les noms précis de planètes, de missions et les guides de mécanique détaillés (plans, câblage, radar, rembobinage) ne sont pas encore vérifiés auprès de sources officielles. Nous les marquons comme non vérifiés et mettons cette page à jour dès que des informations officielles sont disponibles."},
        ],
    },
    "ship-building-guide": {
        "title": "Guide de construction de vaisseaux Approximately Up",
        "metaTitle": "Guide de construction de vaisseaux Approximately Up : du premier vaisseau aux grosses constructions",
        "metaDescription": "Apprenez à construire des vaisseaux dans Approximately Up : le processus modulaire construire-s'écraser-reconstruire, propulseurs et câbles, plus les besoins de la communauté comme la Lune et le radar.",
        "intro": "La construction de vaisseaux est le cœur d'Approximately Up. Le pitch officiel est simple : boulonner des pièces jusqu'à ce que ça vole, puis reconstruire plus malin. Ce guide détaille le processus sans inventer de statistiques encore non vérifiées.",
        "sections": [
            {"heading": "Construire votre premier vaisseau", "body": "D'après la description officielle (pièces modulaires, propulseurs, câbles, construire-s'écraser-reconstruire), voici le processus :",
             "items": [
                ["Rassemblez des pièces", "Collectez les pièces disponibles et boulonnez-les. Le pitch officiel dit que toute construction « se boulonne assez longtemps pour voler » — commencez là."],
                ["Ajoutez des propulseurs", "Montez des propulseurs pour avancer. La description officielle met en avant les « propulseurs géants » comme élément central."],
                ["Tirez les câbles", "Reliez votre construction avec des câbles — les « câbles agaçants » font partie de l'expérience. Attendez-vous à un câblage brouillon."],
                ["Vol d'essai", "Décollez. Votre premier vaisseau n'a pas besoin d'être beau ; il doit vous apprendre ce qui tient."],
                ["Écraser et itérer", "Reconstruisez avec ce que vous avez appris. La boucle est construire → s'écraser → reconstruire."],
             ]},
            {"heading": "Principes de conception (alignés sur l'officiel)",
             "items": [
                "Vaisseau entièrement modulaire : tout peut être réorganisé entre deux vols.",
                "Équilibrez poids et poussée — un vaisseau plus lourd demande plus de poussée (chiffres précis non vérifiés).",
                "Gardez des pièces de rechange : les crashs sont prévus.",
                "Prévoyez pour le co-op : avec un équipage, répartissez les rôles (pilote, constructeur, ingénieur).",
             ]},
            {"heading": "Tutoriels demandés par la communauté",
             "items": [
                ["Comment aller sur la Lune", "Un vrai fil Steam — les joueurs veulent un guide pour la Lune. Les mécaniques lunaires précises sont non vérifiées."],
                ["Moniteur / appareil radar pour débutant", "Un vrai fil Steam — les joueurs veulent un tutoriel sur l'appareil radar. Les mécaniques du radar sont non vérifiées."],
             ]},
            {"heading": "Ce qui reste non vérifié", "body": "Les noms précis de pièces, statistiques, recettes, destinations de planètes et noms de missions ne sont pas encore vérifiés. Ce guide n'utilise que la description officielle et des questions communautaires marquées ; nous l'approfondirons dès que des informations vérifiées arriveront."},
        ],
    },
    "blueprints-guide": {
        "title": "Guide des plans Approximately Up",
        "metaTitle": "Plans Approximately Up : télécharger, partager et utiliser",
        "metaDescription": "Les plans Approximately Up : ce que nous savons pour les trouver et les utiliser, le support du Steam Workshop, et ce qui reste non vérifié.",
        "intro": "Les plans sont l'un des sujets les plus recherchés sur Approximately Up. Les mécaniques officielles (import, export, partage) ne sont pas encore vérifiées ; cette page couvre donc ce qui est confirmé et ce qui ne l'est pas.",
        "sections": [
            {"heading": "Détails des plans : non vérifiés", "body": "Les mécaniques d'import, d'export et de partage des plans sont sur notre liste non vérifiée — nous ne les avons pas confirmées auprès d'une source officielle. Cette page sera développée dès qu'une information fiable sera vérifiée."},
            {"heading": "Trouver des designs de vaisseaux aujourd'hui", "body": "Si les outils de plans officiels sont non vérifiés, le Steam Workshop est l'endroit confirmé où vit le contenu communautaire :",
             "items": [
                ["Ouvrez le Steam Workshop d'Approximately Up", "Le contenu publié par la communauté y est hébergé (le support du Workshop est confirmé sur la page du magasin)."],
                ["Parcourez vaisseaux et constructions", "Cherchez des designs partagés par d'autres joueurs."],
                ["Abonnez-vous", "L'abonnement enregistre le contenu dans votre bibliothèque."],
                ["Vérifiez dans le jeu", "Voyez comment les éléments abonnés apparaissent en jeu — étapes précises non vérifiées."],
             ]},
            {"heading": "FAQ des plans",
             "items": [
                ["Puis-je télécharger des plans dans Approximately Up ?", "Non vérifié. Le contenu du Workshop est le canal confirmé le plus proche aujourd'hui."],
                ["Puis-je partager mes designs de vaisseaux ?", "Non vérifié. Nous confirmerons le processus exact de partage une fois vérifié."],
                ["Les plans sont-ils les mêmes que les objets du Workshop ?", "Pas forcément — la relation entre plans en jeu et objets du Workshop est non vérifiée."],
             ]},
            {"heading": "Sources à surveiller", "body": "Nous vérifierons les mécaniques de plans auprès des canaux officiels (annonces Steam, site officiel, Discord) et mettrons cette page à jour. Rien ici n'invente de mécanique."},
        ],
    },
    "wiring-electronics": {
        "title": "Guide du câblage et de l'électronique Approximately Up",
        "metaTitle": "Câblage et électronique Approximately Up : ce que nous savons",
        "metaDescription": "Le câblage et l'électronique dans Approximately Up : câbles dans les constructions, questions de la communauté sur l'ère des tubes à vide et le Remapper — avec les détails non vérifiés marqués.",
        "intro": "Le câblage et l'électronique sont un grand sujet communautaire — mais les informations officielles sont minces. Cette page rassemble ce qui est vérifié et ce que demandent les joueurs, tout ce qui n'est pas vérifié étant clairement marqué.",
        "sections": [
            {"heading": "Les informations officielles sont limitées", "body": "La description officielle mentionne les câbles comme partie de la construction modulaire (« des câbles agaçants, et tout le reste »), mais les mécaniques détaillées de câblage et de circuits ne sont pas encore vérifiées. Nous les marquons comme non vérifiées."},
            {"heading": "Fils communautaires (de vraies questions de joueurs)",
             "items": [
                ["Peut-on dépasser l'ère des tubes à vide pour l'électronique ?", "Un fil Steam demandant la progression/les paliers de l'électronique — suggère un thème électronique de première époque ; mécaniques exactes non vérifiées."],
                ["Impossible de définir des valeurs dans Remapper", "Un fil Steam signalant des difficultés à définir des valeurs dans Remapper/Constant — le processus exact est non vérifié."],
             ]},
            {"heading": "Ce que nous pouvons affirmer sans risque",
             "items": [
                "Les câbles font officiellement partie de la construction modulaire de vaisseaux.",
                "L'électronique semble être un axe de progression (la communauté mentionne une « ère des tubes à vide » au début).",
                "Des outils de réglage de paramètres/valeurs existent en jeu (Remapper), mais l'usage exact est non vérifié.",
             ]},
            {"heading": "FAQ câblage et électronique",
             "items": [
                ["Comment fonctionne le câblage dans Approximately Up ?", "Non vérifié. Nous publierons un guide dès qu'une information officielle ou fiabilisée par recoupement existera."],
                ["Quels sont les paliers de l'électronique ?", "Un fil communautaire mentionne une « ère des tubes à vide » ; les paliers et déblocages exacts sont non vérifiés."],
                ["Pourquoi ne puis-je pas définir des valeurs dans le Remapper ?", "Un fil communautaire signale ce problème ; le processus officiel est non vérifié."],
             ]},
        ],
    },
    "controls": {
        "title": "Contrôles Approximately Up",
        "metaTitle": "Contrôles Approximately Up : clavier, souris et statut manette",
        "metaDescription": "Guide des contrôles Approximately Up : ce que nous savons du clavier/souris, du support manette et du remappeur intégré — plus ce qui reste non vérifié.",
        "intro": "Le support manette est l'une des questions les plus posées dans la communauté Steam juste après la sortie. Voici ce que nous pouvons confirmer, ce que demandent les joueurs, et ce qui reste non vérifié.",
        "sections": [
            {"heading": "Ce que nous savons (vérifié)",
             "items": [
                ["Plateforme", "Le jeu est sur PC (Steam). Clavier et souris sont l'entrée par défaut."],
                ["Support manette", "Pas encore confirmé par le développeur. Un fil Steam demande « Controller Support in the Future? », ce qui suggère que le support complet n'est pas confirmé au lancement."],
                ["Remappeur intégré", "Les joueurs discutent du Remapper — un fil communautaire signale des difficultés à y définir des valeurs. Le processus exact de remappage est marqué non vérifié."],
             ]},
            {"heading": "Configurer les contrôles maintenant",
             "items": [
                "Ouvrez les paramètres en jeu et vérifiez la section entrée / contrôles pour la configuration actuelle des touches.",
                "Utilisez le Remapper intégré pour redéfinir les touches ; si les valeurs ne s'appliquent pas, consultez le fil communautaire et les notes du développeur.",
                "Pour les mises à jour du support manette, suivez le Discord officiel et les annonces Steam.",
             ]},
            {"heading": "Non vérifié : la carte complète des touches", "body": "La carte complète officielle (mouvement, caméra, menu de construction, contrôle des propulseurs) n'est pas encore vérifiée. Nous la marquons non vérifiée et publierons le tableau une fois confirmé."},
            {"heading": "FAQ des contrôles",
             "items": [
                ["Approximately Up prend-il en charge les manettes ?", "Pas encore confirmé. La communauté demande ; nous marquons cela non vérifié jusqu'à confirmation du développeur ou d'une source officielle."],
                ["Puis-je redéfinir les touches ?", "Il y a un Remapper intégré. Certains joueurs signalent des problèmes de valeurs ; le processus exact est non vérifié."],
                ["Y a-t-il une disposition Steam Deck ?", "La compatibilité Steam Deck est elle-même une question ouverte dans la communauté — la disposition est non vérifiée."],
             ]},
        ],
    },
    "multiplayer": {
        "title": "Guide multijoueur Approximately Up",
        "metaTitle": "Multijoueur Approximately Up : co-op, nombre de joueurs et crossplay",
        "metaDescription": "Le multijoueur Approximately Up expliqué : co-op en ligne, nombre de joueurs, existence d'un multijoueur asynchrone, et ce qui reste non vérifié.",
        "intro": "Approximately Up est officiellement un jeu solo et co-op en ligne. Cette page répond aux questions multijoueur réellement posées par les joueurs et marque ce que nous ne pouvons pas encore vérifier.",
        "sections": [
            {"heading": "Statut officiel", "body": "La page Steam officielle liste « Solo » et « Coopération en ligne » comme modes pris en charge. Le pitch du jeu repose sur un équipage explorant des planètes ensemble dans un vaisseau modulaire."},
            {"heading": "FAQ multijoueur",
             "items": [
                ["Combien de joueurs peuvent jouer ensemble ?", "Le nombre exact n'est pas vérifié dans notre base de connaissances — nous le marquons non vérifié."],
                ["Y a-t-il un co-op en ligne ?", "Oui — le multijoueur coopératif en ligne figure sur la page Steam officielle."],
                ["Y a-t-il un multijoueur multiplateforme ?", "Non vérifié. Le jeu est actuellement sur PC (Steam) ; les versions console ne sont pas annoncées, donc le crossplay est non vérifié."],
                ["Y a-t-il un multijoueur asynchrone ?", "Non confirmé. Un fil Steam demande « Asynchronous Multiplayer », ce qui suggère que ce n'est pas encore une fonctionnalité officielle — non vérifié."],
                ["Puis-je jouer en solo ?", "Oui — le solo est listé comme mode pris en charge."],
             ]},
            {"heading": "Ce que demande la communauté",
             "items": [
                "Multijoueur asynchrone — si les joueurs attendent un mode asynchrone.",
                "Le nombre de joueurs / « combien de joueurs » est un besoin de recherche majeur ; nous publierons le chiffre vérifié dès qu'il sera disponible.",
             ]},
            {"heading": "Ce qui reste non vérifié", "body": "Le nombre maximal exact, le flux d'invitation, les détails d'hébergement et le crossplay ne sont pas encore vérifiés. Nous mettrons cette page à jour dès confirmation."},
        ],
    },
    "best-ship-designs": {
        "title": "Meilleurs designs de vaisseaux Approximately Up",
        "metaTitle": "Idées de vaisseaux et meilleurs designs Approximately Up",
        "metaDescription": "Idées de designs de vaisseaux Approximately Up : points de départ pour vos constructions, questions de design de la communauté, et où trouver plus de designs.",
        "intro": "Vous cherchez des idées de vaisseaux ? Cette page rassemble des points de départ basés sur la fantaisie officielle construire-s'écraser-reconstruire, plus les questions communautaires qui façonnent ce que veulent construire les joueurs.",
        "sections": [
            {"heading": "Points de départ (inspiration, pas des specs officielles)",
             "items": [
                "Speedster à gros propulseurs : montez des propulseurs géants et acceptez que le contrôle vienne plus tard.",
                "Transport utilitaire : privilégiez la cargaison et les pièces de mission à la vitesse — les missions demandent de la capacité (détails non vérifiés).",
                "Vaisseau d'équipage co-op : concevez pour un équipage explorant des planètes ensemble.",
                "Construction à câbles brouillons : adoptez les « câbles agaçants » — le câblage fait partie du charme (mécaniques non vérifiées).",
             ]},
            {"heading": "Questions de design de la communauté",
             "items": [
                ["Compteur de courbure de trajectoire", "Un fil Steam sur un outil de trajectoire — les joueurs veulent de meilleurs outils de vol ; statut officiel non vérifié."],
                ["mods pour plusieurs vaisseaux ?", "Un fil Steam sur le contrôle de plusieurs vaisseaux — non vérifié."],
             ]},
            {"heading": "Où trouver plus de designs",
             "items": [
                "Le Steam Workshop d'Approximately Up (support confirmé).",
                "La chaîne YouTube officielle pour les constructions des bandes-annonces.",
                "Les discussions de la communauté Steam pour les captures et idées des joueurs.",
             ]},
            {"heading": "Ce qui reste non vérifié", "body": "Les statistiques précises de pièces, les plans de designs nommés et tout « meilleur » classement ne sont pas vérifiés. Nous gardons cette page en inspiration + sources vérifiées, le reste étant marqué non vérifié."},
        ],
    },
    "system-requirements": {
        "title": "Configuration requise Approximately Up",
        "metaTitle": "Configuration requise Approximately Up (PC)",
        "metaDescription": "Configuration requise PC Approximately Up : les specs minimales et recommandées ne sont pas encore vérifiées — voici ce que nous savons et comment vérifier la compatibilité.",
        "intro": "Les joueurs veulent une réponse claire sur la capacité de leur PC à faire tourner Approximately Up. Les specs minimales et recommandées officielles ne sont pas encore vérifiées ; cette page indique donc ce que nous savons et ce qui ne l'est pas.",
        "sections": [
            {"heading": "Specs officielles : non vérifiées", "body": "Nous n'avons pas encore vérifié la configuration minimale et recommandée auprès d'une source officielle. Plutôt que d'inventer des chiffres, nous marquons le tableau non vérifié et le remplirons dès confirmation (page Steam ou site officiel)."},
            {"heading": "Tableau des specs (non vérifié)",
             "columns": ["Élément", "Minimum", "Recommandé"],
             "rows": [
                ["OS", "non vérifié", "non vérifié"],
                ["Processeur", "non vérifié", "non vérifié"],
                ["Mémoire", "non vérifié", "non vérifié"],
                ["Carte graphique", "non vérifié", "non vérifié"],
                ["Stockage", "non vérifié", "non vérifié"],
                ["DirectX", "non vérifié", "non vérifié"],
             ]},
            {"heading": "Vérifier votre PC",
             "items": [
                "Ouvrez Steam et consultez la page du magasin — la configuration apparaît généralement dès qu'elle est publiée.",
                "Comparez CPU/GPU/RAM aux chiffres officiels une fois que nous les publions.",
                "Steam Deck : la compatibilité est une question ouverte de la communauté (« Playable on Deck? ») ; nous la marquons non vérifiée.",
             ]},
            {"heading": "FAQ configuration",
             "items": [
                ["Mon PC peut-il faire tourner Approximately Up ?", "Pas encore confirmé — les specs minimales/recommandées officielles sont non vérifiées. Consultez la page Steam quand le développeur les publiera."],
                ["Approximately Up est-il sur Steam Deck ?", "Non confirmé. Un fil Steam demande « Playable on Deck? » — la compatibilité est non vérifiée en attendant une réponse officielle."],
                ["Est-ce exigeant ?", "C'est un jeu de construction sandbox spatial avec des vaisseaux physiques modulaires ; nous publierons les chiffres vérifiés dès qu'ils seront disponibles."],
             ]},
        ],
    },
    "console-release": {
        "title": "Sortie console Approximately Up : statut PS5, Xbox et Switch",
        "metaTitle": "Date de sortie console Approximately Up (PS5, Xbox, Switch)",
        "metaDescription": "Approximately Up arrive-t-il sur PS5, Xbox ou Switch ? Aucune annonce officielle pour l'instant — voici le statut console et comment suivre l'actualité officielle.",
        "intro": "« Date de sortie PS5 Approximately Up », « version Xbox » et « version Switch » sont des recherches que le wiki du jeu lui-même ne couvre pas. La réponse honnête aujourd'hui : aucune annonce console officielle vérifiée — voici la page de statut.",
        "sections": [
            {"heading": "Statut console (au 09/08/2026)",
             "items": [
                ["Plateformes actuelles", "PC (Steam) uniquement. Le jeu est sorti le 6 août 2026 sur Steam."],
                ["PS5", "non vérifié — aucune annonce officielle vérifiée d'une version PlayStation 5."],
                ["Xbox", "non vérifié — aucune annonce officielle vérifiée d'une version Xbox."],
                ["Nintendo Switch", "non vérifié — aucune annonce officielle vérifiée d'une version Switch."],
                ["Déclaration officielle", "Nous n'avons pas vérifié de déclaration officielle du développeur sur les projets console ; non vérifié, mis à jour dès qu'il en existe une."],
             ]},
            {"heading": "Comment rester informé",
             "items": [
                "Suivez le site officiel approximatelyup.com et le Discord officiel (discord.gg/approximatelyup).",
                "Surveillez la chaîne YouTube du développeur (@ApproximatelyUp) et TikTok (@approximatelyup) pour les annonces.",
                "Consultez la page Steam — les nouvelles console y sont généralement annoncées en premier.",
             ]},
            {"heading": "FAQ console",
             "items": [
                ["Approximately Up est-il sur PS5 ?", "Non annoncé — non vérifié. Aucune déclaration officielle vérifiée pour l'instant."],
                ["Est-il sur Xbox ?", "Non annoncé — non vérifié."],
                ["Est-il sur Nintendo Switch ?", "Non annoncé — non vérifié."],
                ["Quand sort la version console ?", "Aucune date n'existe encore. Cette page sera mise à jour dès qu'une annonce officielle sera vérifiée."],
             ]},
            {"heading": "Pourquoi cette page existe", "body": "La sortie console est l'une des questions à plus forte intention pour ce jeu, mais aucune source fiable n'y répond. Cette page donne le statut vérifié (PC uniquement) et suit les futures annonces au lieu d'inventer une date."},
        ],
    },
    "mods": {
        "title": "Guide des mods Approximately Up",
        "metaTitle": "Mods Approximately Up : Steam Workshop, installation et questions",
        "metaDescription": "Les mods Approximately Up expliqués : support du Steam Workshop, comment s'abonner aux mods, et les questions communautaires comme plusieurs vaisseaux.",
        "intro": "Approximately Up prend en charge le Steam Workshop, ce qui rend la recherche et l'installation de mods simple. Voici ce qui est confirmé et ce que demandent les joueurs.",
        "sections": [
            {"heading": "Obtenir des mods depuis le Steam Workshop", "body": "Le support du Workshop est confirmé sur la page officielle. Le flux standard :",
             "items": [
                ["Ouvrez le Workshop", "Depuis la page Steam du jeu, ouvrez l'onglet Workshop (ou le hub communautaire du Workshop)."],
                ["Parcourez et abonnez-vous", "Trouvez un mod ou un objet et appuyez sur S'abonner — Steam le télécharge automatiquement."],
                ["Lancez le jeu", "Ouvrez Approximately Up et vérifiez le menu mods/contenu du jeu pour voir les éléments abonnés."],
                ["Activez ce que vous voulez", "Activez les mods souhaités. Les détails du menu des mods en jeu sont non vérifiés."],
             ]},
            {"heading": "Ce que demande la communauté",
             "items": [
                "mods pour plusieurs vaisseaux ? — un vrai fil Steam ; le support multi-vaisseaux via mods est non vérifié.",
                "Les recherches liées à cheat engine existent pour beaucoup de jeux ; nous ne fournissons pas de cheats, seulement des informations vérifiées sur les mods.",
             ]},
            {"heading": "FAQ des mods",
             "items": [
                ["Approximately Up prend-il en charge les mods ?", "Officiellement, il prend en charge le Steam Workshop (selon la page du magasin). La documentation complète de modding est non vérifiée."],
                ["Comment installer des mods ?", "Abonnez-vous via le Steam Workshop ; Steam gère l'installation. Les étapes en jeu sont non vérifiées."],
                ["Les mods permettent-ils de contrôler plusieurs vaisseaux ?", "Un fil communautaire le demande ; aucun mod vérifié ne le permet encore — non vérifié."],
             ]},
            {"heading": "Ce qui reste non vérifié", "body": "Les fonctionnalités exactes du Workshop, les directives sur les mods et l'effet des mods sur les succès ou le multijoueur ne sont pas encore vérifiés. Nous mettrons cette page à jour à la confirmation de la documentation officielle."},
        ],
    },
    "patch-notes": {
        "title": "Notes de mise à jour Approximately Up",
        "metaTitle": "Notes de mise à jour et historique des versions Approximately Up",
        "metaDescription": "Notes de mise à jour et historique Approximately Up : infos de lancement, où sont publiées les mises à jour officielles, et notre journal suivi (éléments non vérifiés marqués).",
        "intro": "Approximately Up est sorti le 6 août 2026. Cette page suit les notes de patch et mises à jour officielles — tout ce qui n'est pas vérifié est clairement marqué.",
        "sections": [
            {"heading": "Faits de lancement (vérifiés)",
             "items": [
                ["Date de sortie", "6 août 2026 (sortie complète Steam)."],
                ["Démo", "Une démo précède la sortie complète."],
                ["Prix", "19,99 $ au lancement (remise de 20 % ; liste 24,99 $)."],
             ]},
            {"heading": "Chronologie des mises à jour (vérifiée via Steam)", "body": "Notes de mise à jour vérifiées à partir des annonces officielles Steam (août 2026) :",
             "items": [
                ["2026-08-12", "1.0.010 — Correction du filtre de tri « Plus populaires » du Workshop, du chargement des pages et des résultats manquants ; amélioration de la clarté de recherche."],
                ["2026-08-11", "1.0.009 — Amélioration de Frame Quarter With Ports (les ports se reflètent de l'autre côté de la chaîne, étiquettes A–D cohérentes) ; correction de la géométrie de Middle Window, Small Switch et Small Button."],
                ["2026-08-10", "1.0.008 — Correction de la hitbox de l'Axis Rotometer et des problèmes restants ; câbles Plasma peignables ; panneaux Autohemisphere de retour en position après Fly Mode ; supports de câble peignables."],
                ["2026-08-09", "1.0.007 — Correction de la compatibilité avec les appareils Metal ; correction du raccourci par défaut (molette pour « prendre le composant ») ; faute de frappe corrigée ; plus d'indices."],
                ["2026-08-08", "1.0.006 — Correction du Fuse Box impossible à rallumer ; Axis Rotometer renvoie des valeurs signées correctes ; aperçu de la grosse batterie corrigé ; ajout des crédits, de l'écran de démarrage et du suivi de progression."],
             ]},
            {"heading": "Où sont publiées les mises à jour officielles",
             "items": [
                "Les annonces Steam du jeu (flux d'actualités de la page du magasin).",
                "Le site officiel approximatelyup.com et le Discord officiel.",
                "La chaîne YouTube du développeur pour les annonces de fonctionnalités.",
             ]},
            {"heading": "Ce qui reste non vérifié", "body": "Le contenu précis des patchs (équilibrage, correctifs, nouvelles pièces) n'est pas vérifié. Nous marquons tout comme non vérifié plutôt que de deviner."},
        ],
    },
    "demo-vs-full": {
        "title": "Démo Approximately Up vs jeu complet",
        "metaTitle": "Démo Approximately Up vs jeu complet : quelle différence ?",
        "metaDescription": "Démo vs version complète Approximately Up : dates de sortie, prix, Workshop et succès — et les différences de contenu encore non vérifiées.",
        "intro": "La démo d'Approximately Up est sortie avant la version complète du 6 août 2026. Voici la comparaison vérifiée, les différences de contenu étant clairement marquées non vérifiées.",
        "sections": [
            {"heading": "Comparaison vérifiée",
             "columns": ["Aspect", "Démo", "Jeu complet"],
             "rows": [
                ["Disponibilité", "Démo (sortie plus tôt, selon la page du magasin)", "Sortie complète le 6 août 2026"],
                ["Prix", "non vérifié", "19,99 $ (remise de lancement de 20 % ; liste 24,99 $)"],
                ["Steam Workshop", "non vérifié", "Pris en charge (selon la page du magasin)"],
                ["Succès", "non vérifié", "22 succès Steam (selon la page du magasin)"],
                ["Multijoueur co-op", "non vérifié", "Solo + co-op en ligne (selon la page du magasin)"],
             ]},
            {"heading": "FAQ démo vs complet",
             "items": [
                ["La démo est-elle gratuite ?", "Nous n'avons pas vérifié le prix/format de la démo — non vérifié."],
                ["La progression de la démo est-elle conservée dans le jeu complet ?", "Non vérifié."],
                ["Quel contenu est exclusif au jeu complet ?", "Non vérifié — les détails de comparaison officiels sont en attente. Le jeu complet ajoute le support du Workshop et 22 succès selon la page du magasin."],
                ["Dois-je d'abord essayer la démo ?", "Pour la plupart des jeux de construction sandbox spatiaux, essayer la démo est un bon moyen de ressentir la boucle construire-s'écraser-reconstruire avant d'acheter — mais les limites exactes de la démo sont non vérifiées."],
             ]},
            {"heading": "Ce qui reste non vérifié", "body": "Le contenu exact de la démo, le transfert de progression et les différences de fonctionnalités ne sont pas vérifiés auprès d'une source officielle. Nous mettrons ce tableau à jour dès confirmation."},
        ],
    },
    "achievements-list": {
        "title": "Liste des succès Approximately Up",
        "metaTitle": "Succès Approximately Up : liste complète (22)",
        "metaDescription": "Approximately Up compte 22 succès Steam. La liste complète des noms est en cours de vérification — voici ce qui est confirmé.",
        "intro": "La page Steam officielle confirme 22 succès. Les noms exacts et conditions de déblocage ne sont pas encore vérifiés ; cette page suit donc le nombre confirmé et marque la liste comme non vérifiée.",
        "sections": [
            {"heading": "Confirmé : 22 succès", "body": "La page Steam liste 22 succès pour Approximately Up. Nous n'avons pas encore vérifié le nom, l'icône et la condition de chaque succès — cette partie est non vérifiée."},
            {"heading": "Liste des succès (non vérifiée)",
             "columns": ["Succès", "Condition"],
             "rows": [
                ["Succès 1–22", "non vérifié — noms et conditions en cours de vérification sur la liste officielle."],
             ]},
            {"heading": "Comment suivre les succès",
             "items": [
                "Utilisez la superposition Steam en jeu pour voir votre progression.",
                "Suivez les annonces Steam officielles — les listes de succès accompagnent parfois les notes de patch.",
                "Nous publierons ici la liste complète vérifiée dès confirmation.",
             ]},
            {"heading": "FAQ des succès",
             "items": [
                ["Combien de succès Approximately Up compte-t-il ?", "22, confirmé sur la page Steam officielle."],
                ["Quels sont les noms des succès ?", "non vérifié — nous vérifions la liste officielle et la publierons une fois confirmée."],
                ["Puis-je obtenir tous les succès en solo ?", "Non vérifié — certains peuvent exiger le co-op, mais nous ne le saurons qu'une fois la liste confirmée."],
             ]},
        ],
    },
    "ships": {
        "title": "Vaisseaux Approximately Up",
        "metaTitle": "Vaisseaux Approximately Up : constructions, idées et designs",
        "metaDescription": "Index du contenu vaisseaux Approximately Up : guide de construction, designs, plans et bases de la construction modulaire.",
        "intro": "Tout sur les vaisseaux d'Approximately Up au même endroit — de votre première construction aux idées de la communauté.",
        "sections": [
            {"heading": "Guides de vaisseaux",
             "items": [
                "Guide de construction — apprenez le processus construire-s'écraser-reconstruire.",
                "Meilleurs designs — points de départ et idées communautaires.",
                "Guide des plans — ce que nous savons des plans et du contenu Workshop.",
                "Mods — support du Workshop et questions sur les mods.",
             ]},
            {"heading": "FAQ des vaisseaux",
             "items": [
                ["Quels vaisseaux puis-je construire ?", "Ils sont entièrement modulaires — boulonnez les pièces comme elles s'assemblent (description officielle). Les listes de pièces précises sont non vérifiées."],
                ["Puis-je voler vers la Lune ?", "Un fil communautaire demande comment ; les mécaniques lunaires sont non vérifiées."],
                ["Puis-je contrôler plusieurs vaisseaux ?", "Un fil communautaire le demande ; non vérifié."],
             ]},
        ],
    },
    "blueprints": {
        "title": "Plans Approximately Up",
        "metaTitle": "Plans Approximately Up : téléchargements et bibliothèque",
        "metaDescription": "Index du contenu plans Approximately Up : comment utiliser les plans, où trouver des designs de vaisseaux, et le Steam Workshop.",
        "intro": "L'index de la bibliothèque de plans — trouvez des designs de vaisseaux, apprenez le flux (non vérifié) des plans et parcourez le Workshop.",
        "sections": [
            {"heading": "Contenu des plans",
             "items": [
                "Guide des plans — ce qui est confirmé et non vérifié sur les plans.",
                "Meilleurs designs — idées et où en trouver plus.",
                "Steam Workshop — le foyer confirmé du contenu communautaire.",
             ]},
            {"heading": "FAQ de l'index des plans",
             "items": [
                ["Où télécharger des plans ?", "Le Steam Workshop est le canal confirmé pour le contenu communautaire ; les mécaniques de téléchargement de plans en jeu sont non vérifiées."],
                ["Comment importer un plan ?", "Non vérifié."],
                ["Puis-je partager mes designs ?", "Non vérifié."],
             ]},
        ],
    },
    "guides": {
        "title": "Guides Approximately Up",
        "metaTitle": "Guides Approximately Up : toutes les pages",
        "metaDescription": "Tous les guides Approximately Up en un index : comment jouer, construction, contrôles, multijoueur, mods, succès et plus.",
        "intro": "L'index complet des guides Approximately Up. Chaque page répond à une question réellement recherchée par les joueurs et marque tout ce qui n'est pas vérifié.",
        "sections": [
            {"heading": "Tous les guides",
             "items": [
                "Comment jouer — la boucle construire-s'écraser-reconstruire pour débutants.",
                "Contrôles — clavier/souris, statut manette et notes sur le remappeur.",
                "Configuration requise — statut des specs et vérification de votre PC.",
                "Multijoueur — co-op en ligne, nombre de joueurs et questions async.",
                "Sortie console — statut PS5/Xbox/Switch.",
                "Mods — Steam Workshop et questions sur les mods.",
                "Notes de mise à jour — faits de lancement et suivi des mises à jour.",
                "Démo vs complet — comparaison vérifiée.",
                "Guide de construction — du premier vaisseau aux grosses constructions.",
                "Câblage et électronique — ce qui est connu, ce qui ne l'est pas.",
                "Guide des plans — statut des plans et Workshop.",
                "Meilleurs designs — idées et designs communautaires.",
                "Liste des succès — 22 succès, liste non vérifiée.",
                "Vaisseaux / Plans / Succès — pages d'index.",
             ]},
            {"heading": "Notre méthode", "body": "Chaque page liste 1 à 2 sources fiables et marque tout ce qui n'est pas vérifié. Nous n'inventons ni chiffres, ni noms, ni mécaniques."},
        ],
    },
    "achievements": {
        "title": "Succès Approximately Up",
        "metaTitle": "Succès Approximately Up : aperçu",
        "metaDescription": "Aperçu des succès Approximately Up : 22 succès Steam confirmés, liste complète en cours de vérification, et comment suivre la progression.",
        "intro": "Le hub des succès d'Approximately Up — nombre confirmé, statut actuel de la liste, et liens vers la page de suivi complet.",
        "sections": [
            {"heading": "22 succès confirmés", "body": "La page Steam confirme 22 succès. La liste complète des noms et conditions est non vérifiée."},
            {"heading": "Contenu des succès",
             "items": [
                "Liste des succès — la page dédiée à la liste complète (non vérifiée).",
                "Steam — consultez la section succès de la page du magasin.",
             ]},
            {"heading": "FAQ aperçu des succès",
             "items": [
                ["Combien y a-t-il de succès ?", "22 (confirmé sur la page Steam)."],
                ["Où est la liste complète ?", "non vérifié — nous vérifions la liste officielle."],
             ]},
        ],
    },
}

TR_DE = {
    "how-to-play": {
        "title": "So spielst du Approximately Up",
        "metaTitle": "So spielst du Approximately Up: kompletter Anfänger-Guide",
        "metaDescription": "Neu bei Approximately Up? Lerne den Bauen-Abstürzen-Neubauen-Loop, modulare Schiffe, Koop-Mehrspieler und Planeten-Erkundung in diesem Anfänger-Guide.",
        "intro": "Approximately Up ist ein Weltraum-Sandbox-Bauspiel, bei dem man Teile zusammenschraubt, abhebt, abstürzt und besser wieder aufbaut. Hier ist der Kern-Loop und was du vor deinem ersten Start wissen solltest.",
        "sections": [
            {"heading": "Der Kern-Loop: bauen, abstürzen, neu bauen", "body": "Die offizielle Beschreibung fasst den Loop in drei Worten zusammen — bauen, abstürzen, neu bauen. Alles andere folgt daraus.",
             "items": [
                ["Fang klein an", "Baue ein Schiff aus allem, was sich lange genug zusammenschrauben lässt, um zu fliegen. Du brauchst kein perfektes Design — nur etwas, das abhebt."],
                ["Montiere Triebwerke und Kabel", "Riesige Triebwerke bringen Bewegung; Kabel und alles dazwischen verbinden deinen Bau. Erwarte anfangs ein chaotisches Layout."],
                ["Testflug", "Heb ab und sieh, was hält. Die ersten Flüge sind Experimente, keine perfekten Flüge."],
                ["Abstürzen (das passiert)", "Abstürze gehören zum Loop. Der offizielle Pitch behandelt sie als normal — Trümmer sind eine Lektion, kein Scheitern."],
                ["Schlauer neu bauen", "Nutze, was du gelernt hast. Jede Iteration zeigt dir, welche Teile halten und welche Kombinationen fliegen."],
             ]},
            {"heading": "Was das Spiel offiziell verspricht", "body": "Aus der offiziellen Steam-Beschreibung:",
             "items": [
                "Erkunde neue Planeten im Koop-Mehrspieler mit deinem vollständig modularen Raumschiff.",
                "Montiere riesige Triebwerke, nervige Kabel und alles dazwischen.",
                "Meistere wilde Missionen und stelle dich den Gefahren des Weltraums.",
                "Spiele solo oder mit einer Crew — und streite dich mit ihr, wie es der offizielle Pitch formuliert.",
             ]},
            {"heading": "Anfänger-FAQ",
             "items": [
                ["Ist Approximately Up ein Mehrspieler-Spiel?", "Ja — die offizielle Store-Seite listet Einzelspieler und Online-Koop-Mehrspieler."],
                ["Brauche ich Ingenieurwissen?", "Nein. Das Spiel basiert auf Versuch und Irrtum: Teile anbauen, fliegen, abstürzen, lernen."],
                ["Gibt es eine Demo?", "Ja — die offizielle Store-Seite listet eine Demo, die vor dem Vollrelease (6. August 2026) erschien."],
                ["Kann ich auf dem Steam Deck spielen?", "Die Kompatibilität ist noch nicht bestätigt. Spieler fragen in den Steam-Foren danach; wir markieren das als unbestätigt, bis es eine offizielle Antwort gibt."],
             ]},
            {"heading": "Was wir noch prüfen müssen", "body": "Konkrete Planeten- und Missionsnamen sowie detaillierte Mechanik-Guides (Baupläne, Verkabelung, Radar, Zeitreise) sind noch nicht gegen offizielle Quellen geprüft. Wir markieren sie als unbestätigt und aktualisieren diese Seite, sobald offizielle Informationen vorliegen."},
        ],
    },
    "ship-building-guide": {
        "title": "Approximately Up Schiffsbau-Guide",
        "metaTitle": "Approximately Up Schiffsbau-Guide: vom ersten Schiff zu großen Bauten",
        "metaDescription": "Lerne, in Approximately Up Schiffe zu bauen: der modulare Bauen-Abstürzen-Neu bauen-Prozess, Triebwerke und Kabel, plus Community-Bedürfnisse wie Mondreisen und Radar.",
        "intro": "Schiffsbau ist das Herz von Approximately Up. Der offizielle Pitch ist einfach: Teile zusammenschrauben, bis sie fliegen, dann schlauer neu bauen. Dieser Guide erklärt den Prozess, ohne noch unbestätigte Teile-Werte zu erfinden.",
        "sections": [
            {"heading": "Baue dein erstes Schiff", "body": "Basierend auf der offiziellen Beschreibung (modulare Teile, Triebwerke, Kabel, bauen-abstürzen-neu bauen) ist hier der Ablauf:",
             "items": [
                ["Sammle Teile", "Sammle verfügbare Teile und schraube sie zusammen. Der offizielle Pitch sagt, jeder Bau 'lässt sich lange genug zusammenschrauben, um zu fliegen' — fang dort an."],
                ["Füge Triebwerke hinzu", "Montiere Triebwerke für Bewegung. Die offizielle Beschreibung hebt 'riesige Triebwerke' als Kern des Spielgefühls hervor."],
                ["Verlege Kabel", "Verbinde deinen Bau mit Kabeln — 'nervige Kabel' gehören zur Erfahrung. Erwarte unordentliche Verkabelung."],
                ["Testflug", "Heb ab. Dein erstes Schiff muss nicht schön sein; es muss dir zeigen, was hält."],
                ["Abstürzen und iterieren", "Baue mit dem Gelernten neu. Der Loop ist bauen → abstürzen → neu bauen."],
             ]},
            {"heading": "Design-Prinzipien (offiziell ausgerichtet)",
             "items": [
                "Vollständig modulares Schiff: alles kann zwischen Flügen neu angeordnet werden.",
                "Gewicht vs. Schub abwägen — schwerere Schiffe brauchen mehr Schub (konkrete Zahlen unbestätigt).",
                "Ersatzteile bereithalten: Abstürze sind eingeplant.",
                "Koop einplanen: Wenn du mit einer Crew spielst, verteilt Rollen (Pilot, Baumeister, Ingenieur).",
             ]},
            {"heading": "Community-Tutorials, die gewünscht werden",
             "items": [
                ["Wie komme ich zum Mond?", "Ein echtes Steam-Forum-Thread — Spieler wollen einen Mondreise-Guide. Die genauen Mond-Mechaniken sind unbestätigt."],
                ["Radar-Monitor/-Gerät für Anfänger", "Ein echtes Steam-Forum-Thread — Spieler wollen ein Radar-Geräte-Tutorial. Die Radar-Mechaniken sind unbestätigt."],
             ]},
            {"heading": "Was noch unbestätigt ist", "body": "Die Patch-Notizen oben sind aus offiziellen Steam-Ankündigungen verifiziert. Details zu Vorab-Builds und nicht angekündigten Änderungen bleiben unbestätigt."}
        ],
    },
    "blueprints-guide": {
        "title": "Approximately Up Bauplan-Guide",
        "metaTitle": "Approximately Up Baupläne: herunterladen, teilen & nutzen",
        "metaDescription": "Approximately Up Baupläne: was wir über das Finden und Nutzen von Bauplänen wissen, Steam-Workshop-Support und was noch unbestätigt ist.",
        "intro": "Baupläne gehören zu den meistgesuchten Approximately-Up-Themen. Die offiziellen Bauplan-Mechaniken (Import, Export, Teilen) sind noch nicht verifiziert, daher deckt diese Seite ab, was bestätigt ist und was nicht.",
        "sections": [
            {"heading": "Bauplan-Details: unbestätigt", "body": "Import-, Export- und Teilen-Mechaniken für Baupläne stehen auf unserer unbestätigten Liste — wir haben sie noch nicht gegen eine offizielle Quelle bestätigt. Diese Seite wird erweitert, sobald zuverlässige Informationen verifiziert sind."},
            {"heading": "Schiffsdesigns heute finden", "body": "Während offizielle Bauplan-Tools unbestätigt sind, ist der Steam-Workshop der bestätigte Ort für Community-Inhalte:",
             "items": [
                ["Öffne den Steam-Workshop für Approximately Up", "Von der Community hochgeladene Inhalte werden dort gehostet (Workshop-Support ist auf der Store-Seite bestätigt)."],
                ["Durchstöbere Schiffe und Bauten", "Suche nach Designs, die andere Spieler geteilt haben."],
                ["Abonnieren", "Abonnieren speichert Inhalte in deiner Bibliothek."],
                ["Im Spiel prüfen", "Sieh, wie abonnierte Inhalte im Spiel erscheinen — genaue Schritte unbestätigt."],
             ]},
            {"heading": "Bauplan-FAQ",
             "items": [
                ["Kann ich in Approximately Up Baupläne herunterladen?", "Unbestätigt. Workshop-Inhalte sind der nächstbeste bestätigte Kanal."],
                ["Kann ich meine Schiffsdesigns teilen?", "Unbestätigt. Wir bestätigen den genauen Teilen-Ablauf, sobald er verifiziert ist."],
                ["Sind Baupläne dasselbe wie Workshop-Objekte?", "Nicht unbedingt — die Beziehung zwischen Bauplänen im Spiel und Workshop-Objekten ist unbestätigt."],
             ]},
            {"heading": "Quellen im Blick behalten", "body": "Wir verifizieren die Bauplan-Mechaniken über offizielle Kanäle (Steam-Ankündigungen, offizielle Website, Discord) und aktualisieren diese Seite. Hier wird nichts erfunden."},
        ],
    },
    "wiring-electronics": {
        "title": "Approximately Up Verkabelungs- & Elektronik-Guide",
        "metaTitle": "Approximately Up Verkabelung & Elektronik: was wir wissen",
        "metaDescription": "Verkabelung und Elektronik in Approximately Up: Kabel in Bauten, Community-Fragen zur Vakuumröhren-Ära und zum Remapper — mit markierten unbestätigten Details.",
        "intro": "Verkabelung und Elektronik sind ein großes Community-Thema — aber offizielle Details sind dünn. Diese Seite sammelt, was verifiziert ist und was Spieler fragen, wobei alles Unbestätigte klar markiert ist.",
        "sections": [
            {"heading": "Offizielle Informationen sind begrenzt", "body": "Die offizielle Beschreibung erwähnt Kabel als Teil des modularen Baus ('nervige Kabel, und alles dazwischen'), aber detaillierte Verkabelungs- und Schaltkreis-Mechaniken sind noch nicht verifiziert. Wir markieren sie als unbestätigt."},
            {"heading": "Community-Threads (echte Fragen von Spielern)",
             "items": [
                ["Können wir bitte über die Vakuumröhren-Ära der Elektronik hinausgehen?", "Ein Steam-Forum-Thread zur Elektronik-Progression/Teile-Ära — deutet auf ein Frühzeit-Elektronik-Thema hin; genaue Mechaniken unbestätigt."],
                ["Werte im Remapper lassen sich nicht setzen", "Ein Steam-Forum-Thread über Probleme beim Setzen von Werten im Remapper/Constant — der genaue Ablauf ist unbestätigt."],
             ]},
            {"heading": "Was wir sicher sagen können",
             "items": [
                "Kabel sind offiziell Teil des modularen Schiffsbau-Gefühls.",
                "Elektronik scheint ein Fortschrittsbereich zu sein (die Community erwähnt eine frühe 'Vakuumröhren-Ära').",
                "Es gibt Werkzeuge zum Einstellen von Parametern/Werten im Spiel (Remapper), aber die genaue Nutzung ist unbestätigt.",
             ]},
            {"heading": "Verkabelungs- & Elektronik-FAQ",
             "items": [
                ["Wie funktioniert Verkabelung in Approximately Up?", "Unbestätigt. Wir veröffentlichen einen Guide, sobald offizielle oder zuverlässig gegengeprüfte Informationen vorliegen."],
                ["Was sind die Elektronik-Stufen?", "Ein Community-Thread erwähnt eine 'Vakuumröhren-Ära'; genaue Stufen und Freischaltungen sind unbestätigt."],
                ["Warum kann ich im Remapper keine Werte setzen?", "Ein Community-Thread meldet dieses Problem; der offizielle Ablauf ist unbestätigt."],
             ]},
        ],
    },
    "controls": {
        "title": "Approximately Up Steuerung",
        "metaTitle": "Approximately Up Steuerung: Tastatur, Maus & Controller-Status",
        "metaDescription": "Approximately Up Steuerungs-Guide: was wir über Tastatur/Maus, Controller-Support und den In-Game-Remapper wissen — plus was noch unbestätigt ist.",
        "intro": "Controller-Support ist direkt nach dem Release eine der meistgestellten Fragen in der Steam-Community. Hier ist, was wir bestätigen können, was Spieler fragen und was noch unbestätigt ist.",
        "sections": [
            {"heading": "Was wir wissen (verifiziert)",
             "items": [
                ["Plattform", "Das Spiel ist auf dem PC (Steam). Tastatur und Maus sind die Standardeingabe."],
                ["Controller-Support", "Noch nicht vom Entwickler bestätigt. Ein Steam-Forum-Thread fragt 'Controller Support in the Future?', was darauf hindeutet, dass der volle Support zum Launch nicht bestätigt ist."],
                ["In-Game-Remapper", "Spieler diskutieren den Remapper — ein Community-Thread meldet Probleme beim Setzen von Werten. Den genauen Mapping-Ablauf markieren wir als unbestätigt."],
             ]},
            {"heading": "Steuerung jetzt einrichten",
             "items": [
                "Öffne die In-Game-Einstellungen und prüfe den Bereich Eingabe/Steuerung für das aktuelle Tastenlayout.",
                "Nutze den In-Game-Remapper zum Umbelegen; wenn Werte nicht greifen, prüfe den Community-Thread und die Entwickler-Notizen.",
                "Für Controller-Updates folge dem offiziellen Discord und den Steam-Ankündigungen.",
             ]},
            {"heading": "Unbestätigt: vollständige Tastenbelegung", "body": "Die vollständige offizielle Tastenbelegung (Bewegung, Kamera, Bau-Menü, Triebwerkssteuerung) ist noch nicht gegen eine offizielle Quelle verifiziert. Wir markieren sie als unbestätigt und veröffentlichen die Tabelle nach Bestätigung."},
            {"heading": "Steuerungs-FAQ",
             "items": [
                ["Unterstützt Approximately Up Controller?", "Noch nicht bestätigt. Die Community fragt; wir markieren das als unbestätigt, bis der Entwickler oder eine offizielle Quelle es bestätigt."],
                ["Kann ich Tasten umbelegen?", "Es gibt einen In-Game-Remapper. Einige Spieler melden Probleme beim Setzen von Werten; der genaue Ablauf ist unbestätigt."],
                ["Gibt es ein Steam-Deck-Layout?", "Die Steam-Deck-Kompatibilität selbst ist in der Community noch offen — das Layout ist unbestätigt."],
             ]},
        ],
    },
    "multiplayer": {
        "title": "Approximately Up Mehrspieler-Guide",
        "metaTitle": "Approximately Up Mehrspieler: Koop, Spielerzahl & Crossplay",
        "metaDescription": "Approximately Up Mehrspieler erklärt: Online-Koop, wie viele Spieler, ob es asynchronen Mehrspieler gibt, und was noch unbestätigt ist.",
        "intro": "Approximately Up ist offiziell ein Einzelspieler- und Online-Koop-Spiel. Diese Seite beantwortet die Mehrspieler-Fragen, die Spieler wirklich stellen, und markiert, was wir noch nicht verifizieren können.",
        "sections": [
            {"heading": "Offizieller Status", "body": "Die offizielle Steam-Store-Seite listet 'Einzelspieler' und 'Online-Koop' als unterstützte Modi. Das Konzept des Spiels dreht sich um eine Crew, die in einem modularen Schiff gemeinsam Planeten erkundet."},
            {"heading": "Mehrspieler-FAQ",
             "items": [
                ["Wie viele Spieler können zusammen spielen?", "Die genaue Spielerzahl ist in unserer Wissensbasis nicht verifiziert — wir markieren sie als unbestätigt."],
                ["Gibt es Online-Koop?", "Ja — Online-Koop-Mehrspieler ist auf der offiziellen Steam-Store-Seite gelistet."],
                ["Gibt es plattformübergreifenden Mehrspieler?", "Unbestätigt. Das Spiel ist derzeit auf dem PC (Steam); Konsolenversionen sind nicht angekündigt, daher ist Crossplay unbestätigt."],
                ["Gibt es asynchronen Mehrspieler?", "Nicht bestätigt. Ein Steam-Forum-Thread fragt nach 'Asynchronous Multiplayer', was nahelegt, dass es noch keine offizielle Funktion ist — unbestätigt."],
                ["Kann ich solo spielen?", "Ja — Einzelspieler ist als unterstützter Modus gelistet."],
             ]},
            {"heading": "Was die Community fragt",
             "items": [
                "Asynchroner Mehrspieler — ob Spieler einen asynchronen Modus erwarten.",
                "Spielerzahl / 'wie viele Spieler' ist ein Top-Suchbedürfnis; wir veröffentlichen die verifizierte Zahl, sobald sie verfügbar ist.",
             ]},
            {"heading": "Was noch unbestätigt ist", "body": "Das genaue Spielerlimit, der Einladungsablauf, Hosting-Details und Crossplay sind noch nicht gegen offizielle Quellen verifiziert. Wir aktualisieren diese Seite, sobald sie bestätigt sind."},
        ],
    },
    "best-ship-designs": {
        "title": "Approximately Up beste Schiffsdesigns",
        "metaTitle": "Approximately Up Schiffs-Ideen & beste Designs",
        "metaDescription": "Approximately Up Schiffsdesign-Ideen: Ausgangspunkte für eigene Bauten, Community-Designfragen und wo man weitere Designs findet.",
        "intro": "Auf der Suche nach Schiffs-Ideen? Diese Seite sammelt Design-Ausgangspunkte basierend auf dem offiziellen Bauen-Abstürzen-Neu bauen-Konzept, plus Community-Fragen, die prägen, was Spieler bauen wollen.",
        "sections": [
            {"heading": "Design-Ausgangspunkte (Inspiration, keine offiziellen Specs)",
             "items": [
                "Triebwerkslastiger Flitzer: montiere riesige Triebwerke und akzeptiere, dass die Kontrolle später kommt.",
                "Nützlicher Transporter: bevorzuge Fracht und Missions-Teile gegenüber Tempo — Missionen brauchen Kapazität (Details unbestätigt).",
                "Koop-Crew-Schiff: gestalte Platz für eine Crew, die gemeinsam Planeten erkundet.",
                "Chaotisches Kabel-Build: nimm 'nervige Kabel' an — Verkabelung gehört zum Charme (Verkabelungs-Mechaniken unbestätigt).",
             ]},
            {"heading": "Community-Designfragen",
             "items": [
                ["Trajektorien-Krümmungsmesser", "Ein Steam-Forum-Thread über ein Trajektorien-Werkzeug — Spieler wollen bessere Flugwerkzeuge; offizieller Status unbestätigt."],
                ["Mods für mehrere Schiffe?", "Ein Steam-Forum-Thread über die Steuerung mehrerer Schiffe — unbestätigt."],
             ]},
            {"heading": "Wo man weitere Designs findet",
             "items": [
                "Steam-Workshop für Approximately Up (Support bestätigt).",
                "Der offizielle YouTube-Kanal für Bauten aus Trailern.",
                "Steam-Community-Diskussionen für Screenshots und Ideen von Spielern.",
             ]},
            {"heading": "Was noch unbestätigt ist", "body": "Konkrete Teile-Werte, Baupläne benannter Designs und jede 'beste'-Rangliste sind nicht verifiziert. Wir halten diese Seite als Inspiration plus verifizierte Quellen und markieren alles andere als unbestätigt."},
        ],
    },
    "system-requirements": {
        "title": "Approximately Up Systemanforderungen",
        "metaTitle": "Approximately Up Systemanforderungen (PC)",
        "metaDescription": "Approximately Up PC-Systemanforderungen: Mindest- und empfohlene Specs sind noch nicht verifiziert — hier ist, was wir wissen und wie man die Kompatibilität prüft.",
        "intro": "Spieler wollen eine klare Antwort, ob ihr PC Approximately Up ausführen kann. Die offiziellen Mindest- und empfohlenen Specs sind noch unbestätigt, daher zeigt diese Seite, was wir wissen und was nicht.",
        "sections": [
            {"heading": "Offizielle Specs: unbestätigt", "body": "Wir haben die offiziellen Mindest- und empfohlenen Systemanforderungen noch nicht gegen eine offizielle Quelle verifiziert. Statt Zahlen zu erfinden, markieren wir die Spec-Tabelle als unbestätigt und füllen sie, sobald sie bestätigt ist (Steam-Store-Seite oder offizielle Website)."},
            {"heading": "Spec-Tabelle (unbestätigt)",
             "columns": ["Element", "Minimum", "Empfohlen"],
             "rows": [
                ["Betriebssystem", "unbestätigt", "unbestätigt"],
                ["Prozessor", "unbestätigt", "unbestätigt"],
                ["Arbeitsspeicher", "unbestätigt", "unbestätigt"],
                ["Grafikkarte", "unbestätigt", "unbestätigt"],
                ["Speicherplatz", "unbestätigt", "unbestätigt"],
                ["DirectX", "unbestätigt", "unbestätigt"],
             ]},
            {"heading": "So prüfst du deinen PC",
             "items": [
                "Öffne Steam und prüfe die Store-Seite des Spiels — Systemanforderungen erscheinen dort normalerweise, sobald sie veröffentlicht sind.",
                "Vergleiche CPU/GPU/RAM mit den offiziellen Zahlen, sobald wir sie veröffentlichen.",
                "Steam Deck: Die Kompatibilität ist eine offene Community-Frage ('Playable on Deck?'); wir markieren sie als unbestätigt.",
             ]},
            {"heading": "Systemanforderungen-FAQ",
             "items": [
                ["Kann mein PC Approximately Up ausführen?", "Noch nicht bestätigt — offizielle Mindest-/empfohlene Specs sind unbestätigt. Prüfe die Steam-Store-Seite, wenn der Entwickler sie veröffentlicht."],
                ["Läuft Approximately Up auf dem Steam Deck?", "Nicht bestätigt. Ein Steam-Forum-Thread fragt 'Playable on Deck?' — Kompatibilität ist unbestätigt, bis es eine offizielle Antwort gibt."],
                ["Ist es anspruchsvoll?", "Es ist ein Weltraum-Sandbox-Bauspiel mit modularen physikbasierten Schiffen; wir melden verifizierte Zahlen, sobald sie verfügbar sind."],
             ]},
        ],
    },
    "console-release": {
        "title": "Approximately Up Konsolen-Release: PS5-, Xbox- & Switch-Status",
        "metaTitle": "Approximately Up Konsolen-Release-Datum (PS5, Xbox, Switch)",
        "metaDescription": "Kommt Approximately Up für PS5, Xbox oder Switch? Noch keine offizielle Ankündigung — hier ist der Konsolen-Status und wie man offizielle News verfolgt.",
        "intro": "'Approximately Up PS5 Release-Datum', 'Xbox-Release' und 'Switch-Release' sind Suchen, die selbst das Wiki des Spiels nicht beantwortet. Die ehrliche Antwort heute: keine verifizierte offizielle Konsolen-Ankündigung — hier ist die Statusseite.",
        "sections": [
            {"heading": "Konsolen-Status (Stand 09.08.2026)",
             "items": [
                ["Aktuelle Plattformen", "Nur PC (Steam). Das Spiel erschien am 6. August 2026 auf Steam."],
                ["PS5", "unbestätigt — keine verifizierte offizielle Ankündigung einer PlayStation-5-Version."],
                ["Xbox", "unbestätigt — keine verifizierte offizielle Ankündigung einer Xbox-Version."],
                ["Nintendo Switch", "unbestätigt — keine verifizierte offizielle Ankündigung einer Switch-Version."],
                ["Offizielle Stellungnahme", "Wir haben keine offizielle Stellungnahme des Entwicklers zu Konsolenplänen verifiziert; unbestätigt, wird aktualisiert, sobald es eine gibt."],
             ]},
            {"heading": "So bleibst du informiert",
             "items": [
                "Folge der offiziellen Website approximatelyup.com und dem offiziellen Discord (discord.gg/approximatelyup).",
                "Beobachte den YouTube-Kanal des Entwicklers (@ApproximatelyUp) und TikTok (@approximatelyup) für Ankündigungen.",
                "Prüfe die Steam-Store-Seite — Konsolen-News werden dort meist zuerst angekündigt.",
             ]},
            {"heading": "Konsolen-FAQ",
             "items": [
                ["Gibt es Approximately Up für PS5?", "Nicht angekündigt — unbestätigt. Es gibt noch keine verifizierte offizielle Stellungnahme."],
                ["Gibt es Approximately Up für Xbox?", "Nicht angekündigt — unbestätigt."],
                ["Gibt es Approximately Up für Nintendo Switch?", "Nicht angekündigt — unbestätigt."],
                ["Wann ist das Konsolen-Release-Datum?", "Es gibt noch kein Datum. Diese Seite wird aktualisiert, sobald eine offizielle Ankündigung verifiziert ist."],
             ]},
            {"heading": "Warum diese Seite existiert", "body": "Der Konsolen-Release ist eine der Fragen mit der höchsten Suchintention für dieses Spiel, aber keine zuverlässige Quelle hat sie beantwortet. Diese Seite gibt den verifizierten Status (nur PC) wieder und verfolgt künftige Ankündigungen, statt ein Datum zu erfinden."},
        ],
    },
    "mods": {
        "title": "Approximately Up Mods-Guide",
        "metaTitle": "Approximately Up Mods: Steam Workshop, Installation & Mod-Fragen",
        "metaDescription": "Approximately Up Mods erklärt: Steam-Workshop-Support, wie man Mods abonniert, und Community-Mod-Fragen wie mehrere Schiffe.",
        "intro": "Approximately Up unterstützt den Steam Workshop, was das Finden und Installieren von Mods einfach macht. Hier ist, was bestätigt ist und was Spieler anfragen.",
        "sections": [
            {"heading": "Mods aus dem Steam Workshop holen", "body": "Workshop-Support ist auf der offiziellen Store-Seite bestätigt. Der Standard-Ablauf:",
             "items": [
                ["Workshop öffnen", "Öffne auf der Steam-Store-Seite des Spiels den Workshop-Tab (oder den Workshop-Community-Hub)."],
                ["Stöbern und abonnieren", "Finde einen Mod oder ein Objekt und drücke auf Abonnieren — Steam lädt es automatisch herunter."],
                ["Spiel starten", "Öffne Approximately Up und prüfe das Mods/Inhalte-Menü des Spiels, um abonnierte Objekte zu sehen."],
                ["Aktivieren, was du willst", "Schalte die gewünschten Mods ein. Details des In-Game-Mod-Menüs sind unbestätigt."],
             ]},
            {"heading": "Was die Community fragt",
             "items": [
                "Mods für mehrere Schiffe? — ein echtes Steam-Forum-Thread; Multi-Schiff-Support per Mods ist unbestätigt.",
                "Cheat-Engine-Suchen gibt es bei vielen Spielen; wir bieten keine Cheats, nur verifizierte Mod-Informationen.",
             ]},
            {"heading": "Mods-FAQ",
             "items": [
                ["Unterstützt Approximately Up Mods?", "Offiziell unterstützt es den Steam Workshop (laut Store-Seite). Vollständige Modding-Dokumentation ist unbestätigt."],
                ["Wie installiere ich Mods?", "Abonniere über den Steam Workshop; Steam übernimmt die Installation. In-Game-Schritte sind unbestätigt."],
                ["Können Mods mich mehrere Schiffe steuern lassen?", "Ein Community-Thread fragt danach; kein verifizierter Mod bietet es bisher — unbestätigt."],
             ]},
            {"heading": "Was noch unbestätigt ist", "body": "Exakte Workshop-Funktionen, Mod-Richtlinien und ob Mods Erfolge oder Mehrspieler beeinflussen, sind noch nicht verifiziert. Wir aktualisieren diese Seite, sobald offizielle Dokumentation bestätigt ist."},
        ],
    },
    "patch-notes": {
        "title": "Approximately Up Patchnotes",
        "metaTitle": "Approximately Up Patchnotes & Update-Verlauf",
        "metaDescription": "Approximately Up Patchnotes und Update-Verlauf: Launch-Infos, wo offizielle Updates erscheinen, und unser verfolgtes Changelog (unbestätigte Punkte markiert).",
        "intro": "Approximately Up erschien am 6. August 2026. Diese Seite verfolgt offizielle Patchnotes und Updates — alles Unbestätigte ist klar markiert.",
        "sections": [
            {"heading": "Launch-Fakten (verifiziert)",
             "items": [
                ["Release-Datum", "6. August 2026 (Steam-Vollrelease)."],
                ["Demo", "Eine Demo erschien vor dem Vollrelease."],
                ["Preis", "19,99 $ zum Launch (20 % Rabatt; Listenpreis 24,99 $)."],
             ]},
            {"heading": "Update-Zeitlinie (via Steam verifiziert)", "body": "Patch-Notizen aus offiziellen Steam-Ankündigungen verifiziert (August 2026):",
             "items": [
                ["2026-08-12", "1.0.010 — Workshop-Sortierung 'Am beliebtesten', Seitenladen und fehlende Ergebnisse behoben; Suchübersicht verbessert."],
                ["2026-08-11", "1.0.009 — Frame Quarter With Ports verbessert (Ports spiegeln sich über die Kette, A–D-Beschriftung konsistent); Geometrie von Middle Window, Small Switch und Small Button behoben."],
                ["2026-08-10", "1.0.008 — Axis-Rotometer-Hitbox und restliche Probleme behoben; Plasma-Kabel lackierbar; Autohemisphere-Solarpanels kehren nach Fly Mode zurück; Kabelhalter lackierbar."],
                ["2026-08-09", "1.0.007 — Metal-Geräte-Kompatibilität behoben; Standard-Tastenzuordnung korrigiert (mittlere Maustaste für 'Komponente aufnehmen'); Tippfehler in Rohrbeschreibung korrigiert; mehr Hinweise."],
                ["2026-08-08", "1.0.006 — Fuse Box ließ sich nicht wieder einschalten; Axis Rotometer gibt nun korrekt vorzeichenbehaftete lokale Achsenwerte aus; Vorschau der Large Disposable Battery behoben; Credits, Startbildschirm und Zielverfolgung hinzugefügt."],
             ]},
            {"heading": "Wo offizielle Updates erscheinen",
             "items": [
                "Steam-Ankündigungen für das Spiel (News-Feed auf der Store-Seite).",
                "Die offizielle Website approximatelyup.com und der offizielle Discord.",
                "Der YouTube-Kanal des Entwicklers für Feature-Ankündigungen.",
             ]},
            {"heading": "Was noch unbestätigt ist", "body": "Konkreter Patch-Inhalt (Balance-Änderungen, Fixes, neue Teile) ist nicht verifiziert. Wir markieren alles als unbestätigt, statt zu raten."},
        ],
    },
    "demo-vs-full": {
        "title": "Approximately Up Demo vs. Vollversion",
        "metaTitle": "Approximately Up Demo vs. Vollversion: Was ist der Unterschied?",
        "metaDescription": "Approximately Up Demo vs. Vollversion: Release-Daten, Preis, Workshop und Erfolge — und welche Inhaltsunterschiede noch unbestätigt sind.",
        "intro": "Die Approximately-Up-Demo erschien vor dem Vollrelease am 6. August 2026. Hier ist der verifizierte Vergleich, wobei Inhaltsunterschiede klar als unbestätigt markiert sind.",
        "sections": [
            {"heading": "Verifizierter Vergleich",
             "columns": ["Aspekt", "Demo", "Vollversion"],
             "rows": [
                ["Verfügbarkeit", "Demo (früher erschienen, laut Store-Seite)", "Vollrelease am 6. August 2026"],
                ["Preis", "unbestätigt", "19,99 $ (20 % Launch-Rabatt; Listenpreis 24,99 $)"],
                ["Steam Workshop", "unbestätigt", "Unterstützt (laut Store-Seite)"],
                ["Erfolge", "unbestätigt", "22 Steam-Erfolge (laut Store-Seite)"],
                ["Koop-Mehrspieler", "unbestätigt", "Einzelspieler + Online-Koop (laut Store-Seite)"],
             ]},
            {"heading": "Demo-vs.-Vollversion-FAQ",
             "items": [
                ["Ist die Demo kostenlos?", "Wir haben Preis/Modell der Demo nicht verifiziert — unbestätigt."],
                ["Wird der Demo-Fortschritt in die Vollversion übernommen?", "Unbestätigt."],
                ["Welche Inhalte gibt es nur in der Vollversion?", "Unbestätigt — offizielle Vergleichsdetails stehen aus. Die Vollversion fügt laut Store-Seite Workshop-Support und 22 Erfolge hinzu."],
                ["Sollte ich zuerst die Demo ausprobieren?", "Bei den meisten Weltraum-Sandbox-Bauspielen ist die Demo ein guter Weg, den Bauen-Abstürzen-Neu bauen-Loop vor dem Kauf zu spüren — aber die genauen Demo-Inhalte sind unbestätigt."],
             ]},
            {"heading": "Was noch unbestätigt ist", "body": "Exakter Demo-Inhalt, Fortschrittsübertragung und Funktionsunterschiede sind nicht gegen eine offizielle Quelle verifiziert. Wir aktualisieren diese Tabelle, sobald sie bestätigt sind."},
        ],
    },
    "achievements-list": {
        "title": "Approximately Up Erfolgsliste",
        "metaTitle": "Approximately Up Erfolge: vollständige Liste (22)",
        "metaDescription": "Approximately Up hat 22 Steam-Erfolge. Die vollständige Namensliste wird noch verifiziert — hier ist, was bestätigt ist.",
        "intro": "Die offizielle Steam-Store-Seite bestätigt 22 Erfolge. Die genauen Namen und Freischaltbedingungen sind noch nicht verifiziert, daher verfolgt diese Seite die bestätigte Zahl und markiert die Liste als unbestätigt.",
        "sections": [
            {"heading": "Bestätigt: 22 Erfolge", "body": "Die Steam-Store-Seite listet 22 Erfolge für Approximately Up. Wir haben noch nicht jeden Namen, jedes Icon und jede Bedingung verifiziert — dieser Teil ist unbestätigt."},
            {"heading": "Erfolgsliste (unbestätigt)",
             "columns": ["Erfolg", "Bedingung"],
             "rows": [
                ["Erfolg 1–22", "unbestätigt — Namen und Bedingungen werden gegen die offizielle Liste verifiziert."],
             ]},
            {"heading": "So verfolgst du Erfolge",
             "items": [
                "Nutze das Steam-Overlay im Spiel, um deinen Fortschritt zu sehen.",
                "Folge den offiziellen Steam-Ankündigungen — Erfolgslisten erscheinen manchmal mit Patchnotes.",
                "Wir veröffentlichen die vollständige verifizierte Liste hier, sobald sie bestätigt ist.",
             ]},
            {"heading": "Erfolge-FAQ",
             "items": [
                ["Wie viele Erfolge hat Approximately Up?", "22, bestätigt auf der offiziellen Steam-Store-Seite."],
                ["Wie lauten die Erfolgsnamen?", "unbestätigt — wir verifizieren die offizielle Liste und veröffentlichen sie nach Bestätigung."],
                ["Kann ich alle Erfolge im Einzelspieler schaffen?", "Unbestätigt — einige könnten Koop erfordern, aber wir wissen es erst, wenn die Liste bestätigt ist."],
             ]},
        ],
    },
    "ships": {
        "title": "Approximately Up Schiffe",
        "metaTitle": "Approximately Up Schiffe: Bauten, Ideen & Designs",
        "metaDescription": "Index der Approximately-Up-Schiffsinhalte: Bau-Guide, Schiffsdesigns, Baupläne und die Grundlagen des modularen Schiffsbaus.",
        "intro": "Alles über Approximately-Up-Schiffe an einem Ort — vom ersten Bau bis zu Community-Design-Ideen.",
        "sections": [
            {"heading": "Schiffs-Guides",
             "items": [
                "Schiffsbau-Guide — lerne den Bauen-Abstürzen-Neu bauen-Prozess.",
                "Beste Schiffsdesigns — Design-Ausgangspunkte und Community-Ideen.",
                "Bauplan-Guide — was wir über Baupläne und Workshop-Inhalte wissen.",
                "Mods — Workshop-Support und Mod-Fragen.",
             ]},
            {"heading": "Schiffe-FAQ",
             "items": [
                ["Welche Schiffe kann ich bauen?", "Sie sind vollständig modular — du schraubst Teile zusammen, wie sie passen (offizielle Beschreibung). Konkrete Teilelisten sind unbestätigt."],
                ["Kann ich zum Mond fliegen?", "Ein Community-Thread fragt wie; die Mond-Mechaniken sind unbestätigt."],
                ["Kann ich mehrere Schiffe steuern?", "Ein Community-Thread fragt danach; unbestätigt."],
             ]},
        ],
    },
    "blueprints": {
        "title": "Approximately Up Baupläne",
        "metaTitle": "Approximately Up Baupläne: Downloads & Bibliothek",
        "metaDescription": "Index der Approximately-Up-Bauplaninhalte: Baupläne nutzen, Schiffsdesigns finden und der Steam Workshop.",
        "intro": "Der Index der Bauplan-Bibliothek — Schiffsdesigns finden, den (unbestätigten) Bauplan-Ablauf lernen und den Workshop durchstöbern.",
        "sections": [
            {"heading": "Bauplan-Inhalte",
             "items": [
                "Bauplan-Guide — was über Baupläne bestätigt und unbestätigt ist.",
                "Beste Schiffsdesigns — Design-Ideen und wo man mehr findet.",
                "Steam Workshop — die bestätigte Heimat der Community-Inhalte.",
             ]},
            {"heading": "Bauplan-Index-FAQ",
             "items": [
                ["Wo kann ich Baupläne herunterladen?", "Der Steam Workshop ist der bestätigte Kanal für Community-Inhalte; die In-Game-Download-Mechaniken für Baupläne sind unbestätigt."],
                ["Wie importiere ich einen Bauplan?", "Unbestätigt."],
                ["Kann ich meine Designs teilen?", "Unbestätigt."],
             ]},
        ],
    },
    "guides": {
        "title": "Approximately Up Guides",
        "metaTitle": "Approximately Up Guides: alle Seiten",
        "metaDescription": "Alle Approximately-Up-Guides in einem Index: Spielanleitung, Schiffsbau, Steuerung, Mehrspieler, Mods, Erfolge und mehr.",
        "intro": "Der komplette Guide-Index für Approximately Up. Jede Seite beantwortet eine Frage, die Spieler wirklich suchen, und markiert alles Unbestätigte.",
        "sections": [
            {"heading": "Alle Guides",
             "items": [
                "So spielst du — der Bauen-Abstürzen-Neu bauen-Loop für Anfänger.",
                "Steuerung — Tastatur/Maus, Controller-Status und Remapper-Notizen.",
                "Systemanforderungen — Spec-Status und wie du deinen PC prüfst.",
                "Mehrspieler — Online-Koop, Spielerzahl und Async-Fragen.",
                "Konsolen-Release — PS5/Xbox/Switch-Status.",
                "Mods — Steam Workshop und Mod-Fragen.",
                "Patchnotes — Launch-Fakten und Update-Verfolgung.",
                "Demo vs. Vollversion — verifizierter Vergleich.",
                "Schiffsbau-Guide — vom ersten Schiff zu großen Bauten.",
                "Verkabelung & Elektronik — was bekannt ist, was nicht.",
                "Bauplan-Guide — Bauplan-Status und Workshop.",
                "Beste Schiffsdesigns — Ideen und Community-Designs.",
                "Erfolgsliste — 22 Erfolge, Liste unbestätigt.",
                "Schiffe / Baupläne / Erfolge — Index-Seiten.",
             ]},
            {"heading": "So arbeiten wir", "body": "Jede Seite listet 1–2 zuverlässige Quellen und markiert alles Nichtverifizierte. Wir erfinden keine Zahlen, Namen oder Mechaniken."},
        ],
    },
    "achievements": {
        "title": "Approximately Up Erfolge",
        "metaTitle": "Approximately Up Erfolge: Überblick",
        "metaDescription": "Approximately-Up-Erfolge im Überblick: 22 Steam-Erfolge bestätigt, vollständige Liste in Prüfung, und wie man Fortschritt verfolgt.",
        "intro": "Das Erfolge-Hub für Approximately Up — bestätigte Zahl, aktueller Listenstatus und Links zur vollständigen Tracking-Seite.",
        "sections": [
            {"heading": "22 Erfolge bestätigt", "body": "Die Steam-Store-Seite bestätigt 22 Erfolge. Die vollständige Liste der Namen und Bedingungen ist unbestätigt."},
            {"heading": "Erfolge-Inhalte",
             "items": [
                "Erfolgsliste — die eigene Seite für die vollständige (unbestätigte) Liste.",
                "Steam — prüfe den Erfolge-Bereich der Store-Seite.",
             ]},
            {"heading": "Erfolge-Überblick-FAQ",
             "items": [
                ["Wie viele Erfolge gibt es?", "22 (bestätigt auf der Steam-Store-Seite)."],
                ["Wo ist die vollständige Liste?", "unbestätigt — wir verifizieren die offizielle Liste."],
             ]},
        ],
    },
}

TR_ES = {
    "how-to-play": {
        "title": "Cómo jugar a Approximately Up",
        "metaTitle": "Cómo jugar a Approximately Up: guía completa para principiantes",
        "metaDescription": "¿Nuevo en Approximately Up? Aprende el ciclo construir-chocar-reconstruir, las naves modulares, el multijugador cooperativo y la exploración de planetas.",
        "intro": "Approximately Up es un juego de construcción sandbox espacial en el que atornillas piezas, despegas, te chocas y reconstruyes mejor. Aquí tienes el ciclo principal y lo que debes saber antes de tu primer despegue.",
        "sections": [
            {"heading": "El ciclo principal: construir, chocar, reconstruir", "body": "La descripción oficial resume el ciclo en tres palabras: construir, chocar, reconstruir. Todo lo demás se deriva de ahí.",
             "items": [
                ["Empieza poco a poco", "Monta una nave con lo que sea que se pueda atornillar el tiempo suficiente para volar. No necesitas un diseño perfecto para empezar: necesitas algo que despegue."],
                ["Monta propulsores y cables", "Los propulsores gigantes te mueven; los cables y todo lo demás conectan tu construcción. Espera un diseño desordenado al principio."],
                ["Vuelo de prueba", "Despega y mira qué aguanta. Los primeros vuelos son experimentos, no vuelos pulidos."],
                ["Chocar (pasa)", "Los choques forman parte del ciclo. El discurso oficial los da por hecho: los escombros son una lección, no un fracaso."],
                ["Reconstruir con más cabeza", "Usa lo aprendido para reconstruir. Cada iteración te enseña qué piezas aguantan y qué combinaciones vuelan."],
             ]},
            {"heading": "Lo que el juego promete oficialmente", "body": "De la descripción oficial de Steam:",
             "items": [
                "Explora nuevos planetas en multijugador cooperativo con tu nave totalmente modular.",
                "Monta propulsores gigantes, cables molestos y todo lo demás.",
                "Completa misiones locas y enfréntate a los peligros del espacio.",
                "Juega en solitario o con una tripulación, y discute con ella, como dice la presentación oficial.",
             ]},
            {"heading": "Preguntas frecuentes para principiantes",
             "items": [
                ["¿Approximately Up es multijugador?", "Sí: la página oficial de Steam lista un jugador y multijugador cooperativo en línea."],
                ["¿Necesito saber de ingeniería?", "No. El juego se basa en prueba y error: atornillar piezas, volar, chocar y aprender."],
                ["¿Hay demo?", "Sí: la página oficial de Steam lista una demo anterior al lanzamiento completo (6 de agosto de 2026)."],
                ["¿Puedo jugar en Steam Deck?", "La compatibilidad aún no está confirmada. Los jugadores lo preguntan en los foros de Steam; lo marcamos como sin verificar hasta que haya respuesta oficial."],
             ]},
            {"heading": "Lo que aún debemos verificar", "body": "Los nombres concretos de planetas y misiones, y las guías de mecánicas detalladas (planos, cableado, radar, rebobinado) aún no están verificados contra fuentes oficiales. Los marcamos como sin verificar y actualizamos esta página cuando haya información oficial."},
        ],
    },
    "ship-building-guide": {
        "title": "Guía de construcción de naves Approximately Up",
        "metaTitle": "Guía de construcción de naves Approximately Up: de la primera nave a las grandes construcciones",
        "metaDescription": "Aprende a construir naves en Approximately Up: el proceso modular construir-chocar-reconstruir, propulsores y cables, y necesidades de la comunidad como la Luna y el radar.",
        "intro": "La construcción de naves es el corazón de Approximately Up. La presentación oficial es simple: atornilla piezas hasta que vuelen y luego reconstruye con más cabeza. Esta guía explica el proceso sin inventar estadísticas aún no verificadas.",
        "sections": [
            {"heading": "Construye tu primera nave", "body": "Según la descripción oficial (piezas modulares, propulsores, cables, construir-chocar-reconstruir), este es el proceso:",
             "items": [
                ["Reúne piezas", "Junta las piezas disponibles y atorníllalas. La presentación oficial dice que cualquier construcción 'se atornilla el tiempo suficiente para volar': empieza ahí."],
                ["Añade propulsores", "Monta propulsores para moverte. La descripción oficial destaca los 'propulsores gigantes' como parte central."],
                ["Pasa los cables", "Conecta tu construcción con cables: los 'cables molestos' forman parte de la experiencia. Espera un cableado desordenado."],
                ["Vuelo de prueba", "Despega. Tu primera nave no necesita ser bonita; necesita enseñarte qué aguanta."],
                ["Choca e itera", "Reconstruye con lo aprendido. El ciclo es construir → chocar → reconstruir."],
             ]},
            {"heading": "Principios de diseño (alineados con lo oficial)",
             "items": [
                "Nave totalmente modular: todo se puede reorganizar entre vuelos.",
                "Equilibra peso y empuje: las naves más pesadas necesitan más empuje (cifras concretas sin verificar).",
                "Guarda piezas de repuesto: los choques están previstos.",
                "Planifica el cooperativo: si juegas con tripulación, reparte roles (piloto, constructor, ingeniero).",
             ]},
            {"heading": "Tutoriales que pide la comunidad",
             "items": [
                ["¿Cómo llego a la Luna?", "Un hilo real del foro de Steam: los jugadores quieren una guía para ir a la Luna. Las mecánicas lunares concretas están sin verificar."],
                ["Monitor/dispositivo de radar para empezar", "Un hilo real del foro de Steam: los jugadores quieren un tutorial del dispositivo de radar. Las mecánicas del radar están sin verificar."],
             ]},
            {"heading": "Lo que aún no está verificado", "body": "Los nombres concretos de piezas, estadísticas, recetas, destinos de planetas y nombres de misiones aún no están verificados. Esta guía solo usa la descripción oficial y preguntas comunitarias marcadas; la ampliaremos cuando llegue información verificada."},
        ],
    },
    "blueprints-guide": {
        "title": "Guía de planos Approximately Up",
        "metaTitle": "Planos Approximately Up: descargar, compartir y usar",
        "metaDescription": "Planos de Approximately Up: lo que sabemos sobre encontrarlos y usarlos, el soporte del Steam Workshop y lo que aún no está verificado.",
        "intro": "Los planos son uno de los temas más buscados de Approximately Up. Las mecánicas oficiales (importar, exportar, compartir) aún no están verificadas, así que esta página cubre lo confirmado y lo que no.",
        "sections": [
            {"heading": "Detalles de los planos: sin verificar", "body": "Las mecánicas de importar, exportar y compartir planos están en nuestra lista de sin verificar: aún no las hemos confirmado contra una fuente oficial. Ampliaremos esta página en cuanto verifiquemos información fiable."},
            {"heading": "Encontrar diseños de naves hoy", "body": "Aunque las herramientas oficiales de planos están sin verificar, el Steam Workshop es el lugar confirmado donde vive el contenido comunitario:",
             "items": [
                ["Abre el Steam Workshop de Approximately Up", "Allí se aloja el contenido subido por la comunidad (el soporte del Workshop está confirmado en la página de la tienda)."],
                ["Explora naves y construcciones", "Busca diseños compartidos por otros jugadores."],
                ["Suscríbete", "La suscripción guarda el contenido en tu biblioteca."],
                ["Compruébalo en el juego", "Mira cómo aparecen los elementos suscritos en el juego: los pasos exactos están sin verificar."],
             ]},
            {"heading": "Preguntas frecuentes sobre planos",
             "items": [
                ["¿Puedo descargar planos en Approximately Up?", "Sin verificar. El contenido del Workshop es el canal confirmado más cercano hoy."],
                ["¿Puedo compartir mis diseños de naves?", "Sin verificar. Confirmaremos el proceso exacto de compartir una vez verificado."],
                ["¿Los planos son lo mismo que los objetos del Workshop?", "No necesariamente: la relación entre planos del juego y objetos del Workshop está sin verificar."],
             ]},
            {"heading": "Fuentes a seguir", "body": "Verificaremos las mecánicas de planos contra canales oficiales (anuncios de Steam, sitio oficial, Discord) y actualizaremos esta página. Aquí no se inventa ninguna mecánica."},
        ],
    },
    "wiring-electronics": {
        "title": "Guía de cableado y electrónica Approximately Up",
        "metaTitle": "Cableado y electrónica Approximately Up: lo que sabemos",
        "metaDescription": "Cableado y electrónica en Approximately Up: cables en las construcciones, preguntas de la comunidad sobre la era de las válvulas de vacío y el Remapper, con detalles sin verificar marcados.",
        "intro": "El cableado y la electrónica son un gran tema comunitario, pero la información oficial es escasa. Esta página reúne lo verificado y lo que preguntan los jugadores, con todo lo no verificado claramente marcado.",
        "sections": [
            {"heading": "La información oficial es limitada", "body": "La descripción oficial menciona los cables como parte de la construcción modular ('cables molestos, y todo lo demás'), pero las mecánicas detalladas de cableado y circuitos aún no están verificadas. Las marcamos como sin verificar."},
            {"heading": "Hilos de la comunidad (preguntas reales de jugadores)",
             "items": [
                ["¿Podemos superar la era de las válvulas de vacío en la electrónica?", "Un hilo del foro de Steam sobre la progresión/era de los componentes electrónicos: sugiere un tema electrónico de época temprana; mecánicas exactas sin verificar."],
                ["No puedo poner valores en Remapper", "Un hilo del foro de Steam que reporta problemas al poner valores en Remapper/Constant: el proceso exacto está sin verificar."],
             ]},
            {"heading": "Lo que podemos afirmar con seguridad",
             "items": [
                "Los cables son oficialmente parte de la fantasía de construcción modular de naves.",
                "La electrónica parece ser un área de progresión (la comunidad menciona una 'era de las válvulas de vacío' temprana).",
                "Existen herramientas para ajustar parámetros/valores en el juego (Remapper), pero el uso exacto no está verificado.",
             ]},
            {"heading": "Preguntas frecuentes sobre cableado y electrónica",
             "items": [
                ["¿Cómo funciona el cableado en Approximately Up?", "Sin verificar. Publicaremos una guía en cuanto exista información oficial o contrastada de forma fiable."],
                ["¿Cuáles son los niveles de electrónica?", "Un hilo comunitario menciona una 'era de las válvulas de vacío'; los niveles y desbloqueos exactos están sin verificar."],
                ["¿Por qué no puedo poner valores en el Remapper?", "Un hilo comunitario reporta este problema; el proceso oficial está sin verificar."],
             ]},
        ],
    },
    "controls": {
        "title": "Controles de Approximately Up",
        "metaTitle": "Controles de Approximately Up: teclado, ratón y estado del mando",
        "metaDescription": "Guía de controles de Approximately Up: lo que sabemos de teclado y ratón, el soporte de mando y el reasignador del juego, además de lo que aún no está verificado.",
        "intro": "El soporte de mando es una de las preguntas más frecuentes en la comunidad de Steam justo después del lanzamiento. Aquí está lo que podemos confirmar, lo que preguntan los jugadores y lo que aún no está verificado.",
        "sections": [
            {"heading": "Lo que sabemos (verificado)",
             "items": [
                ["Plataforma", "El juego está en PC (Steam). Teclado y ratón son la entrada predeterminada."],
                ["Soporte de mando", "Aún no lo ha confirmado el desarrollador. Un hilo del foro de Steam pregunta 'Controller Support in the Future?', lo que sugiere que el soporte completo no está confirmado en el lanzamiento."],
                ["Reasignador del juego", "Los jugadores discuten el Remapper: un hilo comunitario reporta problemas al poner valores. Marcamos el proceso exacto de asignación como sin verificar."],
             ]},
            {"heading": "Cómo configurar los controles ahora",
             "items": [
                "Abre los ajustes del juego y revisa la sección de entrada/controles para ver el mapa de teclas actual.",
                "Usa el Remapper del juego para reasignar teclas; si los valores no se aplican, revisa el hilo comunitario y las notas del desarrollador.",
                "Para novedades del soporte de mando, sigue el Discord oficial y los anuncios de Steam.",
             ]},
            {"heading": "Sin verificar: mapa de teclas completo", "body": "El mapa de teclas oficial completo (movimiento, cámara, menú de construcción, control de propulsores) aún no está verificado contra una fuente oficial. Lo marcamos como sin verificar y publicaremos la tabla cuando se confirme."},
            {"heading": "Preguntas frecuentes sobre controles",
             "items": [
                ["¿Approximately Up admite mandos?", "Aún no confirmado. La comunidad lo pregunta; lo marcamos como sin verificar hasta que el desarrollador o una fuente oficial lo confirme."],
                ["¿Puedo reasignar las teclas?", "Hay un Remapper en el juego. Algunos jugadores reportan problemas con los valores; el proceso exacto está sin verificar."],
                ["¿Hay una disposición para Steam Deck?", "La compatibilidad con Steam Deck es en sí una cuestión abierta en la comunidad: la disposición está sin verificar."],
             ]},
        ],
    },
    "multiplayer": {
        "title": "Guía multijugador de Approximately Up",
        "metaTitle": "Multijugador de Approximately Up: cooperativo, número de jugadores y juego cruzado",
        "metaDescription": "El multijugador de Approximately Up explicado: cooperativo en línea, cuántos jugadores, si hay multijugador asíncrono y lo que aún no está verificado.",
        "intro": "Approximately Up es oficialmente un juego de un jugador y cooperativo en línea. Esta página responde a las preguntas multijugador que los jugadores hacen de verdad y marca lo que aún no podemos verificar.",
        "sections": [
            {"heading": "Estado oficial", "body": "La página oficial de Steam lista 'Un jugador' y 'Cooperativo en línea' como modos admitidos. La propuesta del juego gira en torno a una tripulación que explora planetas junta en una nave modular."},
            {"heading": "Preguntas frecuentes sobre multijugador",
             "items": [
                ["¿Cuántos jugadores pueden jugar juntos?", "El número exacto no está verificado en nuestra base de conocimiento: lo marcamos como sin verificar."],
                ["¿Hay cooperativo en línea?", "Sí: el multijugador cooperativo en línea figura en la página oficial de Steam."],
                ["¿Hay multijugador multiplataforma?", "Sin verificar. El juego está actualmente en PC (Steam); no se han anunciado versiones de consola, así que el juego cruzado está sin verificar."],
                ["¿Hay multijugador asíncrono?", "No confirmado. Un hilo del foro de Steam pregunta por 'Asynchronous Multiplayer', lo que sugiere que aún no es una función oficial: lo marcamos como sin verificar."],
                ["¿Puedo jugar solo?", "Sí: el modo de un jugador figura como admitido."],
             ]},
            {"heading": "Lo que pregunta la comunidad",
             "items": [
                "Multijugador asíncrono: si los jugadores esperan un modo asíncrono.",
                "El número de jugadores / 'cuántos jugadores' es una necesidad de búsqueda principal; publicaremos la cifra verificada cuando esté disponible.",
             ]},
            {"heading": "Lo que aún no está verificado", "body": "El límite exacto de jugadores, el flujo de invitaciones, los detalles de alojamiento y el juego cruzado aún no están verificados contra fuentes oficiales. Actualizaremos esta página en cuanto se confirmen."},
        ],
    },
    "best-ship-designs": {
        "title": "Mejores diseños de naves Approximately Up",
        "metaTitle": "Ideas de naves y mejores diseños Approximately Up",
        "metaDescription": "Ideas de diseño de naves Approximately Up: puntos de partida para tus construcciones, preguntas de diseño de la comunidad y dónde encontrar más diseños.",
        "intro": "¿Buscas ideas de naves? Esta página reúne puntos de partida basados en la fantasía oficial construir-chocar-reconstruir, además de las preguntas comunitarias que dan forma a lo que quieren construir los jugadores.",
        "sections": [
            {"heading": "Puntos de partida de diseño (inspiración, no especificaciones oficiales)",
             "items": [
                "Deportiva de propulsores: monta propulsores gigantes y acepta que el control llega después.",
                "Transporte utilitario: prioriza la carga y las piezas de misión sobre la velocidad: las misiones necesitan capacidad (detalles sin verificar).",
                "Nave de tripulación cooperativa: diseña espacio para una tripulación que explore planetas junta.",
                "Construcción de cables desordenados: abraza los 'cables molestos': el cableado forma parte del encanto (mecánicas de cableado sin verificar).",
             ]},
            {"heading": "Preguntas de diseño de la comunidad",
             "items": [
                ["Medidor de curvatura de trayectoria", "Un hilo del foro de Steam sobre una herramienta de trayectoria: los jugadores quieren mejores herramientas de vuelo; estado oficial sin verificar."],
                ["¿mods para crear varias naves?", "Un hilo del foro de Steam sobre controlar más de una nave: sin verificar."],
             ]},
            {"heading": "Dónde encontrar más diseños",
             "items": [
                "El Steam Workshop de Approximately Up (soporte confirmado).",
                "El canal oficial de YouTube para las construcciones de los tráileres.",
                "Las discusiones de la comunidad de Steam para capturas e ideas de jugadores.",
             ]},
            {"heading": "Lo que aún no está verificado", "body": "Las estadísticas concretas de piezas, los planos de diseños con nombre y cualquier lista de 'mejores' no están verificados. Mantenemos esta página como inspiración más fuentes verificadas, y marcamos el resto como sin verificar."},
        ],
    },
    "system-requirements": {
        "title": "Requisitos del sistema de Approximately Up",
        "metaTitle": "Requisitos del sistema de Approximately Up (PC)",
        "metaDescription": "Requisitos del sistema de Approximately Up para PC: los requisitos mínimos y recomendados aún no están verificados; esto es lo que sabemos y cómo comprobar la compatibilidad.",
        "intro": "Los jugadores quieren una respuesta clara sobre si su PC puede ejecutar Approximately Up. Los requisitos mínimos y recomendados oficiales aún no están verificados, así que esta página dice lo que sabemos y lo que no.",
        "sections": [
            {"heading": "Especificaciones oficiales: sin verificar", "body": "Aún no hemos verificado los requisitos mínimos y recomendados oficiales contra una fuente oficial. En lugar de inventar cifras, marcamos la tabla como sin verificar y la rellenaremos en cuanto se confirme (página de Steam o sitio oficial)."},
            {"heading": "Tabla de especificaciones (sin verificar)",
             "columns": ["Elemento", "Mínimo", "Recomendado"],
             "rows": [
                ["Sistema operativo", "sin verificar", "sin verificar"],
                ["Procesador", "sin verificar", "sin verificar"],
                ["Memoria", "sin verificar", "sin verificar"],
                ["Gráficos", "sin verificar", "sin verificar"],
                ["Almacenamiento", "sin verificar", "sin verificar"],
                ["DirectX", "sin verificar", "sin verificar"],
             ]},
            {"heading": "Cómo comprobar tu PC",
             "items": [
                "Abre Steam y revisa la página del juego: los requisitos suelen aparecer ahí una vez publicados.",
                "Compara tu CPU/GPU/RAM con las cifras oficiales cuando las publiquemos.",
                "Steam Deck: la compatibilidad es una cuestión abierta de la comunidad ('Playable on Deck?'); la marcamos como sin verificar.",
             ]},
            {"heading": "Preguntas frecuentes sobre requisitos",
             "items": [
                ["¿Mi PC puede ejecutar Approximately Up?", "Aún no podemos confirmarlo: los requisitos mínimos/recomendados oficiales están sin verificar. Consulta la página de Steam cuando el desarrollador los publique."],
                ["¿Approximately Up está en Steam Deck?", "No confirmado. Un hilo del foro de Steam pregunta 'Playable on Deck?': la compatibilidad está sin verificar hasta que haya respuesta oficial."],
                ["¿Es exigente?", "Es un juego de construcción sandbox espacial con naves físicas modulares; publicaremos cifras verificadas en cuanto estén disponibles."],
             ]},
        ],
    },
    "console-release": {
        "title": "Lanzamiento en consola de Approximately Up: estado en PS5, Xbox y Switch",
        "metaTitle": "Fecha de lanzamiento en consola de Approximately Up (PS5, Xbox, Switch)",
        "metaDescription": "¿Approximately Up llegará a PS5, Xbox o Switch? Aún no hay anuncio oficial: este es el estado en consolas y cómo seguir las noticias oficiales.",
        "intro": "'Fecha de lanzamiento en PS5', 'versión Xbox' y 'versión Switch' son búsquedas que ni el wiki del propio juego responde. La respuesta honesta hoy: no hay anuncio oficial de consola verificado: esta es la página de estado.",
        "sections": [
            {"heading": "Estado en consolas (al 09/08/2026)",
             "items": [
                ["Plataformas actuales", "Solo PC (Steam). El juego salió el 6 de agosto de 2026 en Steam."],
                ["PS5", "sin verificar: no hay anuncio oficial verificado de una versión de PlayStation 5."],
                ["Xbox", "sin verificar: no hay anuncio oficial verificado de una versión de Xbox."],
                ["Nintendo Switch", "sin verificar: no hay anuncio oficial verificado de una versión de Switch."],
                ["Declaración oficial", "No hemos verificado ninguna declaración oficial del desarrollador sobre planes de consolas; lo marcamos como sin verificar y actualizaremos cuando exista."],
             ]},
            {"heading": "Cómo mantenerte informado",
             "items": [
                "Sigue el sitio oficial approximatelyup.com y el Discord oficial (discord.gg/approximatelyup).",
                "Vigila el canal de YouTube del desarrollador (@ApproximatelyUp) y TikTok (@approximatelyup) para anuncios.",
                "Consulta la página de Steam: las noticias de consolas suelen anunciarse primero allí.",
             ]},
            {"heading": "Preguntas frecuentes sobre consolas",
             "items": [
                ["¿Approximately Up está en PS5?", "No anunciado: lo marcamos como sin verificar. Aún no hay declaración oficial verificada."],
                ["¿Está en Xbox?", "No anunciado: sin verificar."],
                ["¿Está en Nintendo Switch?", "No anunciado: sin verificar."],
                ["¿Cuándo sale la versión de consola?", "Aún no hay fecha. Esta página se actualizará en cuanto se verifique un anuncio oficial."],
             ]},
            {"heading": "Por qué existe esta página", "body": "El lanzamiento en consola es una de las preguntas de mayor intención de búsqueda para este juego, pero ninguna fuente fiable la ha respondido. Esta página ofrece el estado verificado (solo PC) y sigue los futuros anuncios en lugar de inventar una fecha."},
        ],
    },
    "mods": {
        "title": "Guía de mods de Approximately Up",
        "metaTitle": "Mods de Approximately Up: Steam Workshop, instalación y preguntas",
        "metaDescription": "Los mods de Approximately Up explicados: soporte del Steam Workshop, cómo suscribirse a mods y preguntas comunitarias como varias naves.",
        "intro": "Approximately Up admite el Steam Workshop, lo que hace sencillo encontrar e instalar mods. Aquí está lo confirmado y lo que piden los jugadores.",
        "sections": [
            {"heading": "Obtener mods del Steam Workshop", "body": "El soporte del Workshop está confirmado en la página oficial. El flujo estándar:",
             "items": [
                ["Abre el Workshop", "Desde la página del juego en Steam, abre la pestaña Workshop (o el centro comunitario del Workshop)."],
                ["Explora y suscríbete", "Encuentra un mod u objeto que te guste y pulsa Suscribirse: Steam lo descarga automáticamente."],
                ["Inicia el juego", "Abre Approximately Up y revisa el menú de mods/contenido del juego para ver los elementos suscritos."],
                ["Activa lo que quieras", "Activa los mods que quieras usar. Los detalles del menú de mods en el juego están sin verificar."],
             ]},
            {"heading": "Lo que pregunta la comunidad",
             "items": [
                "¿mods para crear varias naves? — un hilo real del foro de Steam; el soporte de varias naves mediante mods está sin verificar.",
                "Existen búsquedas de cheat engine para muchos juegos; no proporcionamos trucos, solo información verificada sobre mods.",
             ]},
            {"heading": "Preguntas frecuentes sobre mods",
             "items": [
                ["¿Approximately Up admite mods?", "Oficialmente admite el Steam Workshop (según la página de la tienda). La documentación completa de modding está sin verificar."],
                ["¿Cómo instalo mods?", "Suscríbete a través del Steam Workshop; Steam gestiona la instalación. Los pasos en el juego están sin verificar."],
                ["¿Los mods me dejan controlar varias naves?", "Un hilo comunitario lo pide; aún ningún mod verificado lo ofrece: sin verificar."],
             ]},
            {"heading": "Lo que aún no está verificado", "body": "Las funciones exactas del Workshop, las directrices de mods y si los mods afectan a los logros o al multijugador aún no están verificados. Actualizaremos esta página cuando se confirme la documentación oficial."},
        ],
    },
    "patch-notes": {
        "title": "Notas del parche de Approximately Up",
        "metaTitle": "Notas del parche e historial de actualizaciones de Approximately Up",
        "metaDescription": "Notas del parche e historial de actualizaciones de Approximately Up: información del lanzamiento, dónde se publican las actualizaciones oficiales y nuestro registro seguido (elementos sin verificar marcados).",
        "intro": "Approximately Up salió el 6 de agosto de 2026. Esta página sigue las notas del parche y las actualizaciones oficiales, con todo lo no verificado claramente marcado.",
        "sections": [
            {"heading": "Datos del lanzamiento (verificados)",
             "items": [
                ["Fecha de lanzamiento", "6 de agosto de 2026 (lanzamiento completo en Steam)."],
                ["Demo", "Una demo precede al lanzamiento completo."],
                ["Precio", "19,99 $ en el lanzamiento (20 % de descuento; precio de lista 24,99 $)."],
             ]},
            {"heading": "Cronología de actualizaciones (verificada desde Steam)", "body": "Notas de parche verificadas desde anuncios oficiales de Steam (agosto de 2026):",
             "items": [
                ["2026-08-12", "1.0.010 — Corregido el filtro de orden 'Más populares' del Workshop, la carga de páginas y los resultados faltantes; mejorada la claridad de búsqueda."],
                ["2026-08-11", "1.0.009 — Mejorado Frame Quarter With Ports (los puertos se reflejan al otro lado de la cadena, etiquetas A–D coherentes); corregida la geometría de Middle Window, Small Switch y Small Button."],
                ["2026-08-10", "1.0.008 — Corregido el hitbox del Axis Rotometer y problemas restantes; cables Plasma ahora pintables; paneles Autohemisphere vuelven a su posición tras Fly Mode; soportes de cable pintables."],
                ["2026-08-09", "1.0.007 — Corregida la compatibilidad con dispositivos Metal; corregido el atajo por defecto (botón central del ratón para 'recoger componente'); corregida la errata de las tuberías; más pistas."],
                ["2026-08-08", "1.0.006 — Corregido Fuse Box que no podía encenderse; Axis Rotometer ahora da valores con signo correctos; corregida la vista previa de la Large Disposable Battery; añadidos créditos, pantalla de inicio y seguimiento de objetivos."],
             ]},
            {"heading": "Dónde se publican las actualizaciones oficiales",
             "items": [
                "Los anuncios de Steam del juego (fuente de noticias de la página de la tienda).",
                "El sitio oficial approximatelyup.com y el Discord oficial.",
                "El canal de YouTube del desarrollador para anuncios de funciones.",
             ]},
            {"heading": "Lo que aún no está verificado", "body": "El contenido concreto de los parches (cambios de equilibrio, correcciones, piezas nuevas) no está verificado. Marcamos todo como sin verificar en lugar de adivinar."},
        ],
    },
    "demo-vs-full": {
        "title": "Demo de Approximately Up vs juego completo",
        "metaTitle": "Demo de Approximately Up vs juego completo: ¿cuál es la diferencia?",
        "metaDescription": "Demo vs versión completa de Approximately Up: fechas de lanzamiento, precio, Workshop y logros, además de las diferencias de contenido aún sin verificar.",
        "intro": "La demo de Approximately Up salió antes del lanzamiento completo del 6 de agosto de 2026. Aquí está la comparación verificada, con las diferencias de contenido claramente marcadas como sin verificar.",
        "sections": [
            {"heading": "Comparación verificada",
             "columns": ["Aspecto", "Demo", "Juego completo"],
             "rows": [
                ["Disponibilidad", "Demo (salió antes, según la página de la tienda)", "Lanzamiento completo el 6 de agosto de 2026"],
                ["Precio", "sin verificar", "19,99 $ (20 % de descuento de lanzamiento; precio de lista 24,99 $)"],
                ["Steam Workshop", "sin verificar", "Admitido (según la página de la tienda)"],
                ["Logros", "sin verificar", "22 logros de Steam (según la página de la tienda)"],
                ["Multijugador cooperativo", "sin verificar", "Un jugador + cooperativo en línea (según la página de la tienda)"],
             ]},
            {"heading": "Preguntas frecuentes sobre demo vs completo",
             "items": [
                ["¿La demo es gratis?", "No hemos verificado el precio/modelo de la demo: sin verificar."],
                ["¿El progreso de la demo pasa al juego completo?", "Sin verificar."],
                ["¿Qué contenido solo está en el juego completo?", "Sin verificar: los detalles oficiales de comparación están pendientes. El juego completo añade soporte del Workshop y 22 logros según la página de la tienda."],
                ["¿Debería probar primero la demo?", "Para la mayoría de los juegos de construcción sandbox espaciales, probar la demo es buena forma de sentir el ciclo construir-chocar-reconstruir antes de comprar, pero los límites exactos de la demo están sin verificar."],
             ]},
            {"heading": "Lo que aún no está verificado", "body": "El contenido exacto de la demo, la transferencia de progreso y las diferencias de funciones no están verificados contra una fuente oficial. Actualizaremos esta tabla en cuanto se confirmen."},
        ],
    },
    "achievements-list": {
        "title": "Lista de logros de Approximately Up",
        "metaTitle": "Logros de Approximately Up: lista completa (22)",
        "metaDescription": "Approximately Up tiene 22 logros de Steam. La lista completa de nombres aún se está verificando: esto es lo confirmado.",
        "intro": "La página oficial de Steam confirma 22 logros. Los nombres exactos y las condiciones de desbloqueo aún no están verificados, así que esta página sigue el número confirmado y marca la lista como sin verificar.",
        "sections": [
            {"heading": "Confirmado: 22 logros", "body": "La página de Steam lista 22 logros para Approximately Up. Aún no hemos verificado el nombre, el icono y la condición de cada logro: esa parte está sin verificar."},
            {"heading": "Lista de logros (sin verificar)",
             "columns": ["Logro", "Condición"],
             "rows": [
                ["Logros 1–22", "sin verificar: nombres y condiciones en proceso de verificación contra la lista oficial."],
             ]},
            {"heading": "Cómo seguir los logros",
             "items": [
                "Usa la superposición de Steam en el juego para ver tu progreso.",
                "Sigue los anuncios oficiales de Steam: las listas de logros a veces acompañan a las notas del parche.",
                "Publicaremos aquí la lista completa verificada cuando se confirme.",
             ]},
            {"heading": "Preguntas frecuentes sobre logros",
             "items": [
                ["¿Cuántos logros tiene Approximately Up?", "22, confirmado en la página oficial de Steam."],
                ["¿Cuáles son los nombres de los logros?", "sin verificar: estamos verificando la lista oficial y la publicaremos cuando se confirme."],
                ["¿Puedo conseguir todos los logros en solitario?", "Sin verificar: algunos pueden requerir cooperativo, pero no lo sabremos hasta confirmar la lista."],
             ]},
        ],
    },
    "ships": {
        "title": "Naves de Approximately Up",
        "metaTitle": "Naves de Approximately Up: construcciones, ideas y diseños",
        "metaDescription": "Índice del contenido de naves de Approximately Up: guía de construcción, diseños, planos y lo básico de la construcción modular.",
        "intro": "Todo sobre las naves de Approximately Up en un solo lugar: desde tu primera construcción hasta las ideas de diseño de la comunidad.",
        "sections": [
            {"heading": "Guías de naves",
             "items": [
                "Guía de construcción de naves: aprende el proceso construir-chocar-reconstruir.",
                "Mejores diseños: puntos de partida e ideas comunitarias.",
                "Guía de planos: lo que sabemos de los planos y el contenido del Workshop.",
                "Mods: soporte del Workshop y preguntas sobre mods.",
             ]},
            {"heading": "Preguntas frecuentes sobre naves",
             "items": [
                ["¿Qué tipo de naves puedo construir?", "Son totalmente modulares: atornillas piezas como encajen (descripción oficial). Las listas concretas de piezas están sin verificar."],
                ["¿Puedo volar a la Luna?", "Un hilo comunitario pregunta cómo; las mecánicas lunares están sin verificar."],
                ["¿Puedo controlar varias naves?", "Un hilo comunitario lo pregunta; sin verificar."],
             ]},
        ],
    },
    "blueprints": {
        "title": "Planos de Approximately Up",
        "metaTitle": "Planos de Approximately Up: descargas y biblioteca",
        "metaDescription": "Índice del contenido de planos de Approximately Up: cómo usar los planos, dónde encontrar diseños de naves y el Steam Workshop.",
        "intro": "El índice de la biblioteca de planos: encuentra diseños de naves, aprende el flujo (sin verificar) de los planos y explora el Workshop.",
        "sections": [
            {"heading": "Contenido de planos",
             "items": [
                "Guía de planos: lo confirmado y lo sin verificar sobre los planos.",
                "Mejores diseños: ideas de diseño y dónde encontrar más.",
                "Steam Workshop: el hogar confirmado del contenido comunitario.",
             ]},
            {"heading": "Preguntas frecuentes del índice de planos",
             "items": [
                ["¿Dónde puedo descargar planos?", "El Steam Workshop es el canal confirmado para el contenido comunitario; las mecánicas de descarga de planos en el juego están sin verificar."],
                ["¿Cómo importo un plano?", "Sin verificar."],
                ["¿Puedo compartir mis diseños?", "Sin verificar."],
             ]},
        ],
    },
    "guides": {
        "title": "Guías de Approximately Up",
        "metaTitle": "Guías de Approximately Up: todas las páginas",
        "metaDescription": "Todas las guías de Approximately Up en un índice: cómo jugar, construcción de naves, controles, multijugador, mods, logros y más.",
        "intro": "El índice completo de guías de Approximately Up. Cada página responde a una pregunta que los jugadores buscan de verdad y marca todo lo no verificado.",
        "sections": [
            {"heading": "Todas las guías",
             "items": [
                "Cómo jugar: el ciclo construir-chocar-reconstruir para principiantes.",
                "Controles: teclado/ratón, estado del mando y notas del reasignador.",
                "Requisitos del sistema: estado de las especificaciones y cómo comprobar tu PC.",
                "Multijugador: cooperativo en línea, número de jugadores y preguntas asíncronas.",
                "Lanzamiento en consola: estado en PS5/Xbox/Switch.",
                "Mods: Steam Workshop y preguntas sobre mods.",
                "Notas del parche: datos del lanzamiento y seguimiento de actualizaciones.",
                "Demo vs completo: comparación verificada.",
                "Guía de construcción de naves: de la primera nave a las grandes construcciones.",
                "Cableado y electrónica: lo conocido y lo sin verificar.",
                "Guía de planos: estado de los planos y Workshop.",
                "Mejores diseños: ideas y diseños comunitarios.",
                "Lista de logros: 22 logros, lista sin verificar.",
                "Naves / Planos / Logros: páginas de índice.",
             ]},
            {"heading": "Cómo trabajamos", "body": "Cada página lista 1 o 2 fuentes fiables y marca todo lo no verificado. No inventamos cifras, nombres ni mecánicas."},
        ],
    },
    "achievements": {
        "title": "Logros de Approximately Up",
        "metaTitle": "Logros de Approximately Up: resumen",
        "metaDescription": "Resumen de los logros de Approximately Up: 22 logros de Steam confirmados, lista completa en verificación y cómo seguir el progreso.",
        "intro": "El centro de logros de Approximately Up: número confirmado, estado actual de la lista y enlaces a la página de seguimiento completo.",
        "sections": [
            {"heading": "22 logros confirmados", "body": "La página de Steam confirma 22 logros. La lista completa de nombres y condiciones está sin verificar."},
            {"heading": "Contenido de logros",
             "items": [
                "Lista de logros: la página dedicada a la lista completa (sin verificar).",
                "Steam: consulta la sección de logros de la página de la tienda.",
             ]},
            {"heading": "Preguntas frecuentes del resumen de logros",
             "items": [
                ["¿Cuántos logros hay?", "22 (confirmado en la página de Steam)."],
                ["¿Dónde está la lista completa?", "sin verificar: estamos verificando la lista oficial."],
             ]},
        ],
    },
}

TR_IT = {
    "how-to-play": {
        "title": "Come si gioca ad Approximately Up",
        "metaTitle": "Come si gioca ad Approximately Up: guida completa per principianti",
        "metaDescription": "Nuovo ad Approximately Up? Scopri il ciclo costruisci-schianta-ricostruisci, le navi modulari, il multigiocatore cooperativo e l'esplorazione dei pianeti.",
        "intro": "Approximately Up è un gioco sandbox spaziale di costruzione in cui avviti pezzi, decolli, schianti e ricostruisci meglio. Ecco il ciclo principale e cosa sapere prima del primo lancio.",
        "sections": [
            {"heading": "Il ciclo principale: costruisci, schianta, ricostruisci", "body": "La descrizione ufficiale riassume il ciclo in tre parole: costruisci, schianta, ricostruisci. Tutto il resto ne deriva.",
             "items": [
                ["Inizia in piccolo", "Assembla una nave con qualsiasi cosa si avviti abbastanza a lungo da volare. Non serve un design perfetto per iniziare: serve qualcosa che decolli."],
                ["Monta propulsori e cavi", "I propulsori giganti ti fanno muovere; i cavi e tutto il resto collegano la tua costruzione. Aspettati un assetto caotico all'inizio."],
                ["Volo di prova", "Decolla e guarda cosa regge. I primi voli sono esperimenti, non voli rifiniti."],
                ["Schiantarsi (succede)", "Gli schianti fanno parte del ciclo. La proposta ufficiale li dà per scontati: i detriti sono una lezione, non un fallimento."],
                ["Ricostruisci con più testa", "Usa ciò che hai imparato per ricostruire. Ogni iterazione ti insegna quali pezzi reggono e quali combinazioni volano."],
             ]},
            {"heading": "Cosa promette ufficialmente il gioco", "body": "Dalla descrizione ufficiale di Steam:",
             "items": [
                "Esplora nuovi pianeti in multigiocatore cooperativo con la tua nave completamente modulare.",
                "Monta propulsori giganti, cavi fastidiosi e tutto il resto.",
                "Completa missioni assurde e affronta i pericoli dello spazio.",
                "Gioca in solitaria o con un equipaggio: e litiga con l'equipaggio, come dice la proposta ufficiale.",
             ]},
            {"heading": "FAQ per principianti",
             "items": [
                ["Approximately Up è multigiocatore?", "Sì: la pagina ufficiale di Steam elenca giocatore singolo e multigiocatore cooperativo online."],
                ["Devo saperne di ingegneria?", "No. Il gioco si basa su tentativi ed errori: avvita pezzi, vola, schiantati, impara."],
                ["C'è una demo?", "Sì: la pagina ufficiale di Steam elenca una demo precedente all'uscita completa (6 agosto 2026)."],
                ["Posso giocare su Steam Deck?", "La compatibilità non è ancora confermata. I giocatori lo chiedono sui forum Steam; lo segniamo come non verificato finché non c'è una risposta ufficiale."],
             ]},
            {"heading": "Cosa ci resta da verificare", "body": "I nomi precisi di pianeti e missioni e le guide meccaniche dettagliate (progetti, cablaggio, radar, riavvolgimento) non sono ancora verificati contro fonti ufficiali. Li segniamo come non verificati e aggiorniamo questa pagina appena disponibili informazioni ufficiali."},
        ],
    },
    "ship-building-guide": {
        "title": "Guida alla costruzione di navi Approximately Up",
        "metaTitle": "Guida alla costruzione di navi Approximately Up: dalla prima nave alle grandi costruzioni",
        "metaDescription": "Impara a costruire navi in Approximately Up: il processo modulare costruisci-schianta-ricostruisci, propulsori e cavi, più le esigenze della community come la Luna e il radar.",
        "intro": "La costruzione di navi è il cuore di Approximately Up. La proposta ufficiale è semplice: avvita i pezzi finché volano, poi ricostruisci con più testa. Questa guida spiega il processo senza inventare statistiche ancora non verificate.",
        "sections": [
            {"heading": "Costruisci la tua prima nave", "body": "In base alla descrizione ufficiale (pezzi modulari, propulsori, cavi, costruisci-schianta-ricostruisci), ecco il processo:",
             "items": [
                ["Raccogli i pezzi", "Raccogli i pezzi disponibili e avvitali. La proposta ufficiale dice che qualsiasi costruzione 'si avvita abbastanza a lungo da volare': parti da lì."],
                ["Aggiungi i propulsori", "Monta i propulsori per muoverti. La descrizione ufficiale mette in evidenza i 'propulsori giganti' come parte centrale."],
                ["Stendi i cavi", "Collega la costruzione con i cavi: i 'cavi fastidiosi' fanno parte dell'esperienza. Aspettati un cablaggio disordinato."],
                ["Volo di prova", "Decolla. La tua prima nave non deve essere bella; deve insegnarti cosa regge."],
                ["Schiantati e itera", "Ricostruisci con ciò che hai imparato. Il ciclo è costruisci → schiantati → ricostruisci."],
             ]},
            {"heading": "Principi di design (allineati all'ufficiale)",
             "items": [
                "Nave completamente modulare: tutto può essere riorganizzato tra un volo e l'altro.",
                "Bilancia peso e spinta: le navi più pesanti richiedono più spinta (numeri precisi non verificati).",
                "Tieni pezzi di ricambio: gli schianti sono previsti.",
                "Prevedi il co-op: se giochi con un equipaggio, dividetevi i ruoli (pilota, costruttore, ingegnere).",
             ]},
            {"heading": "Tutorial richiesti dalla community",
             "items": [
                ["Come si arriva sulla Luna?", "Un thread reale del forum Steam: i giocatori vogliono una guida per la Luna. Le meccaniche lunari precise sono non verificate."],
                ["Monitor/dispositivo radar per iniziare", "Un thread reale del forum Steam: i giocatori vogliono un tutorial sul dispositivo radar. Le meccaniche del radar sono non verificate."],
             ]},
            {"heading": "Cosa resta non verificato", "body": "Nomi precisi di pezzi, statistiche, ricette, destinazioni planetarie e nomi di missioni non sono ancora verificati. Questa guida usa solo la descrizione ufficiale e domande comunitarie marcate; la approfondiremo quando arriveranno informazioni verificate."},
        ],
    },
    "blueprints-guide": {
        "title": "Guida ai progetti Approximately Up",
        "metaTitle": "Progetti Approximately Up: scaricare, condividere e usare",
        "metaDescription": "Progetti di Approximately Up: cosa sappiamo su trovarli e usarli, il supporto del Workshop di Steam e cosa resta non verificato.",
        "intro": "I progetti sono uno dei temi più cercati su Approximately Up. Le meccaniche ufficiali (import, export, condivisione) non sono ancora verificate, quindi questa pagina copre ciò che è confermato e ciò che non lo è.",
        "sections": [
            {"heading": "Dettagli dei progetti: non verificati", "body": "Le meccaniche di import, export e condivisione dei progetti sono nella nostra lista non verificata: non le abbiamo confermate contro una fonte ufficiale. Amplieremo questa pagina appena verificate informazioni affidabili."},
            {"heading": "Trovare design di navi oggi", "body": "Mentre gli strumenti ufficiali per i progetti sono non verificati, il Workshop di Steam è il luogo confermato dei contenuti della community:",
             "items": [
                ["Apri il Workshop di Steam per Approximately Up", "I contenuti caricati dalla community sono ospitati lì (il supporto del Workshop è confermato sulla pagina del negozio)."],
                ["Sfoglia navi e costruzioni", "Cerca design condivisi da altri giocatori."],
                ["Abbonati", "L'abbonamento salva i contenuti nella tua libreria."],
                ["Controlla nel gioco", "Vedi come appaiono gli elementi abbonati nel gioco: i passaggi esatti sono non verificati."],
             ]},
            {"heading": "FAQ sui progetti",
             "items": [
                ["Posso scaricare progetti in Approximately Up?", "Non verificato. I contenuti del Workshop sono oggi il canale confermato più vicino."],
                ["Posso condividere i miei design di navi?", "Non verificato. Confermeremo la procedura esatta di condivisione una volta verificata."],
                ["I progetti sono la stessa cosa degli oggetti del Workshop?", "Non necessariamente: il rapporto tra progetti di gioco e oggetti del Workshop è non verificato."],
             ]},
            {"heading": "Fonti da tenere d'occhio", "body": "Verificheremo le meccaniche dei progetti sui canali ufficiali (annunci Steam, sito ufficiale, Discord) e aggiorneremo questa pagina. Qui non si inventa alcuna meccanica."},
        ],
    },
    "wiring-electronics": {
        "title": "Guida al cablaggio e all'elettronica Approximately Up",
        "metaTitle": "Cablaggio ed elettronica Approximately Up: cosa sappiamo",
        "metaDescription": "Cablaggio ed elettronica in Approximately Up: cavi nelle costruzioni, domande della community sull'era delle valvole termoioniche e sul Remapper, con dettagli non verificati marcati.",
        "intro": "Cablaggio ed elettronica sono un grande tema della community, ma le informazioni ufficiali sono poche. Questa pagina raccoglie ciò che è verificato e ciò che chiedono i giocatori, con tutto il non verificato chiaramente marcato.",
        "sections": [
            {"heading": "Le informazioni ufficiali sono limitate", "body": "La descrizione ufficiale menziona i cavi come parte della costruzione modulare ('cavi fastidiosi, e tutto il resto'), ma le meccaniche dettagliate di cablaggio e circuiti non sono ancora verificate. Le segniamo come non verificate."},
            {"heading": "Thread della community (domande reali dei giocatori)",
             "items": [
                ["Possiamo superare l'era delle valvole termoioniche nell'elettronica?", "Un thread del forum Steam sulla progressione/era dei componenti elettronici: suggerisce un tema elettronico di prima era; meccaniche esatte non verificate."],
                ["Non riesco a impostare valori nel Remapper", "Un thread del forum Steam che segnala problemi nell'impostare valori in Remapper/Constant: la procedura esatta è non verificata."],
             ]},
            {"heading": "Cosa possiamo dire con sicurezza",
             "items": [
                "I cavi fanno ufficialmente parte della fantasia di costruzione modulare delle navi.",
                "L'elettronica sembra essere un'area di progressione (la community menziona una prima 'era delle valvole termoioniche').",
                "Esistono strumenti per impostare parametri/valori nel gioco (Remapper), ma l'uso esatto è non verificato.",
             ]},
            {"heading": "FAQ su cablaggio ed elettronica",
             "items": [
                ["Come funziona il cablaggio in Approximately Up?", "Non verificato. Pubblicheremo una guida appena esistono informazioni ufficiali o incrociate in modo affidabile."],
                ["Quali sono i livelli dell'elettronica?", "Un thread della community menziona un'era delle valvole termoioniche; i livelli e gli sblocchi esatti sono non verificati."],
                ["Perché non riesco a impostare valori nel Remapper?", "Un thread della community segnala il problema; la procedura ufficiale è non verificata."],
             ]},
        ],
    },
    "controls": {
        "title": "Controlli Approximately Up",
        "metaTitle": "Controlli Approximately Up: tastiera, mouse e stato del controller",
        "metaDescription": "Guida ai controlli di Approximately Up: cosa sappiamo di tastiera e mouse, supporto controller e remappatore di gioco, più cosa resta non verificato.",
        "intro": "Il supporto controller è una delle domande più frequenti nella community di Steam subito dopo l'uscita. Ecco cosa possiamo confermare, cosa chiedono i giocatori e cosa resta non verificato.",
        "sections": [
            {"heading": "Cosa sappiamo (verificato)",
             "items": [
                ["Piattaforma", "Il gioco è su PC (Steam). Tastiera e mouse sono l'input predefinito."],
                ["Supporto controller", "Non ancora confermato dallo sviluppatore. Un thread del forum Steam chiede 'Controller Support in the Future?', il che suggerisce che il supporto completo non è confermato al lancio."],
                ["Remappatore di gioco", "I giocatori discutono del Remapper: un thread della community segnala problemi nell'impostare i valori. La procedura esatta di mappatura è marcata come non verificata."],
             ]},
            {"heading": "Come configurare i controlli ora",
             "items": [
                "Apri le impostazioni di gioco e controlla la sezione input/controlli per la mappatura attuale dei tasti.",
                "Usa il Remapper di gioco per riassegnare i tasti; se i valori non si applicano, controlla il thread della community e le note dello sviluppatore.",
                "Per gli aggiornamenti sul supporto controller, segui il Discord ufficiale e gli annunci Steam.",
             ]},
            {"heading": "Non verificato: mappa tasti completa", "body": "La mappa tasti ufficiale completa (movimento, telecamera, menu di costruzione, controllo dei propulsori) non è ancora verificata contro una fonte ufficiale. La segniamo come non verificata e pubblicheremo la tabella una volta confermata."},
            {"heading": "FAQ sui controlli",
             "items": [
                ["Approximately Up supporta i controller?", "Non ancora confermato. La community lo chiede; lo segniamo come non verificato finché lo sviluppatore o una fonte ufficiale non lo conferma."],
                ["Posso riassegnare i tasti?", "C'è un Remapper di gioco. Alcuni giocatori segnalano problemi con i valori; la procedura esatta è non verificata."],
                ["C'è un layout per Steam Deck?", "La compatibilità con Steam Deck è di per sé una questione aperta nella community: il layout è non verificato."],
             ]},
        ],
    },
    "multiplayer": {
        "title": "Guida multigiocatore Approximately Up",
        "metaTitle": "Multigiocatore Approximately Up: co-op, numero di giocatori e crossplay",
        "metaDescription": "Il multigiocatore di Approximately Up spiegato: co-op online, quanti giocatori, se esiste il multigiocatore asincrono e cosa resta non verificato.",
        "intro": "Approximately Up è ufficialmente un gioco per giocatore singolo e co-op online. Questa pagina risponde alle domande multigiocatore che i giocatori fanno davvero e marca ciò che non possiamo ancora verificare.",
        "sections": [
            {"heading": "Stato ufficiale", "body": "La pagina ufficiale di Steam elenca 'Giocatore singolo' e 'Co-op online' come modalità supportate. La proposta del gioco si basa su un equipaggio che esplora pianeti insieme in una nave modulare."},
            {"heading": "FAQ sul multigiocatore",
             "items": [
                ["Quanti giocatori possono giocare insieme?", "Il numero esatto non è verificato nella nostra base di conoscenze: lo segniamo come non verificato."],
                ["C'è il co-op online?", "Sì: il multigiocatore cooperativo online è elencato nella pagina ufficiale di Steam."],
                ["C'è il multigiocatore multipiattaforma?", "Non verificato. Il gioco è attualmente su PC (Steam); le versioni console non sono annunciate, quindi il crossplay è non verificato."],
                ["C'è il multigiocatore asincrono?", "Non confermato. Un thread del forum Steam chiede informazioni su 'Asynchronous Multiplayer', il che suggerisce che non è ancora una funzione ufficiale: lo segniamo come non verificato."],
                ["Posso giocare da solo?", "Sì: il giocatore singolo è elencato come modalità supportata."],
             ]},
            {"heading": "Cosa chiede la community",
             "items": [
                "Multigiocatore asincrono: se i giocatori si aspettano una modalità asincrona.",
                "Il numero di giocatori / 'quanti giocatori' è un bisogno di ricerca primario; pubblicheremo il numero verificato quando sarà disponibile.",
             ]},
            {"heading": "Cosa resta non verificato", "body": "Il limite esatto di giocatori, il flusso di invito, i dettagli di hosting e il crossplay non sono ancora verificati contro fonti ufficiali. Aggiorneremo questa pagina appena confermati."},
        ],
    },
    "best-ship-designs": {
        "title": "Migliori design di navi Approximately Up",
        "metaTitle": "Idee di navi e migliori design Approximately Up",
        "metaDescription": "Idee di design di navi Approximately Up: punti di partenza per le tue costruzioni, domande di design della community e dove trovare altri design.",
        "intro": "Cerchi idee per le navi? Questa pagina raccoglie punti di partenza basati sulla fantasia ufficiale costruisci-schianta-ricostruisci, più le domande della community che danno forma a ciò che i giocatori vogliono costruire.",
        "sections": [
            {"heading": "Punti di partenza di design (ispirazione, non specifiche ufficiali)",
             "items": [
                "Sportiva a propulsori: monta propulsori giganti e accetta che il controllo arrivi dopo.",
                "Trasporto utilitario: preferisci carico e pezzi di missione alla velocità: le missioni richiedono capacità (dettagli non verificati).",
                "Nave equipaggio co-op: progetta spazio per un equipaggio che esplora pianeti insieme.",
                "Costruzione a cavi disordinati: abbraccia i 'cavi fastidiosi': il cablaggio fa parte del fascino (meccaniche di cablaggio non verificate).",
             ]},
            {"heading": "Domande di design della community",
             "items": [
                ["Misuratore di curvatura di traiettoria", "Un thread del forum Steam su uno strumento di traiettoria: i giocatori vogliono strumenti di volo migliori; stato ufficiale non verificato."],
                ["mod per creare più navi?", "Un thread del forum Steam sul controllo di più navi: non verificato."],
             ]},
            {"heading": "Dove trovare altri design",
             "items": [
                "Il Workshop di Steam per Approximately Up (supporto confermato).",
                "Il canale YouTube ufficiale per le costruzioni dei trailer.",
                "Le discussioni della community di Steam per screenshot e idee dei giocatori.",
             ]},
            {"heading": "Cosa resta non verificato", "body": "Statistiche precise dei pezzi, progetti di design nominati e qualsiasi classifica dei 'migliori' non sono verificati. Manteniamo questa pagina come ispirazione più fonti verificate, e segniamo il resto come non verificato."},
        ],
    },
    "system-requirements": {
        "title": "Requisiti di sistema Approximately Up",
        "metaTitle": "Requisiti di sistema Approximately Up (PC)",
        "metaDescription": "Requisiti di sistema PC di Approximately Up: requisiti minimi e consigliati non ancora verificati: ecco cosa sappiamo e come controllare la compatibilità.",
        "intro": "I giocatori vogliono una risposta chiara su se il loro PC possa eseguire Approximately Up. I requisiti minimi e consigliati ufficiali non sono ancora verificati, quindi questa pagina dice cosa sappiamo e cosa no.",
        "sections": [
            {"heading": "Specifiche ufficiali: non verificate", "body": "Non abbiamo ancora verificato i requisiti minimi e consigliati ufficiali contro una fonte ufficiale. Invece di inventare numeri, segniamo la tabella come non verificata e la compileremo appena confermata (pagina Steam o sito ufficiale)."},
            {"heading": "Tabella specifiche (non verificata)",
             "columns": ["Elemento", "Minimo", "Consigliato"],
             "rows": [
                ["Sistema operativo", "non verificato", "non verificato"],
                ["Processore", "non verificato", "non verificato"],
                ["Memoria", "non verificato", "non verificato"],
                ["Scheda grafica", "non verificato", "non verificato"],
                ["Archiviazione", "non verificato", "non verificato"],
                ["DirectX", "non verificato", "non verificato"],
             ]},
            {"heading": "Come controllare il tuo PC",
             "items": [
                "Apri Steam e controlla la pagina del gioco: i requisiti di sistema di solito compaiono lì una volta pubblicati.",
                "Confronta CPU/GPU/RAM con i numeri ufficiali quando li pubblichiamo.",
                "Steam Deck: la compatibilità è una questione aperta della community ('Playable on Deck?'); la segniamo come non verificata.",
             ]},
            {"heading": "FAQ sui requisiti di sistema",
             "items": [
                ["Il mio PC può eseguire Approximately Up?", "Non possiamo ancora confermarlo: i requisiti minimi/consigliati ufficiali sono non verificati. Controlla la pagina Steam quando lo sviluppatore li pubblicherà."],
                ["Approximately Up è su Steam Deck?", "Non confermato. Un thread del forum Steam chiede 'Playable on Deck?': la compatibilità è non verificata finché non c'è una risposta ufficiale."],
                ["È impegnativo?", "È un gioco sandbox spaziale di costruzione con navi fisiche modulari; riporteremo numeri verificati appena disponibili."],
             ]},
        ],
    },
    "console-release": {
        "title": "Uscita console Approximately Up: stato PS5, Xbox e Switch",
        "metaTitle": "Data di uscita console Approximately Up (PS5, Xbox, Switch)",
        "metaDescription": "Approximately Up arriverà su PS5, Xbox o Switch? Nessun annuncio ufficiale per ora: ecco lo stato su console e come seguire le notizie ufficiali.",
        "intro": "'Data di uscita PS5 Approximately Up', 'versione Xbox' e 'versione Switch' sono ricerche a cui non risponde nemmeno il wiki del gioco. La risposta onesta oggi: nessun annuncio console ufficiale verificato: ecco la pagina di stato.",
        "sections": [
            {"heading": "Stato console (al 09/08/2026)",
             "items": [
                ["Piattaforme attuali", "Solo PC (Steam). Il gioco è uscito il 6 agosto 2026 su Steam."],
                ["PS5", "non verificato: nessun annuncio ufficiale verificato di una versione PlayStation 5."],
                ["Xbox", "non verificato: nessun annuncio ufficiale verificato di una versione Xbox."],
                ["Nintendo Switch", "non verificato: nessun annuncio ufficiale verificato di una versione Switch."],
                ["Dichiarazione ufficiale", "Non abbiamo verificato una dichiarazione ufficiale dello sviluppatore sui piani console; la segniamo come non verificata e aggiorneremo appena esiste."],
             ]},
            {"heading": "Come restare informati",
             "items": [
                "Segui il sito ufficiale approximatelyup.com e il Discord ufficiale (discord.gg/approximatelyup).",
                "Controlla il canale YouTube dello sviluppatore (@ApproximatelyUp) e TikTok (@approximatelyup) per gli annunci.",
                "Controlla la pagina Steam: le notizie console di solito vengono annunciate lì per prime.",
             ]},
            {"heading": "FAQ console",
             "items": [
                ["Approximately Up è su PS5?", "Non annunciato: lo segniamo come non verificato. Non esiste ancora una dichiarazione ufficiale verificata."],
                ["È su Xbox?", "Non annunciato: non verificato."],
                ["È su Nintendo Switch?", "Non annunciato: non verificato."],
                ["Quando esce la versione console?", "Non esiste ancora una data. Questa pagina verrà aggiornata nel momento in cui verrà verificato un annuncio ufficiale."],
             ]},
            {"heading": "Perché esiste questa pagina", "body": "L'uscita su console è una delle domande a più alta intenzione di ricerca per questo gioco, ma nessuna fonte affidabile le ha risposto. Questa pagina dà lo stato verificato (solo PC) e segue i futuri annunci invece di inventare una data."},
        ],
    },
    "mods": {
        "title": "Guida alle mod Approximately Up",
        "metaTitle": "Mod Approximately Up: Steam Workshop, installazione e domande",
        "metaDescription": "Le mod di Approximately Up spiegate: supporto del Workshop di Steam, come abbonarsi alle mod e domande della community come più navi.",
        "intro": "Approximately Up supporta il Workshop di Steam, il che rende semplice trovare e installare mod. Ecco cosa è confermato e cosa chiedono i giocatori.",
        "sections": [
            {"heading": "Ottenere mod dal Workshop di Steam", "body": "Il supporto del Workshop è confermato sulla pagina ufficiale. Il flusso standard:",
             "items": [
                ["Apri il Workshop", "Dalla pagina Steam del gioco, apri la scheda Workshop (o l'hub comunitario del Workshop)."],
                ["Sfoglia e abbonati", "Trova una mod o un oggetto che ti piace e premi Abbonati: Steam lo scarica automaticamente."],
                ["Avvia il gioco", "Apri Approximately Up e controlla il menu mod/contenuti del gioco per vedere gli elementi abbonati."],
                ["Attiva ciò che vuoi", "Attiva le mod che vuoi usare. I dettagli del menu mod di gioco sono non verificati."],
             ]},
            {"heading": "Cosa chiede la community",
             "items": [
                "mod per creare più navi? — un thread reale del forum Steam; il supporto multi-nave tramite mod è non verificato.",
                "Le ricerche legate a cheat engine esistono per molti giochi; non forniamo cheat, solo informazioni verificate sulle mod.",
             ]},
            {"heading": "FAQ sulle mod",
             "items": [
                ["Approximately Up supporta le mod?", "Ufficialmente supporta il Workshop di Steam (secondo la pagina del negozio). La documentazione completa sul modding è non verificata."],
                ["Come installo le mod?", "Abbonati tramite il Workshop di Steam; Steam gestisce l'installazione. I passaggi di gioco sono non verificati."],
                ["Le mod mi permettono di controllare più navi?", "Un thread della community lo chiede; nessuna mod verificata lo offre ancora: non verificato."],
             ]},
            {"heading": "Cosa resta non verificato", "body": "Le funzioni esatte del Workshop, le linee guida sulle mod e se le mod influiscono su obiettivi o multigiocatore non sono ancora verificate. Aggiorneremo questa pagina alla conferma della documentazione ufficiale."},
        ],
    },
    "patch-notes": {
        "title": "Note di patch Approximately Up",
        "metaTitle": "Note di patch e cronologia aggiornamenti Approximately Up",
        "metaDescription": "Note di patch e cronologia aggiornamenti di Approximately Up: info di lancio, dove vengono pubblicati gli aggiornamenti ufficiali e il nostro registro seguito (elementi non verificati marcati).",
        "intro": "Approximately Up è uscito il 6 agosto 2026. Questa pagina segue le note di patch e gli aggiornamenti ufficiali, con tutto il non verificato chiaramente marcato.",
        "sections": [
            {"heading": "Fatti di lancio (verificati)",
             "items": [
                ["Data di uscita", "6 agosto 2026 (uscita completa su Steam)."],
                ["Demo", "Una demo precede l'uscita completa."],
                ["Prezzo", "19,99 $ al lancio (sconto del 20 %; prezzo di listino 24,99 $)."],
             ]},
            {"heading": "Cronologia aggiornamenti (verificata da Steam)", "body": "Note di patch verificate dagli annunci ufficiali di Steam (agosto 2026):",
             "items": [
                ["2026-08-12", "1.0.010 — Corretti il filtro di ordinamento 'Più popolari' del Workshop, il caricamento delle pagine e i risultati mancanti; migliorata la chiarezza della ricerca."],
                ["2026-08-11", "1.0.009 — Migliorato Frame Quarter With Ports (le porte si riflettono sul lato opposto della catena, etichette A–D coerenti); corretta la geometria di Middle Window, Small Switch e Small Button."],
                ["2026-08-10", "1.0.008 — Corretti hitbox dell'Axis Rotometer e problemi residui; cavi Plasma verniciabili; pannelli Autohemisphere tornano in posizione dopo Fly Mode; supporti cavi verniciabili."],
                ["2026-08-09", "1.0.007 — Corretta la compatibilità con i dispositivi Metal; corretto il tasto predefinito (tasto centrale del mouse per 'raccogliere componente'); corretta la svista nelle descrizioni dei tubi; aggiunti più suggerimenti."],
                ["2026-08-08", "1.0.006 — Corretto Fuse Box impossibile da riaccendere; Axis Rotometer ora emette valori con segno corretti; corretta l'anteprima della Large Disposable Battery; aggiunti crediti, schermata iniziale e tracciamento obiettivi."],
             ]},
            {"heading": "Dove vengono pubblicati gli aggiornamenti ufficiali",
             "items": [
                "Gli annunci Steam del gioco (feed notizie della pagina del negozio).",
                "Il sito ufficiale approximatelyup.com e il Discord ufficiale.",
                "Il canale YouTube dello sviluppatore per gli annunci delle funzioni.",
             ]},
            {"heading": "Cosa resta non verificato", "body": "Il contenuto specifico delle patch (bilanciamento, correzioni, nuovi pezzi) non è verificato. Segniamo tutto come non verificato invece di fare ipotesi."},
        ],
    },
    "demo-vs-full": {
        "title": "Demo di Approximately Up vs gioco completo",
        "metaTitle": "Demo di Approximately Up vs gioco completo: qual è la differenza?",
        "metaDescription": "Demo vs versione completa di Approximately Up: date di uscita, prezzo, Workshop e obiettivi, più le differenze di contenuto ancora non verificate.",
        "intro": "La demo di Approximately Up è arrivata prima dell'uscita completa del 6 agosto 2026. Ecco il confronto verificato, con le differenze di contenuto chiaramente marcate come non verificate.",
        "sections": [
            {"heading": "Confronto verificato",
             "columns": ["Aspetto", "Demo", "Gioco completo"],
             "rows": [
                ["Disponibilità", "Demo (uscita prima, secondo la pagina del negozio)", "Uscita completa il 6 agosto 2026"],
                ["Prezzo", "non verificato", "19,99 $ (sconto di lancio del 20 %; prezzo di listino 24,99 $)"],
                ["Workshop di Steam", "non verificato", "Supportato (secondo la pagina del negozio)"],
                ["Obiettivi", "non verificato", "22 obiettivi Steam (secondo la pagina del negozio)"],
                ["Multigiocatore co-op", "non verificato", "Giocatore singolo + co-op online (secondo la pagina del negozio)"],
             ]},
            {"heading": "FAQ demo vs completo",
             "items": [
                ["La demo è gratuita?", "Non abbiamo verificato prezzo/modello della demo: non verificato."],
                ["I progressi della demo passano al gioco completo?", "Non verificato."],
                ["Quali contenuti ci sono solo nel gioco completo?", "Non verificato: i dettagli ufficiali di confronto sono in sospeso. Il gioco completo aggiunge il supporto del Workshop e 22 obiettivi secondo la pagina del negozio."],
                ["Dovrei provare prima la demo?", "Per la maggior parte dei giochi sandbox spaziali di costruzione, provare la demo è un buon modo per sentire il ciclo costruisci-schianta-ricostruisci prima di comprare: ma i limiti esatti della demo sono non verificati."],
             ]},
            {"heading": "Cosa resta non verificato", "body": "Contenuto esatto della demo, trasferimento dei progressi e differenze di funzioni non sono verificati contro una fonte ufficiale. Aggiorneremo questa tabella appena confermati."},
        ],
    },
    "achievements-list": {
        "title": "Elenco obiettivi Approximately Up",
        "metaTitle": "Obiettivi Approximately Up: elenco completo (22)",
        "metaDescription": "Approximately Up ha 22 obiettivi Steam. L'elenco completo dei nomi è ancora in fase di verifica: ecco cosa è confermato.",
        "intro": "La pagina ufficiale di Steam conferma 22 obiettivi. I nomi esatti e le condizioni di sblocco non sono ancora verificati, quindi questa pagina tiene traccia del numero confermato e marca l'elenco come non verificato.",
        "sections": [
            {"heading": "Confermato: 22 obiettivi", "body": "La pagina Steam elenca 22 obiettivi per Approximately Up. Non abbiamo ancora verificato nome, icona e condizione di ogni obiettivo: quella parte è non verificata."},
            {"heading": "Elenco obiettivi (non verificato)",
             "columns": ["Obiettivo", "Condizione"],
             "rows": [
                ["Obiettivi 1–22", "non verificato: nomi e condizioni in fase di verifica sull'elenco ufficiale."],
             ]},
            {"heading": "Come seguire gli obiettivi",
             "items": [
                "Usa l'overlay di Steam nel gioco per vedere i tuoi progressi.",
                "Segui gli annunci ufficiali di Steam: gli elenchi di obiettivi a volte arrivano con le note di patch.",
                "Pubblicheremo qui l'elenco completo verificato quando sarà confermato.",
             ]},
            {"heading": "FAQ sugli obiettivi",
             "items": [
                ["Quanti obiettivi ha Approximately Up?", "22, confermato sulla pagina ufficiale di Steam."],
                ["Quali sono i nomi degli obiettivi?", "non verificato: stiamo verificando l'elenco ufficiale e lo pubblicheremo quando confermato."],
                ["Posso ottenere tutti gli obiettivi in singolo?", "Non verificato: alcuni potrebbero richiedere il co-op, ma non lo sapremo finché l'elenco non sarà confermato."],
             ]},
        ],
    },
    "ships": {
        "title": "Navi Approximately Up",
        "metaTitle": "Navi Approximately Up: costruzioni, idee e design",
        "metaDescription": "Indice dei contenuti sulle navi di Approximately Up: guida alla costruzione, design, progetti e basi della costruzione modulare.",
        "intro": "Tutto sulle navi di Approximately Up in un unico posto: dalla tua prima costruzione alle idee di design della community.",
        "sections": [
            {"heading": "Guide sulle navi",
             "items": [
                "Guida alla costruzione di navi: impara il processo costruisci-schianta-ricostruisci.",
                "Migliori design: punti di partenza e idee della community.",
                "Guida ai progetti: cosa sappiamo di progetti e contenuti del Workshop.",
                "Mod: supporto del Workshop e domande sulle mod.",
             ]},
            {"heading": "FAQ sulle navi",
             "items": [
                ["Che tipo di navi posso costruire?", "Sono completamente modulari: avviti i pezzi come si incastrano (descrizione ufficiale). Gli elenchi specifici di pezzi sono non verificati."],
                ["Posso volare sulla Luna?", "Un thread della community chiede come; le meccaniche lunari sono non verificate."],
                ["Posso controllare più navi?", "Un thread della community lo chiede; non verificato."],
             ]},
        ],
    },
    "blueprints": {
        "title": "Progetti Approximately Up",
        "metaTitle": "Progetti Approximately Up: download e libreria",
        "metaDescription": "Indice dei contenuti sui progetti di Approximately Up: come usare i progetti, dove trovare design di navi e il Workshop di Steam.",
        "intro": "L'indice della libreria progetti: trova design di navi, impara il flusso (non verificato) dei progetti ed esplora il Workshop.",
        "sections": [
            {"heading": "Contenuti dei progetti",
             "items": [
                "Guida ai progetti: cosa è confermato e cosa non lo è sui progetti.",
                "Migliori design: idee di design e dove trovarne altre.",
                "Workshop di Steam: la casa confermata dei contenuti della community.",
             ]},
            {"heading": "FAQ dell'indice progetti",
             "items": [
                ["Dove posso scaricare i progetti?", "Il Workshop di Steam è il canale confermato per i contenuti della community; le meccaniche di download dei progetti nel gioco sono non verificate."],
                ["Come importo un progetto?", "Non verificato."],
                ["Posso condividere i miei design?", "Non verificato."],
             ]},
        ],
    },
    "guides": {
        "title": "Guide Approximately Up",
        "metaTitle": "Guide Approximately Up: tutte le pagine",
        "metaDescription": "Tutte le guide di Approximately Up in un indice: come si gioca, costruzione di navi, controlli, multigiocatore, mod, obiettivi e altro.",
        "intro": "L'indice completo delle guide di Approximately Up. Ogni pagina risponde a una domanda che i giocatori cercano davvero e marca tutto il non verificato.",
        "sections": [
            {"heading": "Tutte le guide",
             "items": [
                "Come si gioca: il ciclo costruisci-schianta-ricostruisci per principianti.",
                "Controlli: tastiera/mouse, stato del controller e note sul remappatore.",
                "Requisiti di sistema: stato delle specifiche e come controllare il tuo PC.",
                "Multigiocatore: co-op online, numero di giocatori e domande async.",
                "Uscita console: stato PS5/Xbox/Switch.",
                "Mod: Workshop di Steam e domande sulle mod.",
                "Note di patch: fatti di lancio e monitoraggio aggiornamenti.",
                "Demo vs completo: confronto verificato.",
                "Guida alla costruzione di navi: dalla prima nave alle grandi costruzioni.",
                "Cablaggio ed elettronica: ciò che è noto, ciò che non lo è.",
                "Guida ai progetti: stato dei progetti e Workshop.",
                "Migliori design: idee e design della community.",
                "Elenco obiettivi: 22 obiettivi, elenco non verificato.",
                "Navi / Progetti / Obiettivi: pagine indice.",
             ]},
            {"heading": "Come lavoriamo", "body": "Ogni pagina elenca 1–2 fonti affidabili e marca tutto il non verificato. Non inventiamo numeri, nomi o meccaniche."},
        ],
    },
    "achievements": {
        "title": "Obiettivi Approximately Up",
        "metaTitle": "Obiettivi Approximately Up: panoramica",
        "metaDescription": "Panoramica degli obiettivi di Approximately Up: 22 obiettivi Steam confermati, elenco completo in verifica e come seguire i progressi.",
        "intro": "L'hub degli obiettivi di Approximately Up: numero confermato, stato attuale dell'elenco e link alla pagina di monitoraggio completo.",
        "sections": [
            {"heading": "22 obiettivi confermati", "body": "La pagina Steam conferma 22 obiettivi. L'elenco completo di nomi e condizioni è non verificato."},
            {"heading": "Contenuti sugli obiettivi",
             "items": [
                "Elenco obiettivi: la pagina dedicata all'elenco completo (non verificato).",
                "Steam: controlla la sezione obiettivi della pagina del negozio.",
             ]},
            {"heading": "FAQ panoramica obiettivi",
             "items": [
                ["Quanti obiettivi ci sono?", "22 (confermato sulla pagina Steam)."],
                ["Dov'è l'elenco completo?", "non verificato: stiamo verificando l'elenco ufficiale."],
             ]},
        ],
    },
}

TR_PL = {
    "how-to-play": {
        "title": "Jak grać w Approximately Up",
        "metaTitle": "Jak grać w Approximately Up: kompletny poradnik dla początkujących",
        "metaDescription": "Nowy w Approximately Up? Poznaj pętlę buduj-rozbijaj-buduj od nowa, modułowe statki, kooperację online i eksplorację planet w tym poradniku.",
        "intro": "Approximately Up to kosmiczna gra sandboxowa o budowaniu, w której skręcasz części, startujesz, rozbijasz się i budujesz lepiej. Oto główna pętla i co warto wiedzieć przed pierwszym startem.",
        "sections": [
            {"heading": "Główna pętla: buduj, rozbijaj, buduj od nowa", "body": "Oficjalny opis streszcza pętlę w trzech słowach — buduj, rozbijaj, buduj od nowa. Wszystko inne z tego wynika.",
             "items": [
                ["Zacznij od małego", "Złóż statek z czegokolwiek, co da się skręcić na tyle długo, by polecieć. Nie potrzebujesz idealnego projektu — potrzebujesz czegoś, co wystartuje."],
                ["Zamontuj silniki i kable", "Ogromne silniki nadają ruch; kable i wszystko pomiędzy łączy twoją konstrukcję. Na początku spodziewaj się bałaganu."],
                ["Lot próbny", "Wystartuj i zobacz, co się trzyma. Pierwsze loty to eksperymenty, nie dopracowane przeloty."],
                ["Rozbij się (to się zdarza)", "Rozbicia są częścią pętli. Oficjalny opis traktuje je jako coś normalnego — gruz to lekcja, nie porażka."],
                ["Buduj mądrzej od nowa", "Wykorzystaj to, czego się nauczyłeś. Każda iteracja uczy, które części się trzymają, a które kombinacje latają."],
             ]},
            {"heading": "Co gra oficjalnie obiecuje", "body": "Z oficjalnego opisu Steam:",
             "items": [
                "Odkrywaj nowe planety w kooperacji online dzięki w pełni modułowemu statkowi.",
                "Montuj ogromne silniki, irytujące kable i wszystko pomiędzy.",
                "Wykonuj zwariowane misje i stawiaj czoła zagrożeniom kosmosu.",
                "Graj solo lub z załogą — i kłóć się z nią, jak to ujmuje oficjalny opis.",
             ]},
            {"heading": "FAQ dla początkujących",
             "items": [
                ["Czy Approximately Up jest multiplayer?", "Tak — oficjalna strona Steam wymienia tryb jednoosobowy i kooperację online."],
                ["Czy muszę znać się na inżynierii?", "Nie. Gra opiera się na próbach i błędach: skręcaj części, lataj, rozbijaj się, ucz się."],
                ["Czy jest demo?", "Tak — oficjalna strona Steam wymienia demo sprzed pełnej premiery (6 sierpnia 2026)."],
                ["Czy mogę grać na Steam Deck?", "Kompatybilność nie została jeszcze potwierdzona. Gracze pytają o to na forach Steam; oznaczamy to jako niepotwierdzone do czasu oficjalnej odpowiedzi."],
             ]},
            {"heading": "Co jeszcze musimy zweryfikować", "body": "Konkretne nazwy planet i misji oraz szczegółowe mechaniki (projekty, okablowanie, radar, cofanie czasu) nie zostały jeszcze zweryfikowane w oficjalnych źródłach. Oznaczamy je jako niepotwierdzone i aktualizujemy tę stronę, gdy pojawią się oficjalne informacje."},
        ],
    },
    "ship-building-guide": {
        "title": "Poradnik budowania statków Approximately Up",
        "metaTitle": "Poradnik budowania statków Approximately Up: od pierwszego statku do wielkich konstrukcji",
        "metaDescription": "Naucz się budować statki w Approximately Up: modułowy proces buduj-rozbijaj-buduj od nowa, silniki i kable, plus potrzeby społeczności jak lot na Księżyc i radar.",
        "intro": "Budowanie statków to serce Approximately Up. Oficjalny opis jest prosty: skręcaj części, aż polecą, potem buduj mądrzej. Ten poradnik pokazuje proces bez wymyślania niezweryfikowanych statystyk części.",
        "sections": [
            {"heading": "Zbuduj swój pierwszy statek", "body": "W oparciu o oficjalny opis (modułowe części, silniki, kable, buduj-rozbijaj-buduj od nowa) oto proces:",
             "items": [
                ["Zbierz części", "Zbierz dostępne części i skręć je. Oficjalny opis mówi, że każda konstrukcja 'skręca się na tyle długo, by polecieć' — zacznij od tego."],
                ["Dodaj silniki", "Zamontuj silniki, aby się poruszać. Oficjalny opis podkreśla 'ogromne silniki' jako kluczowy element."],
                ["Poprowadź kable", "Połącz konstrukcję kablami — 'irytujące kable' są częścią doświadczenia. Spodziewaj się niechlujnego okablowania."],
                ["Lot próbny", "Wystartuj. Twój pierwszy statek nie musi być ładny; ma ci pokazać, co się trzyma."],
                ["Rozbij się i iteruj", "Buduj od nowa z tym, czego się nauczyłeś. Pętla to buduj → rozbijaj → buduj od nowa."],
             ]},
            {"heading": "Zasady projektowania (zgodne z oficjalnymi)",
             "items": [
                "W pełni modułowy statek: wszystko można przearanżować między lotami.",
                "Balansuj masę i ciąg — cięższe statki potrzebują większego ciągu (konkretne liczby niepotwierdzone).",
                "Miej części zapasowe: rozbicia są przewidziane.",
                "Zaplanuj kooperację: grając z załogą, ustalcie role (pilot, budowniczy, inżynier).",
             ]},
            {"heading": "Tutoriale, o które prosi społeczność",
             "items": [
                ["Jak dostać się na Księżyc?", "Prawdziwy wątek na forum Steam — gracze chcą poradnika lotu na Księżyc. Konkretne mechaniki Księżyca są niepotwierdzone."],
                ["Radar monitor / urządzenie dla początkujących", "Prawdziwy wątek na forum Steam — gracze chcą tutoriala urządzenia radarowego. Mechaniki radaru są niepotwierdzone."],
             ]},
            {"heading": "Co pozostaje niepotwierdzone", "body": "Konkretne nazwy części, statystyki, przepisy, cele planetarne i nazwy misji nie zostały jeszcze zweryfikowane. Ten poradnik używa tylko oficjalnego opisu i oznaczonych pytań społeczności; pogłębimy go, gdy pojawią się zweryfikowane informacje."},
        ],
    },
    "blueprints-guide": {
        "title": "Poradnik projektów Approximately Up",
        "metaTitle": "Projekty Approximately Up: pobieranie, udostępnianie i użycie",
        "metaDescription": "Projekty Approximately Up: co wiemy o znajdowaniu i używaniu projektów, wsparcie Steam Workshop i co pozostaje niepotwierdzone.",
        "intro": "Projekty to jeden z najczęściej wyszukiwanych tematów Approximately Up. Oficjalne mechaniki projektów (import, eksport, udostępnianie) nie są jeszcze zweryfikowane, więc ta strona obejmuje to, co potwierdzone, i to, co nie.",
        "sections": [
            {"heading": "Szczegóły projektów: niepotwierdzone", "body": "Mechaniki importu, eksportu i udostępniania projektów są na naszej liście niepotwierdzonych — nie zweryfikowaliśmy ich w oficjalnym źródle. Rozbudujemy tę stronę, gdy tylko potwierdzimy wiarygodne informacje."},
            {"heading": "Znajdowanie projektów statków już dziś", "body": "Choć oficjalne narzędzia projektów są niepotwierdzone, Steam Workshop to potwierdzone miejsce, gdzie żyją treści społeczności:",
             "items": [
                ["Otwórz Steam Workshop dla Approximately Up", "Treści wgrywane przez społeczność są tam hostowane (wsparcie Workshop potwierdzone na stronie sklepu)."],
                ["Przeglądaj statki i konstrukcje", "Szukaj projektów udostępnionych przez innych graczy."],
                ["Subskrybuj", "Subskrypcja zapisuje treści w twojej bibliotece."],
                ["Sprawdź w grze", "Zobacz, jak zasubskrybowane elementy pojawiają się w grze — dokładne kroki niepotwierdzone."],
             ]},
            {"heading": "FAQ o projektach",
             "items": [
                ["Czy mogę pobierać projekty w Approximately Up?", "Niepotwierdzone. Treści z Workshop to obecnie najbliższy potwierdzony kanał."],
                ["Czy mogę udostępniać swoje projekty statków?", "Niepotwierdzone. Potwierdzimy dokładny proces udostępniania po weryfikacji."],
                ["Czy projekty to to samo co elementy Workshop?", "Niekoniecznie — związek między projektami w grze a elementami Workshop jest niepotwierdzony."],
             ]},
            {"heading": "Źródła, które warto obserwować", "body": "Zweryfikujemy mechaniki projektów w oficjalnych kanałach (ogłoszenia Steam, oficjalna strona, Discord) i zaktualizujemy tę stronę. Nic tu nie jest wymyślone."},
        ],
    },
    "wiring-electronics": {
        "title": "Poradnik okablowania i elektroniki Approximately Up",
        "metaTitle": "Okablowanie i elektronika Approximately Up: co wiemy",
        "metaDescription": "Okablowanie i elektronika w Approximately Up: kable w konstrukcjach, pytania społeczności o erę lamp próżniowych i Remapper — z oznaczonymi niepotwierdzonymi szczegółami.",
        "intro": "Okablowanie i elektronika to wielki temat społeczności, ale oficjalne informacje są skąpe. Ta strona zbiera to, co zweryfikowane, i to, o co pytają gracze, z wyraźnym oznaczeniem wszystkiego, co niepotwierdzone.",
        "sections": [
            {"heading": "Oficjalne informacje są ograniczone", "body": "Oficjalny opis wspomina kable jako część modułowej konstrukcji ('irytujące kable i wszystko pomiędzy'), ale szczegółowe mechaniki okablowania i obwodów nie są jeszcze zweryfikowane. Oznaczamy je jako niepotwierdzone."},
            {"heading": "Wątki społeczności (prawdziwe pytania graczy)",
             "items": [
                ["Czy możemy wyjść poza erę lamp próżniowych w elektronice?", "Wątek na forum Steam o etapach/erze części elektronicznych — sugeruje wczesnoetapową tematykę; dokładne mechaniki niepotwierdzone."],
                ["Nie mogę ustawić wartości w Remapper", "Wątek na forum Steam o problemach z ustawianiem wartości w Remapper/Constant — dokładny proces niepotwierdzony."],
             ]},
            {"heading": "Co możemy bezpiecznie powiedzieć",
             "items": [
                "Kable są oficjalną częścią modułowego budowania statków.",
                "Elektronika wydaje się obszarem postępu (społeczność wspomina wczesną 'erę lamp próżniowych').",
                "W grze istnieją narzędzia do ustawiania parametrów/wartości (Remapper), ale dokładne użycie jest niepotwierdzone.",
             ]},
            {"heading": "FAQ o okablowaniu i elektronice",
             "items": [
                ["Jak działa okablowanie w Approximately Up?", "Niepotwierdzone. Opublikujemy poradnik, gdy pojawią się oficjalne lub wiarygodnie potwierdzone informacje."],
                ["Jakie są poziomy elektroniki?", "Wątek społeczności wspomina 'erę lamp próżniowych'; dokładne poziomy i odblokowania są niepotwierdzone."],
                ["Dlaczego nie mogę ustawić wartości w Remapper?", "Wątek społeczności zgłasza ten problem; oficjalny proces jest niepotwierdzony."],
             ]},
        ],
    },
    "controls": {
        "title": "Sterowanie Approximately Up",
        "metaTitle": "Sterowanie Approximately Up: klawiatura, mysz i status pada",
        "metaDescription": "Poradnik sterowania Approximately Up: co wiemy o klawiaturze i myszy, wsparciu pada i remapperze w grze — plus co pozostaje niepotwierdzone.",
        "intro": "Wsparcie pada to jedno z najczęstszych pytań w społeczności Steam zaraz po premierze. Oto, co możemy potwierdzić, o co pytają gracze i co pozostaje niepotwierdzone.",
        "sections": [
            {"heading": "Co wiemy (zweryfikowane)",
             "items": [
                ["Platforma", "Gra jest na PC (Steam). Klawiatura i mysz to domyślne sterowanie."],
                ["Wsparcie pada", "Niepotwierdzone jeszcze przez dewelopera. Wątek na forum Steam pyta 'Controller Support in the Future?', co sugeruje, że pełne wsparcie nie jest potwierdzone na premierę."],
                ["Remapper w grze", "Gracze dyskutują o Remapper — wątek społeczności zgłasza problemy z ustawianiem wartości. Dokładny proces mapowania oznaczamy jako niepotwierdzony."],
             ]},
            {"heading": "Jak skonfigurować sterowanie teraz",
             "items": [
                "Otwórz ustawienia w grze i sprawdź sekcję wejście/sterowanie, aby zobaczyć aktualne przypisanie klawiszy.",
                "Użyj Remapper w grze do przebindowania klawiszy; jeśli wartości nie działają, sprawdź wątek społeczności i notatki dewelopera.",
                "Aktualizacje wsparcia pada śledź na oficjalnym Discordzie i w ogłoszeniach Steam.",
             ]},
            {"heading": "Niepotwierdzone: pełna mapa klawiszy", "body": "Pełna oficjalna mapa klawiszy (ruch, kamera, menu budowania, sterowanie silnikami) nie została jeszcze zweryfikowana w oficjalnym źródle. Oznaczamy ją jako niepotwierdzoną i opublikujemy tabelę po potwierdzeniu."},
            {"heading": "FAQ o sterowaniu",
             "items": [
                ["Czy Approximately Up wspiera pady?", "Jeszcze niepotwierdzone. Społeczność pyta; oznaczamy to jako niepotwierdzone, dopóki deweloper lub oficjalne źródło tego nie potwierdzi."],
                ["Czy mogę przebindować klawisze?", "W grze jest Remapper. Niektórzy gracze zgłaszają problemy z wartościami; dokładny proces jest niepotwierdzony."],
                ["Czy jest układ dla Steam Deck?", "Kompatybilność ze Steam Deck to wciąż otwarte pytanie w społeczności — układ jest niepotwierdzony."],
             ]},
        ],
    },
    "multiplayer": {
        "title": "Poradnik multiplayera Approximately Up",
        "metaTitle": "Multiplayer Approximately Up: kooperacja, liczba graczy i crossplay",
        "metaDescription": "Multiplayer Approximately Up wyjaśniony: kooperacja online, ilu graczy, czy jest tryb asynchroniczny i co pozostaje niepotwierdzone.",
        "intro": "Approximately Up to oficjalnie gra jednoosobowa z kooperacją online. Ta strona odpowiada na pytania o multiplayer, które gracze naprawdę zadają, i oznacza to, czego jeszcze nie możemy zweryfikować.",
        "sections": [
            {"heading": "Status oficjalny", "body": "Oficjalna strona Steam wymienia 'Tryb jednoosobowy' i 'Kooperacja online' jako wspierane tryby. Koncepcja gry opiera się na załodze wspólnie eksplorującej planety modułowym statkiem."},
            {"heading": "FAQ o multiplayerze",
             "items": [
                ["Ilu graczy może grać razem?", "Dokładna liczba nie jest zweryfikowana w naszej bazie wiedzy — oznaczamy ją jako niepotwierdzoną."],
                ["Czy jest kooperacja online?", "Tak — kooperacja online jest wymieniona na oficjalnej stronie Steam."],
                ["Czy jest crossplay między platformami?", "Niepotwierdzone. Gra jest obecnie na PC (Steam); wersje konsolowe nie są zapowiedziane, więc crossplay jest niepotwierdzony."],
                ["Czy jest tryb asynchroniczny?", "Niepotwierdzone. Wątek na forum Steam pyta o 'Asynchronous Multiplayer', co sugeruje, że to jeszcze nie oficjalna funkcja — oznaczamy jako niepotwierdzone."],
                ["Czy mogę grać solo?", "Tak — tryb jednoosobowy jest wymieniony jako wspierany."],
             ]},
            {"heading": "O co pyta społeczność",
             "items": [
                "Tryb asynchroniczny — czy gracze oczekują trybu async.",
                "Liczba graczy / 'ilu graczy' to najważniejsza potrzeba wyszukiwania; opublikujemy zweryfikowaną liczbę, gdy będzie dostępna.",
             ]},
            {"heading": "Co pozostaje niepotwierdzone", "body": "Dokładny limit graczy, proces zapraszania, szczegóły hostowania i crossplay nie zostały jeszcze zweryfikowane w oficjalnych źródłach. Zaktualizujemy tę stronę, gdy tylko zostaną potwierdzone."},
        ],
    },
    "best-ship-designs": {
        "title": "Najlepsze projekty statków Approximately Up",
        "metaTitle": "Pomysły na statki i najlepsze projekty Approximately Up",
        "metaDescription": "Pomysły na projekty statków Approximately Up: punkty startowe dla własnych konstrukcji, pytania społeczności o projektowanie i gdzie znaleźć więcej projektów.",
        "intro": "Szukasz pomysłów na statki? Ta strona zbiera punkty startowe oparte na oficjalnej fantazji buduj-rozbijaj-buduj od nowa oraz pytania społeczności, które kształtują to, co gracze chcą budować.",
        "sections": [
            {"heading": "Punkty startowe projektowania (inspiracja, nie oficjalne specyfikacje)",
             "items": [
                "Szybka maszyna na silnikach: zamontuj ogromne silniki i zaakceptuj, że kontrola przyjdzie później.",
                "Użytkowy transportowiec: stawiaj na ładunek i części misji zamiast prędkości — misje wymagają ładowności (szczegóły niepotwierdzone).",
                "Statek załogowy do kooperacji: zaprojektuj przestrzeń dla załogi wspólnie eksplorującej planety.",
                "Budowa z bałaganem kabli: zaakceptuj 'irytujące kable' — okablowanie to część uroku (mechaniki okablowania niepotwierdzone).",
             ]},
            {"heading": "Pytania społeczności o projektowanie",
             "items": [
                ["Miernik krzywizny trajektorii", "Wątek na forum Steam o narzędziu trajektorii — gracze chcą lepszych narzędzi lotu; oficjalny status niepotwierdzony."],
                ["mody do tworzenia wielu statków?", "Wątek na forum Steam o sterowaniu więcej niż jednym statkiem — niepotwierdzone."],
             ]},
            {"heading": "Gdzie znaleźć więcej projektów",
             "items": [
                "Steam Workshop dla Approximately Up (wsparcie potwierdzone).",
                "Oficjalny kanał YouTube dla konstrukcji z zwiastunów.",
                "Dyskusje społeczności Steam dla zrzutów ekranu i pomysłów graczy.",
             ]},
            {"heading": "Co pozostaje niepotwierdzone", "body": "Konkretne statystyki części, projekty nazwanych konstrukcji i jakiekolwiek listy 'najlepszych' nie są zweryfikowane. Trzymamy tę stronę jako inspirację plus zweryfikowane źródła, a resztę oznaczamy jako niepotwierdzoną."},
        ],
    },
    "system-requirements": {
        "title": "Wymagania systemowe Approximately Up",
        "metaTitle": "Wymagania systemowe Approximately Up (PC)",
        "metaDescription": "Wymagania systemowe Approximately Up na PC: minimalne i zalecane specyfikacje nie są jeszcze potwierdzone — oto, co wiemy i jak sprawdzić kompatybilność.",
        "intro": "Gracze chcą prostej odpowiedzi, czy ich PC uruchomi Approximately Up. Oficjalne wymagania minimalne i zalecane nie są jeszcze zweryfikowane, więc ta strona mówi, co wiemy, a co nie.",
        "sections": [
            {"heading": "Oficjalne specyfikacje: niepotwierdzone", "body": "Nie zweryfikowaliśmy jeszcze oficjalnych wymagań minimalnych i zalecanych w oficjalnym źródle. Zamiast wymyślać liczby, oznaczamy tabelę jako niepotwierdzoną i wypełnimy ją po potwierdzeniu (strona Steam lub oficjalna strona)."},
            {"heading": "Tabela specyfikacji (niepotwierdzona)",
             "columns": ["Element", "Minimalne", "Zalecane"],
             "rows": [
                ["System operacyjny", "niepotwierdzone", "niepotwierdzone"],
                ["Procesor", "niepotwierdzone", "niepotwierdzone"],
                ["Pamięć", "niepotwierdzone", "niepotwierdzone"],
                ["Karta graficzna", "niepotwierdzone", "niepotwierdzone"],
                ["Miejsce na dysku", "niepotwierdzone", "niepotwierdzone"],
                ["DirectX", "niepotwierdzone", "niepotwierdzone"],
             ]},
            {"heading": "Jak sprawdzić swój PC",
             "items": [
                "Otwórz Steam i sprawdź stronę gry — wymagania systemowe zwykle pojawiają się tam po publikacji.",
                "Porównaj CPU/GPU/RAM z oficjalnymi liczbami, gdy je opublikujemy.",
                "Steam Deck: kompatybilność to otwarte pytanie społeczności ('Playable on Deck?'); oznaczamy je jako niepotwierdzone.",
             ]},
            {"heading": "FAQ o wymaganiach systemowych",
             "items": [
                ["Czy mój PC uruchomi Approximately Up?", "Jeszcze nie możemy potwierdzić — oficjalne wymagania minimalne/zalecane są niepotwierdzone. Sprawdź stronę Steam, gdy deweloper je opublikuje."],
                ["Czy Approximately Up jest na Steam Deck?", "Niepotwierdzone. Wątek na forum Steam pyta 'Playable on Deck?' — kompatybilność jest niepotwierdzona do czasu oficjalnej odpowiedzi."],
                ["Czy gra jest wymagająca?", "To kosmiczna gra sandboxowa z modułowymi statkami opartymi na fizyce; podamy zweryfikowane liczby, gdy tylko będą dostępne."],
             ]},
        ],
    },
    "console-release": {
        "title": "Premiera konsolowa Approximately Up: status PS5, Xbox i Switch",
        "metaTitle": "Data premiery konsolowej Approximately Up (PS5, Xbox, Switch)",
        "metaDescription": "Czy Approximately Up trafi na PS5, Xbox lub Switch? Na razie brak oficjalnej zapowiedzi — oto status konsolowy i jak śledzić oficjalne wieści.",
        "intro": "'Data premiery Approximately Up PS5', 'wersja Xbox' i 'wersja Switch' to wyszukiwania, na które nie odpowiada nawet wiki gry. Uczciwa odpowiedź dziś: brak zweryfikowanej oficjalnej zapowiedzi konsolowej — oto strona statusu.",
        "sections": [
            {"heading": "Status konsolowy (stan na 09.08.2026)",
             "items": [
                ["Obecne platformy", "Tylko PC (Steam). Gra ukazała się 6 sierpnia 2026 na Steam."],
                ["PS5", "niepotwierdzone — brak zweryfikowanej oficjalnej zapowiedzi wersji na PlayStation 5."],
                ["Xbox", "niepotwierdzone — brak zweryfikowanej oficjalnej zapowiedzi wersji na Xbox."],
                ["Nintendo Switch", "niepotwierdzone — brak zweryfikowanej oficjalnej zapowiedzi wersji na Switch."],
                ["Oficjalne oświadczenie", "Nie zweryfikowaliśmy oficjalnego oświadczenia dewelopera o planach konsolowych; oznaczamy to jako niepotwierdzone i zaktualizujemy, gdy się pojawi."],
             ]},
            {"heading": "Jak być na bieżąco",
             "items": [
                "Obserwuj oficjalną stronę approximatelyup.com i oficjalny Discord (discord.gg/approximatelyup).",
                "Śledź kanał YouTube dewelopera (@ApproximatelyUp) i TikTok (@approximatelyup) w poszukiwaniu zapowiedzi.",
                "Sprawdzaj stronę Steam — wieści o konsolach zwykle pojawiają się tam najpierw.",
             ]},
            {"heading": "FAQ o konsolach",
             "items": [
                ["Czy Approximately Up jest na PS5?", "Niezapowiedziane — oznaczamy jako niepotwierdzone. Nie ma jeszcze zweryfikowanego oficjalnego oświadczenia."],
                ["Czy jest na Xbox?", "Niezapowiedziane — niepotwierdzone."],
                ["Czy jest na Nintendo Switch?", "Niezapowiedziane — niepotwierdzone."],
                ["Kiedy premiera konsolowa?", "Nie ma jeszcze daty. Ta strona zostanie zaktualizowana w chwili zweryfikowania oficjalnej zapowiedzi."],
             ]},
            {"heading": "Dlaczego ta strona istnieje", "body": "Premiera konsolowa to jedno z pytań o najwyższej intencji wyszukiwania dla tej gry, ale żadne wiarygodne źródło na nie nie odpowiedziało. Ta strona podaje zweryfikowany status (tylko PC) i śledzi przyszłe zapowiedzi, zamiast wymyślać datę."},
        ],
    },
    "mods": {
        "title": "Poradnik modów Approximately Up",
        "metaTitle": "Mody Approximately Up: Steam Workshop, instalacja i pytania",
        "metaDescription": "Mody Approximately Up wyjaśnione: wsparcie Steam Workshop, jak subskrybować mody i pytania społeczności, np. o wiele statków.",
        "intro": "Approximately Up wspiera Steam Workshop, co ułatwia znajdowanie i instalowanie modów. Oto, co jest potwierdzone i o co proszą gracze.",
        "sections": [
            {"heading": "Pobieranie modów ze Steam Workshop", "body": "Wsparcie Workshop jest potwierdzone na oficjalnej stronie. Standardowy proces:",
             "items": [
                ["Otwórz Workshop", "Na stronie gry w Steam otwórz zakładkę Workshop (lub centrum społeczności Workshop)."],
                ["Przeglądaj i subskrybuj", "Znajdź mod lub element i naciśnij Subskrybuj — Steam pobierze go automatycznie."],
                ["Uruchom grę", "Otwórz Approximately Up i sprawdź menu modów/treści, aby zobaczyć zasubskrybowane elementy."],
                ["Włącz, co chcesz", "Włącz mody, których chcesz używać. Szczegóły menu modów w grze są niepotwierdzone."],
             ]},
            {"heading": "O co pyta społeczność",
             "items": [
                "mody do tworzenia wielu statków? — prawdziwy wątek na forum Steam; wsparcie wielu statków przez mody jest niepotwierdzone.",
                "Wyszukiwania związane z cheat engine istnieją dla wielu gier; nie dostarczamy cheatów, tylko zweryfikowane informacje o modach.",
             ]},
            {"heading": "FAQ o modach",
             "items": [
                ["Czy Approximately Up wspiera mody?", "Oficjalnie wspiera Steam Workshop (według strony sklepu). Pełna dokumentacja modowania jest niepotwierdzona."],
                ["Jak instalować mody?", "Subskrybuj przez Steam Workshop; instalacją zajmuje się Steam. Kroki w grze są niepotwierdzone."],
                ["Czy mody pozwolą mi sterować wieloma statkami?", "Wątek społeczności o to prosi; żaden zweryfikowany mod tego jeszcze nie oferuje — niepotwierdzone."],
             ]},
            {"heading": "Co pozostaje niepotwierdzone", "body": "Dokładne funkcje Workshop, wytyczne dotyczące modów oraz wpływ modów na osiągnięcia lub multiplayer nie zostały jeszcze zweryfikowane. Zaktualizujemy tę stronę po potwierdzeniu oficjalnej dokumentacji."},
        ],
    },
    "patch-notes": {
        "title": "Noty aktualizacji Approximately Up",
        "metaTitle": "Noty aktualizacji i historia wersji Approximately Up",
        "metaDescription": "Noty aktualizacji i historia wersji Approximately Up: informacje o premierze, gdzie publikowane są oficjalne aktualizacje i nasz śledzony dziennik zmian (niepotwierdzone elementy oznaczone).",
        "intro": "Approximately Up ukazało się 6 sierpnia 2026. Ta strona śledzi oficjalne noty aktualizacji i patche — wszystko niepotwierdzone jest wyraźnie oznaczone.",
        "sections": [
            {"heading": "Fakty o premierze (zweryfikowane)",
             "items": [
                ["Data premiery", "6 sierpnia 2026 (pełna premiera na Steam)."],
                ["Demo", "Demo ukazało się przed pełną premierą."],
                ["Cena", "19,99 $ przy premierze (20% zniżki; cena katalogowa 24,99 $)."],
             ]},
            {"heading": "Oś czasu aktualizacji (zweryfikowana przez Steam)", "body": "Notatki aktualizacji zweryfikowane z oficjalnych ogłoszeń Steam (sierpień 2026):",
             "items": [
                ["2026-08-12", "1.0.010 — Naprawiono filtr sortowania „Najpopularniejsze” w Warsztacie, ładowanie stron i brakujące wyniki; poprawiono czytelność wyszukiwania."],
                ["2026-08-11", "1.0.009 — Ulepszono Frame Quarter With Ports (porty odbijają się po drugiej stronie łańcucha, etykiety A–D spójne); naprawiono geometrię Middle Window, Small Switch i Small Button."],
                ["2026-08-10", "1.0.008 — Naprawiono hitbox Axis Rotometer i pozostałe problemy; kable Plasma można malować; panele Autohemisphere wracają po Fly Mode; uchwyty kabli można malować."],
                ["2026-08-09", "1.0.007 — Naprawiono kompatybilność z urządzeniami Metal; poprawiono domyślny klawisz (środkowy przycisk myszy do 'podnoszenia komponentu'); poprawiono literówkę w opisach rur; dodano więcej podpowiedzi."],
                ["2026-08-08", "1.0.006 — Naprawiono Fuse Box, którego nie można było włączyć; Axis Rotometer poprawnie podaje wartości ze znakiem; naprawiono podgląd Large Disposable Battery; dodano napisy, ekran startowy i śledzenie postępów."],
             ]},
            {"heading": "Gdzie publikowane są oficjalne aktualizacje",
             "items": [
                "Ogłoszenia Steam dla gry (kanał aktualności na stronie sklepu).",
                "Oficjalna strona approximatelyup.com i oficjalny Discord.",
                "Kanał YouTube dewelopera dla zapowiedzi funkcji.",
             ]},
            {"heading": "Co pozostaje niepotwierdzone", "body": "Konkretna zawartość patchy (zmiany balansu, poprawki, nowe części) nie jest zweryfikowana. Oznaczamy wszystko jako niepotwierdzone, zamiast zgadywać."},
        ],
    },
    "demo-vs-full": {
        "title": "Demo Approximately Up vs pełna gra",
        "metaTitle": "Demo Approximately Up vs pełna gra: jaka jest różnica?",
        "metaDescription": "Demo a pełna wersja Approximately Up: daty premiery, cena, Workshop i osiągnięcia — oraz wciąż niepotwierdzone różnice w zawartości.",
        "intro": "Demo Approximately Up ukazało się przed pełną premierą 6 sierpnia 2026. Oto zweryfikowane porównanie, z różnicami w zawartości wyraźnie oznaczonymi jako niepotwierdzone.",
        "sections": [
            {"heading": "Zweryfikowane porównanie",
             "columns": ["Aspekt", "Demo", "Pełna gra"],
             "rows": [
                ["Dostępność", "Demo (ukazało się wcześniej, według strony sklepu)", "Pełna premiera 6 sierpnia 2026"],
                ["Cena", "niepotwierdzone", "19,99 $ (20% zniżki startowej; cena katalogowa 24,99 $)"],
                ["Steam Workshop", "niepotwierdzone", "Wspierany (według strony sklepu)"],
                ["Osiągnięcia", "niepotwierdzone", "22 osiągnięcia Steam (według strony sklepu)"],
                ["Kooperacja online", "niepotwierdzone", "Tryb jednoosobowy + kooperacja online (według strony sklepu)"],
             ]},
            {"heading": "FAQ demo vs pełna gra",
             "items": [
                ["Czy demo jest darmowe?", "Nie zweryfikowaliśmy ceny/modelu demo — niepotwierdzone."],
                ["Czy postęp z demo przechodzi do pełnej gry?", "Niepotwierdzone."],
                ["Jaka zawartość jest tylko w pełnej grze?", "Niepotwierdzone — oficjalne szczegóły porównania w toku. Pełna gra dodaje wsparcie Workshop i 22 osiągnięcia według strony sklepu."],
                ["Czy powinienem najpierw wypróbować demo?", "W większości kosmicznych gier sandboxowych demo to dobry sposób, by poczuć pętlę buduj-rozbijaj-buduj od nowa przed zakupem — ale dokładny zakres demo jest niepotwierdzony."],
             ]},
            {"heading": "Co pozostaje niepotwierdzone", "body": "Dokładna zawartość demo, przenoszenie postępu i różnice w funkcjach nie są zweryfikowane w oficjalnym źródle. Zaktualizujemy tę tabelę po potwierdzeniu."},
        ],
    },
    "achievements-list": {
        "title": "Lista osiągnięć Approximately Up",
        "metaTitle": "Osiągnięcia Approximately Up: pełna lista (22)",
        "metaDescription": "Approximately Up ma 22 osiągnięcia Steam. Pełna lista nazw jest wciąż weryfikowana — oto, co jest potwierdzone.",
        "intro": "Oficjalna strona Steam potwierdza 22 osiągnięcia. Dokładne nazwy i warunki odblokowania nie są jeszcze zweryfikowane, więc ta strona śledzi potwierdzoną liczbę i oznacza listę jako niepotwierdzoną.",
        "sections": [
            {"heading": "Potwierdzone: 22 osiągnięcia", "body": "Strona Steam wymienia 22 osiągnięcia dla Approximately Up. Nie zweryfikowaliśmy jeszcze nazwy, ikony i warunku każdego osiągnięcia — ta część jest niepotwierdzona."},
            {"heading": "Lista osiągnięć (niepotwierdzona)",
             "columns": ["Osiągnięcie", "Warunek"],
             "rows": [
                ["Osiągnięcia 1–22", "niepotwierdzone — nazwy i warunki są weryfikowane względem oficjalnej listy."],
             ]},
            {"heading": "Jak śledzić osiągnięcia",
             "items": [
                "Użyj nakładki Steam w grze, aby zobaczyć postęp.",
                "Obserwuj oficjalne ogłoszenia Steam — listy osiągnięć czasem pojawiają się z notami aktualizacji.",
                "Opublikujemy tutaj pełną zweryfikowaną listę po potwierdzeniu.",
             ]},
            {"heading": "FAQ o osiągnięciach",
             "items": [
                ["Ile osiągnięć ma Approximately Up?", "22, potwierdzone na oficjalnej stronie Steam."],
                ["Jakie są nazwy osiągnięć?", "niepotwierdzone — weryfikujemy oficjalną listę i opublikujemy ją po potwierdzeniu."],
                ["Czy mogę zdobyć wszystkie osiągnięcia w trybie solo?", "Niepotwierdzone — niektóre mogą wymagać kooperacji, ale dowiemy się tego po potwierdzeniu listy."],
             ]},
        ],
    },
    "ships": {
        "title": "Statki Approximately Up",
        "metaTitle": "Statki Approximately Up: konstrukcje, pomysły i projekty",
        "metaDescription": "Indeks treści o statkach Approximately Up: poradnik budowania, projekty statków, plany i podstawy modułowego budowania.",
        "intro": "Wszystko o statkach Approximately Up w jednym miejscu — od pierwszej konstrukcji po pomysły społeczności.",
        "sections": [
            {"heading": "Poradniki o statkach",
             "items": [
                "Poradnik budowania statków — poznaj proces buduj-rozbijaj-buduj od nowa.",
                "Najlepsze projekty — punkty startowe i pomysły społeczności.",
                "Poradnik projektów — co wiemy o projektach i treściach Workshop.",
                "Mody — wsparcie Workshop i pytania o mody.",
             ]},
            {"heading": "FAQ o statkach",
             "items": [
                ["Jakie statki mogę zbudować?", "Są w pełni modułowe — skręcasz części, jak pasują (oficjalny opis). Konkretne listy części są niepotwierdzone."],
                ["Czy mogę polecieć na Księżyc?", "Wątek społeczności pyta, jak; mechaniki Księżyca są niepotwierdzone."],
                ["Czy mogę sterować wieloma statkami?", "Wątek społeczności o to pyta; niepotwierdzone."],
             ]},
        ],
    },
    "blueprints": {
        "title": "Projekty Approximately Up",
        "metaTitle": "Projekty Approximately Up: pobieranie i biblioteka",
        "metaDescription": "Indeks treści o projektach Approximately Up: jak używać projektów, gdzie znaleźć projekty statków i Steam Workshop.",
        "intro": "Indeks biblioteki projektów — znajdź projekty statków, poznaj (niepotwierdzony) proces pracy z projektami i przeglądaj Workshop.",
        "sections": [
            {"heading": "Treści o projektach",
             "items": [
                "Poradnik projektów — co jest potwierdzone, a co nie, w kwestii projektów.",
                "Najlepsze projekty — pomysły na projekty i gdzie znaleźć więcej.",
                "Steam Workshop — potwierdzone miejsce treści społeczności.",
             ]},
            {"heading": "FAQ indeksu projektów",
             "items": [
                ["Gdzie mogę pobrać projekty?", "Steam Workshop to potwierdzony kanał treści społeczności; mechaniki pobierania projektów w grze są niepotwierdzone."],
                ["Jak zaimportować projekt?", "Niepotwierdzone."],
                ["Czy mogę udostępniać swoje projekty?", "Niepotwierdzone."],
             ]},
        ],
    },
    "guides": {
        "title": "Poradniki Approximately Up",
        "metaTitle": "Poradniki Approximately Up: wszystkie strony",
        "metaDescription": "Wszystkie poradniki Approximately Up w jednym indeksie: jak grać, budowanie statków, sterowanie, multiplayer, mody, osiągnięcia i więcej.",
        "intro": "Kompletny indeks poradników Approximately Up. Każda strona odpowiada na jedno pytanie, którego gracze naprawdę szukają, i oznacza wszystko, co niepotwierdzone.",
        "sections": [
            {"heading": "Wszystkie poradniki",
             "items": [
                "Jak grać — pętla buduj-rozbijaj-buduj od nowa dla początkujących.",
                "Sterowanie — klawiatura/mysz, status pada i notatki o remapperze.",
                "Wymagania systemowe — status specyfikacji i jak sprawdzić swój PC.",
                "Multiplayer — kooperacja online, liczba graczy i pytania o async.",
                "Premiera konsolowa — status PS5/Xbox/Switch.",
                "Mody — Steam Workshop i pytania o mody.",
                "Noty aktualizacji — fakty o premierze i śledzenie aktualizacji.",
                "Demo vs pełna gra — zweryfikowane porównanie.",
                "Poradnik budowania statków — od pierwszego statku do wielkich konstrukcji.",
                "Okablowanie i elektronika — co wiadomo, co nie.",
                "Poradnik projektów — status projektów i Workshop.",
                "Najlepsze projekty — pomysły i projekty społeczności.",
                "Lista osiągnięć — 22 osiągnięcia, lista niepotwierdzona.",
                "Statki / Projekty / Osiągnięcia — strony indeksowe.",
             ]},
            {"heading": "Jak pracujemy", "body": "Każda strona wymienia 1–2 wiarygodne źródła i oznacza wszystko, co niepotwierdzone. Nie wymyślamy liczb, nazw ani mechanik."},
        ],
    },
    "achievements": {
        "title": "Osiągnięcia Approximately Up",
        "metaTitle": "Osiągnięcia Approximately Up: przegląd",
        "metaDescription": "Przegląd osiągnięć Approximately Up: 22 osiągnięcia Steam potwierdzone, pełna lista w weryfikacji i jak śledzić postęp.",
        "intro": "Centrum osiągnięć Approximately Up — potwierdzona liczba, aktualny status listy i linki do strony pełnego śledzenia.",
        "sections": [
            {"heading": "Potwierdzono 22 osiągnięcia", "body": "Strona Steam potwierdza 22 osiągnięcia. Pełna lista nazw i warunków jest niepotwierdzona."},
            {"heading": "Treści o osiągnięciach",
             "items": [
                "Lista osiągnięć — dedykowana strona pełnej (niepotwierdzonej) listy.",
                "Steam — sprawdź sekcję osiągnięć na stronie sklepu.",
             ]},
            {"heading": "FAQ przeglądu osiągnięć",
             "items": [
                ["Ile jest osiągnięć?", "22 (potwierdzone na stronie Steam)."],
                ["Gdzie jest pełna lista?", "niepotwierdzone — weryfikujemy oficjalną listę."],
             ]},
        ],
    },
}

TR_PT = {
    "how-to-play": {
        "title": "Como jogar Approximately Up",
        "metaTitle": "Como jogar Approximately Up: guia completo para iniciantes",
        "metaDescription": "Novo em Approximately Up? Aprenda o ciclo construa-caia-reconstrua, as naves modulares, o multijogador cooperativo e a exploração de planetas.",
        "intro": "Approximately Up é um jogo de construção sandbox espacial em que você aparafusa peças, decola, cai e reconstrói melhor. Aqui está o ciclo principal e o que saber antes do primeiro lançamento.",
        "sections": [
            {"heading": "O ciclo principal: construa, caia, reconstrua", "body": "A descrição oficial resume o ciclo em três palavras: construa, caia, reconstrua. Todo o resto vem disso.",
             "items": [
                ["Comece pequeno", "Monte uma nave com o que quer que se aparafuse por tempo suficiente para voar. Você não precisa de um design perfeito para começar — precisa de algo que decole."],
                ["Monte propulsores e cabos", "Propulsores gigantes te movem; cabos e tudo mais conectam sua construção. Espere um layout bagunçado no começo."],
                ["Voo de teste", "Decole e veja o que segura. Os primeiros voos são experimentos, não voos refinados."],
                ["Cair (acontece)", "As quedas fazem parte do ciclo. A proposta oficial as trata como normais: os destroços são uma lição, não um fracasso."],
                ["Reconstrua com mais inteligência", "Use o que aprendeu para reconstruir. Cada iteração ensina quais peças seguram e quais combinações voam."],
             ]},
            {"heading": "O que o jogo promete oficialmente", "body": "Da descrição oficial na Steam:",
             "items": [
                "Explore novos planetas no multijogador cooperativo com sua nave totalmente modular.",
                "Monte propulsores gigantes, cabos irritantes e tudo mais.",
                "Complete missões malucas e enfrente os perigos do espaço.",
                "Jogue sozinho ou com uma tripulação — e discuta com a tripulação, como diz a proposta oficial.",
             ]},
            {"heading": "Perguntas frequentes para iniciantes",
             "items": [
                ["Approximately Up é multijogador?", "Sim: a página oficial da Steam lista um jogador e multijogador cooperativo online."],
                ["Preciso saber de engenharia?", "Não. O jogo é baseado em tentativa e erro: aparafuse peças, voe, caia, aprenda."],
                ["Tem demo?", "Sim: a página oficial da Steam lista uma demo anterior ao lançamento completo (6 de agosto de 2026)."],
                ["Posso jogar no Steam Deck?", "A compatibilidade ainda não foi confirmada. Jogadores estão perguntando nos fóruns da Steam; marcamos isso como não verificado até haver resposta oficial."],
             ]},
            {"heading": "O que ainda precisamos verificar", "body": "Nomes específicos de planetas e missões e guias de mecânica detalhados (plantas, fiação, radar, rebobinar) ainda não foram verificados em fontes oficiais. Marcamos como não verificados e atualizamos esta página quando houver informações oficiais."},
        ],
    },
    "ship-building-guide": {
        "title": "Guia de construção de naves Approximately Up",
        "metaTitle": "Guia de construção de naves Approximately Up: da primeira nave às grandes construções",
        "metaDescription": "Aprenda a construir naves em Approximately Up: o processo modular construa-caia-reconstrua, propulsores e cabos, e necessidades da comunidade como a Lua e o radar.",
        "intro": "A construção de naves é o coração de Approximately Up. A proposta oficial é simples: aparafuse peças até voarem e depois reconstrua com mais inteligência. Este guia explica o processo sem inventar estatísticas ainda não verificadas.",
        "sections": [
            {"heading": "Construa sua primeira nave", "body": "Com base na descrição oficial (peças modulares, propulsores, cabos, construa-caia-reconstrua), aqui está o processo:",
             "items": [
                ["Junte peças", "Colete as peças disponíveis e aparafuse-as. A proposta oficial diz que qualquer construção 'se aparafusa por tempo suficiente para voar' — comece por aí."],
                ["Adicione propulsores", "Monte propulsores para se mover. A descrição oficial destaca os 'propulsores gigantes' como parte central."],
                ["Passe os cabos", "Conecte sua construção com cabos — os 'cabos irritantes' fazem parte da experiência. Espere uma fiação bagunçada."],
                ["Voo de teste", "Decole. Sua primeira nave não precisa ser bonita; ela precisa te ensinar o que segura."],
                ["Caia e itere", "Reconstrua com o que aprendeu. O ciclo é construa → caia → reconstrua."],
             ]},
            {"heading": "Princípios de design (alinhados ao oficial)",
             "items": [
                "Nave totalmente modular: tudo pode ser reorganizado entre voos.",
                "Equilibre peso e empuxo — naves mais pesadas precisam de mais empuxo (números específicos não verificados).",
                "Mantenha peças sobressalentes: quedas são esperadas.",
                "Planeje o cooperativo: se jogar com uma tripulação, dividam papéis (piloto, construtor, engenheiro).",
             ]},
            {"heading": "Tutoriais pedidos pela comunidade",
             "items": [
                ["Como ir até a Lua?", "Um tópico real do fórum da Steam — jogadores querem um guia de viagem à Lua. As mecânicas lunares específicas não são verificadas."],
                ["Monitor/dispositivo de radar para iniciantes", "Um tópico real do fórum da Steam — jogadores querem um tutorial do dispositivo de radar. As mecânicas de radar não são verificadas."],
             ]},
            {"heading": "O que ainda não está verificado", "body": "Nomes específicos de peças, estatísticas, receitas, destinos de planetas e nomes de missões ainda não foram verificados. Este guia usa apenas a descrição oficial e perguntas comunitárias marcadas; vamos aprofundá-lo quando chegarem informações verificadas."},
        ],
    },
    "blueprints-guide": {
        "title": "Guia de plantas Approximately Up",
        "metaTitle": "Plantas Approximately Up: baixar, compartilhar e usar",
        "metaDescription": "Plantas de Approximately Up: o que sabemos sobre encontrá-las e usá-las, o suporte à Oficina da Steam e o que ainda não está verificado.",
        "intro": "As plantas são um dos tópicos mais pesquisados de Approximately Up. As mecânicas oficiais (importar, exportar, compartilhar) ainda não foram verificadas, então esta página cobre o que é confirmado e o que não é.",
        "sections": [
            {"heading": "Detalhes das plantas: não verificados", "body": "As mecânicas de importar, exportar e compartilhar plantas estão na nossa lista de não verificados — ainda não as confirmamos em uma fonte oficial. Expandiremos esta página assim que verificarmos informações confiáveis."},
            {"heading": "Encontrar designs de naves hoje", "body": "Embora as ferramentas oficiais de plantas não sejam verificadas, a Oficina da Steam é o lugar confirmado onde vive o conteúdo da comunidade:",
             "items": [
                ["Abra a Oficina da Steam de Approximately Up", "O conteúdo enviado pela comunidade fica lá (o suporte à Oficina é confirmado na página da loja)."],
                ["Navegue por naves e construções", "Procure designs compartilhados por outros jogadores."],
                ["Inscreva-se", "A inscrição salva o conteúdo na sua biblioteca."],
                ["Confira no jogo", "Veja como os itens inscritos aparecem no jogo — os passos exatos não são verificados."],
             ]},
            {"heading": "Perguntas frequentes sobre plantas",
             "items": [
                ["Posso baixar plantas em Approximately Up?", "Não verificado. O conteúdo da Oficina é o canal confirmado mais próximo hoje."],
                ["Posso compartilhar meus designs de naves?", "Não verificado. Vamos confirmar o fluxo exato de compartilhamento quando for verificado."],
                ["Plantas são o mesmo que itens da Oficina?", "Não necessariamente — a relação entre plantas do jogo e itens da Oficina não é verificada."],
             ]},
            {"heading": "Fontes a acompanhar", "body": "Vamos verificar as mecânicas de plantas nos canais oficiais (anúncios da Steam, site oficial, Discord) e atualizar esta página. Nada aqui inventa mecânicas."},
        ],
    },
    "wiring-electronics": {
        "title": "Guia de fiação e eletrônica Approximately Up",
        "metaTitle": "Fiação e eletrônica Approximately Up: o que sabemos",
        "metaDescription": "Fiação e eletrônica em Approximately Up: cabos nas construções, perguntas da comunidade sobre a era das válvulas e o Remapper — com detalhes não verificados marcados.",
        "intro": "Fiação e eletrônica são um grande tópico da comunidade, mas as informações oficiais são escassas. Esta página reúne o que é verificado e o que os jogadores perguntam, com tudo não verificado claramente marcado.",
        "sections": [
            {"heading": "As informações oficiais são limitadas", "body": "A descrição oficial menciona cabos como parte da construção modular ('cabos irritantes, e tudo mais'), mas as mecânicas detalhadas de fiação e circuitos ainda não foram verificadas. Nós as marcamos como não verificadas."},
            {"heading": "Tópicos da comunidade (perguntas reais de jogadores)",
             "items": [
                ["Podemos ir além da era das válvulas na eletrônica?", "Um tópico do fórum da Steam sobre a progressão/era dos componentes eletrônicos — sugere um tema eletrônico de era inicial; mecânicas exatas não verificadas."],
                ["Não consigo definir valores no Remapper", "Um tópico do fórum da Steam relatando problemas ao definir valores no Remapper/Constant — o fluxo exato não é verificado."],
             ]},
            {"heading": "O que podemos dizer com segurança",
             "items": [
                "Cabos fazem oficialmente parte da fantasia de construção modular de naves.",
                "A eletrônica parece ser uma área de progressão (a comunidade menciona uma 'era das válvulas' inicial).",
                "Existem ferramentas de ajuste de parâmetros/valores no jogo (Remapper), mas o uso exato não é verificado.",
             ]},
            {"heading": "Perguntas frequentes sobre fiação e eletrônica",
             "items": [
                ["Como a fiação funciona em Approximately Up?", "Não verificado. Publicaremos um guia assim que existirem informações oficiais ou verificadas de forma confiável."],
                ["Quais são os níveis da eletrônica?", "Um tópico da comunidade menciona uma 'era das válvulas'; os níveis e desbloqueios exatos não são verificados."],
                ["Por que não consigo definir valores no Remapper?", "Um tópico da comunidade relata esse problema; o fluxo oficial não é verificado."],
             ]},
        ],
    },
    "controls": {
        "title": "Controles de Approximately Up",
        "metaTitle": "Controles de Approximately Up: teclado, mouse e status do controle",
        "metaDescription": "Guia de controles de Approximately Up: o que sabemos sobre teclado e mouse, suporte a controle e o remapeador do jogo — além do que ainda não está verificado.",
        "intro": "O suporte a controle é uma das perguntas mais frequentes na comunidade da Steam logo após o lançamento. Aqui está o que podemos confirmar, o que os jogadores perguntam e o que ainda não está verificado.",
        "sections": [
            {"heading": "O que sabemos (verificado)",
             "items": [
                ["Plataforma", "O jogo está no PC (Steam). Teclado e mouse são a entrada padrão."],
                ["Suporte a controle", "Ainda não confirmado pelo desenvolvedor. Um tópico do fórum da Steam pergunta 'Controller Support in the Future?', o que sugere que o suporte completo não é confirmado no lançamento."],
                ["Remapeador do jogo", "Jogadores estão discutindo o Remapper — um tópico da comunidade relata problemas ao definir valores. Marcamos o fluxo exato de mapeamento como não verificado."],
             ]},
            {"heading": "Como configurar os controles agora",
             "items": [
                "Abra as configurações do jogo e confira a seção de entrada/controles para o mapeamento de teclas atual.",
                "Use o Remapper do jogo para rebindar teclas; se os valores não aplicarem, confira o tópico da comunidade e as notas do desenvolvedor.",
                "Para atualizações do suporte a controle, siga o Discord oficial e os anúncios da Steam.",
             ]},
            {"heading": "Não verificado: mapa completo de teclas", "body": "O mapa oficial completo de teclas (movimento, câmera, menu de construção, controle de propulsores) ainda não foi verificado em uma fonte oficial. Marcamos como não verificado e publicaremos a tabela quando for confirmado."},
            {"heading": "Perguntas frequentes sobre controles",
             "items": [
                ["Approximately Up suporta controles?", "Ainda não confirmado. A comunidade está perguntando; marcamos como não verificado até o desenvolvedor ou uma fonte oficial confirmar."],
                ["Posso rebindar as teclas?", "Há um Remapper no jogo. Alguns jogadores relatam problemas com valores; o fluxo exato não é verificado."],
                ["Há um layout para Steam Deck?", "A compatibilidade com Steam Deck em si é uma questão aberta na comunidade — o layout não é verificado."],
             ]},
        ],
    },
    "multiplayer": {
        "title": "Guia de multijogador Approximately Up",
        "metaTitle": "Multijogador Approximately Up: cooperativo, número de jogadores e crossplay",
        "metaDescription": "O multijogador de Approximately Up explicado: cooperativo online, quantos jogadores, se há multijogador assíncrono e o que ainda não está verificado.",
        "intro": "Approximately Up é oficialmente um jogo de um jogador e cooperativo online. Esta página responde às perguntas de multijogador que os jogadores realmente fazem e marca o que ainda não podemos verificar.",
        "sections": [
            {"heading": "Status oficial", "body": "A página oficial da Steam lista 'Um jogador' e 'Cooperativo online' como modos suportados. A proposta do jogo gira em torno de uma tripulação explorando planetas juntos em uma nave modular."},
            {"heading": "Perguntas frequentes sobre multijogador",
             "items": [
                ["Quantos jogadores podem jogar juntos?", "O número exato não está verificado em nossa base de conhecimento — marcamos como não verificado."],
                ["Há cooperativo online?", "Sim — o multijogador cooperativo online está listado na página oficial da Steam."],
                ["Há multijogador multiplataforma?", "Não verificado. O jogo está atualmente no PC (Steam); versões de console não são anunciadas, então o crossplay não é verificado."],
                ["Há multijogador assíncrono?", "Não confirmado. Um tópico do fórum da Steam pergunta sobre 'Asynchronous Multiplayer', o que sugere que ainda não é um recurso oficial — marcamos como não verificado."],
                ["Posso jogar sozinho?", "Sim — o modo de um jogador está listado como suportado."],
             ]},
            {"heading": "O que a comunidade pergunta",
             "items": [
                "Multijogador assíncrono — se os jogadores esperam um modo assíncrono.",
                "O número de jogadores / 'quantos jogadores' é uma necessidade de busca importante; publicaremos o número verificado quando disponível.",
             ]},
            {"heading": "O que ainda não está verificado", "body": "O limite exato de jogadores, o fluxo de convite, os detalhes de hospedagem e o crossplay ainda não foram verificados em fontes oficiais. Atualizaremos esta página assim que forem confirmados."},
        ],
    },
    "best-ship-designs": {
        "title": "Melhores designs de naves Approximately Up",
        "metaTitle": "Ideias de naves e melhores designs Approximately Up",
        "metaDescription": "Ideias de design de naves Approximately Up: pontos de partida para suas construções, perguntas de design da comunidade e onde encontrar mais designs.",
        "intro": "Procurando ideias de naves? Esta página reúne pontos de partida baseados na fantasia oficial construa-caia-reconstrua, além de perguntas da comunidade que moldam o que os jogadores querem construir.",
        "sections": [
            {"heading": "Pontos de partida de design (inspiração, não especificações oficiais)",
             "items": [
                "Veloz de propulsores: monte propulsores gigantes e aceite que o controle vem depois.",
                "Transportador utilitário: priorize carga e peças de missão em vez de velocidade — missões precisam de capacidade (detalhes não verificados).",
                "Nave de tripulação cooperativa: projete espaço para uma tripulação explorar planetas juntos.",
                "Construção com cabos bagunçados: abrace os 'cabos irritantes' — a fiação faz parte do charme (mecânicas de fiação não verificadas).",
             ]},
            {"heading": "Perguntas de design da comunidade",
             "items": [
                ["Medidor de curvatura de trajetória", "Um tópico do fórum da Steam sobre uma ferramenta de trajetória — jogadores querem melhores ferramentas de voo; status oficial não verificado."],
                ["mods para fazer várias naves?", "Um tópico do fórum da Steam sobre controlar mais de uma nave — não verificado."],
             ]},
            {"heading": "Onde encontrar mais designs",
             "items": [
                "A Oficina da Steam de Approximately Up (suporte confirmado).",
                "O canal oficial do YouTube para as construções dos trailers.",
                "As discussões da comunidade da Steam para capturas de tela e ideias dos jogadores.",
             ]},
            {"heading": "O que ainda não está verificado", "body": "Estatísticas específicas de peças, plantas de designs nomeados e qualquer lista dos 'melhores' não são verificadas. Mantemos esta página como inspiração + fontes verificadas e marcamos o resto como não verificado."},
        ],
    },
    "system-requirements": {
        "title": "Requisitos de sistema Approximately Up",
        "metaTitle": "Requisitos de sistema Approximately Up (PC)",
        "metaDescription": "Requisitos de sistema de Approximately Up para PC: requisitos mínimos e recomendados ainda não verificados — aqui está o que sabemos e como checar a compatibilidade.",
        "intro": "Os jogadores querem uma resposta direta sobre se o PC deles roda Approximately Up. Os requisitos mínimos e recomendados oficiais ainda não estão verificados, então esta página diz o que sabemos e o que não.",
        "sections": [
            {"heading": "Especificações oficiais: não verificadas", "body": "Ainda não verificamos os requisitos mínimos e recomendados oficiais em uma fonte oficial. Em vez de inventar números, marcamos a tabela como não verificada e a preencheremos assim que for confirmada (página da Steam ou site oficial)."},
            {"heading": "Tabela de especificações (não verificada)",
             "columns": ["Item", "Mínimo", "Recomendado"],
             "rows": [
                ["Sistema operacional", "não verificado", "não verificado"],
                ["Processador", "não verificado", "não verificado"],
                ["Memória", "não verificado", "não verificado"],
                ["Placa de vídeo", "não verificado", "não verificado"],
                ["Armazenamento", "não verificado", "não verificado"],
                ["DirectX", "não verificado", "não verificado"],
             ]},
            {"heading": "Como verificar seu PC",
             "items": [
                "Abra a Steam e confira a página do jogo — os requisitos de sistema costumam aparecer lá quando publicados.",
                "Compare sua CPU/GPU/RAM com os números oficiais quando os publicarmos.",
                "Steam Deck: a compatibilidade é uma questão aberta da comunidade ('Playable on Deck?'); marcamos como não verificada.",
             ]},
            {"heading": "Perguntas frequentes sobre requisitos",
             "items": [
                ["Meu PC roda Approximately Up?", "Ainda não podemos confirmar — os requisitos mínimos/recomendados oficiais não são verificados. Confira a página da Steam quando o desenvolvedor os publicar."],
                ["Approximately Up roda no Steam Deck?", "Não confirmado. Um tópico do fórum da Steam pergunta 'Playable on Deck?' — a compatibilidade é não verificada até haver resposta oficial."],
                ["É pesado?", "É um jogo de construção sandbox espacial com naves físicas modulares; relataremos números verificados assim que disponíveis."],
             ]},
        ],
    },
    "console-release": {
        "title": "Lançamento para consoles Approximately Up: status PS5, Xbox e Switch",
        "metaTitle": "Data de lançamento para consoles Approximately Up (PS5, Xbox, Switch)",
        "metaDescription": "Approximately Up vai sair para PS5, Xbox ou Switch? Ainda não há anúncio oficial — aqui está o status para consoles e como acompanhar as notícias oficiais.",
        "intro": "'Data de lançamento PS5 Approximately Up', 'versão Xbox' e 'versão Switch' são buscas que nem o wiki do jogo responde. A resposta honesta hoje: nenhum anúncio oficial de console verificado — esta é a página de status.",
        "sections": [
            {"heading": "Status para consoles (em 09/08/2026)",
             "items": [
                ["Plataformas atuais", "Apenas PC (Steam). O jogo foi lançado em 6 de agosto de 2026 na Steam."],
                ["PS5", "não verificado — nenhum anúncio oficial verificado de uma versão para PlayStation 5."],
                ["Xbox", "não verificado — nenhum anúncio oficial verificado de uma versão para Xbox."],
                ["Nintendo Switch", "não verificado — nenhum anúncio oficial verificado de uma versão para Switch."],
                ["Declaração oficial", "Não verificamos uma declaração oficial do desenvolvedor sobre planos para consoles; marcamos como não verificado e atualizaremos assim que existir."],
             ]},
            {"heading": "Como se manter informado",
             "items": [
                "Siga o site oficial approximatelyup.com e o Discord oficial (discord.gg/approximatelyup).",
                "Acompanhe o canal do YouTube do desenvolvedor (@ApproximatelyUp) e o TikTok (@approximatelyup) para anúncios.",
                "Confira a página da Steam — notícias de consoles costumam ser anunciadas lá primeiro.",
             ]},
            {"heading": "Perguntas frequentes sobre consoles",
             "items": [
                ["Approximately Up está no PS5?", "Não anunciado — marcamos como não verificado. Ainda não existe declaração oficial verificada."],
                ["Está no Xbox?", "Não anunciado — não verificado."],
                ["Está no Nintendo Switch?", "Não anunciado — não verificado."],
                ["Quando é a data de lançamento para consoles?", "Ainda não existe data. Esta página será atualizada no momento em que um anúncio oficial for verificado."],
             ]},
            {"heading": "Por que esta página existe", "body": "O lançamento para consoles é uma das perguntas de maior intenção para este jogo, mas nenhuma fonte confiável a respondeu. Esta página dá o status verificado (apenas PC) e acompanha futuros anúncios em vez de inventar uma data."},
        ],
    },
    "mods": {
        "title": "Guia de mods Approximately Up",
        "metaTitle": "Mods Approximately Up: Oficina da Steam, instalação e perguntas",
        "metaDescription": "Mods de Approximately Up explicados: suporte à Oficina da Steam, como assinar mods e perguntas da comunidade como várias naves.",
        "intro": "Approximately Up suporta a Oficina da Steam, o que torna simples encontrar e instalar mods. Aqui está o que é confirmado e o que os jogadores pedem.",
        "sections": [
            {"heading": "Obtendo mods da Oficina da Steam", "body": "O suporte à Oficina é confirmado na página oficial. O fluxo padrão:",
             "items": [
                ["Abra a Oficina", "Na página da Steam do jogo, abra a aba Oficina (ou o hub comunitário da Oficina)."],
                ["Navegue e inscreva-se", "Encontre um mod ou item e pressione Inscrever-se — a Steam baixa automaticamente."],
                ["Inicie o jogo", "Abra Approximately Up e confira o menu de mods/conteúdo do jogo para ver os itens inscritos."],
                ["Ative o que quiser", "Ative os mods que deseja usar. Os detalhes do menu de mods no jogo não são verificados."],
             ]},
            {"heading": "O que a comunidade pergunta",
             "items": [
                "mods para fazer várias naves? — um tópico real do fórum da Steam; o suporte a várias naves via mods não é verificado.",
                "Buscas relacionadas a cheat engine existem para muitos jogos; não fornecemos cheats, apenas informações verificadas sobre mods.",
             ]},
            {"heading": "Perguntas frequentes sobre mods",
             "items": [
                ["Approximately Up suporta mods?", "Oficialmente suporta a Oficina da Steam (segundo a página da loja). A documentação completa de modding não é verificada."],
                ["Como instalo mods?", "Inscreva-se pela Oficina da Steam; a Steam cuida da instalação. Os passos no jogo não são verificados."],
                ["Mods me deixam controlar várias naves?", "Um tópico da comunidade pede isso; nenhum mod verificado oferece ainda — não verificado."],
             ]},
            {"heading": "O que ainda não está verificado", "body": "Os recursos exatos da Oficina, as diretrizes de mods e se os mods afetam conquistas ou multijogador ainda não foram verificados. Atualizaremos esta página quando a documentação oficial for confirmada."},
        ],
    },
    "patch-notes": {
        "title": "Notas de atualização Approximately Up",
        "metaTitle": "Notas de atualização e histórico de versões Approximately Up",
        "metaDescription": "Notas de atualização e histórico Approximately Up: informações de lançamento, onde as atualizações oficiais são publicadas e nosso changelog acompanhado (itens não verificados marcados).",
        "intro": "Approximately Up foi lançado em 6 de agosto de 2026. Esta página acompanha as notas de patch e atualizações oficiais — com tudo não verificado claramente marcado.",
        "sections": [
            {"heading": "Fatos de lançamento (verificados)",
             "items": [
                ["Data de lançamento", "6 de agosto de 2026 (lançamento completo na Steam)."],
                ["Demo", "Uma demo precede o lançamento completo."],
                ["Preço", "US$ 19,99 no lançamento (20% de desconto; preço de tabela US$ 24,99)."],
             ]},
            {"heading": "Linha do tempo de atualizações (verificada via Steam)", "body": "Notas de patch verificadas nos anúncios oficiais da Steam (agosto de 2026):",
             "items": [
                ["2026-08-12", "1.0.010 — Corrigidos o filtro de classificação 'Mais populares' da Workshop, o carregamento de páginas e resultados ausentes; melhorada a clareza da busca."],
                ["2026-08-11", "1.0.009 — Melhorado Frame Quarter With Ports (as portas se espelham no outro lado da cadeia, rótulos A–D consistentes); corrigidas as geometrias de Middle Window, Small Switch e Small Button."],
                ["2026-08-10", "1.0.008 — Corrigidos o hitbox do Axis Rotometer e problemas restantes; cabos Plasma agora pintáveis; painéis Autohemisphere voltam à posição após Fly Mode; suportes de cabo pintáveis."],
                ["2026-08-09", "1.0.007 — Corrigida a compatibilidade com dispositivos Metal; corrigida a tecla padrão (botão do meio do mouse para 'pegar componente'); corrigido erro de digitação nas descrições de canos; mais dicas."],
                ["2026-08-08", "1.0.006 — Corrigido Fuse Box que não ligava; Axis Rotometer agora exibe valores com sinal corretos; corrigida a pré-visualização da Large Disposable Battery; adicionados créditos, tela inicial e rastreamento de objetivos."],
             ]},
            {"heading": "Onde as atualizações oficiais são publicadas",
             "items": [
                "Os anúncios da Steam para o jogo (feed de notícias na página da loja).",
                "O site oficial approximatelyup.com e o Discord oficial.",
                "O canal do YouTube do desenvolvedor para anúncios de recursos.",
             ]},
            {"heading": "O que ainda não está verificado", "body": "O conteúdo específico dos patches (mudanças de balanceamento, correções, novas peças) não é verificado. Marcamos tudo como não verificado em vez de adivinhar."},
        ],
    },
    "demo-vs-full": {
        "title": "Demo de Approximately Up vs jogo completo",
        "metaTitle": "Demo de Approximately Up vs jogo completo: qual a diferença?",
        "metaDescription": "Demo vs versão completa de Approximately Up: datas de lançamento, preço, Oficina e conquistas — e as diferenças de conteúdo ainda não verificadas.",
        "intro": "A demo de Approximately Up veio antes do lançamento completo em 6 de agosto de 2026. Aqui está a comparação verificada, com as diferenças de conteúdo claramente marcadas como não verificadas.",
        "sections": [
            {"heading": "Comparação verificada",
             "columns": ["Aspecto", "Demo", "Jogo completo"],
             "rows": [
                ["Disponibilidade", "Demo (lançada antes, segundo a página da loja)", "Lançamento completo em 6 de agosto de 2026"],
                ["Preço", "não verificado", "US$ 19,99 (desconto de lançamento de 20%; preço de tabela US$ 24,99)"],
                ["Oficina da Steam", "não verificado", "Suportada (segundo a página da loja)"],
                ["Conquistas", "não verificado", "22 conquistas da Steam (segundo a página da loja)"],
                ["Multijogador cooperativo", "não verificado", "Um jogador + cooperativo online (segundo a página da loja)"],
             ]},
            {"heading": "Perguntas frequentes demo vs completo",
             "items": [
                ["A demo é gratuita?", "Não verificamos o preço/modelo da demo — não verificado."],
                ["O progresso da demo passa para o jogo completo?", "Não verificado."],
                ["Qual conteúdo só existe no jogo completo?", "Não verificado — os detalhes oficiais de comparação estão pendentes. O jogo completo adiciona suporte à Oficina e 22 conquistas segundo a página da loja."],
                ["Devo experimentar a demo primeiro?", "Para a maioria dos jogos de construção sandbox espacial, experimentar a demo é um bom jeito de sentir o ciclo construa-caia-reconstrua antes de comprar — mas os limites exatos da demo não são verificados."],
             ]},
            {"heading": "O que ainda não está verificado", "body": "O conteúdo exato da demo, a transferência de progresso e as diferenças de recursos não são verificados em uma fonte oficial. Atualizaremos esta tabela assim que forem confirmados."},
        ],
    },
    "achievements-list": {
        "title": "Lista de conquistas Approximately Up",
        "metaTitle": "Conquistas Approximately Up: lista completa (22)",
        "metaDescription": "Approximately Up tem 22 conquistas na Steam. A lista completa de nomes ainda está sendo verificada — aqui está o que é confirmado.",
        "intro": "A página oficial da Steam confirma 22 conquistas. Os nomes exatos e as condições de desbloqueio ainda não estão verificados, então esta página acompanha o número confirmado e marca a lista como não verificada.",
        "sections": [
            {"heading": "Confirmado: 22 conquistas", "body": "A página da Steam lista 22 conquistas para Approximately Up. Ainda não verificamos o nome, o ícone e a condição de cada conquista — essa parte não é verificada."},
            {"heading": "Lista de conquistas (não verificada)",
             "columns": ["Conquista", "Condição"],
             "rows": [
                ["Conquistas 1–22", "não verificado — nomes e condições em verificação na lista oficial."],
             ]},
            {"heading": "Como acompanhar as conquistas",
             "items": [
                "Use a sobreposição da Steam no jogo para ver seu progresso.",
                "Siga os anúncios oficiais da Steam — listas de conquistas às vezes saem com notas de patch.",
                "Publicaremos aqui a lista completa verificada quando confirmada.",
             ]},
            {"heading": "Perguntas frequentes sobre conquistas",
             "items": [
                ["Quantas conquistas Approximately Up tem?", "22, confirmado na página oficial da Steam."],
                ["Quais são os nomes das conquistas?", "não verificado — estamos verificando a lista oficial e a publicaremos quando confirmada."],
                ["Posso conseguir todas as conquistas no modo um jogador?", "Não verificado — algumas podem exigir cooperativo, mas só saberemos quando a lista for confirmada."],
             ]},
        ],
    },
    "ships": {
        "title": "Naves Approximately Up",
        "metaTitle": "Naves Approximately Up: construções, ideias e designs",
        "metaDescription": "Índice do conteúdo de naves de Approximately Up: guia de construção, designs de naves, plantas e o básico da construção modular.",
        "intro": "Tudo sobre as naves de Approximately Up em um só lugar — da sua primeira construção às ideias de design da comunidade.",
        "sections": [
            {"heading": "Guias de naves",
             "items": [
                "Guia de construção de naves — aprenda o processo construa-caia-reconstrua.",
                "Melhores designs — pontos de partida e ideias da comunidade.",
                "Guia de plantas — o que sabemos sobre plantas e conteúdo da Oficina.",
                "Mods — suporte à Oficina e perguntas sobre mods.",
             ]},
            {"heading": "Perguntas frequentes sobre naves",
             "items": [
                ["Que tipo de naves posso construir?", "Elas são totalmente modulares — você aparafusa peças como elas se encaixam (descrição oficial). Listas específicas de peças não são verificadas."],
                ["Posso voar até a Lua?", "Um tópico da comunidade pergunta como; as mecânicas lunares não são verificadas."],
                ["Posso controlar várias naves?", "Um tópico da comunidade pergunta sobre isso; não verificado."],
             ]},
        ],
    },
    "blueprints": {
        "title": "Plantas Approximately Up",
        "metaTitle": "Plantas Approximately Up: downloads e biblioteca",
        "metaDescription": "Índice do conteúdo de plantas de Approximately Up: como usar plantas, onde encontrar designs de naves e a Oficina da Steam.",
        "intro": "O índice da biblioteca de plantas — encontre designs de naves, aprenda o fluxo (não verificado) de plantas e explore a Oficina.",
        "sections": [
            {"heading": "Conteúdo de plantas",
             "items": [
                "Guia de plantas — o que é confirmado e o que não é sobre plantas.",
                "Melhores designs — ideias de design e onde encontrar mais.",
                "Oficina da Steam — o lar confirmado do conteúdo da comunidade.",
             ]},
            {"heading": "Perguntas frequentes do índice de plantas",
             "items": [
                ["Onde posso baixar plantas?", "A Oficina da Steam é o canal confirmado para conteúdo da comunidade; as mecânicas de download de plantas no jogo não são verificadas."],
                ["Como importo uma planta?", "Não verificado."],
                ["Posso compartilhar meus designs?", "Não verificado."],
             ]},
        ],
    },
    "guides": {
        "title": "Guias Approximately Up",
        "metaTitle": "Guias Approximately Up: todas as páginas",
        "metaDescription": "Todos os guias de Approximately Up em um índice: como jogar, construção de naves, controles, multijogador, mods, conquistas e mais.",
        "intro": "O índice completo de guias de Approximately Up. Cada página responde a uma pergunta que os jogadores realmente pesquisam e marca tudo o que não é verificado.",
        "sections": [
            {"heading": "Todos os guias",
             "items": [
                "Como jogar — o ciclo construa-caia-reconstrua para iniciantes.",
                "Controles — teclado/mouse, status do controle e notas do remapeador.",
                "Requisitos de sistema — status das especificações e como verificar seu PC.",
                "Multijogador — cooperativo online, número de jogadores e perguntas assíncronas.",
                "Lançamento para consoles — status PS5/Xbox/Switch.",
                "Mods — Oficina da Steam e perguntas sobre mods.",
                "Notas de atualização — fatos de lançamento e acompanhamento de updates.",
                "Demo vs completo — comparação verificada.",
                "Guia de construção de naves — da primeira nave às grandes construções.",
                "Fiação e eletrônica — o que é conhecido, o que não é.",
                "Guia de plantas — status das plantas e Oficina.",
                "Melhores designs — ideias e designs da comunidade.",
                "Lista de conquistas — 22 conquistas, lista não verificada.",
                "Naves / Plantas / Conquistas — páginas de índice.",
             ]},
            {"heading": "Como trabalhamos", "body": "Cada página lista 1–2 fontes confiáveis e marca tudo o que não é verificado. Não inventamos números, nomes ou mecânicas."},
        ],
    },
    "achievements": {
        "title": "Conquistas Approximately Up",
        "metaTitle": "Conquistas Approximately Up: visão geral",
        "metaDescription": "Visão geral das conquistas de Approximately Up: 22 conquistas da Steam confirmadas, lista completa em verificação e como acompanhar o progresso.",
        "intro": "O hub de conquistas de Approximately Up — número confirmado, status atual da lista e links para a página de acompanhamento completo.",
        "sections": [
            {"heading": "22 conquistas confirmadas", "body": "A página da Steam confirma 22 conquistas. A lista completa de nomes e condições não é verificada."},
            {"heading": "Conteúdo de conquistas",
             "items": [
                "Lista de conquistas — a página dedicada à lista completa (não verificada).",
                "Steam — confira a seção de conquistas da página da loja.",
             ]},
            {"heading": "Perguntas frequentes da visão geral",
             "items": [
                ["Quantas conquistas existem?", "22 (confirmado na página da Steam)."],
                ["Onde está a lista completa?", "não verificado — estamos verificando a lista oficial."],
             ]},
        ],
    },
}

TR_RU = {
    "how-to-play": {
        "title": "Как играть в Approximately Up",
        "metaTitle": "Как играть в Approximately Up: полный гайд для новичков",
        "metaDescription": "Новичок в Approximately Up? Узнайте цикл «строй-разбивай-строй заново», модульные корабли, кооперативный мультиплеер и исследование планет.",
        "intro": "Approximately Up — космическая песочница о строительстве, где вы скручиваете детали, взлетаете, разбиваетесь и строите лучше. Вот основной цикл и что знать перед первым запуском.",
        "sections": [
            {"heading": "Основной цикл: строй, разбивай, строй заново", "body": "Официальное описание сводит цикл к трём словам: строй, разбивай, строй заново. Всё остальное вытекает из этого.",
             "items": [
                ["Начните с малого", "Соберите корабль из всего, что можно скрутить достаточно надолго, чтобы взлететь. Идеальный дизайн не нужен — нужно что-то, что оторвётся от земли."],
                ["Установите двигатели и кабели", "Гигантские двигатели дают движение; кабели и всё остальное соединяют конструкцию. Сначала беспорядок — это нормально."],
                ["Пробный полёт", "Взлетите и посмотрите, что держится. Первые полёты — это эксперименты, а не отточенные пилотажи."],
                ["Разбиться (бывает)", "Крушения — часть цикла. Официальная подача считает их нормой: обломки — это урок, а не провал."],
                ["Строить умнее", "Используйте опыт, чтобы перестроить. Каждая итерация учит, какие детали держатся, а какие комбинации летают."],
             ]},
            {"heading": "Что игра официально обещает", "body": "Из официального описания в Steam:",
             "items": [
                "Исследуйте новые планеты в кооперативном мультиплеере на полностью модульном корабле.",
                "Устанавливайте гигантские двигатели, надоедливые кабели и всё остальное.",
                "Выполняйте безумные миссии и встречайте опасности космоса.",
                "Играйте в одиночку или с командой — и спорьте с командой, как сказано в официальной подаче.",
             ]},
            {"heading": "FAQ для новичков",
             "items": [
                ["Approximately Up — мультиплеерная игра?", "Да — на официальной странице Steam указаны одиночный режим и онлайн-кооператив."],
                ["Нужно ли знать инженерию?", "Нет. Игра построена на методе проб и ошибок: скручивай детали, лети, разбивайся, учись."],
                ["Есть ли демо?", "Да — на официальной странице Steam указано демо, вышедшее до полного релиза (6 августа 2026)."],
                ["Можно ли играть на Steam Deck?", "Совместимость пока не подтверждена. Игроки спрашивают об этом на форумах Steam; мы помечаем это как неподтверждённое до официального ответа."],
             ]},
            {"heading": "Что ещё нужно проверить", "body": "Конкретные названия планет и миссий, а также детальные гайды по механикам (чертежи, проводка, радар, перемотка времени) ещё не проверены по официальным источникам. Мы помечаем их как неподтверждённые и обновляем страницу по мере появления официальной информации."},
        ],
    },
    "ship-building-guide": {
        "title": "Гайд по строительству кораблей Approximately Up",
        "metaTitle": "Гайд по строительству кораблей Approximately Up: от первого корабля до больших построек",
        "metaDescription": "Научитесь строить корабли в Approximately Up: модульный цикл «строй-разбивай-строй заново», двигатели и кабели, а также запросы сообщества вроде полёта на Луну и радара.",
        "intro": "Строительство кораблей — сердце Approximately Up. Официальная подача проста: скручивай детали, пока они не полетят, затем строй умнее. Этот гайд объясняет процесс, не выдумывая неподтверждённые характеристики деталей.",
        "sections": [
            {"heading": "Постройте свой первый корабль", "body": "На основе официального описания (модульные детали, двигатели, кабели, строй-разбивай-строй заново) вот процесс:",
             "items": [
                ["Соберите детали", "Соберите доступные детали и скрутите их. Официальная подача говорит, что любая конструкция «скручивается достаточно долго, чтобы взлететь», — начните с этого."],
                ["Добавьте двигатели", "Установите двигатели для движения. Официальное описание выделяет «гигантские двигатели» как ключевую часть."],
                ["Проложите кабели", "Соедините конструкцию кабелями — «надоедливые кабели» часть опыта. Будьте готовы к неопрятной проводке."],
                ["Пробный полёт", "Взлетите. Первый корабль не обязан быть красивым; он должен показать, что держится."],
                ["Разбейтесь и повторяйте", "Перестраивайте с учётом опыта. Цикл: строй → разбивай → строй заново."],
             ]},
            {"heading": "Принципы дизайна (по официальным)",
             "items": [
                "Полностью модульный корабль: всё можно перестроить между полётами.",
                "Баланс массы и тяги — тяжёлым кораблям нужно больше тяги (точные цифры неподтверждены).",
                "Держите запасные детали: крушения предусмотрены.",
                "Планируйте кооператив: играя с командой, распределите роли (пилот, строитель, инженер).",
             ]},
            {"heading": "Туториалы, которые просит сообщество",
             "items": [
                ["Как попасть на Луну?", "Реальный тред на форуме Steam — игроки хотят гайд по полёту на Луну. Конкретные лунные механики неподтверждены."],
                ["Радар-монитор / устройство для новичков", "Реальный тред на форуме Steam — игроки хотят туториал по радар-устройству. Механики радара неподтверждены."],
             ]},
            {"heading": "Что остаётся неподтверждённым", "body": "Конкретные названия деталей, характеристики, рецепты, планеты-цели и названия миссий ещё не проверены. Этот гайд использует только официальное описание и отмеченные вопросы сообщества; мы углубим его, когда появятся проверенные данные."},
        ],
    },
    "blueprints-guide": {
        "title": "Гайд по чертежам Approximately Up",
        "metaTitle": "Чертежи Approximately Up: скачать, делиться и использовать",
        "metaDescription": "Чертежи Approximately Up: что мы знаем о поиске и использовании чертежей, поддержка Мастерской Steam и что остаётся неподтверждённым.",
        "intro": "Чертежи — одна из самых популярных тем Approximately Up. Официальные механики чертежей (импорт, экспорт, обмен) ещё не проверены, поэтому эта страница описывает, что подтверждено, а что нет.",
        "sections": [
            {"heading": "Детали чертежей: неподтверждены", "body": "Механики импорта, экспорта и обмена чертежами в нашем списке неподтверждённых — мы ещё не подтвердили их по официальному источнику. Мы расширим страницу, как только проверим надёжную информацию."},
            {"heading": "Где найти дизайны кораблей уже сейчас", "body": "Хотя официальные инструменты чертежей неподтверждены, Мастерская Steam — подтверждённое место, где живёт контент сообщества:",
             "items": [
                ["Откройте Мастерскую Steam для Approximately Up", "Контент сообщества размещается там (поддержка Мастерской подтверждена на странице магазина)."],
                ["Просматривайте корабли и постройки", "Ищите дизайны, опубликованные другими игроками."],
                ["Подпишитесь", "Подписка сохраняет контент в вашу библиотеку."],
                ["Проверьте в игре", "Посмотрите, как подписки отображаются в игре, — точные шаги неподтверждены."],
             ]},
            {"heading": "FAQ по чертежам",
             "items": [
                ["Можно ли скачивать чертежи в Approximately Up?", "Неподтверждено. Контент Мастерской — ближайший подтверждённый канал."],
                ["Можно ли делиться своими дизайнами кораблей?", "Неподтверждено. Мы подтвердим точный процесс обмена после проверки."],
                ["Чертежи — то же самое, что предметы Мастерской?", "Не обязательно — связь между чертежами в игре и предметами Мастерской неподтверждена."],
             ]},
            {"heading": "Какие источники отслеживать", "body": "Мы проверим механики чертежей по официальным каналам (анонсы Steam, официальный сайт, Discord) и обновим эту страницу. Здесь ничего не выдумано."},
        ],
    },
    "wiring-electronics": {
        "title": "Гайд по проводке и электронике Approximately Up",
        "metaTitle": "Проводка и электроника Approximately Up: что мы знаем",
        "metaDescription": "Проводка и электроника в Approximately Up: кабели в постройках, вопросы сообщества об эпохе радиоламп и Remapper — с отмеченными неподтверждёнными деталями.",
        "intro": "Проводка и электроника — большая тема сообщества, но официальной информации мало. Эта страница собирает проверенное и то, о чём спрашивают игроки, с чёткой пометкой всего неподтверждённого.",
        "sections": [
            {"heading": "Официальной информации мало", "body": "Официальное описание упоминает кабели как часть модульной постройки («надоедливые кабели и всё остальное»), но детальные механики проводки и схем ещё не проверены. Мы помечаем их как неподтверждённые."},
            {"heading": "Треды сообщества (реальные вопросы игроков)",
             "items": [
                ["Можно ли выйти за пределы эпохи радиоламп в электронике?", "Тред на форуме Steam о прогрессе/эпохе электронных деталей — намекает на раннюю электронную эпоху; точные механики неподтверждены."],
                ["Не получается задать значения в Remapper", "Тред на форуме Steam о проблемах с заданием значений в Remapper/Constant — точный процесс неподтверждён."],
             ]},
            {"heading": "Что мы можем утверждать безопасно",
             "items": [
                "Кабели официально являются частью модульного строительства кораблей.",
                "Электроника, похоже, область прогресса (сообщество упоминает раннюю «эпоху радиоламп»).",
                "В игре есть инструменты настройки параметров/значений (Remapper), но точное использование неподтверждено.",
             ]},
            {"heading": "FAQ по проводке и электронике",
             "items": [
                ["Как работает проводка в Approximately Up?", "Неподтверждено. Мы опубликуем гайд, как только появится официальная или надёжно проверенная информация."],
                ["Какие есть уровни электроники?", "Тред сообщества упоминает «эпоху радиоламп»; точные уровни и открытия неподтверждены."],
                ["Почему не получается задать значения в Remapper?", "Тред сообщества сообщает об этой проблеме; официальный процесс неподтверждён."],
             ]},
        ],
    },
    "controls": {
        "title": "Управление Approximately Up",
        "metaTitle": "Управление Approximately Up: клавиатура, мышь и статус геймпада",
        "metaDescription": "Гайд по управлению Approximately Up: что мы знаем о клавиатуре и мыши, поддержке геймпада и внутриигровом ремаппере — плюс что остаётся неподтверждённым.",
        "intro": "Поддержка геймпада — один из самых частых вопросов в сообществе Steam сразу после релиза. Вот что мы можем подтвердить, о чём спрашивают игроки и что ещё неподтверждено.",
        "sections": [
            {"heading": "Что мы знаем (подтверждено)",
             "items": [
                ["Платформа", "Игра на ПК (Steam). Клавиатура и мышь — стандартное управление."],
                ["Поддержка геймпада", "Ещё не подтверждена разработчиком. Тред на форуме Steam спрашивает «Controller Support in the Future?», что намекает: полная поддержка на запуске не подтверждена."],
                ["Внутриигровой ремаппер", "Игроки обсуждают Remapper — тред сообщества сообщает о проблемах с заданием значений. Точный процесс маппинга мы помечаем как неподтверждённый."],
             ]},
            {"heading": "Как настроить управление сейчас",
             "items": [
                "Откройте внутриигровые настройки и проверьте раздел ввода/управления для текущей раскладки.",
                "Используйте внутриигровой Remapper для переназначения клавиш; если значения не применяются, проверьте тред сообщества и заметки разработчика.",
                "Обновления поддержки геймпада смотрите в официальном Discord и анонсах Steam.",
             ]},
            {"heading": "Неподтверждено: полная раскладка клавиш", "body": "Полная официальная раскладка (движение, камера, меню строительства, управление двигателями) ещё не проверена по официальному источнику. Мы помечаем её как неподтверждённую и опубликуем таблицу после подтверждения."},
            {"heading": "FAQ по управлению",
             "items": [
                ["Поддерживает ли Approximately Up геймпады?", "Пока не подтверждено. Сообщество спрашивает; мы помечаем это как неподтверждённое, пока разработчик или официальный источник не подтвердит."],
                ["Можно ли переназначить клавиши?", "Есть внутриигровой Remapper. Некоторые игроки сообщают о проблемах со значениями; точный процесс неподтверждён."],
                ["Есть ли раскладка для Steam Deck?", "Совместимость со Steam Deck сама по себе открытый вопрос сообщества — раскладка неподтверждена."],
             ]},
        ],
    },
    "multiplayer": {
        "title": "Гайд по мультиплееру Approximately Up",
        "metaTitle": "Мультиплеер Approximately Up: кооператив, число игроков и кроссплей",
        "metaDescription": "Мультиплеер Approximately Up: онлайн-кооператив, сколько игроков, есть ли асинхронный мультиплеер и что остаётся неподтверждённым.",
        "intro": "Approximately Up официально игра с одиночным режимом и онлайн-кооперативом. Эта страница отвечает на реальные вопросы игроков о мультиплеере и помечает то, что мы пока не можем проверить.",
        "sections": [
            {"heading": "Официальный статус", "body": "Официальная страница Steam указывает «Одиночный режим» и «Онлайн-кооператив» как поддерживаемые режимы. Концепция игры строится вокруг команды, исследующей планеты вместе на модульном корабле."},
            {"heading": "FAQ по мультиплееру",
             "items": [
                ["Сколько игроков могут играть вместе?", "Точное число не подтверждено в нашей базе знаний — мы помечаем его как неподтверждённое."],
                ["Есть ли онлайн-кооператив?", "Да — онлайн-кооператив указан на официальной странице Steam."],
                ["Есть ли кроссплатформенный мультиплеер?", "Неподтверждено. Игра сейчас на ПК (Steam); консольные версии не анонсированы, поэтому кроссплей неподтверждён."],
                ["Есть ли асинхронный мультиплеер?", "Не подтверждён. Тред на форуме Steam спрашивает об «Asynchronous Multiplayer», что намекает: это ещё не официальная функция, — помечаем как неподтверждённое."],
                ["Можно ли играть одному?", "Да — одиночный режим указан как поддерживаемый."],
             ]},
            {"heading": "О чём спрашивает сообщество",
             "items": [
                "Асинхронный мультиплеер — ожидают ли игроки асинхронный режим.",
                "Число игроков / «сколько игроков» — главный поисковый запрос; мы опубликуем проверенное число, когда оно появится.",
             ]},
            {"heading": "Что остаётся неподтверждённым", "body": "Точный лимит игроков, процесс приглашений, детали хостинга и кроссплей ещё не проверены по официальным источникам. Мы обновим страницу, как только они будут подтверждены."},
        ],
    },
    "best-ship-designs": {
        "title": "Лучшие дизайны кораблей Approximately Up",
        "metaTitle": "Идеи кораблей и лучшие дизайны Approximately Up",
        "metaDescription": "Идеи дизайна кораблей Approximately Up: отправные точки для своих построек, вопросы сообщества о дизайне и где найти больше дизайнов.",
        "intro": "Ищете идеи кораблей? Эта страница собирает отправные точки на основе официальной фантазии «строй-разбивай-строй заново» и вопросы сообщества, которые формируют то, что игроки хотят строить.",
        "sections": [
            {"heading": "Отправные точки дизайна (вдохновение, не официальные характеристики)",
             "items": [
                "Скоростной корабль на двигателях: ставьте гигантские двигатели и примите, что управление придёт позже.",
                "Утилитарный грузовик: ставьте груз и детали миссий выше скорости — миссиям нужна вместимость (детали неподтверждены).",
                "Кооперативный корабль для команды: проектируйте место для команды, исследующей планеты вместе.",
                "Постройка с кабельным бардаком: примите «надоедливые кабели» — проводка часть очарования (механики проводки неподтверждены).",
             ]},
            {"heading": "Вопросы сообщества о дизайне",
             "items": [
                ["Измеритель кривизны траектории", "Тред на форуме Steam об инструменте траектории — игроки хотят лучших инструментов полёта; официальный статус неподтверждён."],
                ["моды на несколько кораблей?", "Тред на форуме Steam об управлении несколькими кораблями — неподтверждено."],
             ]},
            {"heading": "Где найти больше дизайнов",
             "items": [
                "Мастерская Steam для Approximately Up (поддержка подтверждена).",
                "Официальный канал YouTube для кораблей из трейлеров.",
                "Обсуждения сообщества Steam для скриншотов и идей игроков.",
             ]},
            {"heading": "Что остаётся неподтверждённым", "body": "Конкретные характеристики деталей, чертежи именованных дизайнов и любые списки «лучших» не подтверждены. Мы держим эту страницу как вдохновение плюс проверенные источники, а остальное помечаем как неподтверждённое."},
        ],
    },
    "system-requirements": {
        "title": "Системные требования Approximately Up",
        "metaTitle": "Системные требования Approximately Up (ПК)",
        "metaDescription": "Системные требования Approximately Up для ПК: минимальные и рекомендуемые характеристики ещё не подтверждены — вот что мы знаем и как проверить совместимость.",
        "intro": "Игроки хотят прямого ответа, потянет ли их ПК Approximately Up. Официальные минимальные и рекомендуемые характеристики ещё не подтверждены, поэтому эта страница говорит, что мы знаем, а что нет.",
        "sections": [
            {"heading": "Официальные характеристики: неподтверждены", "body": "Мы ещё не проверили официальные минимальные и рекомендуемые системные требования по официальному источнику. Вместо выдуманных цифр мы помечаем таблицу как неподтверждённую и заполним её после подтверждения (страница Steam или официальный сайт)."},
            {"heading": "Таблица характеристик (неподтверждена)",
             "columns": ["Параметр", "Минимальные", "Рекомендуемые"],
             "rows": [
                ["ОС", "неподтверждено", "неподтверждено"],
                ["Процессор", "неподтверждено", "неподтверждено"],
                ["Память", "неподтверждено", "неподтверждено"],
                ["Видеокарта", "неподтверждено", "неподтверждено"],
                ["Место на диске", "неподтверждено", "неподтверждено"],
                ["DirectX", "неподтверждено", "неподтверждено"],
             ]},
            {"heading": "Как проверить свой ПК",
             "items": [
                "Откройте Steam и проверьте страницу игры — системные требования обычно появляются там после публикации.",
                "Сравните CPU/GPU/RAM с официальными цифрами, когда мы их опубликуем.",
                "Steam Deck: совместимость — открытый вопрос сообщества («Playable on Deck?»); помечаем как неподтверждённое.",
             ]},
            {"heading": "FAQ по системным требованиям",
             "items": [
                ["Потянет ли мой ПК Approximately Up?", "Пока не можем подтвердить — официальные минимальные/рекомендуемые характеристики неподтверждены. Проверьте страницу Steam, когда разработчик их опубликует."],
                ["Есть ли Approximately Up на Steam Deck?", "Не подтверждено. Тред на форуме Steam спрашивает «Playable on Deck?» — совместимость неподтверждена до официального ответа."],
                ["Игра требовательная?", "Это космическая песочница с модульными физическими кораблями; мы сообщим проверенные цифры, как только они появятся."],
             ]},
        ],
    },
    "console-release": {
        "title": "Консольный релиз Approximately Up: статус PS5, Xbox и Switch",
        "metaTitle": "Дата консольного релиза Approximately Up (PS5, Xbox, Switch)",
        "metaDescription": "Выйдет ли Approximately Up на PS5, Xbox или Switch? Официальных анонсов пока нет — вот статус консольных версий и как следить за официальными новостями.",
        "intro": "«Дата выхода Approximately Up на PS5», «версия Xbox» и «версия Switch» — запросы, на которые не отвечает даже вики игры. Честный ответ сегодня: подтверждённых официальных анонсов консолей нет — вот страница статуса.",
        "sections": [
            {"heading": "Консольный статус (на 09.08.2026)",
             "items": [
                ["Текущие платформы", "Только ПК (Steam). Игра вышла 6 августа 2026 в Steam."],
                ["PS5", "неподтверждено — нет подтверждённого официального анонса версии для PlayStation 5."],
                ["Xbox", "неподтверждено — нет подтверждённого официального анонса версии для Xbox."],
                ["Nintendo Switch", "неподтверждено — нет подтверждённого официального анонса версии для Switch."],
                ["Официальное заявление", "Мы не подтвердили официальное заявление разработчика о консольных планах; помечаем как неподтверждённое и обновим, как только оно появится."],
             ]},
            {"heading": "Как оставаться в курсе",
             "items": [
                "Следите за официальным сайтом approximatelyup.com и официальным Discord (discord.gg/approximatelyup).",
                "Смотрите канал YouTube разработчика (@ApproximatelyUp) и TikTok (@approximatelyup) на предмет анонсов.",
                "Проверяйте страницу Steam — консольные новости обычно анонсируются там первыми.",
             ]},
            {"heading": "FAQ по консолям",
             "items": [
                ["Есть ли Approximately Up на PS5?", "Не анонсировано — помечаем как неподтверждённое. Подтверждённого официального заявления пока нет."],
                ["Есть ли на Xbox?", "Не анонсировано — неподтверждено."],
                ["Есть ли на Nintendo Switch?", "Не анонсировано — неподтверждено."],
                ["Когда консольный релиз?", "Даты пока нет. Эта страница обновится в момент подтверждения официального анонса."],
             ]},
            {"heading": "Зачем эта страница", "body": "Консольный релиз — один из самых высокоинтентных запросов по этой игре, но ни один надёжный источник на него не ответил. Эта страница даёт подтверждённый статус (только ПК) и отслеживает будущие анонсы, вместо того чтобы выдумывать дату."},
        ],
    },
    "mods": {
        "title": "Гайд по модам Approximately Up",
        "metaTitle": "Моды Approximately Up: Мастерская Steam, установка и вопросы",
        "metaDescription": "Моды Approximately Up: поддержка Мастерской Steam, как подписываться на моды и вопросы сообщества вроде нескольких кораблей.",
        "intro": "Approximately Up поддерживает Мастерскую Steam, что упрощает поиск и установку модов. Вот что подтверждено и что просят игроки.",
        "sections": [
            {"heading": "Получение модов из Мастерской Steam", "body": "Поддержка Мастерской подтверждена на официальной странице. Стандартный процесс:",
             "items": [
                ["Откройте Мастерскую", "На странице игры в Steam откройте вкладку Мастерской (или центр сообщества Мастерской)."],
                ["Просматривайте и подписывайтесь", "Найдите мод или предмет и нажмите «Подписаться» — Steam скачает его автоматически."],
                ["Запустите игру", "Откройте Approximately Up и проверьте меню модов/контента, чтобы увидеть подписки."],
                ["Включите нужное", "Включите моды, которые хотите использовать. Детали внутриигрового меню модов неподтверждены."],
             ]},
            {"heading": "О чём спрашивает сообщество",
             "items": [
                "моды на несколько кораблей? — реальный тред на форуме Steam; поддержка нескольких кораблей через моды неподтверждена.",
                "Запросы про cheat engine есть у многих игр; мы не даём читы, только проверенную информацию о модах.",
             ]},
            {"heading": "FAQ по модам",
             "items": [
                ["Поддерживает ли Approximately Up моды?", "Официально поддерживает Мастерскую Steam (согласно странице магазина). Полная документация по модам неподтверждена."],
                ["Как установить моды?", "Подпишитесь через Мастерскую Steam; установкой занимается Steam. Шаги в игре неподтверждены."],
                ["Могут ли моды дать управление несколькими кораблями?", "Тред сообщества просит об этом; подтверждённого мода пока нет — неподтверждено."],
             ]},
            {"heading": "Что остаётся неподтверждённым", "body": "Точные функции Мастерской, правила модов и влияние модов на достижения или мультиплеер ещё не проверены. Мы обновим страницу после подтверждения официальной документации."},
        ],
    },
    "patch-notes": {
        "title": "Патчноуты Approximately Up",
        "metaTitle": "Патчноуты и история обновлений Approximately Up",
        "metaDescription": "Патчноуты и история обновлений Approximately Up: информация о релизе, где публикуются официальные обновления и наш отслеживаемый чейнджлог (неподтверждённое отмечено).",
        "intro": "Approximately Up вышла 6 августа 2026. Эта страница отслеживает официальные патчноуты и обновления — всё неподтверждённое чётко помечено.",
        "sections": [
            {"heading": "Факты о релизе (подтверждено)",
             "items": [
                ["Дата релиза", "6 августа 2026 (полный релиз в Steam)."],
                ["Демо", "Демо вышло до полного релиза."],
                ["Цена", "19,99 $ на релизе (скидка 20 %; обычная цена 24,99 $)."],
             ]},
            {"heading": "Таймлайн обновлений (подтверждено через Steam)", "body": "Примечания к обновлениям подтверждены официальными объявлениями Steam (август 2026):",
             "items": [
                ["2026-08-12", "1.0.010 — Исправлены фильтр сортировки «Самые популярные» в Мастерской, загрузка страниц и пропадающие результаты; улучшена понятность поиска."],
                ["2026-08-11", "1.0.009 — Улучшен Frame Quarter With Ports (порты зеркалятся на другой стороне цепи, метки A–D согласованы); исправлена геометрия Middle Window, Small Switch и Small Button."],
                ["2026-08-10", "1.0.008 — Исправлены хитбокс Axis Rotometer и оставшиеся проблемы; Plasma Cables теперь красятся; Autohemisphere Solar Panels возвращаются на место после Fly Mode; держатели кабелей красятся."],
                ["2026-08-09", "1.0.007 — Исправлена совместимость с устройствами Metal; исправлена клавиша по умолчанию (средняя кнопка мыши для «поднять компонент»); исправлена опечатка в описании труб; добавлены подсказки."],
                ["2026-08-08", "1.0.006 — Исправлен Fuse Box, который нельзя было включить; Axis Rotometer теперь выдаёт корректные значения со знаком; исправлен предпросмотр Large Disposable Battery; добавлены титры, стартовый экран и отслеживание целей."],
             ]},
            {"heading": "Где публикуются официальные обновления",
             "items": [
                "Анонсы Steam для игры (лента новостей на странице магазина).",
                "Официальный сайт approximatelyup.com и официальный Discord.",
                "Канал YouTube разработчика для анонсов функций.",
             ]},
            {"heading": "Что остаётся неподтверждённым", "body": "Конкретное содержание патчей (баланс, исправления, новые детали) не подтверждено. Мы помечаем всё как неподтверждённое, а не гадаем."},
        ],
    },
    "demo-vs-full": {
        "title": "Демо Approximately Up vs полная версия",
        "metaTitle": "Демо Approximately Up vs полная версия: в чём разница?",
        "metaDescription": "Демо vs полная версия Approximately Up: даты релиза, цена, Мастерская и достижения — и ещё неподтверждённые различия в контенте.",
        "intro": "Демо Approximately Up вышло раньше полного релиза 6 августа 2026. Вот подтверждённое сравнение, с различиями в контенте, чётко помеченными как неподтверждённые.",
        "sections": [
            {"heading": "Подтверждённое сравнение",
             "columns": ["Аспект", "Демо", "Полная версия"],
             "rows": [
                ["Доступность", "Демо (вышло раньше, по странице магазина)", "Полный релиз 6 августа 2026"],
                ["Цена", "неподтверждено", "19,99 $ (скидка 20 %; обычная цена 24,99 $)"],
                ["Мастерская Steam", "неподтверждено", "Поддерживается (по странице магазина)"],
                ["Достижения", "неподтверждено", "22 достижения Steam (по странице магазина)"],
                ["Кооперативный мультиплеер", "неподтверждено", "Одиночный режим + онлайн-кооператив (по странице магазина)"],
             ]},
            {"heading": "FAQ: демо vs полная версия",
             "items": [
                ["Демо бесплатное?", "Мы не проверили цену/модель демо — неподтверждено."],
                ["Переносится ли прогресс из демо в полную версию?", "Неподтверждено."],
                ["Какой контент только в полной версии?", "Неподтверждено — официальные детали сравнения в работе. Полная версия добавляет поддержку Мастерской и 22 достижения по странице магазина."],
                ["Стоит ли сначала попробовать демо?", "Для большинства космических песочниц демо — хороший способ почувствовать цикл «строй-разбивай-строй заново» перед покупкой, но точные границы демо неподтверждены."],
             ]},
            {"heading": "Что остаётся неподтверждённым", "body": "Точный контент демо, перенос прогресса и различия функций не проверены по официальному источнику. Мы обновим таблицу после подтверждения."},
        ],
    },
    "achievements-list": {
        "title": "Список достижений Approximately Up",
        "metaTitle": "Достижения Approximately Up: полный список (22)",
        "metaDescription": "В Approximately Up 22 достижения Steam. Полный список названий ещё проверяется — вот что подтверждено.",
        "intro": "Официальная страница Steam подтверждает 22 достижения. Точные названия и условия открытия ещё не проверены, поэтому эта страница отслеживает подтверждённое число и помечает список как неподтверждённый.",
        "sections": [
            {"heading": "Подтверждено: 22 достижения", "body": "Страница Steam указывает 22 достижения для Approximately Up. Мы ещё не проверили название, иконку и условие каждого достижения — эта часть неподтверждена."},
            {"heading": "Список достижений (неподтверждён)",
             "columns": ["Достижение", "Условие"],
             "rows": [
                ["Достижения 1–22", "неподтверждено — названия и условия сверяются с официальным списком."],
             ]},
            {"heading": "Как отслеживать достижения",
             "items": [
                "Используйте оверлей Steam в игре, чтобы видеть прогресс.",
                "Следите за официальными анонсами Steam — списки достижений иногда выходят вместе с патчноутами.",
                "Мы опубликуем полный проверенный список здесь после подтверждения.",
             ]},
            {"heading": "FAQ по достижениям",
             "items": [
                ["Сколько достижений в Approximately Up?", "22, подтверждено на официальной странице Steam."],
                ["Какие названия достижений?", "неподтверждено — мы проверяем официальный список и опубликуем его после подтверждения."],
                ["Можно ли получить все достижения в одиночном режиме?", "Неподтверждено — некоторые могут требовать кооператив, но мы узнаем это после подтверждения списка."],
             ]},
        ],
    },
    "ships": {
        "title": "Корабли Approximately Up",
        "metaTitle": "Корабли Approximately Up: постройки, идеи и дизайны",
        "metaDescription": "Индекс контента о кораблях Approximately Up: гайд по строительству, дизайны кораблей, чертежи и основы модульного строительства.",
        "intro": "Всё о кораблях Approximately Up в одном месте — от первой постройки до идей сообщества.",
        "sections": [
            {"heading": "Гайды по кораблям",
             "items": [
                "Гайд по строительству кораблей — узнайте цикл «строй-разбивай-строй заново».",
                "Лучшие дизайны — отправные точки и идеи сообщества.",
                "Гайд по чертежам — что мы знаем о чертежах и контенте Мастерской.",
                "Моды — поддержка Мастерской и вопросы о модах.",
             ]},
            {"heading": "FAQ по кораблям",
             "items": [
                ["Какие корабли можно построить?", "Они полностью модульные — скручиваете детали, как они подходят (официальное описание). Конкретные списки деталей неподтверждены."],
                ["Можно ли долететь до Луны?", "Тред сообщества спрашивает, как; лунные механики неподтверждены."],
                ["Можно ли управлять несколькими кораблями?", "Тред сообщества спрашивает об этом; неподтверждено."],
             ]},
        ],
    },
    "blueprints": {
        "title": "Чертежи Approximately Up",
        "metaTitle": "Чертежи Approximately Up: скачивание и библиотека",
        "metaDescription": "Индекс контента о чертежах Approximately Up: как использовать чертежи, где найти дизайны кораблей и Мастерская Steam.",
        "intro": "Индекс библиотеки чертежей — находите дизайны кораблей, изучайте (неподтверждённый) процесс работы с чертежами и просматривайте Мастерскую.",
        "sections": [
            {"heading": "Контент о чертежах",
             "items": [
                "Гайд по чертежам — что подтверждено и что нет.",
                "Лучшие дизайны — идеи дизайна и где найти больше.",
                "Мастерская Steam — подтверждённый дом контента сообщества.",
             ]},
            {"heading": "FAQ индекса чертежей",
             "items": [
                ["Где скачать чертежи?", "Мастерская Steam — подтверждённый канал контента сообщества; внутриигровые механики скачивания чертежей неподтверждены."],
                ["Как импортировать чертёж?", "Неподтверждено."],
                ["Можно ли делиться своими дизайнами?", "Неподтверждено."],
             ]},
        ],
    },
    "guides": {
        "title": "Гайды Approximately Up",
        "metaTitle": "Гайды Approximately Up: все страницы",
        "metaDescription": "Все гайды Approximately Up в одном индексе: как играть, строительство кораблей, управление, мультиплеер, моды, достижения и другое.",
        "intro": "Полный индекс гайдов Approximately Up. Каждая страница отвечает на один реальный запрос игроков и помечает всё неподтверждённое.",
        "sections": [
            {"heading": "Все гайды",
             "items": [
                "Как играть — цикл «строй-разбивай-строй заново» для новичков.",
                "Управление — клавиатура/мышь, статус геймпада и заметки о ремаппере.",
                "Системные требования — статус характеристик и проверка своего ПК.",
                "Мультиплеер — онлайн-кооператив, число игроков и вопросы об async.",
                "Консольный релиз — статус PS5/Xbox/Switch.",
                "Моды — Мастерская Steam и вопросы о модах.",
                "Патчноуты — факты о релизе и отслеживание обновлений.",
                "Демо vs полная версия — подтверждённое сравнение.",
                "Гайд по строительству кораблей — от первого корабля до больших построек.",
                "Проводка и электроника — что известно, что нет.",
                "Гайд по чертежам — статус чертежей и Мастерская.",
                "Лучшие дизайны — идеи и дизайны сообщества.",
                "Список достижений — 22 достижения, список неподтверждён.",
                "Корабли / Чертежи / Достижения — индексные страницы.",
             ]},
            {"heading": "Как мы работаем", "body": "Каждая страница перечисляет 1–2 надёжных источника и помечает всё неподтверждённое. Мы не выдумываем цифры, названия и механики."},
        ],
    },
    "achievements": {
        "title": "Достижения Approximately Up",
        "metaTitle": "Достижения Approximately Up: обзор",
        "metaDescription": "Обзор достижений Approximately Up: 22 достижения Steam подтверждены, полный список проверяется, и как отслеживать прогресс.",
        "intro": "Центр достижений Approximately Up — подтверждённое число, текущий статус списка и ссылки на страницу полного отслеживания.",
        "sections": [
            {"heading": "22 достижения подтверждены", "body": "Страница Steam подтверждает 22 достижения. Полный список названий и условий неподтверждён."},
            {"heading": "Контент о достижениях",
             "items": [
                "Список достижений — отдельная страница полного (неподтверждённого) списка.",
                "Steam — проверьте раздел достижений на странице магазина.",
             ]},
            {"heading": "FAQ обзора достижений",
             "items": [
                ["Сколько достижений?", "22 (подтверждено на странице Steam)."],
                ["Где полный список?", "неподтверждено — мы проверяем официальный список."],
             ]},
        ],
    },
}

TR_UK = {
    "how-to-play": {
        "title": "Як грати в Approximately Up",
        "metaTitle": "Як грати в Approximately Up: повний гайд для новачків",
        "metaDescription": "Новачок в Approximately Up? Дізнайтеся про цикл «будуй-розбивай-будуй заново», модульні кораблі, кооперативний мультиплеєр і дослідження планет.",
        "intro": "Approximately Up — космічна пісочниця про будівництво, де ви скручуєте деталі, злітаєте, розбиваєтеся й будуєте краще. Ось основний цикл і що знати перед першим запуском.",
        "sections": [
            {"heading": "Основний цикл: будуй, розбивай, будуй заново", "body": "Офіційний опис зводить цикл до трьох слів: будуй, розбивай, будуй заново. Усе інше випливає з цього.",
             "items": [
                ["Почніть з малого", "Зберіть корабель із будь-чого, що можна скрутити достатньо довго, щоб злетіти. Ідеальний дизайн не потрібен — потрібне щось, що відірветься від землі."],
                ["Установіть двигуни й кабелі", "Гігантські двигуни дають рух; кабелі та все інше з'єднують конструкцію. Спочатку безлад — це нормально."],
                ["Пробний політ", "Злетіть і подивіться, що тримається. Перші польоти — це експерименти, а не відточені пілотажі."],
                ["Розбитися (буває)", "Крушення — частина циклу. Офіційна подача вважає їх нормою: уламки — це урок, а не провал."],
                ["Будувати розумніше", "Використайте досвід, щоб перебудувати. Кожна ітерація вчить, які деталі тримаються, а які комбінації літають."],
             ]},
            {"heading": "Що гра офіційно обіцяє", "body": "З офіційного опису в Steam:",
             "items": [
                "Досліджуйте нові планети в кооперативному мультиплеєрі на повністю модульному кораблі.",
                "Установлюйте гігантські двигуни, набридливі кабелі та все інше.",
                "Виконуйте божевільні місії та зустрічайте небезпеки космосу.",
                "Грайте наодинці або з командою — і сперечайтеся з командою, як сказано в офіційній подачі.",
             ]},
            {"heading": "FAQ для новачків",
             "items": [
                ["Approximately Up — мультиплеєрна гра?", "Так — на офіційній сторінці Steam указано одиночний режим та онлайн-кооператив."],
                ["Чи потрібно знати інженерію?", "Ні. Гра побудована на методі проб і помилок: скручуй деталі, лети, розбивайся, вчися."],
                ["Чи є демо?", "Так — на офіційній сторінці Steam указано демо, що вийшло раніше за повний реліз (6 серпня 2026)."],
                ["Чи можна грати на Steam Deck?", "Сумісність поки не підтверджена. Гравці питають про це на форумах Steam; ми позначаємо це як непідтверджене до офіційної відповіді."],
             ]},
            {"heading": "Що ще потрібно перевірити", "body": "Конкретні назви планет і місій, а також детальні гайди з механік (креслення, проводка, радар, перемотка часу) ще не перевірені за офіційними джерелами. Ми позначаємо їх як непідтверджені та оновлюємо сторінку, коли з'явиться офіційна інформація."},
        ],
    },
    "ship-building-guide": {
        "title": "Гайд з будівництва кораблів Approximately Up",
        "metaTitle": "Гайд з будівництва кораблів Approximately Up: від першого корабля до великих будов",
        "metaDescription": "Навчіться будувати кораблі в Approximately Up: модульний цикл «будуй-розбивай-будуй заново», двигуни й кабелі, а також запити спільноти на кшталт польоту на Місяць і радара.",
        "intro": "Будівництво кораблів — серце Approximately Up. Офіційна подача проста: скручуй деталі, поки вони не полетять, а потім будуй розумніше. Цей гайд пояснює процес, не вигадуючи непідтверджених характеристик деталей.",
        "sections": [
            {"heading": "Побудуйте свій перший корабель", "body": "На основі офіційного опису (модульні деталі, двигуни, кабелі, будуй-розбивай-будуй заново) ось процес:",
             "items": [
                ["Зберіть деталі", "Зберіть доступні деталі та скрутіть їх. Офіційна подача каже, що будь-яка конструкція «скручується достатньо довго, щоб злетіти», — почніть із цього."],
                ["Додайте двигуни", "Установіть двигуни для руху. Офіційний опис виділяє «гігантські двигуни» як ключову частину."],
                ["Прокладіть кабелі", "З'єднайте конструкцію кабелями — «набридливі кабелі» є частиною досвіду. Будьте готові до неохайної проводки."],
                ["Пробний політ", "Злетіть. Перший корабель не зобов'язаний бути гарним; він має показати, що тримається."],
                ["Розбийтеся й повторюйте", "Перебудовуйте з урахуванням досвіду. Цикл: будуй → розбивай → будуй заново."],
             ]},
            {"heading": "Принципи дизайну (згідно з офіційними)",
             "items": [
                "Повністю модульний корабель: усе можна перебудувати між польотами.",
                "Баланс маси та тяги — важким кораблям потрібно більше тяги (точні цифри непідтверджені).",
                "Тримайте запасні деталі: крушення передбачені.",
                "Плануйте кооператив: граючи з командою, розподіліть ролі (пілот, будівельник, інженер).",
             ]},
            {"heading": "Туторіали, які просить спільнота",
             "items": [
                ["Як потрапити на Місяць?", "Реальний тред на форумі Steam — гравці хочуть гайд про політ на Місяць. Конкретні місячні механіки непідтверджені."],
                ["Радар-монітор / пристрій для новачків", "Реальний тред на форумі Steam — гравці хочуть туторіал про радар-пристрій. Механіки радара непідтверджені."],
             ]},
            {"heading": "Що лишається непідтвердженим", "body": "Примітки до оновлень вище підтверджено офіційними оголошеннями Steam. Деталі передрелізних збірок і неанонсовані зміни залишаються непідтвердженими."}
        ],
    },
    "blueprints-guide": {
        "title": "Гайд з креслень Approximately Up",
        "metaTitle": "Креслення Approximately Up: завантажити, ділитися та використовувати",
        "metaDescription": "Креслення Approximately Up: що ми знаємо про пошук і використання креслень, підтримку Майстерні Steam і що лишається непідтвердженим.",
        "intro": "Креслення — одна з найпопулярніших тем Approximately Up. Офіційні механіки креслень (імпорт, експорт, обмін) ще не перевірені, тому ця сторінка описує, що підтверджено, а що ні.",
        "sections": [
            {"heading": "Деталі креслень: непідтверджені", "body": "Механіки імпорту, експорту та обміну кресленнями у нашому списку непідтверджених — ми ще не підтвердили їх за офіційним джерелом. Ми розширимо сторінку, щойно перевіримо надійну інформацію."},
            {"heading": "Де знайти дизайни кораблів уже зараз", "body": "Хоча офіційні інструменти креслень непідтверджені, Майстерня Steam — підтверджене місце, де живе контент спільноти:",
             "items": [
                ["Відкрийте Майстерню Steam для Approximately Up", "Контент спільноти розміщується там (підтримка Майстерні підтверджена на сторінці магазину)."],
                ["Переглядайте кораблі та будови", "Шукайте дизайни, опубліковані іншими гравцями."],
                ["Підпишіться", "Підписка зберігає контент у вашу бібліотеку."],
                ["Перевірте в грі", "Подивіться, як підписки відображаються в грі, — точні кроки непідтверджені."],
             ]},
            {"heading": "FAQ з креслень",
             "items": [
                ["Чи можна завантажувати креслення в Approximately Up?", "Непідтверджено. Контент Майстерні — найближчий підтверджений канал."],
                ["Чи можна ділитися своїми дизайнами кораблів?", "Непідтверджено. Ми підтвердимо точний процес обміну після перевірки."],
                ["Креслення — те саме, що предмети Майстерні?", "Не обов'язково — зв'язок між кресленнями в грі та предметами Майстерні непідтверджений."],
             ]},
            {"heading": "Які джерела відстежувати", "body": "Ми перевіримо механіки креслень за офіційними каналами (анонси Steam, офіційний сайт, Discord) та оновимо цю сторінку. Тут нічого не вигадано."},
        ],
    },
    "wiring-electronics": {
        "title": "Гайд з проводки та електроніки Approximately Up",
        "metaTitle": "Проводка та електроніка Approximately Up: що ми знаємо",
        "metaDescription": "Проводка та електроніка в Approximately Up: кабелі в будовах, питання спільноти про епоху радіоламп і Remapper — із позначеними непідтвердженими деталями.",
        "intro": "Проводка та електроніка — велика тема спільноти, але офіційної інформації мало. Ця сторінка збирає перевірене та те, про що питають гравці, із чіткою позначкою всього непідтвердженого.",
        "sections": [
            {"heading": "Офіційної інформації мало", "body": "Офіційний опис згадує кабелі як частину модульної будови («набридливі кабелі та все інше»), але детальні механіки проводки та схем ще не перевірені. Ми позначаємо їх як непідтверджені."},
            {"heading": "Треди спільноти (реальні питання гравців)",
             "items": [
                ["Чи можна вийти за межі епохи радіоламп в електроніці?", "Тред на форумі Steam про прогрес/епоху електронних деталей — натякає на ранню електронну епоху; точні механіки непідтверджені."],
                ["Не виходить задати значення в Remapper", "Тред на форумі Steam про проблеми із заданням значень у Remapper/Constant — точний процес непідтверджений."],
             ]},
            {"heading": "Що ми можемо стверджувати безпечно",
             "items": [
                "Кабелі офіційно є частиною модульного будівництва кораблів.",
                "Електроніка, схоже, є областю прогресу (спільнота згадує ранню «епоху радіоламп»).",
                "У грі є інструменти налаштування параметрів/значень (Remapper), але точне використання непідтверджене.",
             ]},
            {"heading": "FAQ з проводки та електроніки",
             "items": [
                ["Як працює проводка в Approximately Up?", "Непідтверджено. Ми опублікуємо гайд, щойно з'явиться офіційна або надійно перевірена інформація."],
                ["Які є рівні електроніки?", "Тред спільноти згадує «епоху радіоламп»; точні рівні та відкриття непідтверджені."],
                ["Чому не виходить задати значення в Remapper?", "Тред спільноти повідомляє про цю проблему; офіційний процес непідтверджений."],
             ]},
        ],
    },
    "controls": {
        "title": "Керування Approximately Up",
        "metaTitle": "Керування Approximately Up: клавіатура, миша та статус геймпада",
        "metaDescription": "Гайд з керування Approximately Up: що ми знаємо про клавіатуру й мишу, підтримку геймпада та внутрішньоігровий ремапер — плюс що лишається непідтвердженим.",
        "intro": "Підтримка геймпада — одне з найчастіших питань у спільноті Steam одразу після релізу. Ось що ми можемо підтвердити, про що питають гравці та що ще непідтверджено.",
        "sections": [
            {"heading": "Що ми знаємо (підтверджено)",
             "items": [
                ["Платформа", "Гра на ПК (Steam). Клавіатура та миша — стандартне керування."],
                ["Підтримка геймпада", "Ще не підтверджена розробником. Тред на форумі Steam питає «Controller Support in the Future?», що натякає: повну підтримку на запуску не підтверджено."],
                ["Внутрішньоігровий ремапер", "Гравці обговорюють Remapper — тред спільноти повідомляє про проблеми із заданням значень. Точний процес мапінгу ми позначаємо як непідтверджений."],
             ]},
            {"heading": "Як налаштувати керування зараз",
             "items": [
                "Відкрийте внутрішньоігрові налаштування та перевірте розділ вводу/керування для поточної розкладки.",
                "Використовуйте внутрішньоігровий Remapper для переназначення клавіш; якщо значення не застосовуються, перевірте тред спільноти та нотатки розробника.",
                "Оновлення підтримки геймпада дивіться в офіційному Discord та анонсах Steam.",
             ]},
            {"heading": "Непідтверджено: повна розкладка клавіш", "body": "Повна офіційна розкладка (рух, камера, меню будівництва, керування двигунами) ще не перевірена за офіційним джерелом. Ми позначаємо її як непідтверджену та опублікуємо таблицю після підтвердження."},
            {"heading": "FAQ з керування",
             "items": [
                ["Чи підтримує Approximately Up геймпади?", "Поки не підтверджено. Спільнота питає; ми позначаємо це як непідтверджене, доки розробник або офіційне джерело не підтвердить."],
                ["Чи можна переназначити клавіші?", "Є внутрішньоігровий Remapper. Деякі гравці повідомляють про проблеми зі значеннями; точний процес непідтверджений."],
                ["Чи є розкладка для Steam Deck?", "Сумісність зі Steam Deck сама по собі відкрите питання спільноти — розкладка непідтверджена."],
             ]},
        ],
    },
    "multiplayer": {
        "title": "Гайд з мультиплеєра Approximately Up",
        "metaTitle": "Мультиплеєр Approximately Up: кооператив, кількість гравців і крос-плей",
        "metaDescription": "Мультиплеєр Approximately Up: онлайн-кооператив, скільки гравців, чи є асинхронний мультиплеєр і що лишається непідтвердженим.",
        "intro": "Approximately Up офіційно гра з одиночним режимом та онлайн-кооперативом. Ця сторінка відповідає на реальні питання гравців про мультиплеєр і позначає те, що ми поки не можемо перевірити.",
        "sections": [
            {"heading": "Офіційний статус", "body": "Офіційна сторінка Steam вказує «Одиночний режим» та «Онлайн-кооператив» як підтримувані режими. Концепція гри будується навколо команди, яка досліджує планети разом на модульному кораблі."},
            {"heading": "FAQ з мультиплеєра",
             "items": [
                ["Скільки гравців можуть грати разом?", "Точне число не підтверджене в нашій базі знань — ми позначаємо його як непідтверджене."],
                ["Чи є онлайн-кооператив?", "Так — онлайн-кооператив вказаний на офіційній сторінці Steam."],
                ["Чи є крос-платформений мультиплеєр?", "Непідтверджено. Гра зараз на ПК (Steam); консольні версії не анонсовані, тому крос-плей непідтверджений."],
                ["Чи є асинхронний мультиплеєр?", "Не підтверджений. Тред на форумі Steam питає про «Asynchronous Multiplayer», що натякає: це ще не офіційна функція, — позначаємо як непідтверджене."],
                ["Чи можна грати одному?", "Так — одиночний режим вказаний як підтримуваний."],
             ]},
            {"heading": "Про що питає спільнота",
             "items": [
                "Асинхронний мультиплеєр — чи очікують гравці асинхронний режим.",
                "Кількість гравців / «скільки гравців» — головний пошуковий запит; ми опублікуємо перевірене число, коли воно з'явиться.",
             ]},
            {"heading": "Що лишається непідтвердженим", "body": "Точний ліміт гравців, процес запрошень, деталі хостингу та крос-плей ще не перевірені за офіційними джерелами. Ми оновимо сторінку, щойно вони будуть підтверджені."},
        ],
    },
    "best-ship-designs": {
        "title": "Найкращі дизайни кораблів Approximately Up",
        "metaTitle": "Ідеї кораблів і найкращі дизайни Approximately Up",
        "metaDescription": "Ідеї дизайну кораблів Approximately Up: відправні точки для власних будов, питання спільноти про дизайн і де знайти більше дизайнів.",
        "intro": "Шукаєте ідеї кораблів? Ця сторінка збирає відправні точки на основі офіційної фантазії «будуй-розбивай-будуй заново» та питання спільноти, які формують те, що гравці хочуть будувати.",
        "sections": [
            {"heading": "Відправні точки дизайну (натхнення, не офіційні характеристики)",
             "items": [
                "Швидкісний корабель на двигунах: ставте гігантські двигуни й прийміть, що керування прийде пізніше.",
                "Утилітарний вантажівка: ставте вантаж і деталі місій вище за швидкість — місіям потрібна місткість (деталі непідтверджені).",
                "Кооперативний корабель для команди: проєктуйте простір для команди, яка досліджує планети разом.",
                "Будова з кабельним безладом: прийміть «набридливі кабелі» — проводка частина чарівності (механіки проводки непідтверджені).",
             ]},
            {"heading": "Питання спільноти про дизайн",
             "items": [
                ["Вимірювач кривизни траєкторії", "Тред на форумі Steam про інструмент траєкторії — гравці хочуть кращих інструментів польоту; офіційний статус непідтверджений."],
                ["моди на кілька кораблів?", "Тред на форумі Steam про керування кількома кораблями — непідтверджено."],
             ]},
            {"heading": "Де знайти більше дизайнів",
             "items": [
                "Майстерня Steam для Approximately Up (підтримка підтверджена).",
                "Офіційний канал YouTube для кораблів із трейлерів.",
                "Обговорення спільноти Steam для скріншотів та ідей гравців.",
             ]},
            {"heading": "Що лишається непідтвердженим", "body": "Конкретні характеристики деталей, креслення іменованих дизайнів та будь-які списки «найкращих» не підтверджені. Ми тримаємо цю сторінку як натхнення плюс перевірені джерела, а решту позначаємо як непідтверджене."},
        ],
    },
    "system-requirements": {
        "title": "Системні вимоги Approximately Up",
        "metaTitle": "Системні вимоги Approximately Up (ПК)",
        "metaDescription": "Системні вимоги Approximately Up для ПК: мінімальні та рекомендовані характеристики ще не підтверджені — ось що ми знаємо і як перевірити сумісність.",
        "intro": "Гравці хочуть прямої відповіді, чи потягне їхній ПК Approximately Up. Офіційні мінімальні та рекомендовані характеристики ще не підтверджені, тому ця сторінка розповідає, що ми знаємо, а що ні.",
        "sections": [
            {"heading": "Офіційні характеристики: непідтверджені", "body": "Ми ще не перевірили офіційні мінімальні та рекомендовані системні вимоги за офіційним джерелом. Замість вигаданих цифр ми позначаємо таблицю як непідтверджену та заповнимо її після підтвердження (сторінка Steam або офіційний сайт)."},
            {"heading": "Таблиця характеристик (непідтверджена)",
             "columns": ["Параметр", "Мінімальні", "Рекомендовані"],
             "rows": [
                ["ОС", "непідтверджено", "непідтверджено"],
                ["Процесор", "непідтверджено", "непідтверджено"],
                ["Пам'ять", "непідтверджено", "непідтверджено"],
                ["Відеокарта", "непідтверджено", "непідтверджено"],
                ["Місце на диску", "непідтверджено", "непідтверджено"],
                ["DirectX", "непідтверджено", "непідтверджено"],
             ]},
            {"heading": "Як перевірити свій ПК",
             "items": [
                "Відкрийте Steam і перевірте сторінку гри — системні вимоги зазвичай з'являються там після публікації.",
                "Порівняйте CPU/GPU/RAM з офіційними цифрами, коли ми їх опублікуємо.",
                "Steam Deck: сумісність — відкрите питання спільноти («Playable on Deck?»); позначаємо як непідтверджене.",
             ]},
            {"heading": "FAQ з системних вимог",
             "items": [
                ["Чи потягне мій ПК Approximately Up?", "Поки не можемо підтвердити — офіційні мінімальні/рекомендовані характеристики непідтверджені. Перевірте сторінку Steam, коли розробник їх опублікує."],
                ["Чи є Approximately Up на Steam Deck?", "Не підтверджено. Тред на форумі Steam питає «Playable on Deck?» — сумісність непідтверджена до офіційної відповіді."],
                ["Гра вимоглива?", "Це космічна пісочниця з модульними фізичними кораблями; ми повідомимо перевірені цифри, щойно вони з'являться."],
             ]},
        ],
    },
    "console-release": {
        "title": "Консольний реліз Approximately Up: статус PS5, Xbox і Switch",
        "metaTitle": "Дата консольного релізу Approximately Up (PS5, Xbox, Switch)",
        "metaDescription": "Чи вийде Approximately Up на PS5, Xbox або Switch? Офіційних анонсів поки немає — ось статус консольних версій і як стежити за офіційними новинами.",
        "intro": "«Дата виходу Approximately Up на PS5», «версія Xbox» і «версія Switch» — запити, на які не відповідає навіть вікі гри. Чесна відповідь сьогодні: підтверджених офіційних анонсів консолей немає — ось сторінка статусу.",
        "sections": [
            {"heading": "Консольний статус (на 09.08.2026)",
             "items": [
                ["Поточні платформи", "Тільки ПК (Steam). Гра вийшла 6 серпня 2026 у Steam."],
                ["PS5", "непідтверджено — немає підтвердженого офіційного анонсу версії для PlayStation 5."],
                ["Xbox", "непідтверджено — немає підтвердженого офіційного анонсу версії для Xbox."],
                ["Nintendo Switch", "непідтверджено — немає підтвердженого офіційного анонсу версії для Switch."],
                ["Офіційна заява", "Ми не підтвердили офіційну заяву розробника про консольні плани; позначаємо як непідтверджене та оновимо, щойно вона з'явиться."],
             ]},
            {"heading": "Як бути в курсі",
             "items": [
                "Слідкуйте за офіційним сайтом approximatelyup.com та офіційним Discord (discord.gg/approximatelyup).",
                "Дивіться канал YouTube розробника (@ApproximatelyUp) і TikTok (@approximatelyup) на предмет анонсів.",
                "Перевіряйте сторінку Steam — консольні новини зазвичай анонсуються там першими.",
             ]},
            {"heading": "FAQ з консолей",
             "items": [
                ["Чи є Approximately Up на PS5?", "Не анонсовано — позначаємо як непідтверджене. Підтвердженої офіційної заяви поки немає."],
                ["Чи є на Xbox?", "Не анонсовано — непідтверджено."],
                ["Чи є на Nintendo Switch?", "Не анонсовано — непідтверджено."],
                ["Коли консольний реліз?", "Дата поки відсутня. Ця сторінка оновиться в момент підтвердження офіційного анонсу."],
             ]},
            {"heading": "Навіщо ця сторінка", "body": "Консольний реліз — один із найвисокоінтентніших запитів по цій грі, але жодне надійне джерело на нього не відповіло. Ця сторінка дає підтверджений статус (тільки ПК) і відстежує майбутні анонси, а не вигадує дату."},
        ],
    },
    "mods": {
        "title": "Гайд з модів Approximately Up",
        "metaTitle": "Моди Approximately Up: Майстерня Steam, установка та питання",
        "metaDescription": "Моди Approximately Up: підтримка Майстерні Steam, як підписуватися на моди та питання спільноти на кшталт кількох кораблів.",
        "intro": "Approximately Up підтримує Майстерню Steam, що спрощує пошук та встановлення модів. Ось що підтверджено та що просять гравці.",
        "sections": [
            {"heading": "Отримання модів із Майстерні Steam", "body": "Підтримка Майстерні підтверджена на офіційній сторінці. Стандартний процес:",
             "items": [
                ["Відкрийте Майстерню", "На сторінці гри в Steam відкрийте вкладку Майстерні (або центр спільноти Майстерні)."],
                ["Переглядайте та підписуйтеся", "Знайдіть мод або предмет і натисніть «Підписатися» — Steam завантажить його автоматично."],
                ["Запустіть гру", "Відкрийте Approximately Up і перевірте меню модів/контенту, щоб побачити підписки."],
                ["Увімкніть потрібне", "Увімкніть моди, які хочете використовувати. Деталі внутрішньоігрового меню модів непідтверджені."],
             ]},
            {"heading": "Про що питає спільнота",
             "items": [
                "моди на кілька кораблів? — реальний тред на форумі Steam; підтримка кількох кораблів через моди непідтверджена.",
                "Запити про cheat engine є в багатьох ігор; ми не даємо читів, лише перевірену інформацію про моди.",
             ]},
            {"heading": "FAQ з модів",
             "items": [
                ["Чи підтримує Approximately Up моди?", "Офіційно підтримує Майстерню Steam (згідно зі сторінкою магазину). Повна документація з модів непідтверджена."],
                ["Як встановити моди?", "Підпишіться через Майстерню Steam; установкою займається Steam. Кроки в грі непідтверджені."],
                ["Чи можуть моди дати керування кількома кораблями?", "Тред спільноти про це просить; підтвердженого мода поки немає — непідтверджено."],
             ]},
            {"heading": "Що лишається непідтвердженим", "body": "Точні функції Майстерні, правила модів і вплив модів на досягнення чи мультиплеєр ще не перевірені. Ми оновимо сторінку після підтвердження офіційної документації."},
        ],
    },
    "patch-notes": {
        "title": "Патчноути Approximately Up",
        "metaTitle": "Патчноути та історія оновлень Approximately Up",
        "metaDescription": "Патчноути та історія оновлень Approximately Up: інформація про реліз, де публікуються офіційні оновлення та наш відстежуваний чейнджлог (непідтверджене позначено).",
        "intro": "Approximately Up вийшла 6 серпня 2026. Ця сторінка відстежує офіційні патчноути та оновлення — усе непідтверджене чітко позначено.",
        "sections": [
            {"heading": "Факти про реліз (підтверджено)",
             "items": [
                ["Дата релізу", "6 серпня 2026 (повний реліз у Steam)."],
                ["Демо", "Демо вийшло раніше за повний реліз."],
                ["Ціна", "19,99 $ на релізі (знижка 20 %; звичайна ціна 24,99 $)."],
             ]},
            {"heading": "Таймлайн оновлень (підтверджено через Steam)", "body": "Примітки до оновлень підтверджено офіційними оголошеннями Steam (серпень 2026):",
             "items": [
                ["2026-08-12", "1.0.010 — Виправлено фільтр сортування «Найпопулярніші» в майстерні, завантаження сторінок і зниклі результати; покращено зрозумілість пошуку."],
                ["2026-08-11", "1.0.009 — Покращено Frame Quarter With Ports (порти дзеркаляться на іншому боці ланцюга, мітки A–D узгоджені); виправлено геометрію Middle Window, Small Switch і Small Button."],
                ["2026-08-10", "1.0.008 — Виправлено хітбокс Axis Rotometer та решту проблем; Plasma Cables тепер можна фарбувати; Autohemisphere Solar Panels повертаються після Fly Mode; тримачі кабелів можна фарбувати."],
                ["2026-08-09", "1.0.007 — Виправлено сумісність із пристроями Metal; виправлено клавішу за замовчуванням (середня кнопка миші для «підняти компонент»); виправлено друкарську помилку в описах труб; додано підказки."],
                ["2026-08-08", "1.0.006 — Виправлено Fuse Box, який не вмикався; Axis Rotometer тепер коректно видає знакові значення; виправлено попередній перегляд Large Disposable Battery; додано титри, стартовий екран і відстеження цілей."],
             ]},
            {"heading": "Де публікуються офіційні оновлення",
             "items": [
                "Анонси Steam для гри (стрічка новин на сторінці магазину).",
                "Офіційний сайт approximatelyup.com та офіційний Discord.",
                "Канал YouTube розробника для анонсів функцій.",
             ]},
            {"heading": "Що лишається непідтвердженим", "body": "Конкретний зміст патчів (баланс, виправлення, нові деталі) не підтверджений. Ми позначаємо все як непідтверджене, а не вгадуємо."},
        ],
    },
    "demo-vs-full": {
        "title": "Демо Approximately Up vs повна версія",
        "metaTitle": "Демо Approximately Up vs повна версія: у чому різниця?",
        "metaDescription": "Демо vs повна версія Approximately Up: дати релізу, ціна, Майстерня та досягнення — і ще непідтверджені відмінності в контенті.",
        "intro": "Демо Approximately Up вийшло раніше за повний реліз 6 серпня 2026. Ось підтверджене порівняння, з відмінностями в контенті, чітко позначеними як непідтверджені.",
        "sections": [
            {"heading": "Підтверджене порівняння",
             "columns": ["Аспект", "Демо", "Повна версія"],
             "rows": [
                ["Доступність", "Демо (вийшло раніше, згідно зі сторінкою магазину)", "Повний реліз 6 серпня 2026"],
                ["Ціна", "непідтверджено", "19,99 $ (знижка 20 %; звичайна ціна 24,99 $)"],
                ["Майстерня Steam", "непідтверджено", "Підтримується (згідно зі сторінкою магазину)"],
                ["Досягнення", "непідтверджено", "22 досягнення Steam (згідно зі сторінкою магазину)"],
                ["Кооперативний мультиплеєр", "непідтверджено", "Одиночний режим + онлайн-кооператив (згідно зі сторінкою магазину)"],
             ]},
            {"heading": "FAQ: демо vs повна версія",
             "items": [
                ["Чи безкоштовне демо?", "Ми не перевірили ціну/модель демо — непідтверджено."],
                ["Чи переноситься прогрес із демо в повну версію?", "Непідтверджено."],
                ["Який контент лише в повній версії?", "Непідтверджено — офіційні деталі порівняння в роботі. Повна версія додає підтримку Майстерні та 22 досягнення згідно зі сторінкою магазину."],
                ["Чи варто спершу спробувати демо?", "Для більшості космічних пісочниць демо — гарний спосіб відчути цикл «будуй-розбивай-будуй заново» перед покупкою, але точні межі демо непідтверджені."],
             ]},
            {"heading": "Що лишається непідтвердженим", "body": "Точний контент демо, перенесення прогресу та відмінності функцій не перевірені за офіційним джерелом. Ми оновимо таблицю після підтвердження."},
        ],
    },
    "achievements-list": {
        "title": "Список досягнень Approximately Up",
        "metaTitle": "Досягнення Approximately Up: повний список (22)",
        "metaDescription": "В Approximately Up 22 досягнення Steam. Повний список назв ще перевіряється — ось що підтверджено.",
        "intro": "Офіційна сторінка Steam підтверджує 22 досягнення. Точні назви та умови відкриття ще не перевірені, тому ця сторінка відстежує підтверджене число та позначає список як непідтверджений.",
        "sections": [
            {"heading": "Підтверджено: 22 досягнення", "body": "Сторінка Steam вказує 22 досягнення для Approximately Up. Ми ще не перевірили назву, іконку та умову кожного досягнення — ця частина непідтверджена."},
            {"heading": "Список досягнень (непідтверджений)",
             "columns": ["Досягнення", "Умова"],
             "rows": [
                ["Досягнення 1–22", "непідтверджено — назви та умови звіряються з офіційним списком."],
             ]},
            {"heading": "Як відстежувати досягнення",
             "items": [
                "Використовуйте оверлей Steam у грі, щоб бачити прогрес.",
                "Слідкуйте за офіційними анонсами Steam — списки досягнень іноді виходять разом із патчноутами.",
                "Ми опублікуємо повний перевірений список тут після підтвердження.",
             ]},
            {"heading": "FAQ з досягнень",
             "items": [
                ["Скільки досягнень в Approximately Up?", "22, підтверджено на офіційній сторінці Steam."],
                ["Які назви досягнень?", "непідтверджено — ми перевіряємо офіційний список та опублікуємо його після підтвердження."],
                ["Чи можна отримати всі досягнення в одиночному режимі?", "Непідтверджено — деякі можуть вимагати кооператив, але ми дізнаємося це після підтвердження списку."],
             ]},
        ],
    },
    "ships": {
        "title": "Кораблі Approximately Up",
        "metaTitle": "Кораблі Approximately Up: будови, ідеї та дизайни",
        "metaDescription": "Індекс контенту про кораблі Approximately Up: гайд з будівництва, дизайни кораблів, креслення та основи модульного будівництва.",
        "intro": "Усе про кораблі Approximately Up в одному місці — від першої будови до ідей спільноти.",
        "sections": [
            {"heading": "Гайди з кораблів",
             "items": [
                "Гайд з будівництва кораблів — дізнайтеся цикл «будуй-розбивай-будуй заново».",
                "Найкращі дизайни — відправні точки та ідеї спільноти.",
                "Гайд з креслень — що ми знаємо про креслення та контент Майстерні.",
                "Моди — підтримка Майстерні та питання про моди.",
             ]},
            {"heading": "FAQ з кораблів",
             "items": [
                ["Які кораблі можна побудувати?", "Вони повністю модульні — скручуєте деталі, як вони підходять (офіційний опис). Конкретні списки деталей непідтверджені."],
                ["Чи можна долетіти до Місяця?", "Тред спільноти питає, як; місячні механіки непідтверджені."],
                ["Чи можна керувати кількома кораблями?", "Тред спільноти питає про це; непідтверджено."],
             ]},
        ],
    },
    "blueprints": {
        "title": "Креслення Approximately Up",
        "metaTitle": "Креслення Approximately Up: завантаження та бібліотека",
        "metaDescription": "Індекс контенту про креслення Approximately Up: як використовувати креслення, де знайти дизайни кораблів та Майстерня Steam.",
        "intro": "Індекс бібліотеки креслень — знаходьте дизайни кораблів, вивчайте (непідтверджений) процес роботи з кресленнями та переглядайте Майстерню.",
        "sections": [
            {"heading": "Контент про креслення",
             "items": [
                "Гайд з креслень — що підтверджено, а що ні.",
                "Найкращі дизайни — ідеї дизайну та де знайти більше.",
                "Майстерня Steam — підтверджений дім контенту спільноти.",
             ]},
            {"heading": "FAQ індексу креслень",
             "items": [
                ["Де завантажити креслення?", "Майстерня Steam — підтверджений канал контенту спільноти; внутрішньоігрові механіки завантаження креслень непідтверджені."],
                ["Як імпортувати креслення?", "Непідтверджено."],
                ["Чи можна ділитися своїми дизайнами?", "Непідтверджено."],
             ]},
        ],
    },
    "guides": {
        "title": "Гайди Approximately Up",
        "metaTitle": "Гайди Approximately Up: усі сторінки",
        "metaDescription": "Усі гайди Approximately Up в одному індексі: як грати, будівництво кораблів, керування, мультиплеєр, моди, досягнення та інше.",
        "intro": "Повний індекс гайдів Approximately Up. Кожна сторінка відповідає на один реальний запит гравців і позначає все непідтверджене.",
        "sections": [
            {"heading": "Усі гайди",
             "items": [
                "Як грати — цикл «будуй-розбивай-будуй заново» для новачків.",
                "Керування — клавіатура/миша, статус геймпада та нотатки про ремапер.",
                "Системні вимоги — статус характеристик і перевірка свого ПК.",
                "Мультиплеєр — онлайн-кооператив, кількість гравців і питання про async.",
                "Консольний реліз — статус PS5/Xbox/Switch.",
                "Моди — Майстерня Steam і питання про моди.",
                "Патчноути — факти про реліз і відстеження оновлень.",
                "Демо vs повна версія — підтверджене порівняння.",
                "Гайд з будівництва кораблів — від першого корабля до великих будов.",
                "Проводка та електроніка — що відомо, що ні.",
                "Гайд з креслень — статус креслень і Майстерня.",
                "Найкращі дизайни — ідеї та дизайни спільноти.",
                "Список досягнень — 22 досягнення, список непідтверджений.",
                "Кораблі / Креслення / Досягнення — індексні сторінки.",
             ]},
            {"heading": "Як ми працюємо", "body": "Кожна сторінка перелічує 1–2 надійні джерела та позначає все непідтверджене. Ми не вигадуємо цифри, назви та механіки."},
        ],
    },
    "achievements": {
        "title": "Досягнення Approximately Up",
        "metaTitle": "Досягнення Approximately Up: огляд",
        "metaDescription": "Огляд досягнень Approximately Up: 22 досягнення Steam підтверджені, повний список перевіряється та як відстежувати прогрес.",
        "intro": "Центр досягнень Approximately Up — підтверджене число, поточний статус списку та посилання на сторінку повного відстеження.",
        "sections": [
            {"heading": "22 досягнення підтверджені", "body": "Сторінка Steam підтверджує 22 досягнення. Повний список назв та умов непідтверджений."},
            {"heading": "Контент про досягнення",
             "items": [
                "Список досягнень — окрема сторінка повного (непідтвердженого) списку.",
                "Steam — перевірте розділ досягнень на сторінці магазину.",
             ]},
            {"heading": "FAQ огляду досягнень",
             "items": [
                ["Скільки досягнень?", "22 (підтверджено на сторінці Steam)."],
                ["Де повний список?", "непідтверджено — ми перевіряємо офіційний список."],
             ]},
        ],
    },
}

TR_VI = {
    "how-to-play": {
        "title": "Cách chơi Approximately Up",
        "metaTitle": "Cách chơi Approximately Up: hướng dẫn đầy đủ cho người mới",
        "metaDescription": "Mới chơi Approximately Up? Tìm hiểu vòng lặp xây-rơi-xây lại, tàu mô-đun, chơi mạng hợp tác và khám phá hành tinh trong hướng dẫn này.",
        "intro": "Approximately Up là trò chơi xây dựng hộp cát không gian, nơi bạn bắt vít các bộ phận, cất cánh, rơi xuống và xây lại tốt hơn. Đây là vòng lặp chính và những điều cần biết trước lần phóng đầu tiên.",
        "sections": [
            {"heading": "Vòng lặp chính: xây, rơi, xây lại", "body": "Mô tả chính thức tóm tắt vòng lặp bằng ba từ: xây, rơi, xây lại. Mọi thứ khác đều từ đó mà ra.",
             "items": [
                ["Bắt đầu nhỏ", "Lắp một con tàu từ bất cứ thứ gì bắt vít đủ lâu để bay. Bạn không cần thiết kế hoàn hảo để bắt đầu — chỉ cần thứ gì đó cất cánh được."],
                ["Gắn động cơ đẩy và dây cáp", "Động cơ đẩy khổng lồ giúp di chuyển; dây cáp và mọi thứ khác kết nối phần xây dựng của bạn. Ban đầu sẽ bừa bộn, điều đó bình thường."],
                ["Bay thử", "Cất cánh và xem thứ gì giữ được. Những chuyến bay đầu là thử nghiệm, không phải chuyến bay hoàn hảo."],
                ["Rơi (chuyện thường)", "Rơi là một phần của vòng lặp. Bài giới thiệu chính thức xem đó là điều bình thường — mảnh vỡ là bài học, không phải thất bại."],
                ["Xây lại thông minh hơn", "Dùng những gì đã học để xây lại. Mỗi lần lặp dạy bạn bộ phận nào giữ được và tổ hợp nào bay được."],
             ]},
            {"heading": "Những gì trò chơi chính thức hứa hẹn", "body": "Từ mô tả chính thức trên Steam:",
             "items": [
                "Khám phá hành tinh mới trong chế độ chơi mạng hợp tác với con tàu hoàn toàn mô-đun của bạn.",
                "Gắn động cơ đẩy khổng lồ, dây cáp phiền phức và mọi thứ khác.",
                "Hoàn thành các nhiệm vụ điên rồ và đối mặt với hiểm nguy ngoài không gian.",
                "Chơi một mình hoặc với một phi hành đoàn — và tranh cãi với phi hành đoàn, như bài giới thiệu chính thức nói.",
             ]},
            {"heading": "Câu hỏi thường gặp cho người mới",
             "items": [
                ["Approximately Up có chơi mạng không?", "Có — trang Steam chính thức ghi chế độ chơi đơn và chơi mạng hợp tác trực tuyến."],
                ["Tôi có cần biết kỹ thuật không?", "Không. Trò chơi dựa trên thử và sai: bắt vít bộ phận, bay, rơi, học hỏi."],
                ["Có bản demo không?", "Có — trang Steam chính thức ghi bản demo ra mắt trước bản đầy đủ (6 tháng 8 năm 2026)."],
                ["Tôi có thể chơi trên Steam Deck không?", "Khả năng tương thích chưa được xác nhận. Người chơi đang hỏi trên diễn đàn Steam; chúng tôi đánh dấu điều này là chưa xác minh cho đến khi có câu trả lời chính thức."],
             ]},
            {"heading": "Những gì chúng tôi còn cần xác minh", "body": "Tên cụ thể của hành tinh và nhiệm vụ, cùng các hướng dẫn cơ chế chi tiết (bản thiết kế, dây điện, radar, tua ngược thời gian) chưa được xác minh từ nguồn chính thức. Chúng tôi đánh dấu là chưa xác minh và cập nhật trang này khi có thông tin chính thức."},
        ],
    },
    "ship-building-guide": {
        "title": "Hướng dẫn chế tạo tàu Approximately Up",
        "metaTitle": "Hướng dẫn chế tạo tàu Approximately Up: từ con tàu đầu tiên đến công trình lớn",
        "metaDescription": "Học cách chế tạo tàu trong Approximately Up: quy trình mô-đun xây-rơi-xây lại, động cơ đẩy và dây cáp, cùng nhu cầu cộng đồng như lên Mặt Trăng và radar.",
        "intro": "Chế tạo tàu là trái tim của Approximately Up. Bài giới thiệu chính thức đơn giản: bắt vít các bộ phận cho đến khi bay được, rồi xây lại thông minh hơn. Hướng dẫn này trình bày quy trình mà không bịa ra các chỉ số chưa xác minh.",
        "sections": [
            {"heading": "Chế tạo con tàu đầu tiên của bạn", "body": "Dựa trên mô tả chính thức (bộ phận mô-đun, động cơ đẩy, dây cáp, xây-rơi-xây lại), đây là quy trình:",
             "items": [
                ["Thu thập bộ phận", "Gom các bộ phận có sẵn và bắt vít chúng lại. Bài giới thiệu chính thức nói bất kỳ công trình nào 'bắt vít đủ lâu để bay' — hãy bắt đầu từ đó."],
                ["Thêm động cơ đẩy", "Gắn động cơ đẩy để di chuyển. Mô tả chính thức nhấn mạnh 'động cơ đẩy khổng lồ' là phần cốt lõi."],
                ["Chạy dây cáp", "Kết nối công trình bằng dây cáp — 'dây cáp phiền phức' là một phần của trải nghiệm. Hãy chấp nhận hệ thống dây lộn xộn."],
                ["Bay thử", "Cất cánh. Con tàu đầu tiên không cần đẹp; nó chỉ cần dạy bạn thứ gì giữ được."],
                ["Rơi và lặp lại", "Xây lại bằng những gì đã học. Vòng lặp là xây → rơi → xây lại."],
             ]},
            {"heading": "Nguyên tắc thiết kế (theo hướng chính thức)",
             "items": [
                "Tàu hoàn toàn mô-đun: mọi thứ có thể sắp xếp lại giữa các chuyến bay.",
                "Cân bằng trọng lượng và lực đẩy — tàu nặng hơn cần lực đẩy lớn hơn (số liệu cụ thể chưa xác minh).",
                "Giữ phụ tùng dự phòng: rơi là chuyện dự kiến.",
                "Lên kế hoạch cho chế độ hợp tác: nếu chơi với phi hành đoàn, hãy phân vai (phi công, thợ xây, kỹ sư).",
             ]},
            {"heading": "Hướng dẫn cộng đồng đang yêu cầu",
             "items": [
                ["Làm sao lên Mặt Trăng?", "Một chủ đề thật trên diễn đàn Steam — người chơi muốn hướng dẫn lên Mặt Trăng. Cơ chế Mặt Trăng cụ thể chưa xác minh."],
                ["Màn hình / thiết bị radar cho người mới", "Một chủ đề thật trên diễn đàn Steam — người chơi muốn hướng dẫn thiết bị radar. Cơ chế radar chưa xác minh."],
             ]},
            {"heading": "Điều vẫn chưa xác minh", "body": "Ghi chú bản vá ở trên được xác minh từ thông báo chính thức của Steam. Chi tiết bản dựng trước phát hành và thay đổi chưa công bố vẫn chưa được xác minh."}
        ],
    },
    "blueprints-guide": {
        "title": "Hướng dẫn bản thiết kế Approximately Up",
        "metaTitle": "Bản thiết kế Approximately Up: tải xuống, chia sẻ và sử dụng",
        "metaDescription": "Bản thiết kế Approximately Up: điều chúng tôi biết về việc tìm và dùng bản thiết kế, hỗ trợ Steam Workshop và điều vẫn chưa xác minh.",
        "intro": "Bản thiết kế là một trong những chủ đề được tìm kiếm nhiều nhất về Approximately Up. Cơ chế chính thức (nhập, xuất, chia sẻ) chưa được xác minh, nên trang này đề cập những gì đã xác nhận và những gì chưa.",
        "sections": [
            {"heading": "Chi tiết bản thiết kế: chưa xác minh", "body": "Cơ chế nhập, xuất và chia sẻ bản thiết kế nằm trong danh sách chưa xác minh của chúng tôi — chúng tôi chưa xác nhận chúng từ nguồn chính thức. Trang này sẽ được mở rộng ngay khi có thông tin đáng tin cậy."},
            {"heading": "Tìm thiết kế tàu ngay hôm nay", "body": "Trong khi công cụ bản thiết kế chính thức chưa xác minh, Steam Workshop là nơi đã xác nhận chứa nội dung cộng đồng:",
             "items": [
                ["Mở Steam Workshop của Approximately Up", "Nội dung do cộng đồng tải lên được lưu ở đó (hỗ trợ Workshop đã xác nhận trên trang cửa hàng)."],
                ["Xem qua tàu và công trình", "Tìm các thiết kế do người chơi khác chia sẻ."],
                ["Đăng ký", "Đăng ký để lưu nội dung vào thư viện của bạn."],
                ["Kiểm tra trong trò chơi", "Xem các mục đã đăng ký hiển thị thế nào trong trò chơi — các bước chính xác chưa xác minh."],
             ]},
            {"heading": "Câu hỏi thường gặp về bản thiết kế",
             "items": [
                ["Tôi có thể tải bản thiết kế trong Approximately Up không?", "Chưa xác minh. Nội dung Workshop là kênh đã xác nhận gần nhất hiện nay."],
                ["Tôi có thể chia sẻ thiết kế tàu của mình không?", "Chưa xác minh. Chúng tôi sẽ xác nhận quy trình chia sẻ chính xác khi được xác minh."],
                ["Bản thiết kế có giống mục Workshop không?", "Không hẳn — mối quan hệ giữa bản thiết kế trong trò chơi và mục Workshop chưa xác minh."],
             ]},
            {"heading": "Nguồn cần theo dõi", "body": "Chúng tôi sẽ xác minh cơ chế bản thiết kế qua các kênh chính thức (thông báo Steam, trang web chính thức, Discord) và cập nhật trang này. Không có gì ở đây bịa ra cơ chế."},
        ],
    },
    "wiring-electronics": {
        "title": "Hướng dẫn dây điện và linh kiện Approximately Up",
        "metaTitle": "Dây điện và linh kiện Approximately Up: những gì chúng tôi biết",
        "metaDescription": "Dây điện và linh kiện trong Approximately Up: dây cáp trong công trình, câu hỏi cộng đồng về thời đại đèn chân không và Remapper — với chi tiết chưa xác minh được đánh dấu.",
        "intro": "Dây điện và linh kiện là chủ đề lớn của cộng đồng — nhưng thông tin chính thức rất ít. Trang này tổng hợp điều đã xác minh và điều người chơi hỏi, với mọi thứ chưa xác minh được đánh dấu rõ ràng.",
        "sections": [
            {"heading": "Thông tin chính thức còn hạn chế", "body": "Mô tả chính thức nhắc đến dây cáp như một phần của công trình mô-đun ('dây cáp phiền phức, và mọi thứ khác'), nhưng cơ chế chi tiết của dây điện và mạch điện chưa được xác minh. Chúng tôi đánh dấu là chưa xác minh."},
            {"heading": "Chủ đề cộng đồng (câu hỏi thật của người chơi)",
             "items": [
                ["Chúng ta có thể vượt qua thời đại đèn chân không của linh kiện không?", "Chủ đề trên diễn đàn Steam hỏi về giai đoạn/thời đại của bộ phận linh kiện — gợi ý chủ đề linh kiện thời kỳ đầu; cơ chế chính xác chưa xác minh."],
                ["Không đặt được giá trị trong Remapper", "Chủ đề trên diễn đàn Steam phản ánh vấn đề đặt giá trị trong Remapper/Constant — quy trình chính xác chưa xác minh."],
             ]},
            {"heading": "Điều chúng tôi có thể nói an toàn",
             "items": [
                "Dây cáp là phần chính thức của trải nghiệm chế tạo tàu mô-đun.",
                "Linh kiện có vẻ là hướng phát triển (cộng đồng nhắc đến 'thời đại đèn chân không' ban đầu).",
                "Trong trò chơi có công cụ đặt thông số/giá trị (Remapper), nhưng cách dùng chính xác chưa xác minh.",
             ]},
            {"heading": "Câu hỏi thường gặp về dây điện và linh kiện",
             "items": [
                ["Dây điện hoạt động thế nào trong Approximately Up?", "Chưa xác minh. Chúng tôi sẽ xuất bản hướng dẫn khi có thông tin chính thức hoặc được đối chiếu đáng tin cậy."],
                ["Các cấp linh kiện là gì?", "Chủ đề cộng đồng nhắc đến 'thời đại đèn chân không'; các cấp và mở khóa chính xác chưa xác minh."],
                ["Vì sao tôi không đặt được giá trị trong Remapper?", "Chủ đề cộng đồng phản ánh vấn đề này; quy trình chính thức chưa xác minh."],
             ]},
        ],
    },
    "controls": {
        "title": "Điều khiển Approximately Up",
        "metaTitle": "Điều khiển Approximately Up: bàn phím, chuột và trạng thái tay cầm",
        "metaDescription": "Hướng dẫn điều khiển Approximately Up: điều chúng tôi biết về bàn phím và chuột, hỗ trợ tay cầm và trình ánh xạ lại trong trò chơi — cùng điều vẫn chưa xác minh.",
        "intro": "Hỗ trợ tay cầm là một trong những câu hỏi được hỏi nhiều nhất trên cộng đồng Steam ngay sau khi phát hành. Đây là điều chúng tôi xác nhận được, điều người chơi hỏi và điều vẫn chưa xác minh.",
        "sections": [
            {"heading": "Những gì chúng tôi biết (đã xác minh)",
             "items": [
                ["Nền tảng", "Trò chơi có trên PC (Steam). Bàn phím và chuột là thiết bị nhập mặc định."],
                ["Hỗ trợ tay cầm", "Nhà phát triển chưa xác nhận. Một chủ đề trên diễn đàn Steam hỏi 'Controller Support in the Future?', cho thấy hỗ trợ tay cầm đầy đủ chưa được xác nhận khi ra mắt."],
                ["Trình ánh xạ lại trong trò chơi", "Người chơi đang bàn về Remapper — một chủ đề cộng đồng phản ánh vấn đề đặt giá trị. Quy trình ánh xạ chính xác được đánh dấu là chưa xác minh."],
             ]},
            {"heading": "Cách thiết lập điều khiển ngay bây giờ",
             "items": [
                "Mở cài đặt trong trò chơi và kiểm tra mục đầu vào/điều khiển để xem ánh xạ phím hiện tại.",
                "Dùng Remapper trong trò chơi để gán lại phím; nếu giá trị không áp dụng, hãy xem chủ đề cộng đồng và ghi chú nhà phát triển.",
                "Để cập nhật hỗ trợ tay cầm, hãy theo dõi Discord chính thức và thông báo Steam.",
             ]},
            {"heading": "Chưa xác minh: bản đồ phím đầy đủ", "body": "Bản đồ phím chính thức đầy đủ (di chuyển, camera, menu xây dựng, điều khiển động cơ đẩy) chưa được xác minh từ nguồn chính thức. Chúng tôi đánh dấu là chưa xác minh và sẽ công bố bảng khi được xác nhận."},
            {"heading": "Câu hỏi thường gặp về điều khiển",
             "items": [
                ["Approximately Up có hỗ trợ tay cầm không?", "Chưa xác nhận. Cộng đồng đang hỏi; chúng tôi đánh dấu là chưa xác minh cho đến khi nhà phát triển hoặc nguồn chính thức xác nhận."],
                ["Tôi có thể gán lại phím không?", "Có Remapper trong trò chơi. Một số người chơi phản ánh vấn đề với giá trị; quy trình chính xác chưa xác minh."],
                ["Có bố cục điều khiển cho Steam Deck không?", "Bản thân khả năng tương thích Steam Deck vẫn là câu hỏi mở trong cộng đồng — bố cục chưa xác minh."],
             ]},
        ],
    },
    "multiplayer": {
        "title": "Hướng dẫn chơi mạng Approximately Up",
        "metaTitle": "Chơi mạng Approximately Up: hợp tác, số người chơi và chơi chéo",
        "metaDescription": "Chế độ chơi mạng Approximately Up được giải thích: hợp tác trực tuyến, bao nhiêu người chơi, có chế độ không đồng bộ hay không và điều vẫn chưa xác minh.",
        "intro": "Approximately Up chính thức là trò chơi chơi đơn và hợp tác trực tuyến. Trang này trả lời các câu hỏi chơi mạng mà người chơi thực sự hỏi và đánh dấu điều chúng tôi chưa xác minh được.",
        "sections": [
            {"heading": "Tình trạng chính thức", "body": "Trang Steam chính thức ghi 'Chơi đơn' và 'Hợp tác trực tuyến' là chế độ được hỗ trợ. Bài giới thiệu của trò chơi xoay quanh một phi hành đoàn cùng khám phá hành tinh trên con tàu mô-đun."},
            {"heading": "Câu hỏi thường gặp về chơi mạng",
             "items": [
                ["Bao nhiêu người có thể chơi cùng nhau?", "Số người chính xác chưa được xác minh trong cơ sở kiến thức của chúng tôi — chúng tôi đánh dấu là chưa xác minh."],
                ["Có hợp tác trực tuyến không?", "Có — chế độ chơi mạng hợp tác trực tuyến được ghi trên trang Steam chính thức."],
                ["Có chơi chéo nền tảng không?", "Chưa xác minh. Trò chơi hiện chỉ có trên PC (Steam); phiên bản console chưa được công bố, nên chơi chéo chưa xác minh."],
                ["Có chế độ không đồng bộ không?", "Chưa xác nhận. Một chủ đề trên diễn đàn Steam hỏi về 'Asynchronous Multiplayer', cho thấy nó chưa phải tính năng chính thức — chúng tôi đánh dấu là chưa xác minh."],
                ["Tôi có thể chơi một mình không?", "Có — chế độ chơi đơn được ghi là được hỗ trợ."],
             ]},
            {"heading": "Điều cộng đồng đang hỏi",
             "items": [
                "Chế độ không đồng bộ — liệu người chơi có mong đợi chế độ không đồng bộ.",
                "Số người chơi / 'bao nhiêu người chơi' là nhu cầu tìm kiếm hàng đầu; chúng tôi sẽ công bố con số đã xác minh khi có.",
             ]},
            {"heading": "Điều vẫn chưa xác minh", "body": "Giới hạn số người chính xác, quy trình mời, chi tiết máy chủ và chơi chéo chưa được xác minh từ nguồn chính thức. Chúng tôi sẽ cập nhật trang này ngay khi được xác nhận."},
        ],
    },
    "best-ship-designs": {
        "title": "Thiết kế tàu tốt nhất Approximately Up",
        "metaTitle": "Ý tưởng tàu và thiết kế tốt nhất Approximately Up",
        "metaDescription": "Ý tưởng thiết kế tàu Approximately Up: điểm khởi đầu cho công trình của bạn, câu hỏi thiết kế của cộng đồng và nơi tìm thêm thiết kế.",
        "intro": "Đang tìm ý tưởng tàu? Trang này tổng hợp các điểm khởi đầu dựa trên trải nghiệm chính thức xây-rơi-xây lại, cùng các câu hỏi cộng đồng định hình điều người chơi muốn xây.",
        "sections": [
            {"heading": "Điểm khởi đầu thiết kế (cảm hứng, không phải thông số chính thức)",
             "items": [
                "Xe tốc độ nặng động cơ: gắn động cơ đẩy khổng lồ và chấp nhận rằng khả năng điều khiển đến sau.",
                "Tàu chở hàng tiện dụng: ưu tiên hàng hóa và bộ phận nhiệm vụ hơn tốc độ — nhiệm vụ cần sức chứa (chi tiết chưa xác minh).",
                "Tàu phi hành đoàn hợp tác: thiết kế chỗ cho phi hành đoàn cùng khám phá hành tinh.",
                "Công trình dây cáp lộn xộn: chấp nhận 'dây cáp phiền phức' — hệ thống dây là một phần sức hút (cơ chế dây điện chưa xác minh).",
             ]},
            {"heading": "Câu hỏi thiết kế của cộng đồng",
             "items": [
                ["Máy đo độ cong quỹ đạo", "Chủ đề trên diễn đàn Steam về công cụ quỹ đạo — người chơi muốn công cụ bay tốt hơn; tình trạng chính thức chưa xác minh."],
                ["mod để tạo nhiều tàu?", "Chủ đề trên diễn đàn Steam về việc điều khiển nhiều tàu — chưa xác minh."],
             ]},
            {"heading": "Nơi tìm thêm thiết kế",
             "items": [
                "Steam Workshop của Approximately Up (đã xác nhận hỗ trợ).",
                "Kênh YouTube chính thức cho các công trình trong trailer.",
                "Thảo luận cộng đồng Steam cho ảnh chụp màn hình và ý tưởng của người chơi.",
             ]},
            {"heading": "Điều vẫn chưa xác minh", "body": "Chỉ số bộ phận cụ thể, bản thiết kế của các thiết kế có tên và bất kỳ danh sách 'tốt nhất' nào chưa được xác minh. Chúng tôi giữ trang này như nguồn cảm hứng cộng với nguồn đã xác minh, và đánh dấu mọi thứ khác là chưa xác minh."},
        ],
    },
    "system-requirements": {
        "title": "Cấu hình yêu cầu Approximately Up",
        "metaTitle": "Cấu hình yêu cầu Approximately Up (PC)",
        "metaDescription": "Cấu hình yêu cầu Approximately Up cho PC: cấu hình tối thiểu và đề xuất chưa được xác minh — đây là điều chúng tôi biết và cách kiểm tra khả năng tương thích.",
        "intro": "Người chơi muốn câu trả lời thẳng thắn về việc PC của họ có chạy được Approximately Up không. Cấu hình tối thiểu và đề xuất chính thức vẫn chưa được xác minh, nên trang này cho biết điều chúng tôi biết và điều chưa.",
        "sections": [
            {"heading": "Thông số chính thức: chưa xác minh", "body": "Chúng tôi chưa xác minh cấu hình tối thiểu và đề xuất chính thức từ nguồn chính thức. Thay vì bịa số liệu, chúng tôi đánh dấu bảng thông số là chưa xác minh và sẽ điền ngay khi được xác nhận (trang Steam hoặc trang web chính thức)."},
            {"heading": "Bảng thông số (chưa xác minh)",
             "columns": ["Thông số", "Tối thiểu", "Đề xuất"],
             "rows": [
                ["Hệ điều hành", "chưa xác minh", "chưa xác minh"],
                ["CPU", "chưa xác minh", "chưa xác minh"],
                ["RAM", "chưa xác minh", "chưa xác minh"],
                ["Card đồ họa", "chưa xác minh", "chưa xác minh"],
                ["Ổ cứng", "chưa xác minh", "chưa xác minh"],
                ["DirectX", "chưa xác minh", "chưa xác minh"],
             ]},
            {"heading": "Cách kiểm tra PC của bạn",
             "items": [
                "Mở Steam và xem trang cửa hàng của trò chơi — cấu hình yêu cầu thường xuất hiện ở đó sau khi công bố.",
                "So sánh CPU/GPU/RAM của bạn với số liệu chính thức khi chúng tôi công bố.",
                "Steam Deck: khả năng tương thích là câu hỏi mở của cộng đồng ('Playable on Deck?'); chúng tôi đánh dấu là chưa xác minh.",
             ]},
            {"heading": "Câu hỏi thường gặp về cấu hình",
             "items": [
                ["PC của tôi có chạy được Approximately Up không?", "Chúng tôi chưa thể xác nhận — cấu hình tối thiểu/đề xuất chính thức chưa xác minh. Hãy xem trang Steam khi nhà phát triển công bố."],
                ["Approximately Up có trên Steam Deck không?", "Chưa xác nhận. Một chủ đề trên diễn đàn Steam hỏi 'Playable on Deck?' — khả năng tương thích chưa xác minh cho đến khi có câu trả lời chính thức."],
                ["Trò chơi có nặng không?", "Đây là trò chơi xây dựng hộp cát không gian với tàu mô-đun vật lý; chúng tôi sẽ báo cáo số liệu đã xác minh ngay khi có."],
             ]},
        ],
    },
    "console-release": {
        "title": "Phát hành console Approximately Up: tình trạng PS5, Xbox và Switch",
        "metaTitle": "Ngày phát hành console Approximately Up (PS5, Xbox, Switch)",
        "metaDescription": "Approximately Up có ra mắt trên PS5, Xbox hay Switch không? Chưa có thông báo chính thức — đây là tình trạng console và cách theo dõi tin chính thức.",
        "intro": "'Ngày phát hành PS5 Approximately Up', 'bản Xbox' và 'bản Switch' là những tìm kiếm mà ngay cả wiki của trò chơi cũng không trả lời. Câu trả lời trung thực hôm nay: chưa có thông báo console chính thức nào được xác minh — đây là trang tình trạng.",
        "sections": [
            {"heading": "Tình trạng console (đến ngày 09/08/2026)",
             "items": [
                ["Nền tảng hiện tại", "Chỉ PC (Steam). Trò chơi phát hành ngày 6 tháng 8 năm 2026 trên Steam."],
                ["PS5", "chưa xác minh — không có thông báo chính thức nào được xác minh về bản PlayStation 5."],
                ["Xbox", "chưa xác minh — không có thông báo chính thức nào được xác minh về bản Xbox."],
                ["Nintendo Switch", "chưa xác minh — không có thông báo chính thức nào được xác minh về bản Switch."],
                ["Tuyên bố chính thức", "Chúng tôi chưa xác minh tuyên bố chính thức nào của nhà phát triển về kế hoạch console; đánh dấu là chưa xác minh và sẽ cập nhật khi có."],
             ]},
            {"heading": "Cách cập nhật thông tin",
             "items": [
                "Theo dõi trang web chính thức approximatelyup.com và Discord chính thức (discord.gg/approximatelyup).",
                "Theo dõi kênh YouTube của nhà phát triển (@ApproximatelyUp) và TikTok (@approximatelyup) để biết thông báo.",
                "Xem trang Steam — tin console thường được công bố ở đó trước tiên.",
             ]},
            {"heading": "Câu hỏi thường gặp về console",
             "items": [
                ["Approximately Up có trên PS5 không?", "Chưa công bố — chúng tôi đánh dấu là chưa xác minh. Chưa có tuyên bố chính thức nào được xác minh."],
                ["Có trên Xbox không?", "Chưa công bố — chưa xác minh."],
                ["Có trên Nintendo Switch không?", "Chưa công bố — chưa xác minh."],
                ["Khi nào có ngày phát hành console?", "Chưa có ngày. Trang này sẽ được cập nhật ngay khi có thông báo chính thức được xác minh."],
             ]},
            {"heading": "Vì sao trang này tồn tại", "body": "Phát hành console là một trong những câu hỏi có ý định tìm kiếm cao nhất cho trò chơi này, nhưng chưa nguồn đáng tin cậy nào trả lời. Trang này đưa ra tình trạng đã xác minh (chỉ PC) và theo dõi các thông báo tương lai thay vì bịa ra một ngày."},
        ],
    },
    "mods": {
        "title": "Hướng dẫn mod Approximately Up",
        "metaTitle": "Mod Approximately Up: Steam Workshop, cài đặt và câu hỏi",
        "metaDescription": "Mod Approximately Up được giải thích: hỗ trợ Steam Workshop, cách đăng ký mod và câu hỏi cộng đồng như nhiều tàu.",
        "intro": "Approximately Up hỗ trợ Steam Workshop, giúp việc tìm và cài mod trở nên đơn giản. Đây là điều đã xác nhận và điều người chơi đang yêu cầu.",
        "sections": [
            {"heading": "Nhận mod từ Steam Workshop", "body": "Hỗ trợ Workshop đã được xác nhận trên trang chính thức. Quy trình chuẩn:",
             "items": [
                ["Mở Workshop", "Từ trang Steam của trò chơi, mở tab Workshop (hoặc trung tâm cộng đồng Workshop)."],
                ["Xem và đăng ký", "Tìm mod hoặc mục bạn thích và nhấn Đăng ký — Steam tự động tải xuống."],
                ["Khởi chạy trò chơi", "Mở Approximately Up và kiểm tra menu mod/nội dung của trò chơi để xem các mục đã đăng ký."],
                ["Bật những gì bạn muốn", "Bật các mod bạn muốn dùng. Chi tiết menu mod trong trò chơi chưa xác minh."],
             ]},
            {"heading": "Điều cộng đồng đang hỏi",
             "items": [
                "mod để tạo nhiều tàu? — một chủ đề thật trên diễn đàn Steam; hỗ trợ nhiều tàu qua mod chưa xác minh.",
                "Các tìm kiếm liên quan cheat engine tồn tại ở nhiều trò chơi; chúng tôi không cung cấp cheat, chỉ cung cấp thông tin mod đã xác minh.",
             ]},
            {"heading": "Câu hỏi thường gặp về mod",
             "items": [
                ["Approximately Up có hỗ trợ mod không?", "Chính thức hỗ trợ Steam Workshop (theo trang cửa hàng). Tài liệu mod đầy đủ chưa xác minh."],
                ["Cách cài mod?", "Đăng ký qua Steam Workshop; Steam lo việc cài đặt. Các bước trong trò chơi chưa xác minh."],
                ["Mod có thể giúp tôi điều khiển nhiều tàu không?", "Một chủ đề cộng đồng yêu cầu điều này; chưa có mod nào được xác minh — chưa xác minh."],
             ]},
            {"heading": "Điều vẫn chưa xác minh", "body": "Tính năng Workshop chính xác, hướng dẫn mod và việc mod có ảnh hưởng đến thành tựu hay chế độ chơi mạng hay không vẫn chưa được xác minh. Chúng tôi sẽ cập nhật trang này khi tài liệu chính thức được xác nhận."},
        ],
    },
    "patch-notes": {
        "title": "Ghi chú bản vá Approximately Up",
        "metaTitle": "Ghi chú bản vá và lịch sử cập nhật Approximately Up",
        "metaDescription": "Ghi chú bản vá và lịch sử cập nhật Approximately Up: thông tin phát hành, nơi đăng cập nhật chính thức và nhật ký thay đổi chúng tôi theo dõi (mục chưa xác minh được đánh dấu).",
        "intro": "Approximately Up phát hành ngày 6 tháng 8 năm 2026. Trang này theo dõi ghi chú bản vá và cập nhật chính thức — mọi thứ chưa xác minh đều được đánh dấu rõ ràng.",
        "sections": [
            {"heading": "Sự kiện phát hành (đã xác minh)",
             "items": [
                ["Ngày phát hành", "6 tháng 8 năm 2026 (bản đầy đủ trên Steam)."],
                ["Demo", "Bản demo ra mắt trước bản đầy đủ."],
                ["Giá", "19,99 $ khi phát hành (giảm 20%; giá niêm yết 24,99 $)."],
             ]},
            {"heading": "Dòng thời gian cập nhật (xác minh từ Steam)", "body": "Ghi chú bản vá được xác minh từ thông báo chính thức trên Steam (tháng 8/2026):",
             "items": [
                ["2026-08-12", "1.0.010 — Đã sửa bộ lọc sắp xếp 'Phổ biến nhất' của Workshop, tải trang và kết quả bị thiếu; cải thiện độ rõ của tìm kiếm."],
                ["2026-08-11", "1.0.009 — Cải thiện Frame Quarter With Ports (cổng phản chiếu sang phía đối diện của chuỗi, nhãn A–D nhất quán); sửa hình dạng Middle Window, Small Switch và Small Button."],
                ["2026-08-10", "1.0.008 — Đã sửa hitbox của Axis Rotometer và các vấn đề còn lại; Plasma Cables giờ sơn được; Autohemisphere Solar Panels trở về vị trí sau Fly Mode; giá đỡ cáp sơn được."],
                ["2026-08-09", "1.0.007 — Đã sửa tương thích với thiết bị Metal; sửa phím mặc định (nút giữa chuột để 'nhặt linh kiện'); sửa lỗi chính tả trong mô tả ống; thêm gợi ý."],
                ["2026-08-08", "1.0.006 — Đã sửa Fuse Box không bật lại được; Axis Rotometer giờ xuất giá trị có dấu đúng; sửa bản xem trước Large Disposable Battery; thêm credits, màn hình khởi động và theo dõi tiến độ mục tiêu."],
             ]},
            {"heading": "Nơi đăng cập nhật chính thức",
             "items": [
                "Thông báo Steam của trò chơi (luồng tin trên trang cửa hàng).",
                "Trang web chính thức approximatelyup.com và Discord chính thức.",
                "Kênh YouTube của nhà phát triển cho các thông báo tính năng.",
             ]},
            {"heading": "Điều vẫn chưa xác minh", "body": "Nội dung bản vá cụ thể (thay đổi cân bằng, sửa lỗi, bộ phận mới) chưa được xác minh. Chúng tôi đánh dấu mọi thứ là chưa xác minh thay vì đoán."},
        ],
    },
    "demo-vs-full": {
        "title": "Demo Approximately Up so với bản đầy đủ",
        "metaTitle": "Demo Approximately Up so với bản đầy đủ: khác gì?",
        "metaDescription": "Demo so với bản đầy đủ Approximately Up: ngày phát hành, giá, Workshop và thành tựu — cùng những khác biệt nội dung vẫn chưa xác minh.",
        "intro": "Bản demo Approximately Up ra mắt trước bản đầy đủ ngày 6 tháng 8 năm 2026. Đây là so sánh đã xác minh, với khác biệt nội dung được đánh dấu rõ là chưa xác minh.",
        "sections": [
            {"heading": "So sánh đã xác minh",
             "columns": ["Khía cạnh", "Demo", "Bản đầy đủ"],
             "rows": [
                ["Khả dụng", "Demo (ra mắt sớm hơn, theo trang cửa hàng)", "Bản đầy đủ phát hành 6 tháng 8 năm 2026"],
                ["Giá", "chưa xác minh", "19,99 $ (giảm 20% khi ra mắt; giá niêm yết 24,99 $)"],
                ["Steam Workshop", "chưa xác minh", "Được hỗ trợ (theo trang cửa hàng)"],
                ["Thành tựu", "chưa xác minh", "22 thành tựu Steam (theo trang cửa hàng)"],
                ["Chơi mạng hợp tác", "chưa xác minh", "Chơi đơn + hợp tác trực tuyến (theo trang cửa hàng)"],
             ]},
            {"heading": "Câu hỏi thường gặp demo so với bản đầy đủ",
             "items": [
                ["Demo có miễn phí không?", "Chúng tôi chưa xác minh giá/mô hình của demo — chưa xác minh."],
                ["Tiến trình demo có chuyển sang bản đầy đủ không?", "Chưa xác minh."],
                ["Nội dung nào chỉ có ở bản đầy đủ?", "Chưa xác minh — chi tiết so sánh chính thức đang chờ. Bản đầy đủ thêm hỗ trợ Workshop và 22 thành tựu theo trang cửa hàng."],
                ["Tôi có nên thử demo trước không?", "Với hầu hết trò chơi xây dựng hộp cát không gian, thử demo là cách tốt để cảm nhận vòng lặp xây-rơi-xây lại trước khi mua — nhưng giới hạn nội dung demo chính xác chưa xác minh."],
             ]},
            {"heading": "Điều vẫn chưa xác minh", "body": "Nội dung demo chính xác, chuyển tiến trình và khác biệt tính năng chưa được xác minh từ nguồn chính thức. Chúng tôi sẽ cập nhật bảng này ngay khi được xác nhận."},
        ],
    },
    "achievements-list": {
        "title": "Danh sách thành tựu Approximately Up",
        "metaTitle": "Thành tựu Approximately Up: danh sách đầy đủ (22)",
        "metaDescription": "Approximately Up có 22 thành tựu Steam. Danh sách tên đầy đủ đang được xác minh — đây là điều đã xác nhận.",
        "intro": "Trang Steam chính thức xác nhận 22 thành tựu. Tên chính xác và điều kiện mở khóa chưa được xác minh, nên trang này theo dõi số đã xác nhận và đánh dấu danh sách là chưa xác minh.",
        "sections": [
            {"heading": "Đã xác nhận: 22 thành tựu", "body": "Trang Steam ghi Approximately Up có 22 thành tựu. Chúng tôi chưa xác minh tên, biểu tượng và điều kiện của từng thành tựu — phần đó chưa xác minh."},
            {"heading": "Danh sách thành tựu (chưa xác minh)",
             "columns": ["Thành tựu", "Điều kiện"],
             "rows": [
                ["Thành tựu 1–22", "chưa xác minh — tên và điều kiện đang được đối chiếu với danh sách chính thức."],
             ]},
            {"heading": "Cách theo dõi thành tựu",
             "items": [
                "Dùng lớp phủ Steam trong trò chơi để xem tiến trình của bạn.",
                "Theo dõi thông báo Steam chính thức — danh sách thành tựu đôi khi đi kèm ghi chú bản vá.",
                "Chúng tôi sẽ công bố danh sách đầy đủ đã xác minh tại đây khi được xác nhận.",
             ]},
            {"heading": "Câu hỏi thường gặp về thành tựu",
             "items": [
                ["Approximately Up có bao nhiêu thành tựu?", "22, đã xác nhận trên trang Steam chính thức."],
                ["Tên các thành tựu là gì?", "chưa xác minh — chúng tôi đang xác minh danh sách chính thức và sẽ công bố khi được xác nhận."],
                ["Tôi có thể lấy hết thành tựu ở chế độ chơi đơn không?", "Chưa xác minh — một số có thể cần hợp tác, nhưng chúng tôi chỉ biết sau khi danh sách được xác nhận."],
             ]},
        ],
    },
    "ships": {
        "title": "Tàu Approximately Up",
        "metaTitle": "Tàu Approximately Up: công trình, ý tưởng và thiết kế",
        "metaDescription": "Chỉ mục nội dung tàu Approximately Up: hướng dẫn chế tạo, thiết kế tàu, bản thiết kế và kiến thức cơ bản về chế tạo mô-đun.",
        "intro": "Mọi thứ về tàu Approximately Up trong một nơi — từ công trình đầu tiên đến ý tưởng thiết kế của cộng đồng.",
        "sections": [
            {"heading": "Hướng dẫn về tàu",
             "items": [
                "Hướng dẫn chế tạo tàu — học quy trình xây-rơi-xây lại.",
                "Thiết kế tốt nhất — điểm khởi đầu và ý tưởng cộng đồng.",
                "Hướng dẫn bản thiết kế — điều chúng tôi biết về bản thiết kế và nội dung Workshop.",
                "Mod — hỗ trợ Workshop và câu hỏi về mod.",
             ]},
            {"heading": "Câu hỏi thường gặp về tàu",
             "items": [
                ["Tôi có thể xây loại tàu nào?", "Chúng hoàn toàn mô-đun — bạn bắt vít các bộ phận theo cách chúng khớp (mô tả chính thức). Danh sách bộ phận cụ thể chưa xác minh."],
                ["Tôi có thể bay lên Mặt Trăng không?", "Một chủ đề cộng đồng hỏi cách làm; cơ chế Mặt Trăng chưa xác minh."],
                ["Tôi có thể điều khiển nhiều tàu không?", "Một chủ đề cộng đồng hỏi về điều này; chưa xác minh."],
             ]},
        ],
    },
    "blueprints": {
        "title": "Bản thiết kế Approximately Up",
        "metaTitle": "Bản thiết kế Approximately Up: tải xuống và thư viện",
        "metaDescription": "Chỉ mục nội dung bản thiết kế Approximately Up: cách dùng bản thiết kế, nơi tìm thiết kế tàu và Steam Workshop.",
        "intro": "Chỉ mục thư viện bản thiết kế — tìm thiết kế tàu, tìm hiểu quy trình (chưa xác minh) và duyệt Workshop.",
        "sections": [
            {"heading": "Nội dung bản thiết kế",
             "items": [
                "Hướng dẫn bản thiết kế — điều đã xác nhận và chưa xác minh về bản thiết kế.",
                "Thiết kế tốt nhất — ý tưởng thiết kế và nơi tìm thêm.",
                "Steam Workshop — nơi đã xác nhận chứa nội dung cộng đồng.",
             ]},
            {"heading": "Câu hỏi thường gặp chỉ mục bản thiết kế",
             "items": [
                ["Tôi có thể tải bản thiết kế ở đâu?", "Steam Workshop là kênh đã xác nhận cho nội dung cộng đồng; cơ chế tải bản thiết kế trong trò chơi chưa xác minh."],
                ["Cách nhập bản thiết kế?", "Chưa xác minh."],
                ["Tôi có thể chia sẻ thiết kế của mình không?", "Chưa xác minh."],
             ]},
        ],
    },
    "guides": {
        "title": "Hướng dẫn Approximately Up",
        "metaTitle": "Hướng dẫn Approximately Up: tất cả trang",
        "metaDescription": "Tất cả hướng dẫn Approximately Up trong một chỉ mục: cách chơi, chế tạo tàu, điều khiển, chơi mạng, mod, thành tựu và hơn thế nữa.",
        "intro": "Chỉ mục hướng dẫn đầy đủ cho Approximately Up. Mỗi trang trả lời một câu hỏi người chơi thực sự tìm kiếm và đánh dấu mọi thứ chưa xác minh.",
        "sections": [
            {"heading": "Tất cả hướng dẫn",
             "items": [
                "Cách chơi — vòng lặp xây-rơi-xây lại cho người mới.",
                "Điều khiển — bàn phím/chuột, trạng thái tay cầm và ghi chú trình ánh xạ lại.",
                "Cấu hình yêu cầu — tình trạng thông số và cách kiểm tra PC.",
                "Chơi mạng — hợp tác trực tuyến, số người chơi và câu hỏi không đồng bộ.",
                "Phát hành console — tình trạng PS5/Xbox/Switch.",
                "Mod — Steam Workshop và câu hỏi về mod.",
                "Ghi chú bản vá — sự kiện phát hành và theo dõi cập nhật.",
                "Demo so với bản đầy đủ — so sánh đã xác minh.",
                "Hướng dẫn chế tạo tàu — từ con tàu đầu tiên đến công trình lớn.",
                "Dây điện và linh kiện — điều đã biết, điều chưa.",
                "Hướng dẫn bản thiết kế — tình trạng bản thiết kế và Workshop.",
                "Thiết kế tốt nhất — ý tưởng và thiết kế cộng đồng.",
                "Danh sách thành tựu — 22 thành tựu, danh sách chưa xác minh.",
                "Tàu / Bản thiết kế / Thành tựu — trang chỉ mục.",
             ]},
            {"heading": "Cách chúng tôi làm việc", "body": "Mỗi trang liệt kê 1–2 nguồn đáng tin cậy và đánh dấu mọi thứ chưa xác minh. Chúng tôi không bịa số liệu, tên hoặc cơ chế."},
        ],
    },
    "achievements": {
        "title": "Thành tựu Approximately Up",
        "metaTitle": "Thành tựu Approximately Up: tổng quan",
        "metaDescription": "Tổng quan thành tựu Approximately Up: 22 thành tựu Steam đã xác nhận, danh sách đầy đủ đang xác minh và cách theo dõi tiến trình.",
        "intro": "Trung tâm thành tựu Approximately Up — số đã xác nhận, tình trạng danh sách hiện tại và liên kết đến trang theo dõi đầy đủ.",
        "sections": [
            {"heading": "22 thành tựu đã xác nhận", "body": "Trang Steam xác nhận 22 thành tựu. Danh sách tên và điều kiện đầy đủ chưa xác minh."},
            {"heading": "Nội dung thành tựu",
             "items": [
                "Danh sách thành tựu — trang dành riêng cho danh sách đầy đủ (chưa xác minh).",
                "Steam — xem mục thành tựu trên trang cửa hàng.",
             ]},
            {"heading": "Câu hỏi thường gặp tổng quan thành tựu",
             "items": [
                ["Có bao nhiêu thành tựu?", "22 (đã xác nhận trên trang Steam)."],
                ["Danh sách đầy đủ ở đâu?", "chưa xác minh — chúng tôi đang xác minh danh sách chính thức."],
             ]},
        ],
    },
}

# =====================================================================
# 组装 site.json：site + game + pages（en）→ 逐语言翻译 → zh-TW（OpenCC）→ 写出
# =====================================================================
TRS = {
    "zh-CN": TR_ZH, "ja": TR_JA, "ko": TR_KO, "fr": TR_FR, "de": TR_DE,
    "es": TR_ES, "it": TR_IT, "pl": TR_PL, "pt-BR": TR_PT, "ru": TR_RU,
    "uk": TR_UK, "vi": TR_VI,
}

def apply_lang(pages, lang, TR):
    """按 en sections 索引对齐，把 TR[slug] 挂到 page.i18n[lang]。"""
    for p in pages:
        tr = TR.get(p["slug"])
        if not tr:
            continue
        en_secs = p["sections"]
        i18n = {}
        for k in ("title", "metaTitle", "metaDescription", "intro"):
            if k in tr:
                i18n[k] = tr[k]
        if "sections" in tr:
            secs = []
            for i, en_sec in enumerate(en_secs):
                cand = tr["sections"][i] if i < len(tr["sections"]) else None
                if cand is None:
                    continue
                new_sec = {}
                if "type" in en_sec:
                    new_sec["type"] = en_sec["type"]
                for k in ("heading", "body", "items", "columns", "rows"):
                    if k in cand:
                        new_sec[k] = cand[k]
                if new_sec:
                    secs.append(new_sec)
            if secs:
                i18n["sections"] = secs
        p.setdefault("i18n", {})[lang] = i18n

PAGES = copy.deepcopy(PAGES)
for lang in TRANS_LANGS:
    if lang == "zh-TW":
        continue
    apply_lang(PAGES, lang, TRS[lang])

# zh-TW：全量由 zh-CN 经 OpenCC(s2tw) 生成（页面翻译）
for p in PAGES:
    zc = p.get("i18n", {}).get("zh-CN")
    if zc:
        p["i18n"]["zh-TW"] = json.loads(cc.convert(json.dumps(zc, ensure_ascii=False)))

# site.i18n / game i18n 的 zh-TW
SITE_I18N["zh-TW"] = json.loads(cc.convert(json.dumps(SITE_I18N["zh-CN"], ensure_ascii=False)))
SITE_I18N["zh-TW"]["name"] = "Approximately Up 攻略網站"
GAME_I18N["zh-TW"] = json.loads(cc.convert(json.dumps(GAME_I18N["zh-CN"], ensure_ascii=False)))

# 组装顶层结构
site = dict(SITE)
site["languages"] = list(LANGS)
site["defaultLanguage"] = "en"
site["i18n"] = SITE_I18N

game = dict(GAME)
game["nameI18n"] = {lang: "Approximately Up" for lang in LANGS}
game["statsI18n"] = {}
game["introI18n"] = {}
game["keyFactsI18n"] = {}
game["aboutPointsI18n"] = {}
for lang in LANGS:
    if lang == "en":
        game["statsI18n"]["en"] = GAME["stats"]
        game["introI18n"]["en"] = GAME["intro"]
        game["keyFactsI18n"]["en"] = GAME["keyFacts"]
        game["aboutPointsI18n"]["en"] = GAME["aboutPoints"]
        continue
    gi = GAME_I18N[lang]
    game["statsI18n"][lang] = gi["stats"]
    game["introI18n"][lang] = gi["intro"]
    game["keyFactsI18n"][lang] = gi["keyFacts"]
    game["aboutPointsI18n"][lang] = gi["aboutPoints"]

# ---------- SEO 长度后处理（title≤60/40，desc≤158/78，词边界截断）----------
import unicodedata as _ud
def _cjkr(t):
    if not t: return 0
    return sum(1 for ch in t if _ud.east_asian_width(ch) in ("W","F")) / max(len(t),1)
def _trunc(t, lim):
    if len(t) <= lim: return t
    cut = t[:lim-1]
    for i in range(len(cut)-1, max(0, len(cut)-25), -1):
        if cut[i] in " .,;:!?、。，；：！？/-":
            if i > lim*0.5:
                return cut[:i].rstrip(" ,;:/-") + "…"
            break
    return cut.rstrip() + "…"

def _trunc_w(t, lim):
    # 按显示宽度截断（CJK 宽字符算 2，拉丁算 1）——修复 _trunc 用字符数导致 CJK 永不截断的 bug
    w = 0; cut = ""
    for ch in t:
        cw = 2 if _ud.east_asian_width(ch) in ("W", "F") else 1
        if w + cw > lim: break
        w += cw; cut += ch
    if cut == t: return t
    return cut.rstrip() + "…"
def _fix_len(v, is_desc):
    # 拉丁语系留转义余量（&amp; 等实体在 HTML 里算 5 字符，audit 按原始 HTML 数）
    lim = 148 if is_desc else 55
    if _cjkr(v) > 0.3:
        lim = 78 if is_desc else 38
    return _trunc(v, lim)
def _fix_cjk(v, is_desc):
    lim = 74 if is_desc else 34   # 留 &amp; 等实体余量（audit 按原始 HTML 数）
    return _trunc_w(v, lim)
def _apply_seo(node, lang="en"):
    cjk = lang in ("zh-CN","zh-TW","ja","ko")
    for f in ("title","metaTitle"):
        if node.get(f):
            node[f] = (_fix_cjk(node[f], False) if cjk else _fix_len(node[f], False))
    if node.get("metaDescription"):
        node["metaDescription"] = (_fix_cjk(node["metaDescription"], True) if cjk else _fix_len(node["metaDescription"], True))
# site 级 description（按语言；site.i18n 用 description 字段，非 metaDescription）
for _lang, _i18n in site.get("i18n", {}).items():
    if _i18n.get("description"):
        _i18n["description"] = (_fix_cjk(_i18n["description"], True) if _lang in ("zh-CN","zh-TW","ja","ko") else _fix_len(_i18n["description"], True))
    if _i18n.get("name") and len(_i18n["name"]) > 60: _i18n["name"] = _trunc(_i18n["name"], 60)
# 页面级
for _p in PAGES:
    _apply_seo(_p, "en")
    for _lang, _tr in (_p.get("i18n") or {}).items():
        _apply_seo(_tr, _lang)

# zh-TW achievements-list metaTitle 手动覆盖：OpenCC 后与 zh-CN 截断结果相同（简繁同文）
# → 用繁体特有词区分，避免 audit dup-title（"列表" vs "清單"）
for _p in PAGES:
    if _p["slug"] == "achievements-list" and "zh-TW" in _p.get("i18n", {}):
        _p["i18n"]["zh-TW"]["metaTitle"] = "Approximately Up 成就完整清單：22 項收錄"

# ---------- heroImage 自动填充（assets/images/<slug>.jpg → 页面 heroImage）----------
# 修复：fill_images.py 填充后被 build 覆盖丢失的 bug——并入构建，每次自动带图
_ASSET_IMG = ROOT.parent / "assets" / "images"
if _ASSET_IMG.exists():
    for _p in PAGES:
        _img = _ASSET_IMG / f"{_p['slug']}.jpg"
        if _img.exists() and _img.stat().st_size > 20000:
            _p["heroImage"] = f"/images/{_p['slug']}.jpg"

d = {"site": site, "game": game, "pages": PAGES}

out = ROOT / "site.json"
out.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- 校验输出 ----------
print("site.json written:", out)
print("langs:", len(LANGS), LANGS)
print("pages:", len(PAGES))
print("page slugs:", [p["slug"] for p in PAGES])

# 每页 × 每语言翻译齐全性 + section 对齐
missing = []
misalign = []
for p in PAGES:
    for lang in LANGS[1:]:
        tr = p.get("i18n", {}).get(lang)
        if not tr:
            missing.append((p["slug"], lang))
            continue
        en_n = len(p["sections"])
        tr_n = len(tr.get("sections", []))
        if tr_n != en_n:
            misalign.append((p["slug"], lang, en_n, tr_n))
print("missing translations:", missing if missing else "NONE ✓")
print("section-count mismatch:", misalign if misalign else "NONE ✓")

# JSON 合法性复查
chk = json.loads(out.read_text(encoding="utf-8"))
print("json valid:", chk["site"]["languages"] == LANGS, "| pages:", len(chk["pages"]))
