# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 AI 编程 Skills 集合，专注于代码开发工作流。所有 Skills 已翻译为中文，技术术语保留英文。

## 项目结构

```
skills/
├── frontend-master/     # 大师级前端开发（含设计数据库、模板）
├── skill-creator/       # Skill 创建工具（含初始化和打包脚本）
└── superpowers/         # 开发增强套件（14 个子技能）
```

## Skill 文件规范

每个 Skill 必须包含 `SKILL.md`，结构如下：

```yaml
---
name: skill-name
description: 触发条件和功能描述（这是唯一决定 Skill 何时被使用的字段）
---
# Markdown 正文（仅在触发后加载）
```

可选资源目录：
- `scripts/` - 可执行脚本
- `references/` - 参考文档（按需加载）
- `assets/` - 输出资源（模板、图片等）

## 常用命令

```bash
# 初始化新 Skill
python skills/skill-creator/scripts/init_skill.py <skill-name> --path <output-dir>

# 打包 Skill（含验证）
python skills/skill-creator/scripts/package_skill.py <path/to/skill>

# 快速验证 Skill
python skills/skill-creator/scripts/quick_validate.py <path/to/skill>
```

## superpowers 工作流

推荐的开发流程：

```
brainstorming → writing-plans → executing-plans → test-driven-development
    → requesting-code-review → finishing-a-development-branch
```

调试流程：`systematic-debugging`

## 编写 Skill 的关键原则

1. **简洁优先** - Context window 是公共资源，只添加 Claude 不知道的信息
2. **description 是触发器** - 所有"何时使用"的信息必须在 frontmatter 的 description 中
3. **渐进式加载** - 大文件拆分到 `references/`，按需读取
4. **不要创建冗余文档** - 不需要 README、CHANGELOG 等辅助文件
