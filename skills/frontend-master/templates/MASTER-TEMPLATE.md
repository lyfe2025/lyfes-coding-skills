# Design System Master File

> **LOGIC:** 构建具体页面时，先检查 `pages/[page-name].md`。存在时使用页面规则覆盖本文件，其余规则继承本文件。

---

**Project:** $project
**Generated:** $generated_at
**Category:** $category

---

## Global Rules

### Color Palette

$color_table

$color_notes

### Typography

$typography_block

### Spacing Variables

| Token | Value | Usage |
| --- | --- | --- |
| `--space-xs` | `4px` / `0.25rem` | Tight gaps |
| `--space-sm` | `8px` / `0.5rem` | Icon gaps, inline spacing |
| `--space-md` | `16px` / `1rem` | Standard padding |
| `--space-lg` | `24px` / `1.5rem` | Section padding |
| `--space-xl` | `32px` / `2rem` | Large gaps |
| `--space-2xl` | `48px` / `3rem` | Section margins |
| `--space-3xl` | `64px` / `4rem` | Hero padding |

### Motion Tokens

```css
:root {
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
  --duration-fast: 160ms;
  --duration-default: 220ms;
}
```

---

## Component Specs

$component_specs

---

## Style Guidelines

$style_guidelines

### Page Pattern

$page_pattern

---

## Anti-Patterns

$anti_patterns

---

## Pre-Delivery Checklist

$verification_checklist
