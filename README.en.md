<div align="center">
  <img src="assets/logo.svg?v=3" alt="OpenDaily" width="300">
  <br>
  <p>Ten open-source projects worth a look, every day — for people looking for their next idea.</p>
  <p><a href="daily/en/"><strong>All issues →</strong></a></p>
  <p><a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a></p>
  <p><a href="README.md">中文</a></p>
</div>

---

<!-- DIGEST:START -->
## [Nov 21, 2026 · Sat](daily/en/2026-11-21.md)

> Today's batch shows AI tooling moving from demo to delivery. Coding agents need approval gates and SOPs, video tools need finished cuts and captions, CI agents must push a fix, and compliance is shipped as an executable guard.

### AI / Agents

* **[Tencent/LoopForge](https://github.com/Tencent/LoopForge)** — Tencent's self-hosted workspace for orchestrating coding agents: describe a task in chat, and a main bot spins up a Docker sandbox, checks out repos,

  > Angle: Aim at teams of five or more devs standardizing agent delivery. The wedge is 'nobody dares merge agent output';

### AI Infrastructure / Models

* **[Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre)** — An open-source CLI agent for CI/CD reliability: it reads a failed run, traces the root cause and pushes a fix for review.

  > Angle: Target teams with Datadog or Grafana alerts but manual triage. Own the last mile from alert to fix;

* **[microsoft/markitdown](https://github.com/microsoft/markitdown)** — Microsoft's lightweight Python utility converting Office files, PDFs and more into Markdown for LLM and text-analysis pipelines.

  > Angle: Better treated as infrastructure than a standalone product. Borrow the reliability of the document-to-token step for format normalization in RAG or agent…

* **[janhq/jan](https://github.com/janhq/jan)** — An open-source ChatGPT alternative that runs models fully offline on your machine, built on Tauri and downloadable across platforms.

  > Angle: For legal, medical and internal enterprise settings where data cannot leave. Versus stitching Ollama with a frontend, the edge is productization;

### Developer Tools / CLI

* **[erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)** — Rewrites an existing app into Rust piece by piece, validating each step against recorded behavior of the original.

  > Angle: For teams maintaining legacy services who fear regressions. The wedge is the 'afraid to touch it' threshold;

* **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** — A pre-indexed code knowledge graph that auto-syncs on changes and feeds coding agents like Claude Code, Codex, Cursor and Copilot, cutting tokens and tool calls.

  > Angle: For heavy agent users bottlenecked by context windows and call costs. The wedge is agents guessing where code lives;

### Frontend / Design

* **[google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)** — A library of agent skills and plugins for Google Stitch, following the Agent Skills open standard and installable into Codex, Gemini CLI,

  > Angle: For frontend teams standardizing design-to-code. The wedge is style drift in agent-generated UI; unlike ad-hoc prompts,

### Vertical Tools / Skills

* **[zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip)** — An open-source desktop AI clipper: paste a link and it turns podcasts, interviews or courses into vertical shorts for Douyin, Xiaohongshu, TikTok and Reels, with subtitles,

  > Angle: For solo creators and small teams doing content repurposing. The wedge is the repetitive long-to-short pipeline;

* **[mjmirza/app-store-compliance](https://github.com/mjmirza/app-store-compliance)** — Turns App Store and Google Play rejections into an open playbook and pre-submission guard: 117 documented rejection patterns with fixes, privacy manifest and Data safety checks,

  > Angle: For indie devs and agencies facing rejection the night before launch. Unlike static checklists, it is executable and can gate submissions inside CI or an agent…

* **[putyy/res-downloader](https://github.com/putyy/res-downloader)** — A cross-platform resource downloader built with Go and Wails, sniffing and saving content from WeChat Channels, mini programs, Douyin, Kuaishou, Xiaohongshu,

  > Angle: For content teams doing asset collection and competitor research. It addresses scattered multi-platform assets, but mind platform terms and copyright;

[This issue (Markdown)](daily/en/2026-11-21.md)

### Archive

#### 2026

**Nov**：[21](daily/en/2026-11-21.md) · [20](daily/en/2026-11-20.md) · [19](daily/en/2026-11-19.md) · [12](daily/en/2026-11-12.md) · [11](daily/en/2026-11-11.md) · [10](daily/en/2026-11-10.md) · [9](daily/en/2026-11-09.md) · [8](daily/en/2026-11-08.md) · [7](daily/en/2026-11-07.md) · [6](daily/en/2026-11-06.md) · [5](daily/en/2026-11-05.md) · [4](daily/en/2026-11-04.md) · [3](daily/en/2026-11-03.md) · [2](daily/en/2026-11-02.md) · [1](daily/en/2026-11-01.md)

**Oct**：[31](daily/en/2026-10-31.md) · [30](daily/en/2026-10-30.md) · [29](daily/en/2026-10-29.md) · [28](daily/en/2026-10-28.md) · [27](daily/en/2026-10-27.md) · [26](daily/en/2026-10-26.md) · [25](daily/en/2026-10-25.md) · [24](daily/en/2026-10-24.md) · [23](daily/en/2026-10-23.md) · [22](daily/en/2026-10-22.md) · [21](daily/en/2026-10-21.md) · [20](daily/en/2026-10-20.md)

<!-- DIGEST:END -->

---

<div align="center">
  <sub>MIT License · Updated daily by GitHub Actions · <a href="DEVELOPMENT.md">Development</a></sub>
</div>
