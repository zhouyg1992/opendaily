# 开发与运行说明

## 它是怎么工作的

1. **收集候选**：抓取 GitHub Trending（总榜 + 6 个语言分榜）、GitHub Search（最近 30 天 / 180 天冒头的新项目、`ai-agents` 话题）和 Hacker News 上被讨论的 GitHub 仓库，合并去重。
2. **过滤与打分**：丢掉 awesome-list、教程、面试题、长期不更新的仓库，以及近 60 天已经推荐过的项目；按 star 数、当日新增 star、HN 热度、项目年龄做初排。
3. **补全信息**：按方向均衡挑出 24 个候选（避免清一色 Agent 框架），拉取仓库元数据和 README 摘要作为判断依据。
4. **精选与写作**：调用 LLM（默认 DeepSeek，任意 OpenAI 兼容接口均可），从候选池里挑 10 个，按方向归类，同时写中英双语的「是什么」和「可以怎么借」；两种语言都原生写作，不做逐字翻译。没有配置 Key 时退回启发式榜单，仍然会生成文件。
5. **写入仓库**：每天为每个 locale 写一份 `daily/<locale>/YYYY-MM-DD.md`，同时更新对应 README 的最新一期，由 GitHub Actions 自动提交。

整个流水线只依赖 Python 标准库，不需要 `pip install`。

当前配置的语言是 `zh` 和 `en`，在 `config.json` 的 `locales` 里维护。

## 本地运行

```bash
# 生成今天的日报（需要能访问 GitHub；未配置 token 时受 60 次/小时限流）
python3 scripts/main.py

# 生成指定日期
python3 scripts/main.py --date 2026-10-20

# 只根据已保存的数据重新生成 md 和 README
python3 scripts/main.py --rebuild
```

想生成双语导读，先导出 Key：

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
- 自动提交 `daily/`、`data/`、`README.md` 和 `README.en.md`；两个 README 里 `<!-- DIGEST:START -->` 到 `<!-- DIGEST:END -->` 之间的内容由脚本维护，不要手改；
- 手动触发时可以指定日期、强制重跑，或只重建 md。

启用步骤：

1. 把代码推到 GitHub。
2. 在 **Settings → Secrets and variables → Actions** 添加 `LLM_API_KEY`（不配也能跑，但摘要会保留项目原始简介）。可选添加 Variables：`LLM_BASE_URL`、`LLM_MODEL`。
3. 在 **Actions** 里手动跑一次 `Daily Digest`，确认能提交。

不需要 GitHub Pages，也不需要 GH_PAT。

## 改哪里

- `config.json`：每天数量、冷却天数、数据源开关、排除规则、分类、LLM 参数、支持的语言。
- `scripts/sources.py`：抓取与解析。
- `scripts/curate.py`：过滤、打分、LLM 提示词与校验。
- `scripts/render.py`：按 locale 生成 Markdown 与 README 输出。
- `i18n/zh.json`、`i18n/en.json`：界面文案、星期、分类译名。
- `data/seen.json`：已推荐项目记录，用来避免短期重复。
- `data/digests/YYYY-MM-DD.json`：每期的双语结构化数据，`--rebuild` 由它重新生成 md。
- `data/overrides/YYYY-MM-DD.json`：人工校对入口，按 locale 覆盖某天的导读、分类、摘要和灵感：

```json
{
  "zh": {
    "intro": "...",
    "items": {
      "owner/repo": {"summary": "...", "insight": "..."}
    }
  },
  "en": {
    "intro": "...",
    "items": {
      "owner/repo": {"summary": "...", "insight": "..."}
    }
  }
}
```

`daily/` 下的文件是生成物，直接改会被下次重建覆盖。

## 目录

```
.github/workflows/daily.yml   每日定时任务
config.json                   全部可调参数
scripts/                      抓取 → 精选 → 生成 Markdown
README.md / README.en.md      中文 / 英文首页
daily/zh/YYYY-MM-DD.md        中文日报
daily/en/YYYY-MM-DD.md        英文日报
i18n/zh.json, en.json         界面文案与分类译名
data/digests/                 每期双语 JSON 数据
data/seen.json                推荐历史（去重）
```
