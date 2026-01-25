---
name: using-superpowers
description: 在任何对话开始时使用：建立“如何发现并使用 skills”的规则，要求在任何回应（包括澄清问题）之前先 invoke Skill tool。
---

<EXTREMELY-IMPORTANT>
只要你觉得“有 1% 的可能某个 skill 适用”，你就必须先 invoke 该 skill。

如果某个 skill 适用于当前任务，你没有选择权：你必须使用它。

这不可协商，不是可选项，也不能用任何理由自我合理化绕过。
</EXTREMELY-IMPORTANT>

## 如何访问 Skills

**在 Claude Code：** 使用 `Skill` tool。invoke 后会加载并展示该 skill 的内容——直接照做。不要对 skill 文件使用 Read tool。

**在其他环境：** 参考平台文档了解 skill 的加载机制。

# Using Skills

## The Rule

**在任何回应或行动之前，先 invoke 相关或被请求的 skill。** 只要有 1% 可能，就先 invoke 来确认；如果最终发现不适用，再不使用也不迟。

```dot
digraph skill_flow {
    "收到用户消息" [shape=doublecircle];
    "是否可能有 skill 适用？" [shape=diamond];
    "Invoke Skill tool" [shape=box];
    "宣告：'使用 [skill] 来 [purpose]'" [shape=box];
    "是否有 checklist？" [shape=diamond];
    "为每项创建 TodoWrite" [shape=box];
    "严格按 skill 执行" [shape=box];
    "回复（包括澄清问题）" [shape=doublecircle];

    "收到用户消息" -> "是否可能有 skill 适用？";
    "是否可能有 skill 适用？" -> "Invoke Skill tool" [label="是，哪怕 1%"];
    "是否可能有 skill 适用？" -> "回复（包括澄清问题）" [label="完全不可能"];
    "Invoke Skill tool" -> "宣告：'使用 [skill] 来 [purpose]'";
    "宣告：'使用 [skill] 来 [purpose]'" -> "是否有 checklist？";
    "是否有 checklist？" -> "为每项创建 TodoWrite" [label="有"];
    "是否有 checklist？" -> "严格按 skill 执行" [label="无"];
    "为每项创建 TodoWrite" -> "严格按 skill 执行";
}
```

## Red Flags

出现以下想法就立刻停下——你在“自我合理化”：

| 想法 | 事实 |
|------|------|
| “这只是个简单问题” | 问题也是任务。先检查 skill。 |
| “我得先问清楚上下文” | skill 检查要在澄清问题之前。 |
| “我先随便逛一下代码库” | skill 会告诉你应该怎么逛。先检查。 |
| “我先快速看下 git/文件” | 文件没有对话上下文。先检查 skill。 |
| “我先收集点信息” | skill 会告诉你如何收集信息。 |
| “这种事不需要正式的 skill” | 既然 skill 存在，就用它。 |
| “我记得这个 skill 大概内容” | skill 会演进。读最新版本。 |
| “这不算任务” | 只要有行动就是任务。先检查。 |
| “skill 太重了” | 小事会变复杂。用它。 |
| “我先做这一件小事再说” | 做任何事之前先检查。 |
| “我感觉这样更高效” | 无纪律的行动会浪费时间。skill 用来避免。 |
| “我知道那是什么意思” | 知道概念 ≠ 使用 skill。先 invoke。 |

## Skill Priority

当多个 skill 都可能适用时，按以下顺序：

1. **先 process skills**（brainstorming、debugging）：决定“怎么做”
2. **再 implementation skills**（例如 frontend-design、mcp-builder）：指导“具体落地”

“我们来做 X” → 先 brainstorming，再用实现类 skill。  
“修这个 bug” → 先 debugging，再用领域类 skill。

## Skill Types

**Rigid**（TDD、debugging）：必须严格照做，不要“灵活变通”掉纪律。

**Flexible**（patterns）：按原则结合上下文调整。

以 skill 本身的要求为准。

## User Instructions

用户指令通常说明 WHAT，而不是 HOW。“加 X / 修 Y”不等于可以跳过 workflow。
