# Repository Guidelines

## 项目结构与模块组织

- `skills/`：所有 Skill 的目录。每个 skill 必须包含入口文件 `SKILL.md`。
  - 常见子目录：`references/`（按需加载的参考文档）、`scripts/`（可执行脚本）、`templates/`/`assets/`（输出时复制/引用的模板与资源）、`data/`（脚本使用的数据集）。
  - 示例：`skills/frontend-master/`、`skills/superpowers/<sub-skill>/`。
- `.claude/`：本仓库的 Claude Code 本地配置（尽量少改；不要提交任何密钥）。
- `README.md`：仓库概览与 Skill 清单。

## 构建、测试与开发命令

本仓库以 Markdown 为主，配套少量 Python 脚本（通常无“构建”步骤）。

- 新建 skill 骨架：`python3 skills/skill-creator/scripts/init_skill.py my-new-skill --path skills`
- 快速校验 skill frontmatter：`python3 skills/skill-creator/scripts/quick_validate.py skills/my-new-skill`
- 打包 skill（生成可分发文件）：`python3 skills/skill-creator/scripts/package_skill.py skills/my-new-skill ./dist`

提示：校验脚本依赖 PyYAML；如缺失可安装：`python3 -m pip install pyyaml`。

## 代码风格与命名约定

- Skill 命名：目录名与 frontmatter 的 `name` 使用 hyphen-case（如 `my-new-skill`）。
- `SKILL.md` 必须以 YAML frontmatter 开头（`---` … `---`），且包含 `name` 与 `description`。
- 文档写法：尽量短、可执行；优先给示例、清单、决策树，少写长段落背景。
- 中文优化：正文以中文为主；技术术语保留英文（如 `YAML`、`frontmatter`、`PR`）；简单标题词可用英文（如 `Overview`、`Workflow`）；示例 prompt/说明尽量用中文。
- Python：保持现有风格（4 空格缩进；标准库 import 优先）。

## 测试与验证

- 当前无统一测试套件；把 `quick_validate.py` 视为最低限度的 smoke check。
- 提交 PR 前：对新增/修改的 skill 目录运行校验，并确认文档里提到的路径与命令在仓库内确实存在。

## Commit 与 PR 规范

- Commit 风格：本仓库使用 Conventional Commits，例如 `feat: …`、`fix: …`、`chore(skills): …`。
- PR 至少包含：改了什么、为什么改，以及 1–2 条“触发示例 prompt”（让人一眼知道该 skill 何时应被调用，例如“帮我为 SaaS dashboard 设计一个侧边栏导航组件”）。
- 新增/删除顶级 skill 时，同步更新 `README.md` 里的清单信息。
