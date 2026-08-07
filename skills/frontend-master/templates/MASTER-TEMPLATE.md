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

$spacing_table

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
