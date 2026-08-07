---
name: skill-creator
description: 初始化新 skill 目录（运行 init_skill.py）、打包 skill（运行 package_skill.py）、或需要了解 skill 结构规范时使用。
license: 完整条款见 LICENSE.txt
---

# Skill Creator

本 Skill 提供“如何编写有效 Skill”的方法与流程。

## 关于 Skill

Skill 是模块化、可复用的“指引包”，通过提供专业知识、workflow、工具与资源，让 Claude 从通用助手变成具备流程化能力的专用助手。

### Skill 提供什么

1. Specialized workflow：面向特定领域的多步流程
2. Tool integration：针对特定文件格式 / API 的操作指引
3. Domain expertise：公司/业务特定的知识、schema、业务逻辑
4. Bundled resources：用于重复性任务的 `scripts/`、`references/`、`assets/`

## 核心原则

### 简洁第一

context window 是公共资源：system prompt、对话历史、其他 Skill metadata、以及用户需求都要共用它。

**默认假设：Claude 已经很聪明。** 只加入 Claude 现实中“拿不到”的信息。对每一段文字都要自问：
- “Claude 真的需要这段解释吗？”
- “这段文字的 token 成本值得吗？”

优先用短小的例子与可执行步骤，避免冗长叙述。

### 设定合适的自由度（Degrees of Freedom）

根据任务的“脆弱性”和“可变性”决定指令有多具体：

- **高自由度（纯文本指导）**：可行方案很多、决策依赖上下文、需要启发式判断时使用
- **中自由度（伪代码 / 可配置脚本）**：存在推荐模式、允许有限变体、配置会影响行为时使用
- **低自由度（明确脚本 + 少量参数）**：流程易出错、需要强一致性、必须按固定顺序执行时使用

可以把 Claude 想象成“走路”：窄桥两侧是悬崖就需要更强的护栏（低自由度）；开阔草地就允许更多路线（高自由度）。

### Skill 的组成结构

每个 skill 由必需的 `SKILL.md` 与可选的资源目录组成：

```
skill-name/
├── SKILL.md（必需）
│   ├── YAML frontmatter metadata（必需）
│   │   ├── name:（必需）
│   │   └── description:（必需）
│   └── Markdown instructions（必需）
└── Bundled resources（可选）
    ├── scripts/          - 可执行代码（Python/Bash 等）
    ├── references/       - 需要时加载的参考文档
    └── assets/           - 用于输出的文件（模板、图标、字体等）
```

#### `SKILL.md`（必需）

`SKILL.md` 包含：

- **Frontmatter（YAML）**：包含 `name` 与 `description`。Claude 主要依赖它们来判断是否触发 skill，因此务必清晰描述“做什么 + 何时用”。
- **Body（Markdown）**：skill 的具体指令与资源使用方法。通常只在 skill 被触发后才加载（如果平台支持）。

#### Bundled resources（可选）

##### `scripts/`

用于需要确定性与可重复执行的任务（Python/Bash 等）。

- **适用场景**：同样的代码反复重写，或需要更高确定性
- **示例**：`scripts/rotate_pdf.py`（旋转 PDF）
- **收益**：省 token、可重复、可直接执行（无需全部读入 context）
- **注意**：脚本仍可能需要被阅读以便 patch 或做环境适配

##### `references/`

按需加载的参考材料，用来支撑 Claude 的推理与决策。

- **适用场景**：Claude 在执行任务时需要查阅的文档
- **示例**：`references/schema.md`（表结构）、`references/api_docs.md`（API 说明）、`references/policies.md`（政策/规范）
- **收益**：让 `SKILL.md` 保持精简；只在需要时加载
- **最佳实践**：如果文件很大（>10k words），在 `SKILL.md` 中提供 grep/搜索提示
- **避免重复**：信息要么放在 `SKILL.md`，要么放在 `references/`；细节优先放 `references/`，`SKILL.md` 只保留关键流程与导航

##### `assets/`

不需要读入 context、但会被复制/引用到输出中的文件。

- **适用场景**：skill 需要模板、图片、图标、字体、boilerplate 等
- **示例**：`assets/logo.png`、`assets/slides.pptx`、`assets/frontend-template/`
- **收益**：把“输出用资源”和“说明文档”分离，减少 context 压力

#### Skill 里不要放什么

Skill 应只包含支撑其功能的必要文件，不要新增无关文档/辅助文件，例如：

- `README.md`
- `INSTALLATION_GUIDE.md`
- `QUICK_REFERENCE.md`
- `CHANGELOG.md`
- 等等

这些“人类文档”会制造噪音与维护成本。Skill 的目标是让 AI agent 能更可靠地完成任务，而不是记录编写过程或面向用户的说明书。

### Progressive Disclosure（渐进式加载）

用三层结构控制 context：

1. **Metadata（name + description）**：始终在 context（~100 words）
2. **`SKILL.md` body**：skill 触发后加载（建议 <5k words）
3. **Bundled resources**：需要时再加载（脚本可直接执行，参考文档按需读取）

#### Progressive Disclosure 的常用模式

尽量把 `SKILL.md` 控制在必要范围内（建议 <500 行），避免 context 膨胀。接近上限时，把细节拆分到独立文件，并在 `SKILL.md` 中明确“何时阅读”。

**关键原则：** 当 skill 支持多种变体/框架/选项时，`SKILL.md` 只保留核心流程与选择指引；把变体细节（pattern、example、config）放到 `references/`。

**模式 1：高层导航 + 引用**

```markdown
# PDF 处理

## Quick start

用 pdfplumber 提取文本：
[code example]

## Advanced features

- **表单填写**：完整指南见 [FORMS.md](FORMS.md)
- **API reference**：所有方法见 [REFERENCE.md](REFERENCE.md)
- **Examples**：常见模式见 [EXAMPLES.md](EXAMPLES.md)
```

需要时才加载 `FORMS.md` / `REFERENCE.md` / `EXAMPLES.md`。

**模式 2：按业务域拆分**

当 skill 覆盖多个 domain 时，按 domain 拆分，避免加载无关内容：

```
bigquery-skill/
├── SKILL.md（概览与导航）
└── reference/
    ├── finance.md（revenue、billing metrics）
    ├── sales.md（opportunities、pipeline）
    ├── product.md（API usage、features）
    └── marketing.md（campaigns、attribution）
```

用户问 sales 指标时，只读 `sales.md`。

类似地，支持多 provider 的部署类技能也可按 provider 拆分：

```
cloud-deploy/
├── SKILL.md（workflow + provider selection）
└── references/
    ├── aws.md（AWS deployment patterns）
    ├── gcp.md（GCP deployment patterns）
    └── azure.md（Azure deployment patterns）
```

**模式 3：条件化细节**

先给基础做法，再链接到高级内容：

```markdown
# DOCX 处理

## Creating documents

新建文档用 docx-js。详见 [DOCX-JS.md](DOCX-JS.md)。

## Editing documents

简单修改可以直接改 XML。

**涉及 tracked changes**：见 [REDLINING.md](REDLINING.md)
**涉及 OOXML 细节**：见 [OOXML.md](OOXML.md)
```

**重要建议：**

- **避免引用链太深**：reference 文件最好都能从 `SKILL.md` 直接链接到（保持一层深度）。
- **长 reference 要结构化**：超过 100 行的文件建议加目录（table of contents），便于快速预览与定位。

## Skill 创建流程

Skill 创建通常按以下步骤推进：

1. 用具体例子理解需求
2. 规划可复用资源（scripts、references、assets）
3. 初始化 skill（运行 `init_skill.py`）
4. 编辑 skill（实现资源并完善 `SKILL.md`）
5. 打包 skill（运行 `package_skill.py`）
6. 结合真实使用迭代

按顺序执行；只有在明确不适用时才跳过某步。

### Step 1：用具体例子理解 Skill

仅当使用方式已非常清晰时才可跳过；即使在迭代已有 skill 时，这一步通常仍有价值。

要写出有效 skill，必须先明确它会如何被使用：可以来自用户提供的真实例子，也可以由你生成例子并让用户确认。

例如：要做一个 image-editor skill，可以问：

- “这个 image-editor skill 需要支持哪些功能？裁剪、旋转、调色、去红眼……还有吗？”
- “你能给我一些你会怎么用它的例子吗？”
- “我能想到的触发语有：‘帮我去掉照片红眼’、‘把这张图片旋转 90 度’。你还会怎么提？”
- “什么样的话应该触发这个 skill？”

避免一次问太多问题；先问最关键的，后续再补。

当你对“要支持的功能边界”有明确共识时，结束本步骤。

### Step 2：规划可复用内容（Reusable contents）

把具体例子转化为 skill 内容时，对每个例子做两件事：

1. 从零执行一次（脑内/纸面）——你会怎么做？
2. 判断哪些 `scripts/`、`references/`、`assets/` 能让重复执行更快、更稳

示例：做 `pdf-editor`（用户问“帮我旋转这个 PDF”）时，你会发现：

1. 旋转 PDF 需要反复写同样的代码
2. 适合沉淀成 `scripts/rotate_pdf.py`

示例：做 `frontend-webapp-builder`（用户问“做个 todo app / 做个 dashboard”）时，你会发现：

1. 前端项目总要重复写同样的 boilerplate（HTML/React 等）
2. 适合准备一个 `assets/hello-world/` 模板目录

示例：做 `big-query`（用户问“今天有多少用户登录？”）时，你会发现：

1. 每次都要重新发现 table schema 与关系
2. 适合写 `references/schema.md` 来记录 schema

把所有例子都过一遍，最终得到“要包含哪些可复用资源”的清单。

### Step 3：初始化 Skill

如果是从零新建 skill，**总是**先运行 `init_skill.py`。它会生成一个包含必需结构的模板目录，减少遗漏与返工。

仅当 skill 已存在且你在做迭代/打包时，才跳过本步骤并进入下一步。

用法：

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

该脚本会：

- 在指定路径创建 skill 目录
- 生成带 TODO 占位的 `SKILL.md` 模板（包含正确的 frontmatter）
- 创建示例资源目录：`scripts/`、`references/`、`assets/`
- 在每个目录放入可按需改造/删除的示例文件

初始化后，按需要修改或删除示例文件与目录。

### Step 4：编辑 Skill

编辑（新生成或已有）skill 时要记住：你是在给“另一个 Claude 实例”写说明。只加入对 Claude 有帮助且不显然的信息：流程化知识、domain 细节、可复用资产等。

#### 学习成熟的设计模式

根据 skill 类型参考以下指南：

- **多步流程**：见 `references/workflows.md`（顺序流程与条件分支）
- **特定输出格式/质量标准**：见 `references/output-patterns.md`（模板与示例模式）

#### 从可复用资源入手

优先实现 Step 2 中识别出的 `scripts/`、`references/`、`assets/`。这一步可能需要用户提供材料：例如 `brand-guidelines` skill 需要用户提供品牌资源放入 `assets/`，或提供文档放入 `references/`。

新增脚本必须“实际运行”验证输出是否符合预期；如果脚本很多且相似，至少运行代表性样本以建立信心（兼顾时间成本）。

不需要的示例文件/目录要删除。模板目录只是演示结构，大多数 skill 不会用到全部内容。

#### 更新 `SKILL.md`

**写作要求：** 统一使用祈使/动词原形（imperative/infinitive）表达（例如“检查… / 运行… / 生成…”）。

##### Frontmatter

`SKILL.md` 顶部的 YAML frontmatter 只写 `name` 与 `description`：

- `name`：skill 名称
- `description`：skill 的主要触发机制，用来告诉 Claude“什么时候用它”
  - 需要同时写清楚“它做什么”与“触发场景/上下文”
  - 所有 “when to use” 信息都应放在这里，而不是正文里（正文只有触发后才会加载）
  - 示例（`docx` skill 的 description）：
    - “支持 tracked changes、comments、格式保留与文本提取的专业文档（.docx）创建/编辑/分析。当 Claude 需要处理 .docx：新建、修改、处理 tracked changes、添加 comments 等场景时使用。”

不要在 frontmatter 里加入其他字段。

##### Body

在正文里写清楚：如何使用该 skill 以及如何使用其 bundled resources。

### Step 5：打包 Skill

开发完成后，需要打包成可分发的 `.skill` 文件。打包脚本会先自动验证 skill 是否符合要求：

`SKILL.md` 可选使用 `compatibility` 字段，描述平台或运行时限制；它必须是长度不超过 500 字符的字符串。`name` 必须使用不超过 64 字符的 kebab-case。

打包器会排除 `__pycache__`、`node_modules`、`*.pyc`、`.DS_Store` 以及 skill 根目录的 `evals/`，避免把构建残留带入分发包。这些是包内容卫生规则，不是 sandbox，也不提供路径穿越、symlink 或不可信代码的安全隔离；执行外部脚本时仍须依赖宿主权限、容器或 sandbox。

```bash
scripts/package_skill.py <path/to/skill-folder>
```

也可指定输出目录：

```bash
scripts/package_skill.py <path/to/skill-folder> ./dist
```

打包脚本会：

1. **Validate**：检查
   - YAML frontmatter 格式与必需字段
   - skill 命名约定与目录结构
   - description 的完整性与质量
   - 文件组织与资源引用
2. **Package**：验证通过后，生成以 skill 目录名命名的 `.skill` 文件（如 `my-skill.skill`），并保持正确的分发目录结构（本质是 zip + `.skill` 扩展名）。

验证失败则输出错误并退出，不会生成包。修复后重新运行打包命令。

### Step 6：迭代

skill 在真实任务中使用后，用户通常会马上提出改进（此时上下文最新、反馈最具体）。

**迭代 workflow：**

1. 在真实任务中使用 skill
2. 观察卡点/低效之处
3. 判断应如何更新 `SKILL.md` 或 bundled resources
4. 修改后再次测试
