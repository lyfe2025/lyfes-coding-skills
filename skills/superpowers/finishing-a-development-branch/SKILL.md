---
name: finishing-a-development-branch
description: 当实现已完成、测试已通过，需要决定如何集成这次工作时使用：通过结构化选项引导 merge/PR/保留/丢弃，并在选择后完成收尾与清理。
---

# Finishing a Development Branch

## Overview

通过给出清晰选项并执行所选 workflow，完成一次开发分支的收尾。

**核心原则：** Verify tests → 给选项 → 执行选择 → 清理。

**开始时宣告：** “我正在使用 finishing-a-development-branch skill 来完成这次工作收尾。”

## The Process

### Step 1：验证测试

**在给选项之前，必须先验证测试通过：**

```bash
# 运行项目的测试套件
npm test / cargo test / pytest / go test ./...
```

**如果测试失败：**
```
测试失败（<N> 个 failure）。必须先修复后才能收尾：

[展示失败信息]

在测试通过前，不能继续 merge/PR。
```

停止，不要进入 Step 2。

**如果测试通过：** 继续 Step 2。

### Step 2：确定 base branch

```bash
# 尝试常见 base branch
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master 2>/dev/null
```

或直接询问：“这个分支是从 main 分出来的吗？”

### Step 3：给出选项

默认只给出以下 3 个选项：

```
实现已完成。你想怎么处理？

1. 本地合并回 <base-branch>
2. push 并创建 Pull Request
3. 保留分支原样（我之后再处理）

你选哪项？
```

不要主动把 discard 放入常规菜单。只有用户明确要求丢弃时，才进入单独确认流程，并要求输入精确的 `discard`。

**不要额外解释** ——保持简短。

### Step 4：执行选择

#### 选项 1：本地合并

```bash
# 切回 base branch
git checkout <base-branch>

# 拉取最新
git pull

# 合并 feature branch
git merge <feature-branch>

# 在合并结果上再跑一次测试
<test command>

# 若测试通过
git branch -d <feature-branch>
```

然后进入：清理 worktree（Step 5）

#### 选项 2：Push 并创建 PR

```bash
# push 分支
git push -u origin <feature-branch>

# 创建 PR
gh pr create --title "<title>" --body "$(cat <<'EOF'
## 概述
<2-3 条变更摘要>

## 测试计划
- [ ] <验证步骤>
EOF
)"
```

默认保留分支与 worktree，便于后续跟进 PR（除非用户明确要求清理）。

#### 选项 3：保留原样

汇报：“保留分支 <name>。worktree 保留在 <path>。”

**不要清理 worktree。**

#### 用户明确要求丢弃：二次确认

**必须先确认：**
```
这会永久删除：
- 分支 <name>
- 所有 commits：<commit-list>
- worktree：<path>

输入 'discard' 以确认。
```

等待用户输入精确的 `discard`。

确认后：
```bash
git checkout <base-branch>
git branch -D <feature-branch>
```

然后进入：清理 worktree（Step 5）

### Step 5：清理 worktree

**对选项 1、4：**

检查是否在 worktree 中：
```bash
git worktree list | grep $(git branch --show-current)
```

如果是：
```bash
git worktree remove <worktree-path>
```

**对选项 2、3：** 保留 worktree。

## Quick Reference

| 选项 | Merge | Push | 保留 Worktree | 清理 Branch |
|------|-------|------|---------------|-------------|
| 1. 本地合并 | ✓ | - | - | ✓ |
| 2. 创建 PR | - | ✓ | ✓ | - |
| 3. 保留原样 | - | - | ✓ | - |
| 用户明确要求丢弃 | - | - | - | ✓（force） |

## Common Mistakes

**跳过测试验证**
- **问题：** 合并坏代码 / 创建会失败的 PR
- **修正：** 给选项前永远先验证测试

**开放式问题**
- **问题：** “接下来该怎么做？”→ 语义模糊
- **修正：** 默认只给 3 个结构化选项；discard 仅在用户明确要求后单独确认

**自动清理 worktree**
- **问题：** 在仍可能需要 worktree 时把它删了（选项 2、3）
- **修正：** 只在选项 1、4（以及按需的 2）做清理

**丢弃不确认**
- **问题：** 误删工作
- **修正：** 必须要求用户输入 `discard`

## Red Flags

**Never：**
- 测试失败还继续
- merge 后不在结果上验证测试
- 未确认就删除工作
- 未经明确请求就 force-push

**Always：**
- 给选项前验证测试
- 默认只给 3 个选项，不主动提供 discard
- 用户明确要求 discard 时必须 typed confirmation
- 仅在需要时清理 worktree

## Integration

**会被调用自：**
- `subagent-driven-development`（Step 7）：全部任务完成后
- `executing-plans`（Step 5）：全部 batch 完成后

**常与其配合：**
- `using-git-worktrees`：清理该 skill 创建的 worktree
