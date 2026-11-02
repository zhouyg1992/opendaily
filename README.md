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
## [2026.11.02 · 周一](daily/zh/2026-11-02.md)

> 今天这批项目里，最清晰的信号是：AI 正在从「能做什么」转向「怎么被信任、怎么被管住」。一边是审计、越狱、安全运营中心这类治理工具冒头，另一边是本地推理、本地听写、本地视频编辑把能力往个人设备上搬。对创业者来说，机会不在再做一个 agent，而在 agent 跑起来之后那些没人愿意干的脏活。

### AI 基础设施 / 模型

* **[FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken)** — 面向消费级硬件的 MoE 推理引擎，把 GPU、CPU、主机内存和互联当成统一资源池，让游戏 PC 也能跑 290B 级别的开源 MoE 模型。它回应的是「前沿模型权重开放了，但普通人跑不动」的落差。

  > 灵感：更适合作为基础设施信号而非直接创业点：真正可借的是「把异构消费硬件当推理集群」这个思路，可以往家庭或小工作室的多机推理调度上做，而不是再包一层聊天界面。

* **[togg53192-cmd/jailbreaks](https://github.com/togg53192-cmd/jailbreaks)** — 一个收集了 32 套系统提示、人格锁定和 agent 操作规范的仓库，覆盖 26 个以上模型，全部可直接粘贴使用。它本身不是产品，但暴露了提示词工程正在沉淀为可复用的配置资产。

  > 灵感：把它当趋势信号：提示词和 agent 规范需要版本管理、评测和权限控制。机会在于给团队做「提示词配置的 CI」，而不是再收集更多 jailbreak。

### 开发工具 / CLI

* **[D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)** — 一个 Python 爬虫框架，把 HTTP 请求、隐身浏览器、解析、并发爬取和代理轮换收进同一个库，还能通过 MCP server 让 AI agent 直接调用。它解决的是「静态页和 JS 渲染页要写两套代码」的老问题。

  > 灵感：机会在垂直数据管道：用它的 MCP 接口把某个行业的数据源（招聘、房产、电商价格）封装成 agent 可直接查询的服务，卖的是稳定性和反封策略，不是爬虫库本身。

* **[anomalyco/hex](https://github.com/anomalyco/hex)** — Mac、Windows、Linux 上的本地语音听写工具，按住快捷键说话，松手即粘贴，转录全部在设备上完成，首次下载模型后不再联网。它解决的是云端听写工具的隐私顾虑和延迟问题。

  > 灵感：不要做通用听写，做垂直场景的「语音输入层」：比如面向医生、律师的术语增强版，或把听写结果直接结构化成工单字段，差异在领域词表和下游集成。

### 数据 / 基础设施

* **[0xJacky/nginx-ui](https://github.com/0xJacky/nginx-ui)** — 给 Nginx 做的 Web 管理界面，支持配置编辑、Let's Encrypt 证书、定时任务和 MCP server，让不熟悉命令行的运维也能管理站点。它填补的是 Nginx 强大但配置门槛高之间的空隙。

  > 灵感：适合做托管运维的入口：面向小企业和独立开发者，把 nginx-ui 包成「站点上线 + 证书续期 + 备份」的一键服务，卖的是省心而不是面板功能。

### 安全 / 隐私

* **[ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi)** — 一个独立的 AI agent 审计工具，检查 agent 是否按预期目标、权限和业务边界行事，支持人工或 agent 自检，几分钟内给出诊断结果。随着 agent 进入生产环境，企业需要能向合规和老板解释「它没乱来」的证据。

  > 灵感：适合切受监管行业的中小团队：把审计报告做成可交付的合规附件，而不是又一个开发者调试面板。和通用 eval 框架的差别在于它盯的是权限越界和组织意图，不是模型分数。

### Skill / 垂直工具

* **[jub0t/Concat](https://github.com/jub0t/Concat)** — 用 Rust 写的本地优先、跨平台视频编辑器，定位是 CapCut 的开源替代，支持 JSON-RPC API 和 MCP，可脚本化操作。它瞄准的是不想把素材上传云端、又嫌专业剪辑软件太重的创作者。

  > 灵感：借它的 MCP 接口做「批量短视频生产」：面向电商和自媒体，把模板、字幕、配乐做成可被 agent 调用的流水线，卖的是产能而不是编辑器功能。

* **[T-Auto/dsh-ops](https://github.com/T-Auto/dsh-ops)** — 一个 DSH 插件，通过新增 ops 系列工具并隐藏部分官方工具来降低 token 消耗和任务耗时，覆盖 Bash、文件批处理和渐进式工具加载。它反映的是 agent 用户开始为「每次调用的成本」而不是「能力上限」买单。

  > 灵感：这是典型的生态位工具，说明 agent 运行时的成本优化正在变成独立品类。可以借它的思路做跨 harness 的 token 预算层，帮团队看清哪个环节在烧钱。

* **[guohuiyuan/go-music-dl](https://github.com/guohuiyuan/go-music-dl)** — Go 写的多平台音乐搜索与下载工具，覆盖网易云、QQ、酷狗、Bilibili 等十个以上来源，支持 CLI、Web、TUI 和桌面端，还能并发搜索和无损解析。它满足的是跨平台找歌、批量整理本地曲库的需求。

  > 灵感：单机工具很难直接变现，但「多源聚合 + 统一元数据」这层能力可以卖给做本地媒体库或车载音乐的产品，省掉他们逐个平台对接的维护成本。

### 学习资源 / 其他

* **[public-apis/public-apis](https://github.com/public-apis/public-apis)** — A collective list of free APIs

[本期 Markdown](daily/zh/2026-11-02.md)

### 往期

#### 2026 年

**11 月**：[2](daily/zh/2026-11-02.md) · [1](daily/zh/2026-11-01.md)

**10 月**：[31](daily/zh/2026-10-31.md) · [30](daily/zh/2026-10-30.md) · [29](daily/zh/2026-10-29.md) · [28](daily/zh/2026-10-28.md) · [27](daily/zh/2026-10-27.md) · [26](daily/zh/2026-10-26.md) · [25](daily/zh/2026-10-25.md) · [24](daily/zh/2026-10-24.md) · [23](daily/zh/2026-10-23.md) · [22](daily/zh/2026-10-22.md) · [21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
