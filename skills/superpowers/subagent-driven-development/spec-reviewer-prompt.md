# Spec Reviewer 兼容入口

此文件保留用于兼容旧计划和旧引用。新流程不要单独派发 spec reviewer；请使用 [task-reviewer-prompt.md](task-reviewer-prompt.md)，由同一个只读 reviewer 同时返回：

- `SPEC_COMPLIANCE`
- `QUALITY`

如需验证修复，使用 [re-review-prompt.md](re-review-prompt.md) 做 scoped re-review。不要重新恢复旧的“spec reviewer → code quality reviewer”双代理串行流程。
