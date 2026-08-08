# -*- coding: utf-8 -*-
"""Approximately Up 配图生成：Seedream 文生图，太空工程蓝图统一风格，16:9 高清."""
import os, re, json, time, urllib.request, base64, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets" / "images"
ASSETS.mkdir(parents=True, exist_ok=True)

env = open("/Users/azu/Documents/跨境电商AI系统/.env", encoding="utf-8").read()
m = re.search(r"^ARK_API_KEY=(.+)$", env, re.M)
if not m:
    sys.exit("ARK_API_KEY not found")
API_KEY = m.group(1).strip().strip('"').strip("'").strip()

ENDPOINT = "https://ark.cn-beijing.volces.com/api/v3/images/generations"
MODEL_PRO = "doubao-seedream-5-0-pro-260628"
MODEL_LITE = "doubao-seedream-5-0-lite-260128"

# ui-ux-pro-max Gaming 方向：vibrant + neon + immersive；太空工程蓝图统一风格
STYLE = ("2D game key art for a co-op space sandbox ship-building game, deep-space navy background with "
         "cyan blueprint grid lines and amber warning accents, modular spaceship parts and holographic "
         "blueprints, dramatic lighting, high detail, cinematic composition, no text, no watermark, no logos, "
         "16:9 widescreen")

PROMPTS = {
  "hero": "A modular starship assembled from scrap parts flying over a strange alien planet, glowing cyan thrusters and cable wiring, holographic blueprint overlay, deep-space navy and cyan palette, " + STYLE,
  "how-to-play": "A pilot in a spacesuit standing on a hangar deck in front of a half-built modular ship, holographic controls and floating parts, " + STYLE,
  "ship-building-guide": "Close-up of a modular ship under construction: giant thrusters being bolted onto a frame, cables hanging, engineering hologram beside it, " + STYLE,
  "blueprints-guide": "A glowing holographic blueprint table showing a spaceship schematic, hands dragging parts into place, cyan lines on dark panels, " + STYLE,
  "wiring-electronics": "A tangle of glowing cables and circuit boards being wired into a ship panel, a technician with a welding tool, amber sparks, " + STYLE,
  "controls": "A spaceship cockpit control panel with holographic displays, joysticks and buttons glowing cyan, viewport showing space, " + STYLE,
  "multiplayer": "Two astronauts in spacesuits working together to assemble a ship in zero gravity, tools floating, connected by tether, " + STYLE,
  "best-ship-designs": "A fleet of creative modular spaceships docked in a spaceport, each with unique designs, neon accents, blueprint holograms, " + STYLE,
  "system-requirements": "A high-tech computer workstation in a spaceship interior, holographic spec sheet floating above the monitor, " + STYLE,
  "console-release": "A game controller floating in zero gravity next to a spaceship window, planet below, console vibe, " + STYLE,
  "mods": "A workshop in space with modular ship parts being modified, tools and holographic mods list, tinkerer vibe, " + STYLE,
  "patch-notes": "A holographic changelog screen in a ship corridor, a crew member reading it, cyan text glow, " + STYLE,
  "demo-vs-full": "Two ships side by side: a small prototype demo ship and a larger full-version ship, comparison holograms, " + STYLE,
  "achievements-list": "A wall of glowing holographic achievement badges in a spaceship lounge, crew member looking at them, " + STYLE,
}

def call(prompt, model=MODEL_PRO, retries=3):
    body = json.dumps({"model": model, "prompt": prompt, "size": "1600x900",
                       "response_format": "url", "watermark": False}).encode()
    for i in range(retries):
        try:
            req = urllib.request.Request(ENDPOINT, data=body, method="POST", headers={
                "Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.loads(r.read().decode())
            items = data.get("data") or []
            if items:
                return items[0].get("url") or (items[0].get("b64_json") and "data:"+items[0]["b64_json"])
        except Exception as e:
            print(f"  attempt {i+1} failed: {e}")
            time.sleep(8 * (i + 1))
    return None

def download(url, dest):
    if url.startswith("data:"):
        b64 = url.split(",", 1)[1]
        Path(dest).write_bytes(base64.b64decode(b64))
        return True
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=180) as r:
        Path(dest).write_bytes(r.read())
    return True

def main():
    todo = dict(PROMPTS)
    done = []
    for name, prompt in todo.items():
        dest = ASSETS / f"{name}.jpg"
        if dest.exists() and dest.stat().st_size > 20000:
            print(f"skip {name} (exists)")
            done.append(name)
            continue
        print(f"generating {name} ...", flush=True)
        url = call(prompt)
        if not url:
            print(f"  FAILED {name}, trying lite model")
            url = call(prompt, model=MODEL_LITE)
        if url:
            download(url, dest)
            print(f"  OK {name} -> {dest.stat().st_size} bytes", flush=True)
            done.append(name)
        else:
            print(f"  FAILED {name}")
        time.sleep(2)
    print(f"\nDone: {len(done)}/{len(todo)} images")

if __name__ == "__main__":
    main()
