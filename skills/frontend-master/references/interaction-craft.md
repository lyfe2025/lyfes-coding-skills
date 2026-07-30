# 交互质感

## 状态完整性

每个交互组件按需覆盖：

- default
- hover
- active / pressed
- focus-visible
- disabled
- loading
- error / success

状态应清晰但克制。不要通过改变尺寸、边框宽度或文字字重造成布局跳动。

## Affordance 必须真实

- 只有真实可点击、可选择或可拖拽的元素使用 pointer cursor。
- 普通信息卡片保持静态，不默认添加 hover lift、阴影变化或 pointer cursor。
- 优先使用 `button`、`a`、`input` 等语义元素，不用可点击 `div` 模拟控件。
- Hover 只能增强体验，不能成为发现功能或读取信息的唯一方式。

```css
@media (hover: hover) and (pointer: fine) {
  .interactive-card:hover {
    transform: translateY(-2px);
  }
}
```

## 响应与反馈

- 用户按下控件时立即反馈，不等待请求完成。
- 按压缩放只用于合适的紧凑控件，通常为 `scale(0.97)` 左右；不是所有可点击元素都需要缩放。
- Loading 状态应防止重复提交，并保留按钮宽度避免跳动。
- 表单错误尽量靠近字段，明确说明如何修正；不要只在提交后给统一错误。
- 成功、失败和撤销状态应与操作因果关系清晰。

## 键盘与触控

- 所有功能均可通过键盘到达和操作。
- 使用 `:focus-visible` 提供清晰焦点，不得只移除 `outline`。
- DOM 顺序与视觉阅读顺序一致。
- 触摸目标通常不小于 44×44px；紧凑视觉可以通过透明 hit area 扩大。
- Hover 样式不能在触屏点击后残留或阻挡下一步操作。

## 浮层与破坏性操作

- Menu 用于命令集合，Popover 用于相关内容，Tooltip 只补充简短说明，Dialog 用于需要集中完成的任务。
- Popover 从触发器方向出现；居中 Modal 保持居中语义。
- 真正不可逆的操作使用主题化确认 Dialog；可撤销操作优先提供 Undo。
- 不使用浏览器原生 `alert`、`confirm` 或 `prompt` 代替产品 UI。

## 内容状态

- Empty state 解释发生了什么，并提供最相关的下一步。
- Skeleton 应贴近最终结构，不用无意义的闪烁矩形填满页面。
- 加载失败提供重试或恢复路径。
- 乐观更新失败时恢复数据并说明原因，不让视觉状态与真实状态分离。
