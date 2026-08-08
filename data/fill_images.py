# -*- coding: utf-8 -*-
"""配图填充：assets/images/<slug>.jpg → site.json 页面 heroImage（幂等，缺失跳过）"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data" / "site.json"
IMAGES = ROOT / "assets" / "images"

d = json.loads(DATA.read_text(encoding="utf-8"))

# 首页 ogImage（hero）
hero = IMAGES / "hero.jpg"
if hero.exists() and hero.stat().st_size > 20000:
    d["site"]["ogImage"] = "/images/hero.jpg"

# 页面 heroImage
filled = []
for p in d["pages"]:
    slug = p["slug"]
    img = IMAGES / f"{slug}.jpg"
    if img.exists() and img.stat().st_size > 20000:
        p["heroImage"] = f"/images/{slug}.jpg"
        filled.append(slug)

DATA.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"✅ 填充 {len(filled)} 页配图: {', '.join(filled)}")
