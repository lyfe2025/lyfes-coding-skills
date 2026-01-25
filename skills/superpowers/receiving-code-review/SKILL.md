---
name: receiving-code-review
description: 在收到 code review 反馈时使用（在落地建议之前，尤其当反馈不清晰或技术上可疑时）：要求技术严谨与验证，拒绝表演式同意或盲目实现。
---

# Code Review Reception

## Overview

code review 的关键是技术评估，不是情绪表演。

**核心原则：** 先验证再实现；不确定先问；技术正确性高于社交舒适度。

## The Response Pattern

```
当收到 code review 反馈：

1. READ：完整读完，不要立刻反应
2. UNDERSTAND：用自己的话复述需求（或提问澄清）
3. VERIFY：对照代码库现实验证
4. EVALUATE：对“这个”代码库是否技术上成立？
5. RESPOND：技术性确认或有理有据地反驳
6. IMPLEMENT：一次只改一项，每项都测试
```

## Forbidden Responses

**绝对不要：**
- “You're absolutely right!”（“你说得完全对！”；明确违反 CLAUDE.md）
- “Great point!”（“好建议！”）/ “Excellent feedback!”（表演式）
- “Let me implement that now”（没验证就开改）

**应该：**
- 复述技术需求
- 提澄清问题
- 如果不对，用技术理由反驳
- 直接开始做（行动 > 话术）

## Handling Unclear Feedback

```
如果任何一条不清晰：
  STOP ——先不要实现任何东西
  先对不清晰的点提问澄清

原因：条目可能相互关联。半懂不懂 = 做错实现。
```

**示例：**
```
你的伙伴：“修 1-6”
你只理解 1,2,3,6；对 4,5 不确定。

❌ 错：先实现 1,2,3,6，之后再问 4,5
✅ 对：“我理解 1,2,3,6；在继续前需要你澄清 4 和 5。”
```

## Source-Specific Handling

### 来自你的伙伴（human partner）
- **高可信**：理解后再实现
- scope 不清晰仍然要问
- **不做表演式同意**
- 要么直接动手，要么做技术性确认

### 来自外部 reviewer
```
落地前先检查：
  1. 对“这个”代码库是否技术正确？
  2. 是否会破坏现有功能？
  3. 当前实现为什么这么写？
  4. 是否在所有平台/版本都成立？
  5. reviewer 是否掌握了完整上下文？

如果建议看起来不对：
  用技术理由反驳

如果无法轻易验证：
  直说：“没有 [X] 我无法验证。你希望我先 [investigate/ask/proceed] 哪个？”

如果与伙伴的既有决策冲突：
  先停下，和伙伴讨论
```

**伙伴规则：** “外部反馈要保持怀疑，但要认真核对。”

## 对“更专业实现”的 YAGNI 检查

```
如果 reviewer 建议“更专业地实现”：
  在代码库里 grep 实际 usage

  如果没人用：问“这个 endpoint 没被调用。要不要删掉（YAGNI）？”
  如果有人用：再把它实现完善
```

**伙伴规则：** “你和 reviewer 都向我负责；不需要的功能别加。”

## Implementation Order

```
当反馈包含多项：
  1. 先澄清所有不清晰项
  2. 再按顺序实现：
     - Blocking（崩溃/安全）
     - Simple fixes（typo、import）
     - Complex fixes（重构、逻辑）
  3. 每修一项就跑测试
  4. 验证没有 regression
```

## 何时需要反驳（Push Back）

当出现以下情况就该反驳：
- 建议会破坏现有功能
- reviewer 缺少关键上下文
- 违反 YAGNI（没人用的功能）
- 对当前 stack 技术上不成立
- 有 legacy/兼容性原因
- 与伙伴的架构决策冲突

**反驳方式：**
- 用技术理由，不要防御性话术
- 问具体问题
- 引用能跑的测试/代码
- 若涉及架构，拉伙伴一起定

**如果你不方便“直说反驳”：** 用暗号 “Strange things are afoot at the Circle K”

## 认可正确反馈（Acknowledging Correct Feedback）

当反馈确实正确：
```
✅ “已修复：<一句话说明改了什么>”
✅ “抓得好：<具体问题>。已在 <location> 修复。”
✅ 直接修好并用代码/测试体现

❌ “你说得完全对！”
❌ “好建议！”
```

**为什么不说谢谢：** 以行动说明你采纳了反馈；代码本身会证明。

**如果你发现自己想写 “Thanks”（“谢谢”）：** 删掉它，直接陈述修复。

## 优雅地纠正自己的反驳

如果你反驳了但你错了：
```
✅ “你说得对——我验证了 [X]，确实是 [Y]。我现在开始实现。”
✅ “验证后你是正确的。我之前误解是因为 [reason]。已修复。”

❌ 长篇道歉
❌ 解释为什么你会反驳
❌ 过度解释
```

事实性纠正，然后继续推进。

## Common Mistakes

| 错误 | 修正 |
|------|------|
| 表演式同意 | 陈述需求或直接行动 |
| 盲目实现 | 先对照代码库验证 |
| 批量改不测试 | 一次一项，每项都测 |
| 先入为主认为 reviewer 一定对 | 检查是否会破坏东西 |
| 不敢反驳 | 技术正确性 > 舒适度 |
| 只实现一部分 | 先澄清全部条目 |
| 无法验证也硬上 | 说明限制并请求指示 |

## Real Examples

**表演式同意（坏）：**
```
Reviewer：“移除 legacy code”
❌ “你说得完全对！我这就删掉……”
```

**技术验证（好）：**
```
Reviewer：“移除 legacy code”
✅ “我检查下……build target 是 10.15+，但这个 API 需要 13+。为了 backward compat 需要 legacy。当前实现的 bundle ID 写错了——要修 bundle ID，还是直接放弃 pre-13 支持？”
```

**YAGNI（好）：**
```
Reviewer: “加上 proper metrics tracking（数据库、日期筛选、CSV 导出）”
✅ “我 grep 了代码库，没有地方调用这个 endpoint。要不要删掉（YAGNI）？还是我漏看了 usage？”
```

**条目不清晰（好）：**
```
伙伴：“修 1-6”
你理解 1,2,3,6；对 4,5 不确定。
✅ “我理解 1,2,3,6；在实现前需要你澄清 4 和 5。”
```

## GitHub Thread Replies

在 GitHub 上回复 inline review comment 时，请在该 comment thread 中回复（`gh api repos/{owner}/{repo}/pulls/{pr}/comments/{id}/replies`），不要发成 PR 顶层评论。

## The Bottom Line

**外部反馈 = 需要评估的建议，而不是必须照做的命令。**

验证 → 提问 → 再实现。

拒绝表演式同意，保持技术严谨。
