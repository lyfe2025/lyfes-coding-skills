---
name: systematic-debugging
description: 遇到任何 bug、测试失败或非预期行为时使用；在提出修复方案之前必须先完成系统化的 root cause 调查。
---

# Systematic Debugging

## Overview

乱改只会浪费时间并制造新 bug；“快速补丁”会掩盖底层问题。

**核心原则：** 在尝试任何修复之前，永远先找到 root cause。只修症状 = 失败。

**只遵守字面、不遵守精神，就是在违背 debugging。**

## The Iron Law

```
未完成 root cause 调查，禁止提出修复
```

如果你还没完成 Phase 1，就不能开始给“修复方案”。

## When to Use

适用于任何技术问题：
- 测试失败
- 线上 bug
- 非预期行为
- 性能问题
- build 失败
- 集成问题

**尤其在这些时候更要用：**
- 时间压力大（越急越容易瞎猜）
- “看起来一个 quick fix 就能搞定”
- 你已经尝试过多个修复
- 上一次修复无效
- 你并不完全理解问题

**不要因为这些理由跳过：**
- “问题很简单”（简单问题也有 root cause）
- “我赶时间”（赶工几乎必返工）
- “老板要立刻修”（系统化比瞎试更快）

## 四个阶段（Four Phases）

你必须完成当前阶段，才能进入下一阶段。

### Phase 1：Root Cause Investigation

**在尝试任何修复之前：**

1) **认真读错误信息**
   - 不要跳过 error/warning
   - 它们经常直接给出答案
   - 完整阅读 stack trace
   - 记录 line number、file path、error code

2) **稳定复现**
   - 能否可靠触发？
   - 具体复现步骤是什么？
   - 每次都发生吗？
   - 如果无法复现 → 先补数据，不要猜

3) **检查近期变更**
   - 最近有什么变化可能导致？
   - 看 git diff、最近 commits
   - 新依赖、配置变更
   - 环境差异

4) **多组件系统：先加证据采集**

当系统存在多个组件边界（CI → build → signing，API → service → database）时：

在提出修复前，先加诊断/日志来定位断点：
```
对每个组件边界：
  - 记录进入该组件的数据
  - 记录离开该组件的数据
  - 验证 environment/config 是否正确传递
  - 在每一层检查 state

跑一遍，收集证据来回答“在哪一层坏掉”
然后只针对坏掉的那层深入调查
```

示例（多层系统）：
```bash
# Layer 1: Workflow
echo "=== Secrets available in workflow: ==="
echo "IDENTITY: ${IDENTITY:+SET}${IDENTITY:-UNSET}"

# Layer 2: Build script
echo "=== Env vars in build script: ==="
env | grep IDENTITY || echo "IDENTITY not in environment"

# Layer 3: Signing script
echo "=== Keychain state: ==="
security list-keychains
security find-identity -v

# Layer 4: Actual signing
codesign --sign "$IDENTITY" --verbose=4 "$APP"
```

这会暴露：到底是哪一层坏了（secrets → workflow ✓，workflow → build ✗）。

5) **追踪数据流（Data flow）**

当错误深埋在 call stack 里：

请阅读本目录的 `root-cause-tracing.md` 获取完整的“逆向回溯”技巧。

快速版：
- 坏值从哪里来的？
- 谁把坏值传进来的？
- 一直向上追踪直到找到源头
- 在源头修复，而不是在症状处打补丁

### Phase 2：Pattern Analysis

**在修复前先找到规律：**

1) **找能工作的对照样例**
   - 在同一代码库里找相似但正常工作的代码
   - 哪些相似的东西是好的？

2) **对照参考实现**
   - 如果你在实现某个 pattern：把 reference 实现完整读完
   - 不要略读：逐行理解
   - 在套用之前先把 pattern 吃透

3) **列出差异**
   - 正常与异常之间有什么不同？
   - 把所有差异都列出来，哪怕很小
   - 不要先入为主认为“这不重要”

4) **理解依赖**
   - 这段逻辑依赖什么组件？
   - 需要哪些 settings/config/environment？
   - 它隐含了哪些假设？

### Phase 3：Hypothesis and Testing

**用科学方法：**

1) **提出一个单一假设**
   - 清晰陈述：“我认为 X 是 root cause，因为 Y”
   - 写下来
   - 要具体，不要含糊

2) **最小化验证**
   - 做最小改动来验证假设
   - 一次只改一个变量
   - 不要一次修多件事

3) **验证结果再继续**
   - 成功？→ 进入 Phase 4
   - 不成功？→ 提出新的假设
   - 不要在一个失败的假设上叠更多修复

4) **当你不知道时**
   - 直接说：“我不理解 X”
   - 不要装懂
   - 请求帮助
   - 继续调查/查资料

### Phase 4：Implementation

**修 root cause，不修症状：**

1) **先写一个会失败的测试用例**
   - 最小可复现
   - 能自动化就写自动化测试
   - 没框架就写一次性 test script
   - 修之前必须有
   - 用 `superpowers:test-driven-development` 来写合格的 failing test

2) **实现单一修复**
   - 针对已定位的 root cause
   - 一次只改一件事
   - 不要“顺手优化一下”
   - 不要捆绑式重构

3) **验证修复**
   - 测试现在通过了吗？
   - 有没有引入其他测试失败？
   - 问题真的解决了吗？

4) **如果修复无效**
   - STOP
   - 计数：你已经尝试了几次修复？
   - 如果 < 3：回到 Phase 1，用新信息重新分析
   - **如果 ≥ 3：停止并质疑架构（见第 5 点）**
   - 在没有架构讨论前，不要尝试 Fix #4

5) **当 3+ 次修复都失败：质疑架构**

   **提示存在架构问题的模式：**
   - 每次修复都会暴露新的共享状态/耦合点/不同位置的问题
   - 修复需要“巨量重构”
   - 每次修复都会在别处制造新症状

   **停止并质疑基本假设：**
   - 这个 pattern 在根上是否可靠？
   - 我们是不是“惯性地硬撑”？
   - 应该重构架构，而不是继续修症状？

   **在继续更多修复前，先与 human partner 讨论。**

   这不是“假设失败”，而是“架构不对”。

## Red Flags（停下并回到流程）

如果你发现自己在想：
- “先 quick fix，之后再查”
- “先试试改 X 看能不能行”
- “多改几处再跑测试”
- “跳过测试，我手动验证”
- “大概率是 X，我先修了”
- “我没完全懂，但可能能行”
- “pattern 说要 X，但我想换种做法”
- “主要问题是这些：……”（直接列修复项但没调查）
- 在追踪 data flow 之前就开始提方案
- **“再试一次修复”**（尤其已经试过 2+ 次）
- **每次修复都在不同位置暴露新问题**

这些都意味着：STOP。回到 Phase 1。

**如果 3+ 次修复失败：** 质疑架构（Phase 4.5）。

## 来自 human partner 的“你做错了”信号

**当你听到这些重定向：**
- “这不是没发生吗？”——你没验证就假设了
- “它能告诉我们……吗？”——你应该先补证据采集
- “别瞎猜”——你没理解就提修复
- “Ultrathink this”——要质疑根本假设，不是修症状
- “我们卡住了？”（烦躁）——你的方法在失效

看到这些：STOP，回到 Phase 1。

## 常见自我合理化（Rationalizations）

| 借口 | 现实 |
|------|------|
| “问题很简单，不需要流程” | 简单问题也有 root cause；流程对简单 bug 更快。 |
| “紧急，没时间走流程” | 系统化比 guess-and-check 更快。 |
| “我先试这个，再调查” | 第一次修复会定下节奏，从一开始就做对。 |
| “我确认修复有效后再写测试” | 没测试的修复不牢靠；test-first 才能证明。 |
| “一次改多个更省时间” | 无法隔离哪个改动起作用，还会引入新 bug。 |
| “reference 太长，我就按感觉套用” | 半懂不懂必出 bug；要完整读完。 |
| “我看到问题了，直接修” | 看到症状 ≠ 理解 root cause。 |
| “再试一次修复”（已失败 2+） | 3+ 失败提示架构问题：别再修症状，去质疑 pattern。 |

## Quick Reference

| Phase | 关键活动 | 成功标准 |
|-------|----------|----------|
| **1. Root Cause** | 读错误、复现、看变更、采证据 | 理解 WHAT + WHY |
| **2. Pattern** | 找对照样例、对照 reference | 找到差异 |
| **3. Hypothesis** | 提假设、最小验证 | 假设被证实或更换假设 |
| **4. Implementation** | 写测试、修复、验证 | 问题解决 + 测试通过 |

## 当流程显示“没有 root cause”

如果系统化调查显示问题确实是环境/时序/外部依赖导致：

1. 你已经完成流程
2. 记录你调查过什么
3. 实现合适的处理（retry、timeout、错误提示）
4. 增加 monitoring/logging 以便后续再调查

**但：** 95% 的“没有 root cause”其实是 Phase 1 不完整。

## Supporting Techniques

本目录包含系统化 debugging 的辅助技巧：

- **`root-cause-tracing.md`**：沿 call stack 逆向回溯到最初触发点
- **`defense-in-depth.md`**：找到 root cause 后，在多层加入校验
- **`condition-based-waiting.md`**：用条件轮询替代任意 timeout

**相关 skills：**
- `superpowers:test-driven-development`：用于 Phase 4 Step 1 的 failing test
- `superpowers:verification-before-completion`：在宣称修复成功前做验证

## Real-World Impact

来自真实排障经验：
- 系统化：通常 15–30 分钟定位并修复
- 乱修：经常 2–3 小时来回折腾
- 首次修复成功率：约 95% vs 40%
- 新 bug 引入：几乎为零 vs 很常见
