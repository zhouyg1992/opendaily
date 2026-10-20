# OpenDaily · 每天 10 个开源项目

从 GitHub Trending、新项目搜索和 Hacker News 里，每天挑 **10 个有意思的开源项目**，写成一份 Markdown 日报：`daily/YYYY-MM-DD.md`。不需要网页，项目本身就是日报仓库，GitHub 直接渲染。

**[全部日报](daily/)**

<!-- DIGEST:START -->
## 最新一期

**[2026.10.20 · 周二](daily/2026-10-20.md)** — 今天的候选池里，Agent 工具正从「能跑」转向「跑得更省、更稳」：有人压缩上下文，有人把多个 Agent 拉进同一张工作台；另一边，纯 Rust 重写的桌面软件和本地推理引擎也在冒头。

### AI / Agent 工具

- **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** — 给 AI 编程 Agent 立规矩：能不加的代码就不加，先想清楚再动手，像资深工程师一样主动拒绝过度设计，专治越改越复杂。
- **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** — 把代码库、文档、SQL schema、配置和 PDF 一起解析成可查询的知识图谱，让人或 Agent 都能顺着关系检索跨文件上下文。
- **[stablyai/orca](https://github.com/stablyai/orca)** — 多 Agent 工作台：把 Claude Code、Grok Bot 等编码 Agent 放进同一处并行调度，复用自己已有的订阅额度，不必为每个 Agent 单独买 API。
- **[Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)** — 节点式扩散模型工作台，在本地把模型、采样器和后处理串成可视化流程；既能直接出图，也常被当作生成式图像产品的底层引擎。

### AI 基础设施 / 模型

- **[Niko1221/Strata](https://github.com/Niko1221/Strata)** — 在消费级硬件上一键运行 Qwen3.8-Flash-Next 的本地推理引擎，启动后在 localhost 暴露 OpenAI / Anthropic 兼容接口，现有客户端可直接接入。

### 开发工具 / CLI

- **[cursor/plugins](https://github.com/cursor/plugins)** — Cursor 官方插件规范与示例，讲清插件如何接入 Agent、注册命令、传递上下文，想给 Cursor 写扩展可以从这里起步。

### Skill / 垂直工具

- **[storytold/photocraft](https://github.com/storytold/photocraft)** — 用纯 Rust 从零重写的开源图片编辑器，目标对齐 Photoshop：图层、蒙版、调整层、PSD 读写都在，且不依赖 Electron，离线可用。
- **[DmNote-App/DmNote](https://github.com/DmNote-App/DmNote)** — 给 DJMAX RESPECT V 做的按键显示器，也能用于其他游戏；把实时按键投到副屏或直播画面，支持自定义皮肤，配置很简单。
- **[Kruk2/jasna](https://github.com/Kruk2/jasna)** — 本地视频与图片修复工具，用 GPU 跑修复模型，同时提供桌面界面和命令行，适合成批处理素材。
- **[hmjz100/LinkSwift](https://github.com/hmjz100/LinkSwift)** — 用 JavaScript 写的网盘直链解析脚本，覆盖百度、阿里、夸克等八家网盘，把分享链接转成可以交给下载器使用的直链。

[全部日报](daily/) · [本期 Markdown](daily/2026-10-20.md)

### 最近更新

| 日期 | 项目数 | 导读 |
| --- | --- | --- |
| [2026-10-20](daily/2026-10-20.md) | 10 | 今天的候选池里，Agent 工具正从「能跑」转向「跑得更省、更稳」：有人压缩上下文，有人把多个 Agent 拉进同一张工作台；另一边，纯 Rust 重写的桌面软件和本地推理引擎也在冒头。 |

<!-- DIGEST:END -->

## 它是怎么工作的

1. **收集候选**：抓取 GitHub Trending（总榜 + 6 个语言分榜）、GitHub Search（最近 30 天 / 180 天冒头的新项目、`ai-agents` 话题）和 Hacker News 上被讨论的 GitHub 仓库，合并去重。
2. **过滤与打分**：丢掉 awesome-list、教程、面试题、长期不更新的仓库，以及近 60 天已经推荐过的项目；按 star 数、当日新增 star、HN 热度、项目年龄做初排。
3. **补全信息**：按方向均衡挑出 24 个候选（避免清一色 Agent 框架），拉取仓库元数据和 README 摘要作为判断依据。
4. **精选与写作**：调用 LLM（默认 DeepSeek，任意 OpenAI 兼容接口均可），从候选池里挑 10 个，按方向归类，并写中文导读；没有配置 Key 时退回启发式榜单，仍然会生成文件。
5. **写入仓库**：每天新增一份 `daily/YYYY-MM-DD.md`，同时更新 README 的「最新一期 / 最近更新」，由 GitHub Actions 自动提交。

整个流水线只依赖 Python 标准库，不需要 `pip install`。

## 本地运行

```bash
# 生成今天的日报（需要能访问 GitHub；未配置 token 时受 60 次/小时限流）
python3 scripts/main.py

# 生成指定日期
python3 scripts/main.py --date 2026-10-20

# 只根据已保存的数据重新生成 md 和 README
python3 scripts/main.py --rebuild
```

想生成中文导读，先导出 Key：

```bash
export LLM_API_KEY="sk-..."
# 可选：切换模型服务
export LLM_BASE_URL="https://api.deepseek.com/v1"
export LLM_MODEL="deepseek-chat"
python3 scripts/main.py --date 2026-10-20 --force
```

## 每天自动更新

仓库已经包含 `.github/workflows/daily.yml`：

- 每天 `23:00 UTC`（北京时间次日 07:00）运行，也可以在 Actions 页面手动触发；
- 自动提交 `daily/`、`data/` 和 README；README 里 `<!-- DIGEST:START -->` 到 `<!-- DIGEST:END -->` 之间的内容由脚本维护，不要手改；
- 手动触发时可以指定日期、强制重跑，或只重建 md。

启用步骤：

1. 把代码推到 GitHub。
2. 在 **Settings → Secrets and variables → Actions** 添加 `LLM_API_KEY`（不配也能跑，但摘要会保留英文简介）。可选添加 Variables：`LLM_BASE_URL`、`LLM_MODEL`。
3. 在 **Actions** 里手动跑一次 `Daily Digest`，确认能提交。

不需要 GitHub Pages，也不需要 GH_PAT。

## 改哪里

- `config.json`：每天数量、冷却天数、数据源开关、排除规则、分类、LLM 参数。
- `scripts/sources.py`：抓取与解析。
- `scripts/curate.py`：过滤、打分、LLM 提示词与校验。
- `scripts/render.py`：Markdown 与 README 输出。
- `data/seen.json`：已推荐项目记录，用来避免短期重复。
- `data/digests/YYYY-MM-DD.json`：每期的结构化数据，`--rebuild` 由它重新生成 md。
- `data/overrides/YYYY-MM-DD.json`：人工校对入口，可覆盖某天的导读、分类和单条摘要；`daily/` 下的文件是生成物，直接改会被下次重建覆盖。

## 目录

```
.github/workflows/daily.yml   每日定时任务
config.json                   全部可调参数
scripts/                      抓取 → 精选 → 生成 Markdown
daily/YYYY-MM-DD.md           每天一份日报
data/digests/                 每期 JSON 数据
data/seen.json                推荐历史（去重）
```
