---
name: pm-prd
description: Generate AI-executable PRDs for PM workflows. Use when the user has a validated problem and needs a structured product requirements document for AI and developers.
license: MIT
---

# pm-prd

默认中文输出，Markdown 格式。
PRD 的目标不是显得专业，而是让 AI 和开发都不用猜。

## 必须输出

1. 文档信息
2. 背景与目标
3. 用户与场景
4. 核心流程
5. 功能需求
6. 非功能需求
7. 不做什么
8. P0 / P1 / P2
9. 验收标准
10. 风险与待确认事项

## 原则

- 证据与假设分开写
- 能视图化就视图化
- 范围控制优先于功能堆砌

## 资产

- 参考方法：`references/prd-rules.md`
- 输出模板：`templates/prd-outline.md`
