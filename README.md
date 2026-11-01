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
## [2026.11.01 · 周日](daily/zh/2026-11-01.md)

> 今天这批项目透露出一个共同信号：围绕编程 agent 的周边配套正在快速成型。有人做终端运行时，有人做多 agent 编排面板，有人做配置切换器，还有人直接给 agent 塞免费模型。模型能力本身不再是稀缺品，稀缺的是让 agent 稳定干活的那层壳，以及围绕它形成的真实使用场景。

### AI / Agent 工具

* **[paperclipai/paperclip](https://github.com/paperclipai/paperclip)** — 把多个 AI agent 当成一个团队来管的开源应用：给每个 agent 分配目标、选模型和 harness，在一个面板里看任务、成本、权限和历史。定位是 agent 的「公司管理层」，不是单个 agent 的壳。

  > 灵感：适合做多 agent 协作的成本与权限治理。切中小团队：谁在跑什么、花了多少、能碰哪些系统，这些现在基本靠人肉盯，做成一键合规报表就有价值。

### AI 基础设施 / 模型

* **[Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model)** — 一个 dsh 插件，装上后无需注册或 API Key 就能调用 DeepSeek、Kimi 等前沿模型，免费不限量，并附带 OpenAI 兼容的本地转发端口。它揭示了免费模型车道正在成为 agent 生态的入口。

  > 灵感：这更像趋势信号而非生意：免费通道依赖上游网关，随时可能变。真正可做的是给企业提供「免费车道 + 付费兜底」的模型路由与配额管理，把不确定性挡在外面。

### 开发工具 / CLI

* **[herdrdev/herdr](https://github.com/herdrdev/herdr)** — 给编程 agent 用的终端运行时：关掉客户端或断掉 SSH，后台服务里的会话继续跑，重启后还能恢复布局并续上支持的 agent 会话。多台机器的本地和远程工作也能收进一个窗口统一管理。

  > 灵感：切「agent 长时间跑任务」这个场景：现在的痛点是终端一断任务就死。可以围绕会话持久化和远程恢复做托管服务，或给团队做 agent 运行审计。

* **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** — 跨平台桌面工具，统一管理 Claude Code、Codex、Gemini CLI 等多个编程 agent 的 API 供应商、MCP、技能和提示词，省去手改 JSON/TOML/YAML 配置。解决的是多 agent 并存后配置碎片化的问题。

  > 灵感：配置管理本身难变现，但可以往团队方向走：集中下发供应商策略、密钥轮换、用量归集。切那些同时用三四个 agent 又要求合规的中型研发团队。

* **[tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft)** — 纯 Rust 写的开源参数化 3D CAD，桌面、浏览器、WASM 都能跑，内置 MCP 服务器让 AI agent 直接建模。把传统上笨重昂贵的 CAD 变成可脚本化、可被 agent 调用的工具。

  > 灵感：机会在「agent 建模」的垂直封装：面向 3D 打印爱好者或小批量硬件团队，把常用零件参数化，用户说需求、agent 改尺寸出 STEP，比通用 CAD 更省事。

* **[horizon-rust/horizon](https://github.com/horizon-rust/horizon)** — 用 Rust 从零重写 Minecraft Java 版，靠三百多个差分测试对照原版校验世界生成和规则，不含任何原版代码或素材，需要用户自备正版。它证明了大型游戏逻辑可以被干净地重新实现。

  > 灵感：对创业者是技术信号：差分测试驱动的重写方法可迁移到其他闭源但有行为规范的系统。对社区是性能机会，围绕低配设备和服务器端优化做托管更有戏。

### 前端 / 设计

* **[pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv)** — 参照 tvOS 设计的开源 Android TV 桌面，无广告无推荐流，开机自动接管，适配小米、TCL、创维等国产电视。还支持手机扫码整理图标、航拍屏保和自定义壁纸。

  > 灵感：国产电视桌面广告是真实痛点，但纯开源难收钱。可做的是面向酒店、民宿、展厅的定制桌面：统一应用集、远程配置、品牌壁纸，按设备收部署费。

### Skill / 垂直工具

* **[calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)** — 把 AI 编程助手改造成视频制作室：用自然语言描述需求，agent 负责调研、写脚本、生成素材、剪辑和合成，内置多条制作管线和大量技能文件。本质是把视频生产流程拆成 agent 可执行的步骤。

  > 灵感：别再做通用视频工具，切垂直品类：电商短视频、课程片头、本地化配音。差异在于把行业模板和素材规范固化进管线，让非专业用户一次出片。

* **[cjpais/Handy](https://github.com/cjpais/Handy)** — 完全离线的开源语音转文字桌面应用：按快捷键说话，文字直接落到任意输入框，全程不联网。它填补的是真正可扩展、免费、隐私优先的听写工具空缺。

  > 灵感：切隐私敏感行业：医疗、法律、律所记录，或涉密研发。差异不是识别率，而是可自托管、可审计、可换模型，卖的是部署和合规而不是软件本身。

* **[DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym)** — 开源自托管的健身与自重训练记录应用，有 iPhone、Apple Watch 和 Android 版本，能规划训练、记录动作、看肌肉覆盖，并支持从 Strong、Hevy 等导入数据。一个 docker compose 就能跑，数据在自己手里。

  > 灵感：健身数据迁移是现成入口：很多人被订阅制锁住。可以做「数据搬家 + 自托管托管」服务，或面向私教的多人训练管理，按教练而非按用户收费。

[本期 Markdown](daily/zh/2026-11-01.md)

### 往期

#### 2026 年

**11 月**：[1](daily/zh/2026-11-01.md)

**10 月**：[31](daily/zh/2026-10-31.md) · [30](daily/zh/2026-10-30.md) · [29](daily/zh/2026-10-29.md) · [28](daily/zh/2026-10-28.md) · [27](daily/zh/2026-10-27.md) · [26](daily/zh/2026-10-26.md) · [25](daily/zh/2026-10-25.md) · [24](daily/zh/2026-10-24.md) · [23](daily/zh/2026-10-23.md) · [22](daily/zh/2026-10-22.md) · [21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
