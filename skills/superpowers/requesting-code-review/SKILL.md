---
name: requesting-code-review
description: 在任务接近完成、实现重大功能或合并前使用：通过 code review 验证实现是否满足需求并尽早发现问题。
---

# Requesting Code Review

派发 `superpowers:code-reviewer` subagent，在问题扩散前把它们抓出来。

**核心原则：** 早 review，常 review。

## 何时请求 Review

**必须：**
- subagent-driven development：每完成一个 task 就 review
- 完成重大 feature 后
- 合并到 main 之前

**可选但很值：**
- 遇到卡点（需要新视角）
- 重构前（先确认 baseline）
- 修复杂 bug 后

## 如何请求 Review

**1) 获取 git SHA：**
```bash
BASE_SHA=$(git rev-parse HEAD~1)  # 或 origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

**2) 派发 code-reviewer subagent：**

使用 Task tool，类型选择 `superpowers:code-reviewer`，并填写 `code-reviewer.md` 模板。

**占位符：**
- `{WHAT_WAS_IMPLEMENTED}`：你刚实现了什么
- `{PLAN_OR_REQUIREMENTS}`：需求/计划是什么
- `{BASE_SHA}`：起始 commit
- `{HEAD_SHA}`：结束 commit
- `{DESCRIPTION}`：简要说明

**3) 处理反馈：**
- Critical：立刻修
- Important：继续之前修
- Minor：记录后续再处理
- 如果 reviewer 判断有误：用清晰的技术理由反驳（给证据）

## 示例

```
[刚完成 Task 2：添加验证函数]

你：在继续之前先做一次 code review。

BASE_SHA=$(git log --oneline | grep "Task 1" | head -1 | awk '{print $1}')
HEAD_SHA=$(git rev-parse HEAD)

[派发 superpowers:code-reviewer subagent]
  WHAT_WAS_IMPLEMENTED: 对话索引的验证与修复函数
  PLAN_OR_REQUIREMENTS: docs/plans/deployment-plan.md 中的 Task 2
  BASE_SHA: a7981ec
  HEAD_SHA: 3df7661
  DESCRIPTION: 新增 verifyIndex() 和 repairIndex()，覆盖 4 类问题

[Subagent 返回]
  优点：架构清晰、测试真实
  问题：
    重要：缺少进度提示
    次要：报告间隔的 magic number（100）
  结论：可以继续

你：[补上进度提示]
[继续 Task 3]
```

## 与其他 Workflow 的集成

**Subagent-Driven Development：**
- 每个 task 之后 review
- 在问题叠加之前抓住它
- 修完再进入下一个 task

**Executing Plans：**
- 每个 batch（如 3 个 task）之后 review
- 获取反馈 → 修正 → 继续

**临时开发（Ad-Hoc）：**
- 合并前 review
- 卡住时 review

## Red Flags

**绝对不要：**
- 因为“很简单”就跳过 review
- 忽略 Critical
- Important 没修就继续推进
- 对合理的技术反馈强行争辩

**如果 reviewer 错了：**
- 用技术理由回击
- 展示能证明正确性的代码/测试
- 请求对方澄清具体点

模板位置：`requesting-code-review/code-reviewer.md`
