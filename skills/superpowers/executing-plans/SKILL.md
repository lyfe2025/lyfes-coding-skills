---
name: executing-plans
description: 当你已经有一份书面的 implementation plan，需要在独立 session 中按批执行并在批次间做 review checkpoint 时使用。
---

# Executing Plans

## Overview

加载计划 → 严格评审 → 分批执行任务 → 每批完成后汇报并等待 review。

**核心原则：** 分批执行 + checkpoint，让架构/代码 review 有节奏地介入。

**开始时宣告：** “我正在使用 executing-plans skill 来执行这个计划。”

## The Process

### Step 1：加载并评审计划
1. 读取计划文件
2. 批判性评审：找出疑问、风险与不一致
3. 如果有顾虑：开工前先与人类伙伴对齐
4. 如果无顾虑：创建 TodoWrite 并继续

### Step 2：执行一个批次（Batch）
**默认：先做前 3 个任务**

对每个任务：
1. 标记为 `in_progress`
2. 严格按步骤执行（计划应是可咀嚼的小步骤）
3. 按计划要求运行 verification
4. 标记为 `completed`

### Step 3：汇报
当本批完成：
- 说明本批实现了什么
- 附上 verification 输出
- 说：“可以给我反馈了。”

### Step 4：继续下一批
根据反馈：
- 必要时先修正
- 执行下一批
- 重复直到全部完成

### Step 5：完成开发收尾

当所有任务完成且验证通过后：
- 宣告：“我正在使用 finishing-a-development-branch skill 来完成收尾。”
- **必用子 skill：** `superpowers:finishing-a-development-branch`
- 按该 skill 完成测试验证、给出选项并执行选择

## 何时停下并求助

**出现以下情况立刻停止执行：**
- 批次中途遇到 blocker（缺依赖、测试失败、指令不清）
- 计划存在关键缺口，导致无法启动
- 你不理解某条指令
- verification 反复失败

**不要猜。优先澄清。**

## 何时回到前面步骤

**在以下情况回到 Review（Step 1）：**
- 伙伴根据你的反馈更新了计划
- 基础方案需要重想

**不要硬顶 blocker** ——停下并问清楚。

## Remember
- 先批判性评审计划
- 严格按计划步骤执行
- 不要跳过 verification
- 计划要求引用 skill 时就引用
- 每批之间：只汇报并等待
- 被卡住就停，不要猜
