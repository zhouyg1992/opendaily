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
## [2026.11.19 · 周四](daily/zh/2026-11-19.md)

> 今天这批项目透露出一个明显信号：围绕编码 agent 的控制层和交互协议正在快速成型，同时轻量化本地基础设施（容器运行时、小模型训练、Docker 管理面板）重新受到关注。开发者不再满足于单个 agent 能力，而是想把它接入自己的工作流和设备，这为做中间层和垂直场景的人留出了空间。

### AI / Agent 工具

* **[pingdotgg/t3code](https://github.com/pingdotgg/t3code)** — T3 Code 是编码 agent 的开源控制平面，agent 跑在你自己的机器上，桌面、网页、手机都能接管同一个会话，支持 Claude Code、Codex 等多家 agent。它不转售 token，直接驱动你已订阅的账号。

  > 灵感：机会在「多 agent 编排 + 移动端审批」这个缝隙：面向重度使用多个编码 agent 的个人开发者，先做会话交接和权限审批的体验，而不是再做一个 agent。

### AI 基础设施 / 模型

* **[ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui)** — AG-UI 是一个事件驱动的开放协议，把 agent 的流式输出、工具调用、状态更新、人工介入统一成一条双向事件流，让任意框架的 agent 都能接入任意前端。1.0 版本刚发布。

  > 灵感：适合作为基础设施押注：做 agent 前端组件库或调试工具，切「同一 agent 多端渲染」的场景，比各家自己写胶水代码省事得多。

* **[jingyaogong/minimind](https://github.com/jingyaogong/minimind)** — MiniMind 用约 3 元成本和 2 小时在单张 3090 上从零训练一个 64M 小模型，并开源了预训练、SFT、LoRA、RLHF、Agentic RL 等全链路 PyTorch 原生代码，同时扩展到视觉和多模态。

  > 灵感：它的价值是教学与实验底座：可以做面向高校或转行者的付费实验课，或基于它做特定领域的极小模型微调服务，卖的是可复现而不是算力。

* **[vllm-project/vllm-ascend](https://github.com/vllm-project/vllm-ascend)** — vllm-ascend 是社区维护的 vLLM 华为昇腾硬件插件，让 vLLM 的推理服务能跑在昇腾 NPU 上，已发布多个正式版本并保持周会节奏。对受限于 GPU 供应的团队是现实选项。

  > 灵感：这是基础设施信号而非创业点子：围绕昇腾做模型适配、性能调优和迁移咨询，服务那些拿不到英伟达卡但要做推理部署的企业。

### 开发工具 / CLI

* **[getarcaneapp/arcane](https://github.com/getarcaneapp/arcane)** — Arcane 是面向普通用户的现代 Docker 管理面板，用 Go 和 SvelteKit 写成，可自托管，覆盖容器和 Compose 的日常操作。v3 正在主分支开发，社区功能请求已迁到 Discussions。

  > 灵感：自托管面板的差异点在「给非运维的人用」：面向家庭服务器或小团队，把备份、更新、告警做成向导式流程，而不是再堆一层仪表盘。

* **[XiaoYouChR/Ghost-Downloader-3](https://github.com/XiaoYouChR/Ghost-Downloader-3)** — Ghost Downloader 3 是一个跨平台下载器，支持 HTTP3、BT、FTP，用异步架构和 Fluent Design 界面，主打把多种下载协议收进一个工具。适合需要批量或跨区域下载的个人用户。

  > 灵感：下载器的机会在「带策略的批量抓取」：面向做数据采集或内容归档的小团队，把代理轮换、断点续传和任务编排做成可编程接口。

### 前端 / 设计

* **[dream-num/univer](https://github.com/dream-num/univer)** — Univer 把表格、文档、幻灯片等办公编辑能力做成可嵌入的 SDK，开源核心可扩展，并提供了让应用和 agent 操作可编辑内容的 Facade 接口。适合想把办公套件塞进自己产品的团队。

  > 灵感：切入点是把「AI 可编辑的表格」嵌进垂直 SaaS，比如财务或供应链工具，让 agent 直接改单元格而不是输出文本，差异化在可撤销的协作编辑。

### 数据 / 基础设施

* **[libracoder/kiri](https://github.com/libracoder/kiri)** — Kiri 是用 Rust 写的轻量容器运行时，兼容 Docker CLI、Compose 和 buildx，在 macOS、Windows、Linux 上跑单个小虚拟机，定位是 Docker Desktop 和 OrbStack 的替代品，还带一个免费的 Ngrok 替代。

  > 灵感：适合做开发者本地环境的周边生意：围绕它做镜像缓存、团队共享配置或内网穿透的托管服务，切「不想为 Docker Desktop 付费」的中小团队。

### Skill / 垂直工具

* **[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)** — 一个 agent skill，跨 Reddit、X、YouTube、HN、Polymarket 抓取某个话题近 30 天的讨论，再按点赞和真实资金排序合成摘要。零配置，可装进 Claude Code 等 50 多个 agent 宿主。

  > 灵感：可以借它的「按真实信号排序」思路做垂直情报产品：面向投资或选品的人，把社区热度与预测市场赔率结合成可订阅的周报。

* **[huami1314/GestaltX](https://github.com/huami1314/GestaltX)** — GestaltX 是一个 iOS 的 MobileGestalt 编辑器，可调整区域代码、灵动岛、常亮显示、充电限制等设备预设，并支持备份。面向喜欢折腾 iPhone 和 iPad 的高级用户。

  > 灵感：这类工具本身难产品化，但反映了越狱后市场对「安全回滚」的需求：可以做配置备份、变更对比和恢复的一站式服务，降低折腾门槛。

[本期 Markdown](daily/zh/2026-11-19.md)

### 往期

#### 2026 年

**11 月**：[19](daily/zh/2026-11-19.md) · [12](daily/zh/2026-11-12.md) · [11](daily/zh/2026-11-11.md) · [10](daily/zh/2026-11-10.md) · [9](daily/zh/2026-11-09.md) · [8](daily/zh/2026-11-08.md) · [7](daily/zh/2026-11-07.md) · [6](daily/zh/2026-11-06.md) · [5](daily/zh/2026-11-05.md) · [4](daily/zh/2026-11-04.md) · [3](daily/zh/2026-11-03.md) · [2](daily/zh/2026-11-02.md) · [1](daily/zh/2026-11-01.md)

**10 月**：[31](daily/zh/2026-10-31.md) · [30](daily/zh/2026-10-30.md) · [29](daily/zh/2026-10-29.md) · [28](daily/zh/2026-10-28.md) · [27](daily/zh/2026-10-27.md) · [26](daily/zh/2026-10-26.md) · [25](daily/zh/2026-10-25.md) · [24](daily/zh/2026-10-24.md) · [23](daily/zh/2026-10-23.md) · [22](daily/zh/2026-10-22.md) · [21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
