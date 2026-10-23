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
## [2026.10.23 · 周五](daily/zh/2026-10-23.md)

> 今天这批项目透出一个共同的信号：Agent 的能力边界正在从「会写代码」转向「会验收结果」。无论是给编码 Agent 补审美、让它自己跑安全审计，还是把网页、视频、桌面环境变成 Agent 可调用的接口，真正的竞争点已经落在可验证的输出和可复用的技能上。

### AI / Agent 工具

* **[anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop)** — 为 DeepSeek Harness 插件生态打造的 Windows 和 macOS 桌面客户端，把本地 Web UI、Host 服务和插件系统集成进原生应用，桌面本身也被设计成插件。它解决的是 Agent 工具本地化使用体验的问题，现在值得看是因为围绕单一模型生态正在长出社区客户端。

  > 灵感：面向想围绕某个模型生态做工具分发的开发者，切「插件市场加桌面入口」这一层。差异在于万物皆插件的架构，机会在于插件发现、安装和变现的基础设施。

### AI 基础设施 / 模型

* **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** — 面向 AI Agent 的网页上下文 API，可大规模搜索、抓取并把网页转成干净的 Markdown 或结构化 JSON，处理代理轮换、JS 渲染和限流等脏活。它解决的是 Agent 拿不到可靠网页数据的问题，现在值得看是因为上下文质量直接决定 Agent 效果。

  > 灵感：适合做垂直 Agent 的团队，切「实时网页数据接入」这一层，不必自建抓取管线。差异在可靠性和 LLM 友好输出，机会在于针对特定行业做数据清洗和结构化封装。

### 开发工具 / CLI

* **[mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)** — 支持 TLS 的交互式 HTTP 拦截代理，提供控制台、命令行和 Web 三种界面，可调试 HTTP/1、HTTP/2 和 WebSocket。它是渗透测试和协议调试的老牌工具，今天出现在 HN 热榜说明抓包调试仍是刚需。

  > 灵感：适合做 API 调试或安全测试产品的团队，把它当底层引擎而非终端产品。差异在于成熟的 TLS 拦截与脚本扩展能力，机会在于围绕团队协作和流量回放做上层封装。

* **[boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5)** — 把 PS5 可执行文件自动移植到 Linux 和 Windows 的工具，通过重链接转换格式并实现系统库的动态链接，不做模拟器也不起独立运行时进程。它解决的是主机游戏跨平台运行的门槛问题，现在值得看是因为它展示了重链接路线在主机移植上的可行性。

  > 灵感：更适合作技术趋势信号而非直接创业点。对做游戏兼容层或逆向工具的团队有参考价值，但法律与版权风险高，商业化需谨慎评估。

* **[storytold/cadcraft](https://github.com/storytold/cadcraft)** — 纯 Rust 编写的开源 AutoCAD 风格二维三维 CAD 应用，保留命令行、对象捕捉、图层、标注、块和 DXF 等熟悉工作流，可原生运行于多平台并通过 WebAssembly 在浏览器中使用。它解决的是专业 CAD 软件昂贵且封闭的问题，现在值得看是因为纯 Rust 加 WASM 让桌面级 CAD 能进入浏览器。

  > 灵感：面向被授权费困扰的小型设计工作室和工程团队，切「轻量 CAD 加浏览器协作」场景。差异在于命令式工作流兼容老用户习惯，机会在于云端审阅和文件互操作。

### 前端 / 设计

* **[remotion-dev/remotion](https://github.com/remotion-dev/remotion)** — 用 React 以编程方式生成视频的工具，代码即视频源，支持 Agent 生成、交互编辑、批量渲染和嵌入应用。它解决的是视频生产难以自动化、难以数据驱动的问题，现在值得看是因为它正把自己重新定位为「Agent 时代的视频工具」。

  > 灵感：面向需要批量产出视频的营销和电商团队，切「模板化视频自动化」场景。差异在于渲染跑在自有基础设施上、可与数据打通，可做按行业定制的视频生成服务。

### 数据 / 基础设施

* **[twentyhq/twenty](https://github.com/twentyhq/twenty)** — Salesforce 的开源替代品，定位是为 AI 设计的 CRM，技术团队可以像管理代码一样构建、发布和版本化自己的 CRM。它解决的是通用 CRM 难以适配复杂业务流程的问题，现在值得看是因为 AI 正在重写客户数据系统的交互方式。

  > 灵感：面向有技术团队但业务定制需求强的公司，切「买来的 CRM 改不动」这一痛点。差异在于把 CRM 当成可版本化的代码库，可围绕行业模板或迁移工具做增值。

* **[NanmiCoder/MediaCrawler](https://github.com/NanmiCoder/MediaCrawler)** — 多平台自媒体数据采集工具，覆盖小红书、抖音、快手、B 站、微博、贴吧、知乎的公开信息与评论抓取。它解决的是国内社交平台数据分散、接口不统一的问题，现在值得看是因为品牌舆情和内容研究对这类数据需求持续增长。

  > 灵感：面向做舆情监测或内容分析的团队，切「跨平台公开数据聚合」场景。注意合规边界，机会不在爬虫本身，而在其上的清洗、趋势分析和预警产品。

### 安全 / 隐私

* **[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)** — Cloudflare 开源的编码 Agent 技能，把 Agent 变成安全审计员，分六个阶段做侦察、覆盖式排查、候选验证和机器可读的独立复核。它源自 Cloudflare 内部漏洞挖掘系统，现在值得看是因为它示范了如何把安全流程固化成可复用的 Agent 技能。

  > 灵感：适合做安全服务的团队，切「中小团队没有专职安全审计」的场景。与扫描器不同，它让 Agent 分阶段推理并交叉验证发现，可包装成按次交付的代码安全体检。

### Skill / 垂直工具

* **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** — 一个给编码 Agent 补「审美」的 Agent Skill，提供艺术方向、真实参考图和浏览器自检，让 Agent 产出有设计感的页面而不是模板化落地页。它解决的是 AI 生成前端千篇一律的问题，现在值得看是因为技能化正在成为 Agent 能力分发的新形态。

  > 灵感：面向独立开发者和小型工作室，切「AI 生成页面质量差」这个痛点。差异在于它不只给提示词，还强制 Agent 在真实浏览器里自查，可把这种「生成加验收」闭环复用到其他设计交付场景。

[本期 Markdown](daily/zh/2026-10-23.md)

### 往期

#### 2026 年

**10 月**：[23](daily/zh/2026-10-23.md) · [22](daily/zh/2026-10-22.md) · [21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
