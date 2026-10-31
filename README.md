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
## [2026.10.31 · 周六](daily/zh/2026-10-31.md)

> 今天这批项目共同指向一件事：AI 正在从「会聊天」转向「能干活」，而围绕它的配套正在快速分层——有人做更轻的浏览器底座，有人做可审计的桌面同事，有人把工程经验固化成可复用的技能包。创业机会不在再做一个模型，而在这些层之间的缝隙里。

### AI / Agent 工具

* **[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)** — 开源的 AI 同事框架，每个代理分到独立浏览器、文件和授权工具，动作执行前先决策、执行后留记录。可接入任意 AG-UI 代理，跑在自己的基础设施上，形态对标 ChatGPT 但完全可改。

  > 灵感：企业最怕代理乱点按钮。它的「先决策后记录」正好切合规敏感行业，比如财务对账、客服工单处理，卖点不是能力而是可审计。

* **[Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas)** — 本地优先的多代理桌面应用，由一个指挥官把目标拆成待办，调度十六个内置专家代理，并接入 Claude Code、Codex 等已有编码代理。项目保存目标、规则、记忆和文件，跨会话延续上下文。

  > 灵感：它把「项目」而非「对话」作为单位，适合做长周期交付场景，比如独立开发者接单或小团队外包。可以围绕某个垂直行业预置代理团队和流程模板。

* **[lfnovo/open-notebook](https://github.com/lfnovo/open-notebook)** — Notebook LM 的开源替代，强调隐私、多模型和完全本地运行。用户可以把自己的资料变成可对话的知识库，不必上传到 Google，功能上还做了扩展。

  > 灵感：适合切教育、律所、医疗等不能外传资料的场景。与其做通用笔记，不如做「某类文档的本地问答」，比如合同、病历或课程材料。

### AI 基础设施 / 模型

* **[lightpanda-io/browser](https://github.com/lightpanda-io/browser)** — 用 Zig 从零写的无头浏览器，专为 AI 代理和自动化设计，不是 Chromium 分支。内存占用约为 Chrome 的十六分之一，执行速度快约九倍，支持 CDP 协议，可直接接 Playwright 和 Puppeteer。

  > 灵感：代理爬取和自动化测试的成本大头是浏览器实例。可以围绕它做按需渲染的抓取服务，或给现有 RPA 产品做降本替换，接口兼容意味着迁移成本低。

* **[NVIDIA-NeMo/Nemotron](https://github.com/NVIDIA-NeMo/Nemotron)** — 英伟达 Nemotron 系列的开发者资源中心，汇集训练配方、使用手册、数据集和端到端示例。新模型面向多模态代理推理和长时运行代理的执行层，权重和配方一并开放。

  > 灵感：开放训练配方意味着可以基于它做行业微调服务，而不是从零训练。适合切有私有数据但缺算力调优能力的垂直行业，交付的是配方适配而非模型。

### 开发工具 / CLI

* **[open-gsd/gsd-core](https://github.com/open-gsd/gsd-core)** — 轻量的元提示与上下文工程框架，用分阶段循环驱动 Claude Code、Codex、Cursor 等多种编码代理，强调规范驱动开发。与重型流程框架相比，它更接近一层薄协议。

  > 灵感：多代理工具并存是现实，跨工具的流程层有需求。可以做团队级的规范与上下文管理，解决换模型或换编辑器后流程重搭的问题。

### 前端 / 设计

* **[storytold/designcraft](https://github.com/storytold/designcraft)** — 纯 Rust 从零写的页面与版式设计编辑器，定位现代桌面出版，原生跑在三大平台，也能通过 WebAssembly 在浏览器里用。自带段落排版引擎，能处理多栏正文和绕排引文。

  > 灵感：桌面出版长期被 Adobe 和 Affinity 把持，开源几乎空白。可以先切细分印刷场景，比如期刊、简历或学术海报，用模板加排版质量做差异。

### Skill / 垂直工具

* **[mattpocock/skills](https://github.com/mattpocock/skills)** — 一位资深工程师公开的日常代理技能目录，强调小而可组合、适配任意模型，反对接管流程的重型框架。它代表了一种态度：技能应该是工程师自己改的东西，而不是被规范绑架。

  > 灵感：技能包本身难变现，但「技能市场加版本管理」有空间。可以切团队协作场景，解决多人共用代理时提示词散落、无法评审和回滚的问题。

* **[anthropics/skills](https://github.com/anthropics/skills)** — Anthropic 官方的代理技能实现，技能是包含指令、脚本和资源的文件夹，由模型按需动态加载，用于把品牌规范、数据流程等重复任务标准化。也是技能标准的事实参考实现。

  > 灵感：这是基础设施和趋势信号。真正的机会在标准之上的工具链：技能打包、权限声明、依赖检查，以及企业内部技能仓库的治理。

* **[jhaizhou-ops/d2r-mobile](https://github.com/jhaizhou-ops/d2r-mobile)** — 开源的兼容层，让玩家把自己合法购买的 Switch 版暗黑破坏神 II 重生跑在 iPhone、iPad、Mac、安卓和鸿蒙上，重做了触屏操作，保持六十帧，并支持原生 macOS。

  > 灵感：这是趋势信号：兼容层加自带游戏文件正在成为一类灰色但活跃的工程方向。可借鉴的是触屏重映射与性能适配层，而非游戏本身。

[本期 Markdown](daily/zh/2026-10-31.md)

### 往期

#### 2026 年

**10 月**：[31](daily/zh/2026-10-31.md) · [30](daily/zh/2026-10-30.md) · [29](daily/zh/2026-10-29.md) · [28](daily/zh/2026-10-28.md) · [27](daily/zh/2026-10-27.md) · [26](daily/zh/2026-10-26.md) · [25](daily/zh/2026-10-25.md) · [24](daily/zh/2026-10-24.md) · [23](daily/zh/2026-10-23.md) · [22](daily/zh/2026-10-22.md) · [21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
