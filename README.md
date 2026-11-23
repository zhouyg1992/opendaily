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
## [2026.11.23 · 周一](daily/zh/2026-11-23.md)

> 今天这批项目透露出一个清晰信号：围绕 Agent 的配套层正在快速成形，从给 Agent 用的 UI 行为库、后台自动接活的调度器，到防止代码被 AI 逆向的防护工具，再到教人拆解视频、上手大模型的教程。真正稀缺的不再是模型本身，而是让 Agent 可靠落地、可控可审计、并且能被人验收的那一层。

### AI / Agent 工具

* **[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)** — 一个极轻量的本地自动化中台，让 Claude Code、Codex 这类命令行 Agent 在后台自己接活、自己跟进，遇到需要决策的事才通过飞书、钉钉、Slack 等推卡片找人拍板。零外部依赖，一台电脑一条命令即可运行。

  > 灵感：适合做「无人值守 Agent 值班」的轻量产品：面向个人开发者和小团队，卖点是任务队列加人工审批卡片的闭环，和云端 Agent 平台比，优势在本地部署、数据不出机器。

* **[mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork)** — 面向团队及其 Agent 的 AI 原生引擎，支持多种 harness 和多 Agent 协作，可自托管。它的主张是对话以答案结束，而一个请求要等到提问的人签字确认才算完成，强调人工验收环节。

  > 灵感：切的是团队里 Agent 产出无人把关的痛点：把审批和签核做成工作流的一等公民，适合做内部工具平台或交付型团队的 Agent 流水线，与纯对话式工具形成差异。

* **[Lordog/dive-into-llms](https://github.com/Lordog/dive-into-llms)** — 上海交大课程讲义扩展而来的大模型编程实践教程，覆盖微调部署、数学推理、GUI Agent、对齐等主题，完全免费，还上线了国产化开发全流程公益教程。对想系统上手大模型的学生和转行者很实用。

  > 灵感：教程本身不是生意，但围绕它的陪练和项目制训练营是：面向高校课程设计和转岗人群，用它的实验手册做骨架，补上评测、答疑和作品集输出。

### AI 基础设施 / 模型

* **[lyogavin/airllm](https://github.com/lyogavin/airllm)** — 通过逐层流式加载权重，让 70B 模型在单张 4GB 显卡上推理，无需量化、蒸馏或剪枝，并宣称能跑更大规模的模型，近期还加入了小显存训练支持。解决的是显存不足这个最硬的部署门槛。

  > 灵感：更适合作为基础设施能力而不是独立产品：可以嵌进私有化部署交付、边缘设备推理、教学实验环境。真正的机会在把这种省显存推理包装成开箱即用的本地模型服务。

### 开发工具 / CLI

* **[RoutineMiku/apkstart](https://github.com/RoutineMiku/apkstart)** — Windows 上的安卓应用运行器，双击 APK 即安装，每个应用生成独立桌面图标和窗口，自带 QEMU 运行时，还做了 Windows 与安卓目录的双向文件同步。作者坦言是早期版本、业余时间维护。

  > 灵感：需求真实但体验粗糙，正是产品化的空隙：面向需要在 PC 上跑安卓办公或游戏小号的用户，做稳定性和兼容性打磨，比从零造模拟器更现实。

### 前端 / 设计

* **[vercel-labs/ui](https://github.com/vercel-labs/ui)** — Vercel 实验室推出的 UI SDK，把键盘导航、焦点、选中、弹层、拖拽和 ARIA 等交互行为抽成 headless 核心，再提供 React、Vue、Svelte、Solid 和 Web Components 适配。它面向的是让 Agent 生成界面的场景，组件由行为原语组合而成。

  > 灵感：切入点不是又一个组件库，而是给 Agent 用的设计系统底座：把无障碍和交互逻辑固化成可被模型调用的原语，做企业内部的 Agent 生成前端规范层，比让模型自由写组件更可控。

* **[jquery/jquery](https://github.com/jquery/jquery)** — jQuery 4.0.0 正式发布，3.x 转入仅关键修复，2.x 和 1.x 停止支持。这个统治了上一代 Web 的库仍在大量存量站点中运行，新版发布对维护老项目的团队是一次明确的升级窗口。

  > 灵感：机会不在重造 jQuery，而在迁移服务：面向仍跑 1.x/2.x 的企业站点做兼容性评估和升级，或做检测旧版本与已知问题的扫描工具，卖给外包和运维团队。

### 安全 / 隐私

* **[qybaihe/bla](https://github.com/qybaihe/bla)** — 开源的蓝队 MCP 服务与 CLI，专门对抗 AI 逆向工程 Agent，覆盖 JS/TS、Electron ASAR、WASM、Python、原生二进制、SQLite、模型权重和 Android DEX。思路是通过投毒、耗尽、幻觉让自动逆向变得不划算。

  > 灵感：软件发布方是明确客户：独立开发者和小型软件公司担心自己的客户端被 AI 工具一键拆解。可以从混淆和反调试升级为「对抗 Agent 的发布流水线插件」，按构建次数收费。

### Skill / 垂直工具

* **[JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)** — 逆向任意视频，逐镜头判断是实拍、AI 生成还是代码制作，并给出复刻方法，结果以开放的 VIDEO.md 格式输出，供 Agent 逐层读取。对做短视频投放和创意拆解的人有直接价值。

  > 灵感：可以做成广告和内容团队的竞品拆解工具：输入竞品短视频，输出镜头结构、生成方式和可复刻脚本。和人工拉片比，差异在于结构化格式能直接喂给制作 Agent。

* **[Minireel/HGhub](https://github.com/Minireel/HGhub)** — 用 Rust 写的插件化通用视频播放器，把浏览、搜索、播放和个人片库放在一个应用里，通过导入 JavaScript 插件接入不同内容来源。应用本身不内置内容源，也不分发第三方插件。

  > 灵感：它的价值不在播放器，而在插件协议：可以把这套「内容源插件加统一播放体验」的架构复用到企业内部视频库、课程平台或垂直内容聚合，绕开版权敏感地带。

[本期 Markdown](daily/zh/2026-11-23.md)

### 往期

#### 2026 年

**11 月**：[23](daily/zh/2026-11-23.md) · [22](daily/zh/2026-11-22.md) · [21](daily/zh/2026-11-21.md) · [20](daily/zh/2026-11-20.md) · [19](daily/zh/2026-11-19.md) · [12](daily/zh/2026-11-12.md) · [11](daily/zh/2026-11-11.md) · [10](daily/zh/2026-11-10.md) · [9](daily/zh/2026-11-09.md) · [8](daily/zh/2026-11-08.md) · [7](daily/zh/2026-11-07.md) · [6](daily/zh/2026-11-06.md) · [5](daily/zh/2026-11-05.md) · [4](daily/zh/2026-11-04.md) · [3](daily/zh/2026-11-03.md) · [2](daily/zh/2026-11-02.md) · [1](daily/zh/2026-11-01.md)

**10 月**：[31](daily/zh/2026-10-31.md) · [30](daily/zh/2026-10-30.md) · [29](daily/zh/2026-10-29.md) · [28](daily/zh/2026-10-28.md) · [27](daily/zh/2026-10-27.md) · [26](daily/zh/2026-10-26.md) · [25](daily/zh/2026-10-25.md) · [24](daily/zh/2026-10-24.md) · [23](daily/zh/2026-10-23.md) · [22](daily/zh/2026-10-22.md) · [21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
