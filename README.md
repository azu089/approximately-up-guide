# Approximately Up Guide · approximatelyupguides.com

> 热词游戏站第 4 站（太空工程蓝图主题）。主词 Approximately Up（Steam 太空沙盒建造/合作多人，2026-08-06）。
> 生成器：`data/build_content.py` → `data/site.json` → `node scripts/generate.js` → `public/`（零依赖纯静态）。

## 快速开始
```bash
cd sites/approximately-up
python3 data/build_content.py   # 从 14 语言内容重建 site.json（幂等，含 SEO 长度后处理）
node scripts/generate.js        # 生成 public/
node packages/site-kit/audit.js sites/approximately-up   # G4 审计
```

## 事实来源
`docs/approximately-up-research.md`（项目级知识库，唯一事实来源，L0 分级）
