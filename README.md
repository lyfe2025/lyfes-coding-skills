# Lyfes Coding Skills

专注于代码开发的 AI 编程 Skills 集合（中文版）。

覆盖完整开发工作流：需求分析 → 计划编写 → TDD 开发 → 代码审查 → 分支完成。

兼容 Claude Code / Codex / Cursor 等 AI 编程工具。

## Skills

| Skill | 功能 |
|-------|------|
| **frontend-master** | 大师级前端开发，反 AI 审美，设计系统持久化 |
| **skill-creator** | 创建/优化 Skill |
| **superpowers** | 完整开发工作流（14 个子技能） |

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
| writing-skills | 编写 Skills |
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
- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

## License

MIT
