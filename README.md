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
## [2026.11.22 · 周日](daily/zh/2026-11-22.md)

> 今天这批项目透露出一个清晰信号：AI 正在从「能跑起来」转向「跑得省、跑得稳、跑得像人做的」。一边是本地推理和量化压缩把大模型塞进普通显卡，一边是账号调度、界面去 AI 味、爬虫与数据引擎这类「让 AI 产品真正可用」的脏活累活开始被认真对待。创业机会不在再做一个 agent 框架，而在这些缝隙里。

### AI / Agent 工具

* **[odysseus-dev/odysseus](https://github.com/odysseus-dev/odysseus)** — 自托管的 AI 工作台，把聊天、agent、研究、文档、邮件、笔记、日历和本地模型串在一个容器化部署里。面向在意数据不出内网、又不想自己拼装一堆开源组件的团队。

  > 灵感：适合做「私有化 AI 办公套件」的交付层：帮中小企业一键部署、接内部知识库和邮件，收费在部署与运维，而不是重写底层。

* **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** — 一个长周期超级 agent 框架，用沙箱、记忆、工具、技能和子 agent 编排需要几分钟到几小时的任务，2.0 是彻底重写。它代表的是「agent 跑长任务」这一形态正在工程化。

  > 灵感：作为基础设施看更合适：与其再做一个通用 agent，不如基于它的沙箱与子 agent 机制，切一个长流程垂直任务，比如竞品调研报告或合规材料整理。

### AI 基础设施 / 模型

* **[FlashML-org/FreeVideo](https://github.com/FlashML-org/FreeVideo)** — 把 MiniMax H3 视频生成模型压到 8GB 显存、16GB 内存就能在本机跑，并按硬件自动选择加速路径。对没有云 GPU 预算、又想做视频生成的个人和小团队来说，这是把门槛从租卡降到用自己电脑。

  > 灵感：切入点不是做另一个视频工具，而是围绕「低配本地视频生成」做工作流封装：批量出片、素材替换、固定风格模板，卖给电商短视频和小型内容工作室。

* **[ShinMegamiBoson/lookatmyquant](https://github.com/ShinMegamiBoson/lookatmyquant)** — 一个量化编译器，按每块权重对输出质量的实际损害来分配编码，在同等文件大小下显著降低 KL 散度。对想在消费级硬件上跑更大模型、又不想明显掉点的人来说，这是压缩策略层面的改进。

  > 灵感：更适合当作技术信号而非产品：关注它能否接入 GGUF 生态和主流推理框架，若能，围绕「同等体积更高质量」做模型分发或端侧部署服务。

### 开发工具 / CLI

* **[lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager)** — 用 Tauri 和 React 写的桌面工具，做 Antigravity 账号多开切换、协议转换和请求调度，本质是一个本地 AI 中转站。反映出多账号、多额度、多模型并存在重度用户里已是常态。

  > 灵感：可借的是「额度与账号编排」这一层：给团队做统一的 AI 服务网关，按成员分配额度、记录用量、自动切换备用账号，而不是让每个人各自折腾。

* **[thedaviddias/Front-End-Checklist](https://github.com/thedaviddias/Front-End-Checklist)** — 把前端最佳实践整理成可执行的检查清单，现在同时面向人和 AI agent，提供网页版、MCP 服务器和 README 三种用法。它回应的是 AI 生成代码越来越多、但质量把关缺标准流程的问题。

  > 灵感：可借的是「把规范变成 agent 可调用的检查器」这一模式：为后端、移动端或无障碍做同类 MCP 检查服务，嵌入代码评审环节收费。

### 前端 / 设计

* **[toeverything/AFFiNE](https://github.com/toeverything/AFFiNE)** — 把文档、白板和表格融合在一个本地优先的知识库里，定位是 Notion 与 Miro 的开源替代，强调隐私和可定制。对不信任云端笔记、又需要团队协作的团队有实际吸引力。

  > 灵感：别做另一个笔记应用。可借的是它的本地优先与 CRDT 架构，去做垂直场景的协作工作台，比如设计评审、教学备课，把同步和离线能力直接复用。

### 数据 / 基础设施

* **[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)** — 面向 AI agent 的网页抓取与结构化提取引擎，把页面转成干净 Markdown 供 RAG 使用，也能直接输出 JSON 或做实时搜索。开源爬虫可自托管，同时提供带免费额度的托管 API，省掉浏览器和代理运维。

  > 灵感：机会在垂直数据管道：针对招聘、房产、电商比价等特定站点做预置抽取模板和增量更新，卖「干净的领域数据集」而不是通用爬虫。

* **[pola-rs/polars](https://github.com/pola-rs/polars)** — Rust 写的分析型查询引擎，DataFrame API 与 SQL 走同一优化器和执行引擎，支持多线程和 out-of-core。当数据量超过 pandas 舒适区、又不想上分布式集群时，它是务实的中间选择。

  > 灵感：机会不在引擎本身，而在其上的托管分析层：面向中小团队做「免运维的列式分析服务」，让业务人员用 SQL 直接查对象存储里的数据。

### Skill / 垂直工具

* **[heydamir/unslop](https://github.com/heydamir/unslop)** — 一个 Claude Code / Codex 技能，专门识别并修掉「AI 味」界面：紫色渐变、发光、emoji 标签、喊话式文案、间距不齐，然后按产品调性逐轮改写。解决的是 vibe coding 产出千篇一律、没法直接上线的问题。

  > 灵感：可以做「设计审查即服务」：把这类规则沉淀成可配置的品牌设计约束，接入 CI 或 PR 流程，卖给用 AI 生成前端但缺设计师的团队。

[本期 Markdown](daily/zh/2026-11-22.md)

### 往期

#### 2026 年

**11 月**：[22](daily/zh/2026-11-22.md) · [21](daily/zh/2026-11-21.md) · [20](daily/zh/2026-11-20.md) · [19](daily/zh/2026-11-19.md) · [12](daily/zh/2026-11-12.md) · [11](daily/zh/2026-11-11.md) · [10](daily/zh/2026-11-10.md) · [9](daily/zh/2026-11-09.md) · [8](daily/zh/2026-11-08.md) · [7](daily/zh/2026-11-07.md) · [6](daily/zh/2026-11-06.md) · [5](daily/zh/2026-11-05.md) · [4](daily/zh/2026-11-04.md) · [3](daily/zh/2026-11-03.md) · [2](daily/zh/2026-11-02.md) · [1](daily/zh/2026-11-01.md)

**10 月**：[31](daily/zh/2026-10-31.md) · [30](daily/zh/2026-10-30.md) · [29](daily/zh/2026-10-29.md) · [28](daily/zh/2026-10-28.md) · [27](daily/zh/2026-10-27.md) · [26](daily/zh/2026-10-26.md) · [25](daily/zh/2026-10-25.md) · [24](daily/zh/2026-10-24.md) · [23](daily/zh/2026-10-23.md) · [22](daily/zh/2026-10-22.md) · [21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
