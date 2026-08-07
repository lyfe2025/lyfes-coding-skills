---
name: using-git-worktrees
description: 当你要开始需要与当前 workspace 隔离的 feature 开发，或在执行 implementation plan 之前使用：创建隔离的 git worktree，并包含目录选择与安全校验。
---

# Using Git Worktrees

## Overview

git worktree 能在同一个 repo 上创建多个隔离工作区，让你同时在多个分支工作而无需频繁切分支。

**核心原则：** 系统化目录选择 + 安全校验 = 可靠隔离。

**开始时宣告：** “我正在使用 using-git-worktrees skill 来创建隔离工作区。”

## Directory Selection Process

### 0) 先检查宿主能力与当前状态

先确认当前是否已经位于 linked worktree，并检查仓库根目录与 submodule 边界：

```bash
git rev-parse --show-toplevel
git rev-parse --git-common-dir
git worktree list
git submodule status 2>/dev/null
```

如果宿主提供原生 worktree 工具（例如 Claude Code 的 `EnterWorktree` / `ExitWorktree`），优先使用它；只有宿主没有该能力时，才继续使用下面的 `git worktree add` fallback。不要把某个宿主 API 当作所有环境都存在的前提，也不要在 submodule 内误操作父仓库的 worktree。

如果创建因 sandbox 或权限限制失败，必须明确报告隔离没有成功，并按宿主允许的方式回退；不得声称已经创建了隔离 workspace。

按以下优先级顺序选择 worktree 目录：

### 1) 检查是否已有目录

```bash
# 按优先级检查
ls -d .worktrees 2>/dev/null     # 首选（隐藏目录）
ls -d worktrees 2>/dev/null      # 备选
```

**如果找到：** 使用该目录；如果两个都存在，以 `.worktrees` 为准。

### 2) 检查 CLAUDE.md

```bash
grep -i "worktree.*director" CLAUDE.md 2>/dev/null
```

**如果已指定偏好：** 不用问，直接按它执行。

### 3) 询问用户

如果没有现成目录，也没有 CLAUDE.md 偏好：

```
没找到 worktree 目录。你希望我把 worktree 放在哪？

1. .worktrees/（项目内，隐藏目录）
2. 其他由宿主或用户明确指定的位置

你选哪一个？
```

不要默认使用历史的全局 Superpowers worktree 路径；如果用户明确指定外部目录，仍须确认该目录的 ownership 和清理责任。

## Safety Verification

### 对项目内目录（.worktrees 或 worktrees）

**创建 worktree 前必须验证该目录被 git ignore：**

```bash
# 检查目录是否被忽略（同时尊重 local/global/system gitignore）
git check-ignore -q .worktrees 2>/dev/null || git check-ignore -q worktrees 2>/dev/null
```

**如果没有被忽略：**

按规则“坏的立刻修”：
1. 在 `.gitignore` 加入对应行
2. 提交该变更
3. 再继续创建 worktree

**为什么关键：** 防止 worktree 内容被意外纳入 repo 追踪并被提交。

### 对用户明确指定的项目外目录

无需 `.gitignore` 校验，因为它在项目目录之外；但必须记录由谁创建和谁负责清理，避免删除宿主管理的 workspace。

## Creation Steps

### 1) 识别项目名

```bash
project=$(basename "$(git rev-parse --show-toplevel)")
```

### 2) 创建 worktree

```bash
# 计算完整路径
case $LOCATION in
  .worktrees|worktrees)
    path="$LOCATION/$BRANCH_NAME"
    ;;
  /*)
    # 仅使用用户或宿主明确指定的项目外绝对路径。
    path="$LOCATION/$project/$BRANCH_NAME"
    ;;
esac

# 创建 worktree 并新建分支
git worktree add "$path" -b "$BRANCH_NAME"
cd "$path"
```

### 3) 运行项目 setup

自动检测并运行适配的依赖安装/初始化：

```bash
# Node.js
if [ -f package.json ]; then npm install; fi

# Rust
if [ -f Cargo.toml ]; then cargo build; fi

# Python
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then poetry install; fi

# Go
if [ -f go.mod ]; then go mod download; fi
```

### 4) 验证干净基线（Clean baseline）

跑测试确保 worktree 起点干净：

```bash
# 示例：使用项目实际的测试命令
npm test
cargo test
pytest
go test ./...
```

**如果测试失败：** 展示失败并询问要继续还是先调查。  
**如果测试通过：** 汇报“可以开始”。

### 5) 汇报位置

```
Worktree 已就绪：<full-path>
测试通过（<N> tests，0 failures）
可以开始实现：<feature-name>
```

## Quick Reference

| 情况 | 操作 |
|------|------|
| `.worktrees/` 存在 | 使用它（并验证已 ignore） |
| `worktrees/` 存在 | 使用它（并验证已 ignore） |
| 两者都存在 | 使用 `.worktrees/` |
| 都不存在 | 查 CLAUDE.md → 询问用户 |
| 目录未被 ignore | 加到 `.gitignore` 并提交 |
| baseline 测试失败 | 展示失败并询问 |
| 无 package.json/Cargo.toml | 跳过依赖安装 |

## Common Mistakes

### 跳过 ignore 校验

- **问题：** worktree 内容被 git 追踪，污染 git status
- **修正：** 创建项目内 worktree 前永远先 `git check-ignore`

### 自己臆测目录位置

- **问题：** 造成不一致，违背项目约定
- **修正：** 按优先级：已有目录 > CLAUDE.md > 询问

### baseline 测试失败还继续

- **问题：** 无法区分新 bug 与旧问题
- **修正：** 先汇报失败并获得明确许可再继续

### 把 setup 命令写死

- **问题：** 不同项目工具链不同，容易跑挂
- **修正：** 通过项目文件自动检测（package.json 等）

## Example Workflow

```
你：我正在使用 using-git-worktrees skill 来创建隔离工作区。

[检查 .worktrees/ - 存在]
[验证已 ignore - git check-ignore 确认 .worktrees/ 被忽略]
[创建 worktree：git worktree add .worktrees/auth -b feature/auth]
[运行 npm install]
[运行 npm test - 47 passing]

Worktree 已就绪：/Users/jesse/myproject/.worktrees/auth
测试通过（47 tests，0 failures）
可以开始实现 auth feature
```

## Red Flags

**Never：**
- 未验证 ignore 就创建项目内 worktree
- 跳过 baseline 测试验证
- baseline 测试失败不问就继续
- 目录不明确时擅自决定位置
- 跳过 CLAUDE.md 检查

**Always：**
- 目录优先级：已有目录 > CLAUDE.md > 询问
- 项目内目录必须验证已 ignore
- 自动检测并运行项目 setup
- 验证干净的测试基线

## Integration

**会被调用自：**
- `brainstorming`（Phase 4）：设计确认后进入实现时要求使用
- 任何需要隔离 workspace 的 skill

**常与其配合：**
- `finishing-a-development-branch`：工作完成后的清理
- `executing-plans` / `subagent-driven-development`：在该 worktree 中执行计划
