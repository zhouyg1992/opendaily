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
## [2026.10.24 · 周六](daily/zh/2026-10-24.md)

> 今天的榜单透出一个清晰信号：AI 正从「能跑起来」转向「跑得安全、跑得可控」。一边是给自主 agent 划定权限边界的运行时，一边是把专业工作流打包成可复用技能与插件的做法，还有团队在认真补齐远程访问、代码规范这类落地环节。基础设施层的老项目依然稳，但增量都发生在让 AI 真正进入生产流程的那一圈。

### AI / Agent 工具

* **[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)** — 面向知识工作者的插件集合，把技能、连接器、斜杠命令和子 agent 按岗位打包，让 Claude 按团队习惯和既有数据源完成工作，而不是每次从零提示。

  > 灵感：插件按职能划分，意味着可以围绕某个具体岗位做深度定制，比如财务对账或法务审阅，卖的是工作流沉淀而非模型本身。

### AI 基础设施 / 模型

* **[NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)** — 给自主 AI agent 用的安全运行时，用声明式策略限定每个 agent 能读哪些文件、装什么包、调哪些 API、用哪些凭证，而不是直接给它们整台机器的权限。

  > 灵感：企业要上 agent，卡点往往不是模型能力而是权限审计。可以从「agent 权限可视化 + 策略模板」切入，先服务需要合规留痕的金融和运维团队。

* **[pollen-robotics/microduck](https://github.com/pollen-robotics/microduck)** — 约 25 厘米、800 克的雙足机器鸭，仓库里是它的「大脑」：50Hz 控制循环驱动十五个舵机，加载强化学习训练出的策略，还有防止变砖的远程更新机制。

  > 灵感：适合做机器人教学和 sim2real 入门套件。真正的门槛在固件更新和策略部署流程，把这块做成托管服务比卖硬件更可持续。

* **[OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)** — 无分词器的语音合成系统，直接生成连续语音表示，支持三十种语言、音色设计和可控克隆，输出 48kHz 音频，绕开离散 token 化以提升自然度。

  > 灵感：多语言加音色设计适合做本地化的有声内容和客服配音。差异化不在模型本身，而在把克隆授权和音色资产管理做扎实。

### 开发工具 / CLI

* **[liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote)** — 基于 DeepSeek Harness 插件机制的多端远程访问方案，通过端到端加密的 P2P 网络，让手机、浏览器随时接回工作机上仍在运行的同一条会话。

  > 灵感：它点中了长任务 agent 的真实痛点：人离开工位但任务还在跑。可以把这个「随时接管」体验做成通用能力，服务跑长任务的开发者和运维。

### 数据 / 基础设施

* **[VikOlliver/RepRapMicron](https://github.com/VikOlliver/RepRapMicron)** — 把开源 RepRap 3D 打印项目延伸到微米尺度，沿用 GCODE、GRBL 和 NEMA17 步进电机等熟悉工具，用廉价易得材料实现可重复的微米级二维刻写。

  > 灵感：更像趋势信号而非现成产品：桌面级微纳加工的门槛在下降。关注它在光学和生物实验耗材上的早期用户，那里可能先出现付费场景。

### 安全 / 隐私

* **[chaitin/SafeLine](https://github.com/chaitin/SafeLine)** — 自托管的 Web 应用防火墙兼反向代理，过滤 SQL 注入、XSS、命令注入、暴力破解和爬虫滥用等流量，部署方式接近装一个网关。

  > 灵感：对中小团队来说，自托管 WAF 的难点在规则调优和误报处理。可以做托管运维或按业务定制的规则包，而不是再做一个同类网关。

### Skill / 垂直工具

* **[luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)** — 把 Claude Code 从基础命令到 hooks、skills、MCP 编排串成一条可视化学习路径，配可直接复制的模板，解决官方文档只讲功能不讲组合的问题。

  > 灵感：这类内容本身难变现，但它暴露了真实需求：团队需要内部版的「怎么在我们代码库里用」。做企业内训和上手引导包比做公开教程更有付费空间。

* **[Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu)** — 紫微斗数开源排盘引擎，含完整排盘算法、四化系统和格局知识库，并放出覆盖近七十年真实日期的大规模解读数据集，把传统术数变成了可计算的数据资产。

  > 灵感：真正的价值在那份结构化解读数据集，而非排盘本身。可以围绕它做命盘问答或内容生成工具，面向已有用户基础的命理内容创作者。

* **[samber/cc-skills-golang](https://github.com/samber/cc-skills-golang)** — 一组面向生产级 Go 项目的 agent 技能，覆盖语言习惯、测试、安全和可观测性，按需加载以免撑爆上下文，作者强调经过人工测试和改写。

  > 灵感：「人工审过的技能包」本身就是卖点。可以按语言或框架复制这个模式，做团队内部统一编码规范的技能库，减少 AI 生成代码的风格漂移。

[本期 Markdown](daily/zh/2026-10-24.md)

### 往期

#### 2026 年

**10 月**：[24](daily/zh/2026-10-24.md) · [23](daily/zh/2026-10-23.md) · [22](daily/zh/2026-10-22.md) · [21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
