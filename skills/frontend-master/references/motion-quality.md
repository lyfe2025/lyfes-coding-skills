# 动效质量

## 先判断是否需要动画

按顺序回答：

1. 用户多久会看到一次？高频或键盘触发操作通常不动画。
2. 动画的目的是什么？必须是反馈、状态指示、空间连续、缓解突变、解释，或低频场景下的适度愉悦。
3. 动画是否帮助理解或操作？装饰不能干扰功能和阅读。
4. 能否在速度预算内完成？普通 UI 动效通常不超过 300ms。

如果只能用“看起来更酷”解释，就不要添加。

## 实现原则

- 禁止 `transition: all`，只声明实际变化的属性。
- 优先动画 `transform` 和 `opacity`，避免逐帧修改会触发布局的属性。
- 进入与用户响应通常用强 `ease-out`；屏幕内位置变化可用 `ease-in-out`。
- UI 进入不要从 `scale(0)` 开始，可从 `scale(0.95–0.98)` 配合 opacity。
- 进入和退出沿相同空间路径，Popover 使用与触发器一致的 transform origin。
- 快速重复触发的 UI 优先使用可重定向的 transition，而不是每次从头播放 keyframes。
- Stagger 只用于低频或解释性场景，间隔通常为 30–80ms，不得阻塞交互。
- Hover motion 使用 `(hover: hover) and (pointer: fine)` 限制。

推荐基础曲线：

```css
:root {
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
  --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
}
```

## 速度预算

| 场景 | 建议范围 |
| --- | --- |
| 按压反馈 | 100–160ms |
| Tooltip / 小 Popover | 125–200ms |
| Dropdown / Select | 150–250ms |
| Modal / Drawer | 200–500ms |
| 营销解释动画 | 可更长，但不能阻塞内容 |

## Reduced Motion

Reduced Motion 不是把所有时长改成 `0.01ms`：

- 移除大幅位移、视差、弹性和持续循环。
- 用短 crossfade、颜色变化或静态状态替代。
- 保留有助于理解且不会引发前庭不适的反馈。
- 在该模式下完整执行任务，确认内容不会消失或顺序错乱。

```css
@media (prefers-reduced-motion: reduce) {
  .panel {
    transform: none;
    transition: opacity 160ms ease-out;
  }
}
```

## 何时交给专项 Skill

- 拖拽、swipe、sheet、spring、momentum、rubber-banding、速度继承或中途反向：`apple-design`
- 页面整体偏静态，需要寻找少量高价值机会：`find-animation-opportunities`
- 已有动效风格混乱或性能不佳，需要系统整改：`improve-animations`
- 用户不知道效果名称：`animation-vocabulary`
