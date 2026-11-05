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
## [2026.11.05 · 周四](daily/zh/2026-11-05.md)

> 今天的项目里，一个明显的信号是「把大能力塞进小场景」：无论是把万亿参数模型压进单机内存、把专利交底书变成可执行技能，还是把闲鱼监控、光盘刻盘这种极窄需求做成完整工具，都在证明通用大模型之上的价值正转向最后一公里的封装。另一个变化是 AI 编码工具开始从「补全代码」走向「组织流程」，用 Markdown 和斜杠命令模拟一支工程团队。

### AI / Agent 工具

* **[garrytan/gstack](https://github.com/garrytan/gstack)** — YC 总裁 Garry Tan 公开的 Claude Code 配置：23 个 Markdown 斜杠命令，分别扮演 CEO、设计、工程经理、QA、安全官和发布工程师。它把编码 agent 从「写代码」升级成「跑一支虚拟工程团队」。

  > 灵感：适合独立开发者和小团队直接 fork 改造，切「一人公司如何组织 AI 流程」的场景。和零散 prompt 相比，它的价值在于把角色分工和交付节奏固化成可复用命令。

* **[elie222/rakazo](https://github.com/elie222/rakazo)** — 开源自托管的常驻 AI 助手，可自带模型和沙箱，支持 Web、Electron 桌面和 iOS/Android，具备独立会话、记忆、例程和语音模式。它瞄准的是想摆脱闭源 Bot、自己掌控数据的人。

  > 灵感：适合做面向隐私敏感用户的托管版或行业定制版，比如律所、诊所的内部助手。和 Grok Bot 类产品相比，差异是模型和算力都能自选、可完全本地跑。

* **[ConardLi/garden-skills](https://github.com/ConardLi/garden-skills)** — 一套面向 Claude Code、Cursor、Codex 的生产级 Agent Skills 合集，涵盖网页设计、代码渲染短视频、演示文稿、图像生成和本地知识检索。它把「怎么让编码 agent 干好非编码活」沉淀成可安装的技能包。

  > 灵感：适合做技能市场或垂直技能包，比如面向电商详情页、公众号排版的技能组合。和零散 prompt 库相比，它的差异是带安装机制和跨 agent 兼容。

### AI 基础设施 / 模型

* **[FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c)** — 用可移植 C99 在单 CPU、8GB 内存下跑 2.78 万亿参数的 Kimi K3，不依赖 BLAS、框架或 GPU，模型从磁盘流式加载。它解决的是「没有 GPU 也想本地跑大模型」的问题，也把推理引擎的复杂度压到 176KB。

  > 灵感：适合做边缘设备或离线场景的推理底座，比如内网合规环境、教学演示、嵌入式 AI 盒子。和 llama.cpp 的差异在于它演示了超大规模模型靠磁盘流式加载也能跑，思路可复用到冷数据推理。

* **[NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)** — NVIDIA 开源的 Python 框架，从企业元数据构建语义图谱层，统一跨系统指标定义，并通过 MCP、CLI、API 暴露给任意 agent。它解决的是 agent 查数据「查得快但算错」的可靠性问题。

  > 灵感：面向有多个数据源、指标口径混乱的中大型企业，切「agent 数据分析可信度」场景。和直接让 LLM 写 SQL 相比，它先把「数据在哪、什么意思、能不能用」固化成可查询的层。

### 开发工具 / CLI

* **[JiaFeiMiao-K-Cat/DiscImageStudio](https://github.com/JiaFeiMiao-K-Cat/DiscImageStudio)** — 把图片转换成符合 CD、DVD、单层蓝光物理层约束的数据，刻录后盘面呈现肉眼可见图案，支持 Windows 图形界面和跨平台 CLI。它服务的是光盘收藏、定制刻录和实体媒介创作的小众需求。

  > 灵感：适合做定制光盘的实体产品生意，比如婚礼纪念盘、乐队专辑、品牌周边。和普通刻录软件相比，它的差异是把盘面当画布，卖的是实体仪式感。

* **[vercel-labs/scriptc](https://github.com/vercel-labs/scriptc)** — Vercel Labs 的实验性编译器，利用 TypeScript 类型检查结果把 TS/JS 编译成原生可执行文件和 WebAssembly，产物无需 Node.js 即可运行，无法编译的代码在构建期报错并给改写建议。它探索的是「TypeScript 全栈统一」的下一步。

  > 灵感：更像趋势信号而非现成产品：值得关注它对 CLI 工具分发和边缘运行时的冲击。想借力的话，可以先在内部小工具上试编译覆盖率，评估替代 Node 打包的可行性。

### Skill / 垂直工具

* **[harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)** — 输入主题或关键词，自动生成脚本、匹配素材、加字幕配乐并合成高清短视频，带 WebUI 和 API。它服务的是批量做短视频的内容团队，把原本需要剪辑师的多步流程压成一次调用。

  > 灵感：机会不在再造一个生成器，而在垂直行业封装：本地生活商家的探店视频、跨境电商的多语言商品短片。差异点是接入具体素材库和平台发布链路。

* **[Usagi-org/ai-goofish-monitor](https://github.com/Usagi-org/ai-goofish-monitor)** — 基于 Playwright 和 AI 的闲鱼多任务监控系统，支持自然语言建任务、多模态分析商品、区域价格筛选和多渠道通知，带完整 Web 管理后台和 Docker 部署。它解决二手交易里「好货秒没」的信息差。

  > 灵感：适合做垂直品类的二手捡漏服务，比如相机、显卡、乐器，靠筛选规则和通知速度收费。和通用爬虫相比，它的差异是 AI 理解商品描述和成色。

* **[handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill)** — 一个中国专利技能包，覆盖专利点挖掘、发明/实用/外观交底书编写、查新检索、通俗解读和审查答复辅助，还能把解读沉淀进 Obsidian 知识库。它服务的是有技术但写不出交底书的研发人员。

  > 灵感：面向中小研发团队和独立发明人，切「技术方案到可提交交底书」这一段。和通用写作助手相比，它内置了中国专利的格式、框图要求和审查语境。

[本期 Markdown](daily/zh/2026-11-05.md)

### 往期

#### 2026 年

**11 月**：[5](daily/zh/2026-11-05.md) · [4](daily/zh/2026-11-04.md) · [3](daily/zh/2026-11-03.md) · [2](daily/zh/2026-11-02.md) · [1](daily/zh/2026-11-01.md)

**10 月**：[31](daily/zh/2026-10-31.md) · [30](daily/zh/2026-10-30.md) · [29](daily/zh/2026-10-29.md) · [28](daily/zh/2026-10-28.md) · [27](daily/zh/2026-10-27.md) · [26](daily/zh/2026-10-26.md) · [25](daily/zh/2026-10-25.md) · [24](daily/zh/2026-10-24.md) · [23](daily/zh/2026-10-23.md) · [22](daily/zh/2026-10-22.md) · [21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
