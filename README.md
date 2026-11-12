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
## [2026.11.12 · 周四](daily/zh/2026-11-12.md)

> 今天这批项目透露出一个明显信号：围绕 AI 编程代理的配套工具正在快速细分，从免费接入多模型、到让代理像同事一样接任务、再到用强模型写计划给弱模型执行，大家不再只卷模型本身，而是卷怎么把代理用得更省、更顺、更可控。

### AI / Agent 工具

* **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** — 把 Claude Code、Codex 等 12 种代理客户端路由到 61 家模型提供商，包括免费和本地模型，保留原生流式与工具调用。解决的是开发者想用熟悉代理界面却受限于单一模型和额度的问题。

  > 灵感：适合做团队内部的模型网关：统一管理密钥、额度和路由策略，按项目切换免费或付费后端。和直接改代理源码相比，胜在不绑定具体客户端。

* **[multica-ai/multica](https://github.com/multica-ai/multica)** — 一个可自托管的工作空间，把 issue 分配给 AI 编码代理，代理会领任务、报进度、提阻塞并交回评审。解决的是多个代理各占一个终端、上下文反复丢失、协作无记录的问题。

  > 灵感：可以切「小团队代理项目看板」场景：把现有 CLI 代理接进看板，让非工程成员也能派活和验收。和纯聊天式代理相比，差在任务状态和交接是可追踪的。

### AI 基础设施 / 模型

* **[sgl-project/sglang-omni](https://github.com/sgl-project/sglang-omni)** — 面向交互式多模态与语音的高性能服务运行时，支持 ASR、音频和音乐生成，提供 OpenAI 兼容 API。解决的是语音和多模态模型上线时缺乏统一推理底座的问题。

  > 灵感：更适合作为基础设施信号：做语音代理的团队可基于它自建推理层，按并发和延迟调优。和通用推理框架相比，差在对音频链路和流式交互的原生支持。

### 开发工具 / CLI

* **[unstablebuild/rune](https://github.com/unstablebuild/rune)** — GPU 加速的 IDE 兼终端复用器，内置语言智能，多实例组成端到端加密网络，可从任意设备连回工作站。解决的是代理自动编程和人工编程割裂、远程开发体验差的问题。

  > 灵感：可面向「一人多机」的独立开发者做远程代理工作台：在笔记本上盯任务，重活跑在台式机。和 VS Code Remote 相比，差在把代理编排和终端复用做进同一层。

* **[anefzaoui/misterdownloadmanager](https://github.com/anefzaoui/misterdownloadmanager)** — 纯 Rust 从零写的开源下载管理器，跨三平台，支持多线程加速、磁力链接和浏览器扩展，无广告无注册。解决的是 IDM 类工具收费、闭源且跨平台支持差的问题。

  > 灵感：可切「团队批量素材下载」场景：把浏览器扩展和 CLI 结合，做可脚本化的下载队列与校验。和 IDM 相比，差在开源可审计、能嵌进自动化流程。

### 前端 / 设计

* **[kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi)** — 本地打开代理生成的 HTML 文件，可点选元素和文本、编辑 Mermaid 白板，并把反馈发回给代理。解决的是人机围绕 HTML 产物协作时只能靠截图和长段文字描述的问题。

  > 灵感：适合做「代理产物的可视化批注层」，面向用代理生成原型或报表的团队：把点选反馈变成结构化指令。和聊天里描述修改相比，差在保留 HTML 的交互性。

### 数据 / 基础设施

* **[LibreSpark/LibreTV](https://github.com/LibreSpark/LibreTV)** — 基于 Next.js 的影视聚合搜索与播放站，支持多采集源并行搜索、HLS 播放、IPTV 和进度同步，可 Docker 一键部署。解决的是自建影视站门槛高、源管理混乱的问题。

  > 灵感：可切「家庭媒体中心或垂直片库」场景，重点做源健康度管理和合规内容接入，而非公开聚合。和现成 CMS 相比，差在跨源聚合与自动换源测速。

### 安全 / 隐私

* **[soxoj/maigret](https://github.com/soxoj/maigret)** — 仅凭用户名在数千个网站收集账号线索并汇总成人物档案，无需 API key。解决的是调查、尽职调查和反欺诈中跨平台身份拼图耗时的问题。

  > 灵感：可切「招聘背调或品牌侵权初筛」场景，把结果做成可导出报告，并加置信度和误报标注。和手工逐站搜索相比，差在批量与可复现。

* **[openai/codex-security](https://github.com/openai/codex-security)** — OpenAI 的代码安全 CLI 与 TypeScript SDK，能扫描仓库、验证候选漏洞、生成补丁并校验修复，还能起草 SECURITY.md。解决的是 AI 生成代码增多后安全审查跟不上的问题。

  > 灵感：适合接进 CI 做「变更级安全门禁」，只扫 Git diff 并自动开修复 PR，面向没有专职安全的小团队。和传统 SAST 相比，差在会验证和修补而非只报错。

### Skill / 垂直工具

* **[shadcn/improve](https://github.com/shadcn/improve)** — 一个代理技能，用最强模型审计代码库并写出实施计划，再交给更便宜的模型执行，自身不写实现。解决的是高能力模型贵、低能力模型乱改的错配问题。

  > 灵感：适合包装成「代码库体检+分阶段改造计划」服务，面向维护老项目的团队：先出可评审的 markdown 计划，再按预算分批执行。和直接让代理改代码相比，风险前置。

[本期 Markdown](daily/zh/2026-11-12.md)

### 往期

#### 2026 年

**11 月**：[12](daily/zh/2026-11-12.md) · [11](daily/zh/2026-11-11.md) · [10](daily/zh/2026-11-10.md) · [9](daily/zh/2026-11-09.md) · [8](daily/zh/2026-11-08.md) · [7](daily/zh/2026-11-07.md) · [6](daily/zh/2026-11-06.md) · [5](daily/zh/2026-11-05.md) · [4](daily/zh/2026-11-04.md) · [3](daily/zh/2026-11-03.md) · [2](daily/zh/2026-11-02.md) · [1](daily/zh/2026-11-01.md)

**10 月**：[31](daily/zh/2026-10-31.md) · [30](daily/zh/2026-10-30.md) · [29](daily/zh/2026-10-29.md) · [28](daily/zh/2026-10-28.md) · [27](daily/zh/2026-10-27.md) · [26](daily/zh/2026-10-26.md) · [25](daily/zh/2026-10-25.md) · [24](daily/zh/2026-10-24.md) · [23](daily/zh/2026-10-23.md) · [22](daily/zh/2026-10-22.md) · [21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
