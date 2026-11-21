<div align="center">
  <img src="assets/logo.svg?v=3" alt="OpenDaily" width="300">
  <br>
  <p>每天 10 个值得一看的开源项目，给正在找方向的人一点灵感。<br>
  项目来自 GitHub 热榜、新项目搜索和 Hacker News，每期写清楚可以怎么借、从哪切入。</p>
  <p><a href="daily/zh/"><strong>全部日报→</strong></a></p>
  <p><a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a></p>
  <p><a href="README.en.md">English</a></p>
</div>

---

<!-- DIGEST:START -->
## [2026.11.21 · 周六](daily/zh/2026-11-21.md)

> 今天这批项目透露出一个明确信号：AI 工具正从「能演示」转向「能交付」。编码代理要有审批和 SOP，视频剪辑要有成片和发布文案，CI 故障要直接给出修复，连合规检查都被做成可执行的 guard。机会不在再造一个模型，而在把模型嵌进真实工作流的卡点里，把一次性能力变成可复用、可审计的流程。

### AI / Agent 工具

* **[Tencent/LoopForge](https://github.com/Tencent/LoopForge)** — 腾讯开源的编码代理自托管编排工作台：在聊天里描述需求，主 Bot 开 Docker 沙箱、拉仓库、分派角色并提 PR，跑通的流程可固化为带人工审批的 SOP。解决的是团队用多个编码代理时流程不可复现的问题。

  > 灵感：面向已有 5 人以上研发团队、想统一代理交付规范的场景。切「代理产出没人敢合并」这一痛点，与只做单机代理的 Cursor 类工具差在审批门和可复用 SOP。

### AI 基础设施 / 模型

* **[Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre)** — 面向 CI/CD 可靠性的开源 CLI 代理：读取失败的流水线运行，追到根因并把修复推到待审状态，可自托管、用自己的模型。CI 只告诉你挂了，它补上「为什么」和「怎么修」。

  > 灵感：适合已有 Datadog、Grafana 告警体系但排障靠人的团队。切「告警到修复」的最后一公里，与纯观测平台差在直接产出可审的补丁而非又一块仪表盘。

* **[microsoft/markitdown](https://github.com/microsoft/markitdown)** — 微软的轻量 Python 工具，把 Office 文档、PDF 等各类文件转成 Markdown，供 LLM 和文本分析流水线使用。属于文档进模型前的标准预处理层，稳定且被大量框架引用。

  > 灵感：更适合作为基础设施而非独立产品。可借的是「文档到 token」这一环的可靠性，在 RAG 或代理管道里做格式归一化，注意不可信输入下的权限与消毒问题。

* **[janhq/jan](https://github.com/janhq/jan)** — 开源的 ChatGPT 替代品，完全离线在本地电脑运行大模型，基于 Tauri 构建，跨平台下载即用。解决的是对数据外流敏感、又想要开箱即用体验的用户需求。

  > 灵感：面向律师、医疗、企业内部等不能把数据发出去的场景。与 Ollama 加前端拼装相比差在产品化程度，机会在垂直行业的本地模型分发与策略管理。

### 开发工具 / CLI

* **[erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)** — 把现有应用逐块重写成 Rust，每一步都用原程序录制的行为做对照验证，支持 TypeScript、Python、C、Go、Ruby、Java 写的 CLI、HTTP 服务和库。它不翻译代码，而是证明重写后行为一致。

  > 灵感：面向维护老旧服务、想迁 Rust 又怕回归的团队。切「不敢动」的心理门槛，与逐行翻译工具差在以行为录制作为验收标准，可接进代理工作流。

* **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** — 预索引的代码知识图谱，代码变更时自动同步，供 Claude Code、Codex、Cursor、Copilot 等编码代理使用，减少 token 和工具调用，完全本地运行，内核用 Rust。

  > 灵感：适合重度使用编码代理、被上下文窗口和调用成本卡住的团队。切「代理找代码靠猜」的问题，与向量检索式代码搜索差在结构化图谱和增量同步。

### 前端 / 设计

* **[google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)** — Google Stitch 的代理技能与插件库，遵循 Agent Skills 开放标准，可装进 Codex、Gemini CLI、Claude Code、Cursor 等编码代理，让代理按设计规范生成界面。

  > 灵感：面向想把设计到代码环节标准化的前端团队。切「代理生成的 UI 风格漂移」问题，与通用提示词差在技能包可版本化、可跨代理复用。

### Skill / 垂直工具

* **[zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip)** — 开源 AI 视频剪辑桌面工具，贴一个链接就能把播客、访谈、课程剪成适配抖音、小红书、TikTok 的竖版短视频，同时生成字幕、封面和发布文案。本地渲染，云端模型按量计费。

  > 灵感：面向做内容分发的个人和小团队，切「长内容转多平台短内容」的重复劳动。与剪映等通用剪辑器差在从链接到成片的端到端，而非手工时间线。

* **[mjmirza/app-store-compliance](https://github.com/mjmirza/app-store-compliance)** — 把 App Store 和 Google Play 的拒审原因整理成开放手册和提交前守卫：117 条已记录的拒审模式与修法、隐私清单和 Data safety 检查、95 个监管截止日期，还附带给编码代理用的 skill。

  > 灵感：面向独立开发者和外包团队，切「上架前夜被拒」的焦虑。与通用清单博客差在可自动执行，能直接挂进 CI 或代理工作流做提交前拦截。

* **[putyy/res-downloader](https://github.com/putyy/res-downloader)** — 基于 Go 和 Wails 的跨平台资源下载器，支持视频号、小程序、抖音、快手、小红书、直播流、m3u8 等资源嗅探与下载，支持代理抓包。作者已说明维护时间有限。

  > 灵感：面向做素材收集和竞品研究的内容团队。切「多平台资源分散」的整理需求，但要注意平台条款与版权边界，更适合做内部工具而非公开产品。

[本期 Markdown](daily/zh/2026-11-21.md)

### 往期

#### 2026 年

**11 月**：[21](daily/zh/2026-11-21.md) · [20](daily/zh/2026-11-20.md) · [19](daily/zh/2026-11-19.md) · [12](daily/zh/2026-11-12.md) · [11](daily/zh/2026-11-11.md) · [10](daily/zh/2026-11-10.md) · [9](daily/zh/2026-11-09.md) · [8](daily/zh/2026-11-08.md) · [7](daily/zh/2026-11-07.md) · [6](daily/zh/2026-11-06.md) · [5](daily/zh/2026-11-05.md) · [4](daily/zh/2026-11-04.md) · [3](daily/zh/2026-11-03.md) · [2](daily/zh/2026-11-02.md) · [1](daily/zh/2026-11-01.md)

**10 月**：[31](daily/zh/2026-10-31.md) · [30](daily/zh/2026-10-30.md) · [29](daily/zh/2026-10-29.md) · [28](daily/zh/2026-10-28.md) · [27](daily/zh/2026-10-27.md) · [26](daily/zh/2026-10-26.md) · [25](daily/zh/2026-10-25.md) · [24](daily/zh/2026-10-24.md) · [23](daily/zh/2026-10-23.md) · [22](daily/zh/2026-10-22.md) · [21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
