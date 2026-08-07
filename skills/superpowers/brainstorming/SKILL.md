---
name: brainstorming
description: "你必须在任何创意工作之前使用：新功能、组件搭建、添加能力或修改行为。先通过对话澄清用户意图、需求与设计，再进入实现。"
---

# Brainstorming Ideas Into Designs

## Overview

通过自然的协作式对话，把模糊想法打磨成清晰的设计与 spec。

先理解当前项目上下文，然后一次只问一个问题来逐步收敛。确认“要做什么”之后，再把设计拆成小段（每段 200–300 字）依次输出，并在每段后询问“到目前为止是否正确”。

## The Process

**理解想法：**
- 先检查当前项目状态（文件、文档、最近的 commit）
- 一次只问一个问题来细化需求
- 能用选择题就优先选择题；必要时再用开放式问题
- 每条消息只问 1 个问题；同一主题需要深入时拆成多轮
- 聚焦：目的、约束、成功标准（success criteria）

**探索方案：**
- 提出 2–3 种不同 approach，并说明 trade-off
- 用对话式方式呈现选项，并给出你的推荐与理由
- 先给推荐方案，再解释为什么

**呈现设计：**
- 当你确信已理解要构建的内容后，再输出设计
- 拆成每段 200–300 字
- 每段后询问“目前这样是否正确”
- 覆盖：architecture、components、data flow、error handling、testing
- 若发现不合理/不清晰，随时回退澄清

## Design Approval Gate

在进入 implementation 或 writing-plans 前：

1. 将已收敛的设计写成简短 spec，覆盖 architecture、components、data flow、error handling 和 testing。
2. 自审 spec：检查范围、约束、接口和验收标准是否一致，删除 TBD、TODO 与假设的未来需求。
3. 明确请求用户批准；未获批准前不要写 production code，也不要调用实现类 workflow。

## After the Design

**Documentation：**
- 把已确认的设计写入 `docs/plans/YYYY-MM-DD-<topic>-design.md`
- 若可用，使用 `elements-of-style:writing-clearly-and-concisely` skill 进行文字优化
- 将设计文档提交到 git

**Implementation（如果继续实现）：**
- 询问：“准备好进入实现了吗？”
- 用 `superpowers:using-git-worktrees` 创建隔离工作区
- 用 `superpowers:writing-plans` 生成详细的实现计划

## Key Principles

- **一次一个问题**：避免用多个问题轰炸用户
- **优先选择题**：在可行时比开放题更易回答
- **Ruthlessly YAGNI**：从设计中移除不必要功能
- **探索替代方案**：先给 2–3 种方案再收敛
- **增量验证**：分段输出设计并逐段确认
- **保持灵活**：不清楚就回退并澄清
