# OpenDaily · 每天 10 个开源项目，找点灵感

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

给想创业但还没找到方向的人，也给每天关注开源社区的人：**每天 10 个**值得一看的开源项目，来自 GitHub 热榜、新项目搜索和 Hacker News。

每期不只告诉你「它是什么」，还会写清楚它解决了谁的问题、为什么现在值得看，以及可能从哪切入——或者它为什么只是一个值得留意的信号。

**[全部日报](daily/)**

<!-- DIGEST:START -->
## 最新一期

**[2026.10.20 · 周二](daily/2026-10-20.md)** — 今天的项目有个共同信号：过去只有大公司用得起的专业能力——代码理解、金融建模、PDF 编辑、无线安全审计——正被做成能本地运行、能嵌进工作流的开源工具。机会未必在再做一个模型，而在把能力包装成垂直场景里开箱即用的产品。

### AI / Agent 工具

- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** — 把代码库、文档、SQL schema、配置和 PDF 一起解析成可查询的知识图谱，让人或 Agent 都能顺着关系检索跨文件上下文。
  > 灵感：把「读懂遗留系统」做成迁移、审计场景的代码知识图谱服务，先切咨询和外包团队。
- **[stablyai/orca](https://github.com/stablyai/orca)** — 多 Agent 工作台：把 Claude Code、Grok Bot 等编码 Agent 放进同一处并行调度，复用自己已有的订阅额度，不必为每个 Agent 单独买 API。
  > 灵感：Agent 工作台的机会不在再做一个 Agent，而在团队协作、成本控制和操作审计。
- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** — 给 AI 编程 Agent 立规矩：能不加的代码就不加，先想清楚再动手，像资深工程师一样主动拒绝过度设计，专治越改越复杂。
  > 灵感：把「让 Agent 少写代码」沉淀成团队规范插件，按仓库订阅，卖的是代码质量。

### AI 基础设施 / 模型

- **[shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)** — 首个面向金融 K 线序列的开源基础模型，在 45 个以上全球交易所的数据上预训练，采用 decoder-only 架构，论文已被 AAAI 2026 接收。提供微调脚本，可迁移到自己的行情预测任务。
  > 灵感：金融时序基础模型可切量化投研 SaaS，或给券商做私有化微调，数据与合规是壁垒。

### 开发工具 / CLI

- **[storytold/pdfcraft](https://github.com/storytold/pdfcraft)** — 同为纯 Rust 实现的 PDF 阅读与编辑工作台，可阅读、整理、合并、拆分和加密 PDF，覆盖 macOS、Windows、Linux、FreeBSD 及网页端。原生应用启动快，适合替换笨重的商业 PDF 套件。
  > 灵感：本地 PDF 工作台可以切合同、病历、标书这类隐私敏感场景，做批注与 OCR 工作流。

### 前端 / 设计

- **[thesysdev/openui](https://github.com/thesysdev/openui)** — 生成式 UI 的开放标准与全栈框架，围绕一套紧凑的流式语言设计，核心与框架无关，官方提供 React、Vue、Svelte、Angular 运行时。相比让模型直接吐 JSON，官方测得 token 用量最多减少约三分之二。
  > 灵感：生成式 UI 有机会成为 AI 应用的前端协议层，先切客服、报表和内部工具。

### 数据 / 基础设施

- **[bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view)** — 浏览器里的「间谍卫星」模拟器，在写实 3D 地球上叠加实时飞机、船舶、卫星、地震与公开摄像头数据，数据源全部公开可查。无需 API key 即可启动，是理解开源地理空间情报能力的直观入口。
  > 灵感：把公开地理数据做成记者、风控、保险用的实时情报面板，比通用地图更垂直。

### 安全 / 隐私

- **[martin-olivier/airgorah](https://github.com/martin-olivier/airgorah)** — 基于 Rust 与 GTK4 的 WiFi 安全审计工具，可抓取周边无线流量、发现接入点下的客户端、执行去认证攻击并捕获握手包与 PMKID，进而尝试破解口令。图形界面降低了 aircrack 系列工具的使用门槛。
  > 灵感：把 WiFi 安全自查做成面向中小企业的订阅服务或硬件盒子，替代昂贵的渗透测试。
- **[Automattic/harper](https://github.com/Automattic/harper)** — 离线运行的英文语法检查器，用 Rust 编写并通过 WebAssembly 接入浏览器扩展与 Node 环境。所有文本留在本地，不经过服务器，主打低延迟与隐私，是 Grammarly 的自托管替代思路。
  > 灵感：离线语法检查适合嵌进 IDE、邮件客户端和写作工具，按 SDK/API 收费，隐私是差异点。

### Skill / 垂直工具

- **[storytold/photocraft](https://github.com/storytold/photocraft)** — 用纯 Rust 从零重写的开源图片编辑器，目标对齐 Photoshop：图层、蒙版、调整层、PSD 读写都在，且不依赖 Electron，离线可用。
  > 灵感：本地专业修图仍有空位：切电商批量修图，或医疗、设计等不能上云的素材工作流。

[全部日报](daily/) · [本期 Markdown](daily/2026-10-20.md)

### 最近更新

| 日期 | 项目数 | 导读 |
| --- | --- | --- |
| [2026-10-20](daily/2026-10-20.md) | 10 | 今天的项目有个共同信号：过去只有大公司用得起的专业能力——代码理解、金融建模、PDF 编辑、无线安全审计——正被做成能本地运行、能嵌进工作流的开源工具。机会未必在再做一个模型，而在把能力包装成垂直场景里开箱即用的产品。 |

<!-- DIGEST:END -->

## 为什么是开源项目

开源社区是最早暴露真实需求的地方：有人已经在用代码解决某个问题，star 和讨论量是需求信号，缺口往往藏在「为什么还没有人把它做成产品」里。每天看 10 个，比刷一周资讯更容易撞见可做的事。

## 适合谁

- **想创业但还没找到方向**：从真实需求和技术变化里找切口，而不是凭空想点子。
- **关注开源社区**：每天 5 分钟，知道今天什么在冒头。
- **做产品、投资或技术选型**：看趋势，也看有哪些能力可以直接复用。

## 每期有什么

- 10 个项目，按方向分组
- 一句话说清它做什么、解决谁的问题
- 一条「灵感」：可以怎么借、切哪个场景，或者它为什么是个信号
- star 数和当日新增，帮你判断热度

## 它是怎么工作的

1. **收集候选**：抓取 GitHub Trending（总榜 + 6 个语言分榜）、GitHub Search（最近 30 天 / 180 天冒头的新项目、`ai-agents` 话题）和 Hacker News 上被讨论的 GitHub 仓库，合并去重。
2. **过滤与打分**：丢掉 awesome-list、教程、面试题、长期不更新的仓库，以及近 60 天已经推荐过的项目；按 star 数、当日新增 star、HN 热度、项目年龄做初排。
3. **补全信息**：按方向均衡挑出 24 个候选（避免清一色 Agent 框架），拉取仓库元数据和 README 摘要作为判断依据。
4. **精选与写作**：调用 LLM（默认 DeepSeek，任意 OpenAI 兼容接口均可），从候选池里挑 10 个，按方向归类，同时写清「是什么」和「可以怎么借」；没有配置 Key 时退回启发式榜单，仍然会生成文件。
5. **写入仓库**：每天新增一份 `daily/YYYY-MM-DD.md`，同时更新 README 的「最新一期 / 最近更新」，由 GitHub Actions 自动提交。

整个流水线只依赖 Python 标准库，不需要 `pip install`。

## 本地运行

```bash
# 生成今天的日报（需要能访问 GitHub；未配置 token 时受 60 次/小时限流）
python3 scripts/main.py

# 生成指定日期
python3 scripts/main.py --date 2026-10-20

# 只根据已保存的数据重新生成 md 和 README
python3 scripts/main.py --rebuild
```

想生成中文导读，先导出 Key：

```bash
export LLM_API_KEY="sk-..."
# 可选：切换模型服务
export LLM_BASE_URL="https://api.deepseek.com/v1"
export LLM_MODEL="deepseek-chat"
python3 scripts/main.py --date 2026-10-20 --force
```

## 每天自动更新

仓库已经包含 `.github/workflows/daily.yml`：

- 每天 `23:00 UTC`（北京时间次日 07:00）运行，也可以在 Actions 页面手动触发；
- 自动提交 `daily/`、`data/` 和 README；README 里 `<!-- DIGEST:START -->` 到 `<!-- DIGEST:END -->` 之间的内容由脚本维护，不要手改；
- 手动触发时可以指定日期、强制重跑，或只重建 md。

启用步骤：

1. 把代码推到 GitHub。
2. 在 **Settings → Secrets and variables → Actions** 添加 `LLM_API_KEY`（不配也能跑，但摘要会保留英文简介）。可选添加 Variables：`LLM_BASE_URL`、`LLM_MODEL`。
3. 在 **Actions** 里手动跑一次 `Daily Digest`，确认能提交。

不需要 GitHub Pages，也不需要 GH_PAT。

## 改哪里

- `config.json`：每天数量、冷却天数、数据源开关、排除规则、分类、LLM 参数。
- `scripts/sources.py`：抓取与解析。
- `scripts/curate.py`：过滤、打分、LLM 提示词与校验。
- `scripts/render.py`：Markdown 与 README 输出。
- `data/seen.json`：已推荐项目记录，用来避免短期重复。
- `data/digests/YYYY-MM-DD.json`：每期的结构化数据，`--rebuild` 由它重新生成 md。
- `data/overrides/YYYY-MM-DD.json`：人工校对入口，可覆盖某天的导读、分类、摘要和灵感；`daily/` 下的文件是生成物，直接改会被下次重建覆盖。

## 目录

```
.github/workflows/daily.yml   每日定时任务
config.json                   全部可调参数
scripts/                      抓取 → 精选 → 生成 Markdown
daily/YYYY-MM-DD.md           每天一份日报
data/digests/                 每期 JSON 数据
data/seen.json                推荐历史（去重）
```

## License

本项目（代码与日报内容）采用 [MIT License](LICENSE) 开源，Copyright (c) 2026 zhouyg1992。

日报中提到的第三方开源项目，其版权与许可证归各自作者所有。
