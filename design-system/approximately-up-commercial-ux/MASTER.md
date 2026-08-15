# Approximately Up Commercial UX — Design System

- task: `ui-approximately-up-ad-layout-repair-20260816-01`
- scope: existing-page commercial layout maintenance; no URL, user job, taxonomy, or IA change
- product IA retained: `sites/approximately-up/DESIGN-PLAN.md` (`e38aae2194807feceffc0afc05eb1a699c6f9558f7ec09c5d19275e954fea8b3`)
- actual stack: Node.js static generator, semantic HTML, plain CSS, small vanilla-JavaScript progressive enhancement
- source system: `ui-ux-pro-max` query `multilingual dark game guide content-first ethical advertising affiliate recommendations`; variance `2`, motion `1`, density `5`

## Selection and rejection record

The searchable design database returned a content-first system, a dark palette, standard spacing, AA contrast, responsive checks, visible focus, and layout-shift avoidance. Those constraints are retained. Its `Video Streaming/OTT`, newsletter form, felt-green palette, Noto Serif typography, oversized headings, card hover lift, GSAP scroll reveal, and “instant state changes are always bad” suggestions are rejected: they misclassify this static game-guide site, conflict with the approved “Space-Engineer Blueprint” identity, add a dependency, and would make advertising visually compete with editorial content.

The current visual language is normative:

| Token | Value | Commercial use |
| --- | --- | --- |
| `--bg` | `#0B1220` | page field |
| `--bg2` | `#0F1B2E` | filled commercial surface only |
| `--bg3` | `#16233B` | neutral loading surface only |
| `--line` | `#1E3A5F` | quiet separator |
| `--line2` | `#2A4E7C` | focus/strong separator |
| `--text` | `#D8E4F2` | primary copy |
| `--muted` | `#8FA6BF` | supporting copy; retain AA contrast at its rendered size |
| `--cyan` | `#4FD1C5` | focus and interaction, not ad decoration |
| `--amber` | `#F59E0B` | advertisement / sponsored disclosure |
| `--radius` | `10px` | filled wrapper only |
| `--ease-out` | `cubic-bezier(.23,1,.32,1)` | press feedback; never ad arrival |

Typography remains the existing `Russo One`/`Chakra Petch`/Noto/system fallback stack. Advertisement and sponsored labels use the mono stack, `12px`, `600`, `0.12em` tracking, uppercase only where the locale supports it. Disclosure must be meaning-complete in all 14 locales; English fallback is not accepted.

## Commercial hierarchy

1. Editorial answer and navigation remain primary.
2. One eligible Adsterra unit is the only network-display opportunity. It is centered inside the current content column, never inside or after the site footer.
3. Contextual product recommendations are a separate affiliate component. They may exist only after the current domain, tracking configuration, destinations, disclosures, and provider action are approved. They are not called an Adsterra ad and do not occupy the display-ad slot.
4. Google AdSense serving remains absent. Ownership metadata or `ads.txt` does not authorize a serving script or an empty AdSense box.
5. Footer contains navigation, provenance, privacy settings, and legal metadata only.

## Geometry and responsive tokens

| Range | Inline container | Filled display slot | Outer spacing | Recommendation links |
| --- | --- | --- | --- | --- |
| `>=1081px` | current `.dossier-main` or home `.fd-right`; `max-width:760px; margin-inline:auto` | `width:100%`; provider content centered; loading reserve `180px` | `32px 0` | 2-column grid, `12px` gap |
| `721–1080px` | current one-column main grid; `max-width:760px; margin-inline:auto` | `width:100%`; loading reserve `220px` | `28px 0` | 2-column until each item would be under `220px` |
| `320–720px` | `width:100%`; respect current `16px` page gutters | `width:100%`; loading reserve `250px` | `24px 0` | one column; each link/control min-height `44px` |

The dimensions apply only to the transient consented loading state and filled state. `before-consent`, `rejected`, `withdrawn`, `blocked`, `no-fill`, `timeout`, `provider-error`, and ineligible states have `display:none`/zero block size, zero padding, zero border, and zero margin. No empty ad band is allowed.

## Placement rules

- Eligible inventory is the home page and the 17 existing content/index pages in each of 14 locales. `about`, `privacy`, `contact`, and `404` are excluded.
- Exactly one Adsterra wrapper and at most one provider container/script may exist on an eligible document.
- Article/index template: insert after the second substantive `.panel-block` when at least three sections exist; after the first when exactly two exist; after the only section when exactly one exists. Never split a table, filter, FAQ item, source list, hero, TOC, or CTA.
- Home template: insert in `.fd-right` after the second `.hab-panel`, not between the hero/image and the first navigation module.
- The wrapper is a sibling in normal document flow. It may not be `fixed`, `sticky`, overlay content, span the viewport, escape the main grid, or become a footer child.

Page-specific rules in `pages/commercial-placement.md` override this master.

## State machine and CLS contract

| State | Request | Geometry | Visible UI |
| --- | --- | --- | --- |
| ineligible / no consent / reject / withdrawn | none | zero | none |
| consented, not near slot | none | zero | none |
| consented and within `1200px` prefetch margin | one request | reserve by breakpoint | localized `Advertisement` label plus non-animated loading text |
| filled | no duplicate request | measured stable height | label + provider creative |
| blocked / no-fill / timeout / provider error | no retry in same page view | zero after cleanup | none |

The provider request begins before viewport entry. Fill is not inferred from `script.onload`; require a provider-supported fill signal or a real descendant/iframe whose non-zero height is stable over two animation frames. Use a `2500ms` timeout. On success, commit measured height before exposing the creative. On failure, remove provider descendants and all wrapper geometry. Transition to loading synchronously with consent or before first paint for a stored accepted choice; resolve timeout offscreen where possible. G4 must show slot-attributable CLS `<=0.05`, page CLS `<=0.10`, and no regression from the fixed baseline.

## Accessibility, semantics, and disclosure

- Filled/loading display wrapper: `<aside aria-label="[localized Advertisement]">`; wrapper is not focusable and has no `aria-live`.
- Provider links retain provider focus behavior, must not be covered by an overlay, and appear at their DOM position in tab order.
- Affiliate heading and plain-language commission disclosure precede the first link. Each paid link uses `rel="sponsored noopener"`; ordinary Steam/navigation/source links never receive `sponsored`.
- Site-authored commercial links/buttons have a `44x44` CSS-pixel target and visible `:focus-visible` outline. Color is not the only disclosure cue.
- No `aria-hidden="true"` ancestor may contain a focusable provider or affiliate link.
- Consent management must obey `hidden` with `[hidden]{display:none!important}` or equally deterministic behavior, isolate dialog background, trap forward/reverse Tab without reaching `BODY`, and restore focus on close/save/reject/withdraw. A successor retaining `consent-hidden-state-and-focus-containment` fails acceptance.

## Emil motion contract

The ad is encountered on every eligible visit and delayed third-party arrival has no valid delight or spatial-explanation purpose. The slot, label, loading reserve, creative arrival, no-fill collapse, and affiliate module have no authored fade, slide, scale, shimmer, pulse, height transition, or scroll reveal. State changes are immediate after resolution. Site-authored pressables may keep `transform:scale(.98)` for `100ms` with `--ease-out`; hover color/border changes are `150ms` and gated by `(hover:hover) and (pointer:fine)`. `prefers-reduced-motion:reduce` removes transforms and preserves visible state/focus changes.

## Forbidden patterns

- Footer advertising, full-viewport commercial rows, left-aligned provider containers, sticky/anchor/interstitial/popunder/social-bar formats.
- Reserved geometry before consent or after no fill; decorative skeletons; animation of width, height, margin, or padding.
- Rendering Amazon because production contains stale links; rendering AdSense because a publisher ID exists; describing an unregistered provider as active.
- Mixing network ads and contextual product links in one unlabeled component.
- More than one provider script/container, retries during a page view, or analytics claims of impression, viewability, click, order, revenue, or profit without provider evidence.

## Required viewports

`320x568`, `375x812`, `414x896`, `768x1024`, `1080x900`, and `1440x900`, plus 200% zoom. Test LTR and a long-label locale; there is no RTL locale in the current 14-language IA.
