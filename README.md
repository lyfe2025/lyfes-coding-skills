# Lyfes Coding Skills

专注于代码开发的 AI 编程 Skills 集合（中文版）。

覆盖前端设计实现与完整开发工作流：设计探索 → 需求分析 → 计划编写 → TDD 开发 → 代码审查 → 分支完成。

兼容 Claude Code / Codex / Cursor 等 AI 编程工具。

## Skills

| Skill | 功能 |
|-------|------|
| **frontend-master** | 高质量前端设计与实现统一入口，支持设计研究、交互动效规范、实际验证和设计系统持久化 |
| **skill-creator** | Skill 初始化/打包工具 |
| **superpowers** | 完整开发工作流（14 个子技能） |

`skill-creator` 已选择性同步上游校验与打包能力：支持 `compatibility` 元数据、kebab-case 校验，并自动排除缓存、依赖、字节码、系统文件和根级评测目录。保留本地中文初始化流程与直接执行命令。

`superpowers` 已按 `obra/superpowers` v6.2.0 选择性优化：保留 14 个中文子技能，加入计划隔离的 SDD workspace、task brief、双 verdict review、scoped re-review、有限修复循环，以及当前 Claude Code 的原生 worktree 优先和分支收尾安全规则。不引入上游插件 hooks、marketplace 或完整评测套件。

## frontend-master

`frontend-master` 用于创建、重构或精修主页、个人品牌页、作品集、Landing Page、Dashboard、表单、卡片、导航及其他 Web UI。它会优先分析项目现有技术栈和设计系统，而不是直接套用固定页面结构或流行视觉风格。

### 六阶段设计流程

1. **Recon**：分析技术栈、现有组件、设计 token 和项目约束
2. **Frame**：明确用户、目标、内容层级、核心行动和视觉方向
3. **Research**：搜索设计数据库，将结果作为候选而非标准答案
4. **Craft**：完成设计、实现、组件状态、响应式和动效精修
5. **Persist**：按需、安全地生成或更新项目设计系统
6. **Verify**：运行项目并验证页面、交互、可访问性和异常内容

### 设计质量基线

- **模板设计**：根据内容叙事选择结构，避免默认套用 `Hero > Features > Testimonials > CTA`
- **交互质感**：区分静态与交互元素，覆盖 hover、focus、disabled、loading、error 等状态
- **动效质量**：先判断动画是否必要，优先使用 `transform` 和 `opacity`，支持 Reduced Motion
- **响应式设计**：分别组织桌面端与移动端信息，而不是简单等比例缩小
- **真实验证**：检查 375 / 768 / 1024 / 1440px、键盘、触控、长内容、缺图、控制台及项目自身命令
- **专项路由**：按需调用交互、物理动效、动效命名或审计类 Skill，不会每次加载全部能力

### 设计数据库与持久化

设计数据库已选择性同步 `ui-ux-pro-max-skill` v2.14.1，包含 84 种 UI styles、192 套语义色板、192 类产品、74 组字体搭配、161 条 UI reasoning rules，并新增 App interface、GSAP motion、Google Fonts 和 9 个技术栈数据集。

可使用 `--variance`、`--motion`、`--density`（1–10）控制视觉差异度、动效强度和信息密度：

```bash
python3 skills/frontend-master/scripts/search.py "数据分析 Dashboard" \
  --design-system \
  --variance 8 \
  --motion 6 \
  --density 9
```

独立搜索域包括 `style`、`color`、`chart`、`landing`、`product`、`ux`、`typography`、`google-fonts`、`icons`、`gsap`、`react`、`web` 和 `app`。其中 `web` 保留 Web/ARIA 规则，`app` 用于 iOS、Android 和 React Native 界面规范。

仅搜索设计建议：

```bash
python3 skills/frontend-master/scripts/search.py "个人品牌主页" --design-system
```

生成设计系统并保存 MASTER 与页面 override：

```bash
python3 skills/frontend-master/scripts/search.py "个人品牌主页" \
  --design-system \
  --persist \
  -p "名片岛" \
  --page "设计师主页"
```

默认不会覆盖已有文件；确认需要更新时显式添加 `--force`。生成结果位于：

```text
design-system/<project-slug>/MASTER.md
design-system/<project-slug>/pages/<page-slug>.md
```

<details>
<summary><b>superpowers 子技能详情</b></summary>

| 子技能 | 功能 |
|--------|------|
| brainstorming | 交互式脑暴，挖掘需求 |
| writing-plans | 编写执行计划 |
| executing-plans | 执行计划 |
| systematic-debugging | 系统化调试 |
| test-driven-development | TDD 开发 |
| requesting-code-review | 请求代码审查 |
| receiving-code-review | 接收代码审查 |
| subagent-driven-development | 子代理驱动开发 |
| dispatching-parallel-agents | 并行代理调度 |
| finishing-a-development-branch | 完成开发分支 |
| using-git-worktrees | Git Worktrees 使用 |
| verification-before-completion | 完成前验证 |
| writing-skills | Skill 内容编写 + TDD 验证 |
| using-superpowers | Superpowers 使用指南 |

</details>

## 安装

### AI 一键导入

复制以下提示词发给你的 AI 编程工具：

**Claude Code:**

```
帮我导入 lyfes-coding-skills 的全部 Skills：
1. 克隆仓库到本地：git clone https://github.com/lyfe2025/lyfes-coding-skills.git
2. 在 ~/.claude/skills/ 下创建符号链接（superpowers 需要链接其子目录而非目录本身）：
   - skills/frontend-master
   - skills/skill-creator
   - skills/superpowers/* （展开为各子技能目录）
3. 验证：列出 ~/.claude/skills/ 确认能看到 brainstorming、test-driven-development 等子技能
```

**Codex / Cursor / 其他工具:**

```
帮我导入 lyfes-coding-skills 的全部 Skills：
1. 克隆仓库：git clone https://github.com/lyfe2025/lyfes-coding-skills.git
2. 将以下两个路径都加入工具的 skills 配置：
   - /path/to/lyfes-coding-skills/skills
   - /path/to/lyfes-coding-skills/skills/superpowers
3. 验证：确认能识别到 superpowers 的各子技能
```

### 手动安装

```bash
git clone https://github.com/lyfe2025/lyfes-coding-skills.git
```

**Claude Code:**

```bash
# 符号链接到 ~/.claude/skills/
ln -s /path/to/lyfes-coding-skills/skills/frontend-master ~/.claude/skills/
ln -s /path/to/lyfes-coding-skills/skills/skill-creator ~/.claude/skills/
ln -s /path/to/lyfes-coding-skills/skills/superpowers/* ~/.claude/skills/
```

或在 `.claude/settings.local.json` 中配置：

```json
{
  "skills": {
    "paths": [
      "/path/to/lyfes-coding-skills/skills",
      "/path/to/lyfes-coding-skills/skills/superpowers"
    ]
  }
}
```

**其他工具:**

- **Codex**: 将 `skills` 和 `skills/superpowers` 添加到 agents 配置
- **Cursor**: 在 `.cursor/rules` 中引用 SKILL.md 内容

## 目录结构

```
skills/
├── frontend-master/     # 大师级前端开发
├── skill-creator/       # Skill 创建工具
└── superpowers/         # 开发增强套件（14 个子技能）
```

## 致谢

- [anthropics/skills](https://github.com/anthropics/skills)
- [obra/superpowers](https://github.com/obra/superpowers)
- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) — 选择性同步至 v2.14.1（`abb7f2f`），保留本仓库中文工作流与持久化约定

## License

MIT
