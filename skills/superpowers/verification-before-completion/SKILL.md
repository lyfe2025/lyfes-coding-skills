---
name: verification-before-completion
description: 在你准备声称“已完成/已修复/已通过”之前使用（尤其在 commit 或提 PR 前）：必须运行 verification 命令并核对输出；永远 Evidence before assertions。
---

# Verification Before Completion

## Overview

不做验证就声称完成，不是效率，而是失信。

**核心原则：** 永远先给证据（evidence），再做断言（claim）。

**只遵守字面、不遵守精神，就是在违反这条规则。**

## The Iron Law

```
没有新的验证证据，就不能做“完成/通过”的声明
```

如果你没有在“当前这条消息/当前这次操作”里运行验证命令，就不能声称它通过。

## The Gate Function

```
在声称任何状态或表达满意之前：

1. IDENTIFY：什么命令能证明你的说法？
2. RUN：执行完整命令（fresh、完整）
3. READ：阅读完整输出，检查 exit code，统计失败数
4. VERIFY：输出是否真的支持你的结论？
   - NO：如实说明当前状态，并给出证据
   - YES：带证据给出结论
5. ONLY THEN：再做声明

漏一步 = 在撒谎（不是在验证）
```

## Common Failures

| 声明 | 需要的证据 | 不够的证据 |
|------|------------|------------|
| 测试通过 | 测试命令输出：0 failures | 之前跑过、“应该能过” |
| Linter 干净 | linter 输出：0 errors | 只跑了部分检查、凭感觉外推 |
| Build 成功 | build 命令：exit 0 | linter 过了、日志看起来不错 |
| Bug 修复了 | 复现原症状：通过 | 代码改了、假设修好了 |
| Regression test 有效 | 验证过 TDD red-green cycle | 测试只跑过一次 |
| Agent 完成了 | VCS diff 展示了变更 | agent 口头“成功” |
| 满足需求 | 逐条 checklist 验证 | 仅仅“测试过了” |

## Red Flags（立刻停）

- 使用“应该 / 大概 / 看起来像”
- 在验证前表达满意（“太好了”“完美”“搞定”等）
- 没验证就准备 commit/push/PR
- 盲信 agent 的成功汇报
- 依赖部分验证
- 觉得“就这一次”
- 太累、只想快点结束
- **任何暗示成功/完成但没跑验证的措辞**

## 防止自我合理化（Rationalization）

| 借口 | 现实 |
|------|------|
| “现在应该能行了” | 去跑验证 |
| “我很有把握” | 信心 ≠ 证据 |
| “就这一次” | 没有例外 |
| “linter 过了” | linter ≠ compiler/build |
| “agent 说 OK 了” | 你要独立验证 |
| “我太累了” | 疲惫 ≠ 免检 |
| “部分检查够了” | 部分不能证明整体 |
| “换个说法就不算” | 以精神为准，不钻字眼 |

## Key Patterns

**Tests：**
```
✅ [运行测试命令] [看到：34/34 pass] “测试全部通过”
❌ “现在应该能过了” / “看起来没问题”
```

**Regression tests（TDD Red-Green）：**
```
✅ 写测试 → 跑（通过）→ 回滚修复 → 再跑（必须失败）→ 恢复修复 → 再跑（通过）
❌ “我写了回归测试”（但没验证 red-green）
```

**Build：**
```
✅ [运行 build] [看到：exit 0] “Build 通过”
❌ “linter 过了”（linter 不保证能编译/打包）
```

**Requirements：**
```
✅ 重读 plan → 做 checklist → 逐条验证 → 汇报缺口或完成
❌ “测试过了，这个阶段完成了”
```

**Agent delegation：**
```
✅ agent 汇报成功 → 检查 VCS diff → 验证变更 → 如实汇报状态
❌ 直接相信 agent
```

## Why This Matters

来自真实失败案例的教训：
- 伙伴说“我不相信你”——信任被破坏
- 未定义函数上线——直接 crash
- 需求缺失上线——功能不完整
- “假完成”导致反复返工与时间浪费
- 违背原则：“诚实是核心价值；如果你撒谎，你会被替换。”

## When To Apply

**永远在以下情况之前使用：**
- 任何形式的成功/完成声明
- 任何满意/肯定表达
- 任何对工作状态的正面判断
- commit、创建 PR、标记任务完成
- 切换到下一项任务
- 委派给其他 agent

**规则覆盖：**
- 原句、同义改写
- 暗示性表达
- 任何让人以为“已经完成/正确”的沟通

## The Bottom Line

**验证没有捷径。**

跑命令，读输出，然后再做结论。

不可协商。
