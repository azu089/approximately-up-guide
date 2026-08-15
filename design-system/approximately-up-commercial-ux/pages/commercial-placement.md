# Page Override — Commercial Placement

This file overrides the master only for display-ad and future contextual-recommendation modules.

## Wireframes

```text
Desktop article (>=1081px)
230 TOC          flexible editorial column (max ad 760)          220 related
┌─────────┐      ┌──────────────────────────────────────┐        ┌─────────┐
│ nodes   │      │ section 01                           │        │ related │
│         │      │ section 02                           │        │ Steam   │
│         │      ├─ centered commercial boundary ───────┤        └─────────┘
│         │      │ ADVERTISEMENT                        │
│         │      │      responsive Adsterra creative    │
│         │      ├──────────────────────────────────────┤
│         │      │ remaining editorial + sources        │
└─────────┘      └──────────────────────────────────────┘

Mobile (<=720px)
16px ┌──────────────────────────────┐ 16px
     │ TOC / section 01 / section 02│
     ├──────────────────────────────┤
     │ ADVERTISEMENT                │
     │ centered responsive creative │
     ├──────────────────────────────┤
     │ remaining guide / related    │
     └──────────────────────────────┘
```

Home retains the flightdeck. Place the single wrapper after `.hab-panel:nth-of-type(2)` inside `.fd-right`; on desktop it aligns only to the right rail, and under `1080px` it becomes one column. Do not place it between the game summary and first navigation module.

## Display wrapper

- Suggested hook: `[data-commercial-slot="primary-display"]` with `data-state="idle|loading|filled|empty|error"`.
- `idle`, `empty`, and `error` are `hidden`; `hidden` is authoritative.
- `loading` and `filled`: `margin-inline:auto; width:100%; max-width:760px`, with amber mono disclosure above the provider surface.
- Filled surface may use `background:var(--bg2)`, `border-block:1px solid var(--line)`, and `padding:12px clamp(0px,2vw,16px)`. Do not imitate an editorial `.panel-block` or add game icons/art.
- Center provider content with `margin-inline:auto; max-width:100%`. Reject or separately reconfigure a fixed-width creative wider than its column; never crop or add horizontal scrolling.

## Future Amazon/contextual recommendations

Current state is absent. After exact provider registration/configuration approval, place a separate `Recommended equipment` module after the final substantive section and before sources, never in the display slot or footer. Use at most four evidence-relevant items, one column on mobile and two on desktop. Avoid fake ratings, urgency, current-price, stock, “best”, or personal-use claims. Commission disclosure precedes the first paid link.

## Instrumentation boundary

Allowed low-cardinality first-party states are `commercial_slot_eligible`, `commercial_slot_request`, and `commercial_slot_rendered`, only after analytics consent. `rendered` is local DOM state, not provider impression/viewability. Provider clicks, orders, commission, revenue, and profit remain provider-measured or `not_measured`; no event is replayed after late consent.

## Rollback

One implementation switch removes the in-main wrapper/state controller and leaves provider serving off. Rollback must not restore stale Amazon footer output or unapproved AdSense serving. If centering, zero-height no-fill, one-request behavior, consent containment, or provider gating fails, reject the successor rather than partially release it.
