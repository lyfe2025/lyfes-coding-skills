---
name: writing-plans
description: 当你有 spec/requirements 且任务需要多步推进时使用；在动代码之前先写出可执行的 implementation plan。
---

# Writing Plans

## Overview

写一份“即使工程师对代码库零上下文、审美存疑也能照做”的实现计划：每个任务要改哪些文件、要写哪些代码、要跑哪些测试、要看哪些文档、怎么验证。把计划拆成可咀嚼的小任务。坚持 DRY / YAGNI / TDD，并保持频繁提交（frequent commits）。

假设对方是熟练开发者，但几乎不了解你的工具链与业务域；也假设对方对测试设计不够擅长，所以计划要把测试写清楚。

**开始时宣告：** “我正在使用 writing-plans skill 来编写实现计划。”

**Context：** 建议在独立 worktree 中编写与执行（由 brainstorming/using-git-worktrees 创建）。

**计划保存到：** `docs/plans/YYYY-MM-DD-<feature-name>.md`

## Bite-Sized Task Granularity

**每一步只做一个动作（2–5 分钟可完成）：**
- “写一个会失败的测试” ——一步
- “运行它，确认会失败” ——一步
- “写最小实现，让测试通过” ——一步
- “运行测试，确认通过” ——一步
- “提交 commit” ——一步

## 计划文档 Header

**每份计划必须以以下 header 开头：**

```markdown
# [功能名] Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: 使用 superpowers:executing-plans 按 task-by-task 执行本计划。

**Goal:** [一句话说明要构建什么]

**Architecture:** [2–3 句说明总体思路]

**Tech Stack:** [关键技术/库]

---
```

## Plan 自审

开始执行前必须检查：

- **Global Constraints**：明确范围、技术限制、兼容契约和不可做事项。
- **Interfaces**：列出修改/新增函数、CLI、文件格式或组件接口。
- 每个 task 都能独立测试和 review，文件路径准确，验收条件可执行。
- 不含 TBD、TODO、“补充适当测试”等未决占位符，也不加入假设的未来需求。
- 测试命令、预期失败/通过现象和依赖关系完整。

## Task 结构

```markdown
### Task N: [组件/模块名]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

**Step 1: 写一个会失败的测试**

```python
def test_specific_behavior():
    result = function(input)
    assert result == expected
```

**Step 2: 运行测试，确认它失败**

运行：`pytest tests/path/test.py::test_name -v`
预期：FAIL，并提示 "function not defined"

**Step 3: 写最小实现**

```python
def function(input):
    return expected
```

**Step 4: 运行测试，确认它通过**

运行：`pytest tests/path/test.py::test_name -v`
预期：PASS

**Step 5: Commit**

```bash
git add tests/path/test.py src/path/file.py
git commit -m "feat: add specific feature"
```
```

## Remember
- 路径必须精确（Exact file paths）
- 计划里给出完整代码，不要只写“加校验”
- 命令必须精确，并写清预期输出/现象
- 用 `@` 语法引用相关 skills
- DRY、YAGNI、TDD、frequent commits

## Execution Handoff

保存计划后，给出执行方式选择：

**“计划已保存到 `docs/plans/<filename>.md`。有两种执行方式：”**

**1) Subagent-Driven（本 session）**：每个 task 派发新的 subagent，task 间 review，迭代快

**2) Parallel Session（独立 session）**：开新 session 使用 executing-plans，按 batch 执行并在 checkpoint 做 review

**你选哪种？**

**如果选择 Subagent-Driven：**
- **必用子 skill：** `superpowers:subagent-driven-development`
- 保持在本 session
- 每 task 一个新 subagent + code review

**如果选择 Parallel Session：**
- 引导对方在 worktree 中开新 session
- **必用子 skill：** 新 session 使用 `superpowers:executing-plans`
