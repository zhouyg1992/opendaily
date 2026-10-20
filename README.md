<div align="center">
  <img src="assets/logo.svg?v=2" alt="OpenDaily" width="300">
  <br><br>
  <p>每天 10 个值得一看的开源项目，给正在找方向的人一点灵感。<br>
  项目来自 GitHub 热榜、新项目搜索和 Hacker News，每期写清楚可以怎么借、从哪切入。</p>
  <br>
  <p><a href="daily/"><strong>→ 全部日报</strong></a></p>
  <p><a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a></p>
</div>

---

<!-- DIGEST:START -->
## [2026.10.20 · 周二](daily/2026-10-20.md)

> 今天的项目有个共同信号：过去只有大公司用得起的专业能力——代码理解、金融建模、PDF 编辑、无线安全审计——正被做成能本地运行、能嵌进工作流的开源工具。机会未必在再做一个模型，而在把能力包装成垂直场景里开箱即用的产品。

> 10 个项目 · 7 个方向 · 当日新增 4.3k stars

### AI / Agent 工具

* **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** — 把代码库、文档、SQL schema、配置和 PDF 一起解析成可查询的知识图谱，让人或 Agent 都能顺着关系检索跨文件上下文。

  `Python` · ★ 129k · 当日 +751

  > 灵感：把「读懂遗留系统」做成迁移、审计场景的代码知识图谱服务，先切咨询和外包团队。

* **[stablyai/orca](https://github.com/stablyai/orca)** — 多 Agent 工作台：把 Claude Code、Grok Bot 等编码 Agent 放进同一处并行调度，复用自己已有的订阅额度，不必为每个 Agent 单独买 API。

  `TypeScript` · ★ 99k · 当日 +1.6k

  > 灵感：Agent 工作台的机会不在再做一个 Agent，而在团队协作、成本控制和操作审计。

* **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** — 给 AI 编程 Agent 立规矩：能不加的代码就不加，先想清楚再动手，像资深工程师一样主动拒绝过度设计，专治越改越复杂。

  `JavaScript` · ★ 168k · 当日 +1k

  > 灵感：把「让 Agent 少写代码」沉淀成团队规范插件，按仓库订阅，卖的是代码质量。

### AI 基础设施 / 模型

* **[shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)** — 首个面向金融 K 线序列的开源基础模型，在 45 个以上全球交易所的数据上预训练，采用 decoder-only 架构，论文已被 AAAI 2026 接收。提供微调脚本，可迁移到自己的行情预测任务。

  `Python` · ★ 42k · 当日 +363

  > 灵感：金融时序基础模型可切量化投研 SaaS，或给券商做私有化微调，数据与合规是壁垒。

### 开发工具 / CLI

* **[storytold/pdfcraft](https://github.com/storytold/pdfcraft)** — 同为纯 Rust 实现的 PDF 阅读与编辑工作台，可阅读、整理、合并、拆分和加密 PDF，覆盖 macOS、Windows、Linux、FreeBSD 及网页端。原生应用启动快，适合替换笨重的商业 PDF 套件。

  `Rust` · ★ 16k

  > 灵感：本地 PDF 工作台可以切合同、病历、标书这类隐私敏感场景，做批注与 OCR 工作流。

### 前端 / 设计

* **[thesysdev/openui](https://github.com/thesysdev/openui)** — 生成式 UI 的开放标准与全栈框架，围绕一套紧凑的流式语言设计，核心与框架无关，官方提供 React、Vue、Svelte、Angular 运行时。相比让模型直接吐 JSON，官方测得 token 用量最多减少约三分之二。

  `TypeScript` · ★ 12k · 当日 +401

  > 灵感：生成式 UI 有机会成为 AI 应用的前端协议层，先切客服、报表和内部工具。

### 数据 / 基础设施

* **[bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view)** — 浏览器里的「间谍卫星」模拟器，在写实 3D 地球上叠加实时飞机、船舶、卫星、地震与公开摄像头数据，数据源全部公开可查。无需 API key 即可启动，是理解开源地理空间情报能力的直观入口。

  `JavaScript` · ★ 58k

  > 灵感：把公开地理数据做成记者、风控、保险用的实时情报面板，比通用地图更垂直。

### 安全 / 隐私

* **[martin-olivier/airgorah](https://github.com/martin-olivier/airgorah)** — 基于 Rust 与 GTK4 的 WiFi 安全审计工具，可抓取周边无线流量、发现接入点下的客户端、执行去认证攻击并捕获握手包与 PMKID，进而尝试破解口令。图形界面降低了 aircrack 系列工具的使用门槛。

  `Rust` · ★ 4.5k · 当日 +135

  > 灵感：把 WiFi 安全自查做成面向中小企业的订阅服务或硬件盒子，替代昂贵的渗透测试。

* **[Automattic/harper](https://github.com/Automattic/harper)** — 离线运行的英文语法检查器，用 Rust 编写并通过 WebAssembly 接入浏览器扩展与 Node 环境。所有文本留在本地，不经过服务器，主打低延迟与隐私，是 Grammarly 的自托管替代思路。

  `Rust` · ★ 17k · 当日 +72

  > 灵感：离线语法检查适合嵌进 IDE、邮件客户端和写作工具，按 SDK/API 收费，隐私是差异点。

### Skill / 垂直工具

* **[storytold/photocraft](https://github.com/storytold/photocraft)** — 用纯 Rust 从零重写的开源图片编辑器，目标对齐 Photoshop：图层、蒙版、调整层、PSD 读写都在，且不依赖 Electron，离线可用。

  `Rust` · ★ 69k

  > 灵感：本地专业修图仍有空位：切电商批量修图，或医疗、设计等不能上云的素材工作流。

[本期 Markdown](daily/2026-10-20.md)

### 往期

#### 2026 年

**10 月**：[20](daily/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
