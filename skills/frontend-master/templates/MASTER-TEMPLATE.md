# 设计系统模板

> 此文件由 Frontend Master Skill 自动生成
> 生成时间: [YYYY-MM-DD HH:mm]
> 最后更新: [YYYY-MM-DD HH:mm]

---

## 1. 设计方向

**风格**: [例: 精致玻璃态 / 极简克制 / 大胆前卫]
**调性**: [一句话描述，例: "专业而不冰冷，现代而不浮夸"]
**参考**: [可选，列出参考的产品/网站]

---

## 2. 配色方案

### 主色板

| 用途 | 颜色值 | Tailwind 变量 | 使用场景 |
|------|--------|---------------|----------|
| 主色 | `#0F172A` | `primary` | 主要按钮、重要链接 |
| 主色浅 | `#1E293B` | `primary-light` | hover 状态 |
| 强调色 | `#3B82F6` | `accent` | CTA、高亮、徽章 |
| 成功 | `#10B981` | `success` | 成功状态、正向反馈 |
| 警告 | `#F59E0B` | `warning` | 警告信息 |
| 错误 | `#EF4444` | `error` | 错误状态、删除操作 |

### 中性色

| 用途 | 颜色值 | Tailwind 变量 |
|------|--------|---------------|
| 背景 | `#FFFFFF` | `background` |
| 卡片背景 | `#F8FAFC` | `card` |
| 边框 | `#E2E8F0` | `border` |
| 主文字 | `#0F172A` | `foreground` |
| 次要文字 | `#64748B` | `muted` |
| 占位符 | `#94A3B8` | `placeholder` |

### Dark Mode（如适用）

| 用途 | Light | Dark |
|------|-------|------|
| 背景 | `#FFFFFF` | `#0F172A` |
| 卡片 | `#F8FAFC` | `#1E293B` |
| 边框 | `#E2E8F0` | `#334155` |
| 主文字 | `#0F172A` | `#F8FAFC` |

---

## 3. 字体系统

### 字体选择

| 用途 | 字体 | 备选 | 加载方式 |
|------|------|------|----------|
| 标题 | Space Grotesk | — | Google Fonts |
| 正文 | DM Sans | — | Google Fonts |
| 代码 | JetBrains Mono | Fira Code | Google Fonts |

### 字号规范

| 级别 | 大小 | 行高 | 字重 | 用途 |
|------|------|------|------|------|
| h1 | 48px / 3rem | 1.1 | 700 | 页面主标题 |
| h2 | 36px / 2.25rem | 1.2 | 600 | 区块标题 |
| h3 | 24px / 1.5rem | 1.3 | 600 | 卡片标题 |
| h4 | 20px / 1.25rem | 1.4 | 500 | 小标题 |
| body | 16px / 1rem | 1.6 | 400 | 正文 |
| small | 14px / 0.875rem | 1.5 | 400 | 辅助文字 |
| caption | 12px / 0.75rem | 1.4 | 400 | 标签、时间戳 |

---

## 4. 间距系统

### 基础单位: 4px

| Token | 值 | 用途 |
|-------|-----|------|
| `space-1` | 4px | 图标与文字间距 |
| `space-2` | 8px | 紧凑元素间距 |
| `space-3` | 12px | 表单元素内间距 |
| `space-4` | 16px | 卡片内间距 |
| `space-6` | 24px | 区块内间距 |
| `space-8` | 32px | 区块间间距 |
| `space-12` | 48px | 大区块间间距 |
| `space-16` | 64px | 页面级间距 |

### 页面边距

| 断点 | 边距 |
|------|------|
| Mobile (< 768px) | 16px |
| Tablet (768px - 1024px) | 32px |
| Desktop (> 1024px) | 64px |

---

## 5. 圆角系统

| Token | 值 | 用途 |
|-------|-----|------|
| `rounded-sm` | 4px | 小标签、徽章 |
| `rounded` | 8px | 按钮、输入框 |
| `rounded-md` | 12px | 卡片、下拉菜单 |
| `rounded-lg` | 16px | 大卡片、模态框 |
| `rounded-xl` | 24px | 特殊容器 |
| `rounded-full` | 9999px | 头像、圆形按钮 |

---

## 6. 阴影系统

| Token | 值 | 用途 |
|-------|-----|------|
| `shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | 微弱层次 |
| `shadow` | `0 4px 6px -1px rgba(0,0,0,0.1)` | 卡片默认 |
| `shadow-md` | `0 10px 15px -3px rgba(0,0,0,0.1)` | 卡片悬浮 |
| `shadow-lg` | `0 20px 25px -5px rgba(0,0,0,0.1)` | 弹窗、下拉 |
| `shadow-xl` | `0 25px 50px -12px rgba(0,0,0,0.25)` | 模态框 |

---

## 7. 动效规范

### 时长

| 类型 | 时长 | 用途 |
|------|------|------|
| 即时反馈 | 100ms | 按钮点击、开关切换 |
| 微交互 | 150-200ms | hover、focus 状态 |
| 展开/收起 | 200-300ms | 下拉菜单、手风琴 |
| 页面过渡 | 300-400ms | 路由切换、模态框 |

### 缓动函数

| 名称 | 值 | 用途 |
|------|-----|------|
| ease-out | `cubic-bezier(0, 0, 0.2, 1)` | 进入动画 |
| ease-in | `cubic-bezier(0.4, 0, 1, 1)` | 退出动画 |
| ease-in-out | `cubic-bezier(0.4, 0, 0.2, 1)` | 状态切换 |

### 无障碍

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 8. 组件规范

### 按钮

| 变体 | 背景 | 文字 | 边框 |
|------|------|------|------|
| Primary | `primary` | `white` | — |
| Secondary | `transparent` | `primary` | `primary` |
| Ghost | `transparent` | `muted` | — |
| Destructive | `error` | `white` | — |

**尺寸**:
- Small: h-8, px-3, text-sm
- Default: h-10, px-4, text-base
- Large: h-12, px-6, text-lg

### 输入框

- 高度: 40px (default), 48px (large)
- 边框: 1px solid `border`
- Focus: 2px ring `accent`
- 圆角: `rounded`

### 卡片

- 背景: `card`
- 边框: 1px solid `border`
- 圆角: `rounded-md`
- 内间距: `space-4` 或 `space-6`
- 悬浮阴影: `shadow-md`

---

## 9. 禁止事项

### 字体
- ❌ Inter（过于通用）
- ❌ Roboto（过于通用）
- ❌ Arial / Helvetica（系统默认）
- ❌ Open Sans（过于通用）

### 配色
- ❌ 紫色渐变配白色背景（AI审美典型）
- ❌ 蓝紫渐变（过度使用）
- ❌ 过多颜色（超过 3 种主要颜色）

### 布局
- ❌ 完全对称的居中布局
- ❌ 千篇一律的 hero section
- ❌ 过度使用卡片网格

### 图标
- ❌ Emoji 作为 UI 图标
- ❌ 混用不同图标库
- ❌ 不一致的图标尺寸

---

## 10. 变更记录

| 日期 | 变更内容 | 原因 |
|------|----------|------|
| [日期] | 初始化设计系统 | 项目启动 |

---

*此设计系统由 Frontend Master Skill 生成和维护*
