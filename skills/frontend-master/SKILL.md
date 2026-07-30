---
name: frontend-master
description: "高质量前端设计与实现的统一入口。用于创建、重构或精修主页、个人品牌页、作品集、Landing Page、Dashboard、表单、卡片、导航和其他 Web UI；先分析项目技术栈与现有设计系统，再确定差异化方向、实现生产级代码，并按需调用交互或动效专项 Skill。"
---

# Frontend Master

以设计工程师的标准完成前端任务：先理解内容和约束，再形成明确的视觉方向，最后用真实运行结果验证。不要把数据库推荐、流行风格或固定页面结构当作答案。

## Workflow

### 1. Recon：读取现状

开始设计前先检查：

- 框架、CSS 方案、UI 库、图标库和现有组件
- CSS variables、主题 token、字体、间距和响应式惯例
- 已有设计系统，以及同类页面的布局与交互模式
- 项目指令、验证命令和可访问性要求

已有系统优先。除非用户明确要求重塑品牌，不要为了“独特”推翻成熟规范。

### 2. Frame：定义问题

编码前明确：

- **Purpose**：页面解决什么问题
- **Audience**：谁使用或浏览
- **Content hierarchy**：什么内容最重要
- **Primary action**：希望用户完成什么
- **Tone**：界面应传达什么气质
- **Signature element**：最值得被记住的一个设计特征
- **Constraints**：技术、内容、性能、无障碍和品牌限制

新建主页、个人品牌页、作品集或平台模板时，必须读取 [template-design.md](references/template-design.md)，先输出简短模板简报，再开始实现。

### 3. Research：把搜索结果当作候选

需要探索方向时使用内置搜索工具：

```bash
python3 scripts/search.py "<项目类型> <行业> <关键词>" --design-system -p "<项目名>"
python3 scripts/search.py "<关键词>" --domain style
python3 scripts/search.py "<关键词>" --stack nextjs
```

搜索结果必须经过受众、品牌、语言、现有系统和实施成本过滤。不要机械采用第一条结果，也不要固定收敛到某个字体、渐变或 `Hero > Features > CTA`。

### 4. Craft：实现并精修

- 视觉决策遵循 [design-philosophy.md](references/design-philosophy.md)。
- 组件状态和反馈遵循 [interaction-craft.md](references/interaction-craft.md)。
- 涉及动画时读取 [motion-quality.md](references/motion-quality.md)。
- 复用项目现有组件与主题 token；不硬编码平行的设计系统。
- 保持语义化、mobile-first、WCAG AA，并匹配项目既有代码风格。

按场景调用专项 Skill，不要每次串行调用全部能力：

| 场景 | 专项 Skill |
| --- | --- |
| 深度检查组件状态、反馈和微观质感 | `emil-design-eng` |
| 拖拽、swipe、sheet、spring、momentum、可中断交互 | `apple-design` |
| 用户只描述效果，需要确认动效术语 | `animation-vocabulary` |
| 页面显得静态，需要寻找真正值得增加的动效 | `find-animation-opportunities` |
| 已有大量动效，需要系统审计和整改计划 | `improve-animations` |

专项 Skill 不可用时，以本 Skill 的 references 为最低质量基线继续完成任务。

### 5. Persist：谨慎维护设计系统

- 已有设计系统：优先读取并遵循，只有明确变更才更新。
- 首次建立：先展示设计方向并获得确认，再执行持久化。
- 默认不覆盖已有文件；用户明确更新时使用 `--force`。

```bash
python3 scripts/search.py "<项目描述>" \
  --design-system \
  --persist \
  -p "<项目名>" \
  --page "<页面名>"
```

生成结构：

```text
design-system/<project-slug>/MASTER.md
design-system/<project-slug>/pages/<page-slug>.md
```

页面规则覆盖 MASTER；其余规则继承 MASTER。

### 6. Verify：用证据完成交付

交付前读取 [verification.md](references/verification.md)：

- 运行项目已有 lint、typecheck、test 和 build
- 实际打开页面，检查真实内容与关键交互
- 验证移动端、桌面端、键盘和 Reduced Motion
- 检查控制台、资源加载、溢出、裁切和固定层遮挡

无法运行的项目必须明确说明未验证项。只看源码或只勾选清单，不等于完成视觉验证。

## Quality Bar

- 设计方向明确且服务内容，不靠装饰堆叠制造“高级感”
- 模板之间有结构性差异，而不是只换颜色、圆角或阴影
- 只有真实可交互元素呈现交互 affordance
- 动效有目的、克制、可中断或可降级
- 字体适配品牌、语言覆盖、性能和阅读场景
- 桌面端与移动端分别组织信息，而不是等比例缩小
- 所有完成声明均有最新验证证据
