# OpenDaily · 每天 10 个开源项目，找点灵感

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

给想创业但还没找到方向的人，也给每天关注开源社区的人：**每天 10 个**值得一看的开源项目，来自 GitHub 热榜、新项目搜索和 Hacker News。每期还会写清楚可以怎么借、从哪切入。

**[全部日报](daily/)**

<!-- DIGEST:START -->
## 最新一期

**[2026.10.20 · 周二](daily/2026-10-20.md)** — 今天的项目有个共同信号：过去只有大公司用得起的专业能力——代码理解、金融建模、PDF 编辑、无线安全审计——正被做成能本地运行、能嵌进工作流的开源工具。机会未必在再做一个模型，而在把能力包装成垂直场景里开箱即用的产品。

1. **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** — 把代码库、文档、SQL schema、配置和 PDF 一起解析成可查询的知识图谱，让人或 Agent 都能顺着关系检索跨文件上下文。
2. **[stablyai/orca](https://github.com/stablyai/orca)** — 多 Agent 工作台：把 Claude Code、Grok Bot 等编码 Agent 放进同一处并行调度，复用自己已有的订阅额度，不必为每个 Agent 单独买 API。
3. **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** — 给 AI 编程 Agent 立规矩：能不加的代码就不加，先想清楚再动手，像资深工程师一样主动拒绝过度设计，专治越改越复杂。
4. **[shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)** — 首个面向金融 K 线序列的开源基础模型，在 45 个以上全球交易所的数据上预训练，采用 decoder-only 架构，论文已被 AAAI 2026 接收。提供微调脚本，可迁移到自己的行情预测任务。
5. **[storytold/pdfcraft](https://github.com/storytold/pdfcraft)** — 同为纯 Rust 实现的 PDF 阅读与编辑工作台，可阅读、整理、合并、拆分和加密 PDF，覆盖 macOS、Windows、Linux、FreeBSD 及网页端。原生应用启动快，适合替换笨重的商业 PDF 套件。
6. **[thesysdev/openui](https://github.com/thesysdev/openui)** — 生成式 UI 的开放标准与全栈框架，围绕一套紧凑的流式语言设计，核心与框架无关，官方提供 React、Vue、Svelte、Angular 运行时。相比让模型直接吐 JSON，官方测得 token 用量最多减少约三分之二。
7. **[bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view)** — 浏览器里的「间谍卫星」模拟器，在写实 3D 地球上叠加实时飞机、船舶、卫星、地震与公开摄像头数据，数据源全部公开可查。无需 API key 即可启动，是理解开源地理空间情报能力的直观入口。
8. **[martin-olivier/airgorah](https://github.com/martin-olivier/airgorah)** — 基于 Rust 与 GTK4 的 WiFi 安全审计工具，可抓取周边无线流量、发现接入点下的客户端、执行去认证攻击并捕获握手包与 PMKID，进而尝试破解口令。图形界面降低了 aircrack 系列工具的使用门槛。
9. **[Automattic/harper](https://github.com/Automattic/harper)** — 离线运行的英文语法检查器，用 Rust 编写并通过 WebAssembly 接入浏览器扩展与 Node 环境。所有文本留在本地，不经过服务器，主打低延迟与隐私，是 Grammarly 的自托管替代思路。
10. **[storytold/photocraft](https://github.com/storytold/photocraft)** — 用纯 Rust 从零重写的开源图片编辑器，目标对齐 Photoshop：图层、蒙版、调整层、PSD 读写都在，且不依赖 Electron，离线可用。

[阅读完整日报（含 10 条灵感）→](daily/2026-10-20.md)

<!-- DIGEST:END -->

MIT License · 由 GitHub Actions 每天自动更新 · [开发说明](DEVELOPMENT.md)
