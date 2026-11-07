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
## [2026.11.07 · 周六](daily/zh/2026-11-07.md)

> 今天这批项目里，最明显的信号是「能力封装」正在成为主流：无论是浏览器操作、云服务技能，还是 UI 组件，都在被拆成可被 AI 调用的独立单元。同时，安全与隐私工具开始从专家走向普通用户，开源项目正用更低的门槛解决具体场景问题。

### AI / Agent 工具

* **[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)** — 一个用 Rust 写的浏览器自动化 CLI，专为 AI agent 设计。它把页面转成带引用的可访问性树，agent 通过短命令逐步操作并检查结果，浏览器在命令间保持打开，适合需要稳定、低延迟的自动化流程。

  > 灵感：如果你在做 agent 产品，可以借鉴它的「快照-操作-验证」循环，把复杂网页交互拆成可回滚的原子步骤，比直接调用 Playwright 更可控。

* **[google/skills](https://github.com/google/skills)** — Google 官方发布的 Agent Skills 集合，覆盖 Google Cloud 等产品。通过 npx 安装后，agent 可以直接调用这些预置技能，减少从头编写工具调用的成本，适合快速搭建与 Google 生态集成的 agent。

  > 灵感：可以围绕「技能市场」做文章：为垂直行业（如电商、数据分析）整理并托管第三方技能包，解决 agent 开发者找工具、配环境的痛点。

* **[Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI)** — 一个自托管、无内容过滤的 AI 图像与视频生成工作室，聚合了 600 多个模型（Flux、Kling、Sora 等），提供 14 个创作工作室。它满足了对开放、可定制生成工具的需求，适合不想被平台束缚的创作者。

  > 灵感：可以针对特定垂直领域（如游戏素材、广告创意）做预配置的工作流模板，降低用户选择模型和调参的门槛。

* **[openai/plugins](https://github.com/openai/plugins)** — OpenAI 的 Codex 插件示例集合，每个插件包含清单文件和可选的技能、命令、钩子等。它展示了如何为 Codex 扩展能力，适合想为 AI 编程助手构建生态的开发者参考。

  > 灵感：可以模仿这种插件结构，为其他 AI 编程工具（如 Claude Code）做第三方插件市场，抢占生态位。

### 前端 / 设计

* **[ppmpreetham/BUI](https://github.com/ppmpreetham/BUI)** — 把 Blender 的 GPU 加速 UI 从原代码库中解耦出来，做成可被 Python、Rust、JS、React、C++ 等调用的库。它让开发者能复用经过数十年优化的界面组件，适合需要高性能原生 UI 的桌面应用。

  > 灵感：对做桌面端工具（如音视频编辑、3D 建模）的团队，可以用它快速搭建专业级界面，省去自研 UI 框架的成本。

### 数据 / 基础设施

* **[pingcap/tidb](https://github.com/pingcap/tidb)** — 一个云原生分布式 SQL 数据库，支持 ACID 事务、分析和向量搜索，专为 agentic 工作负载设计。它解决了 AI 应用对数据一致性和弹性扩展的双重需求，适合需要统一数据层的 agent 系统。

  > 灵感：作为基础设施，可以关注它为 agent 记忆和上下文提供的原生支持，在构建多 agent 协作产品时直接利用，避免自建状态存储。

### 安全 / 隐私

* **[sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)** — 通过用户名在数百个社交网络上追踪账号的开源工具，是 OSINT 和数字取证领域的经典项目。它解决了跨平台身份关联的重复劳动，适合安全研究人员和隐私调查场景。

  > 灵感：面向企业安全团队，可以把它包装成员工账号暴露面监测服务，定期扫描并告警，比人工排查更高效。

* **[PrivSec-dev/banking-apps-compat-report](https://github.com/PrivSec-dev/banking-apps-compat-report)** — 一个众包维护的 GrapheneOS 银行应用兼容性报告，记录哪些银行应用可以运行、需要什么变通方法。它解决了隐私系统用户在日常金融场景中的实际障碍，是社区驱动的实用数据集。

  > 灵感：可以扩展成通用的「隐私系统兼容性数据库」，覆盖更多应用类别，为隐私手机厂商或社区提供订阅式数据服务。

* **[aquasecurity/trivy](https://github.com/aquasecurity/trivy)** — 一个综合安全扫描器，能查容器、K8s、代码仓库、云环境中的漏洞、配置错误、密钥和 SBOM。它把多种扫描能力集成到一个工具里，适合 DevSecOps 流程中的自动化安全检查。

  > 灵感：可以围绕它做轻量级的合规报告生成器，面向中小团队，把扫描结果转成可交付的审计文档，省去人工整理。

### Skill / 垂直工具

* **[valentderah/totk-pc-recomp](https://github.com/valentderah/totk-pc-recomp)** — 将《塞尔达传说：王国之泪》静态重编译为 Windows 和 Linux 原生应用的项目，使用 Vulkan 渲染。它展示了静态重编译技术在游戏移植上的可行性，适合对二进制翻译和游戏 preservation 感兴趣的人。

  > 灵感：作为技术信号，可以关注静态重编译工具链在老旧商业软件现代化上的应用，比如把遗留 Windows 应用迁移到 Linux。

[本期 Markdown](daily/zh/2026-11-07.md)

### 往期

#### 2026 年

**11 月**：[7](daily/zh/2026-11-07.md) · [6](daily/zh/2026-11-06.md) · [5](daily/zh/2026-11-05.md) · [4](daily/zh/2026-11-04.md) · [3](daily/zh/2026-11-03.md) · [2](daily/zh/2026-11-02.md) · [1](daily/zh/2026-11-01.md)

**10 月**：[31](daily/zh/2026-10-31.md) · [30](daily/zh/2026-10-30.md) · [29](daily/zh/2026-10-29.md) · [28](daily/zh/2026-10-28.md) · [27](daily/zh/2026-10-27.md) · [26](daily/zh/2026-10-26.md) · [25](daily/zh/2026-10-25.md) · [24](daily/zh/2026-10-24.md) · [23](daily/zh/2026-10-23.md) · [22](daily/zh/2026-10-22.md) · [21](daily/zh/2026-10-21.md) · [20](daily/zh/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · 每天由 GitHub Actions 自动更新 · <a href="DEVELOPMENT.md">开发说明</a></sub>
</div>
