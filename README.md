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
## [2026.10.21 · 周三](daily/zh/2026-10-21.md)

> 今天这批项目透露出一个清晰信号：AI 正在从「聊天框」下沉到具体工作流和具体设备上。有人把助手塞进你已有的聊天软件，有人用纯 C 让大模型在旧电脑上跑起来，还有人把设计、科研、视频剪辑这些专业手艺拆成可安装的技能包。机会不在再造一个通用 agent，而在把某个垂直环节做深、做稳、做到别人愿意付费。

### AI / Agent 工具

* **[openclaw/openclaw](https://github.com/openclaw/openclaw)** — 一个跑在你自己电脑上的开源 AI 助手，直接接入 Discord、iMessage、Slack、Telegram 等二十多个聊天渠道，状态、记忆和凭证都留在本地硬件。模型和 agent 框架可插拔替换，同一套网关既能当个人助理也能做团队共享部署。

  > 灵感：切「数据不出内网」的团队场景：把网关部署在公司自己的机器上，卖的是部署、渠道对接和权限治理，而不是模型本身。和云端助手比，差异在合规和可控。

### AI 基础设施 / 模型

* **[NandhaKishorM/laya](https://github.com/NandhaKishorM/laya)** — 一个非自回归的「系统一」决策引擎，对任意文本做类型化选择、打分和是/否判断，单次前向约 33 毫秒，覆盖 100 多种语言，并带按请求选检查点的路由器。提供 HTTP、MCP 和主流 agent 框架适配。

  > 灵感：适合替换 agent 流程里那些「用大模型做简单判断」的昂贵环节，比如意图分类、路由和审核。卖点是延迟和成本，切的是高并发、低复杂度的判定场景。

* **[JustVugg/colibri](https://github.com/JustVugg/colibri)** — 纯 C 编写、零依赖的推理引擎，利用 MoE 模型每 token 只激活少量专家的特性，把专家留在磁盘、按需流式读取，从而在普通机器上跑数百亿参数的开源模型，不需要 GPU。

  > 灵感：这是基础设施层的信号：本地推理的门槛正被拉到消费级硬件。可以围绕它做「离线可用的私有模型盒子」，切对网络和隐私敏感的行业客户。

### 开发工具 / CLI

* **[vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils)** — 一个 macOS 菜单栏工具集，把按应用调音量、系统监控、窗口吸附、剪贴板历史、卸载器等通常要逐个付费购买的小工具收进一个图标，无账号、无遥测、无订阅，可按需安装单项功能。

  > 灵感：验证了「订阅疲劳」下的付费意愿：用户愿意为一次买断的实用工具付费。可以照此思路做 Windows 或跨平台的同类合集，靠口碑和本地化取胜。

* **[rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA)** — 自托管的 WhatsApp API 网关，基于可插拔架构，数据库、媒体存储和缓存层都通过配置切换，面向需要完全掌控消息基础设施、不想被厂商锁定或按量收费的开发者。

  > 灵感：适合做中小商家的客服和通知自动化：以网关为底座，卖的是模板、合规话术和托管运维，而不是再包一层 API 转售。

### 前端 / 设计

* **[pbakaus/impeccable](https://github.com/pbakaus/impeccable)** — 给 AI 编程工具补上设计能力的技能包，含 24 条命令、浏览器内实时迭代和 61 条确定性检测规则，专门治理 AI 生成前端千篇一律的模板感。装进现有编码工具即可用。

  > 灵感：面向接外包或做内部工具的小团队：把「AI 出稿后统一走一遍设计检查」做成流程，卖的是审美标准和检测规则，不是又一个生成器。

### 安全 / 隐私

* **[microg/GmsCore](https://github.com/microg/GmsCore)** — Google Play 服务的自由实现，让依赖 Play Services 的应用能运行在没有官方服务的系统上，覆盖登录、推送、定位等能力，是去谷歌化安卓设备的关键基础组件。

  > 灵感：这是趋势信号而非创业点：隐私导向的安卓生态仍有基础设施缺口。围绕它做设备预装、企业定制 ROM 或兼容性测试服务，比直接改核心更现实。

### Skill / 垂直工具

* **[storytold/filmcraft](https://github.com/storytold/filmcraft)** — 用纯 Rust 从零写的开源非线性视频剪辑器，覆盖剪辑、调色和声音，原生支持三大桌面系统，也能通过 WebAssembly 跑在浏览器里。同一团队还在做矢量绘图和 CAD 工具。

  > 灵感：浏览器内可用的专业剪辑器，意味着可以嵌进在线协作或教育场景。切「不想装大型软件、但要真剪辑」的用户，卖托管版和团队素材管理。

* **[eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter)** — 一份中文「高性价比人生指南」，765 条建议覆盖健康、理财、法律、社保、婚育和创业合规，每条标注成本、收益、证据等级和原始出处，并提供让 AI 按书回答的 skill。

  > 灵感：这是知识库加 skill 的样板：把高信任度的结构化内容做成可被 AI 检索引用的条目。可复制到税务、劳动法、医保等同样需要「有出处」的领域。

* **[Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)** — 面向科研人员的技能合集，把论文润色和科研绘图等 Nature 风格的工作流封装成可安装的 skill，支持 Claude Code、Codex 等工具，并提供网页版入口。

  > 灵感：科研写作是高频、高付费意愿的垂直场景。可以只切其中一环，比如图表规范检查或投稿格式转换，做成独立工具，比大而全的技能库更容易建立信任。

[本期 Markdown](daily/zh/2026-10-21.md)

### 往期

#### 2026 年

**10 月**：[21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
