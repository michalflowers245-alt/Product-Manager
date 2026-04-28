# PM Vibe Skills

像产品经理一样，把模糊想法变成可验证需求、可执行 PRD、可上线 MVP 与可复盘作品。

适合人群：
- 产品经理
- PM 候选人
- 大学生
- 非程序员

核心能力：
- 想法验证
- 用户访谈
- PRD
- MVP 裁剪
- 页面文案与交互
- 上线与反馈
- 项目包装

## 为什么做这个仓库

很多 AI 工具会直接给你一堆“看起来很完整”的答案。
真正难的是：

- 先判断问题值不值得做
- 把想法翻译成 AI 和开发都能执行的文档
- 控制范围，别一上来做大
- 上线后收反馈，再把项目讲清楚

这个仓库把这些高频 PM 工作流做成可安装、可调用、可更新的 GitHub Skills。

## 仓库结构

```text
pm-vibe-skills/
├─ README.md
├─ AGENTS.md
├─ CONTRIBUTING.md
├─ docs/
│  ├─ skill-map.md
│  └─ examples/
├─ skills/
│  ├─ pm-discover/
│  ├─ pm-interview/
│  ├─ pm-prd/
│  ├─ pm-prioritize/
│  ├─ pm-ux-copy/
│  ├─ pm-launch-loop/
│  └─ pm-portfolio/
└─ .github/
   ├─ copilot-instructions.md
   └─ instructions/
```

## 模块

| 模块 | 用途 |
|---|---|
| `pm-discover` | 把模糊想法变成值得验证的问题 |
| `pm-interview` | 生成真实访谈提纲、记录表和证据标签 |
| `pm-prd` | 把需求整理成 AI 和开发都能执行的 PRD |
| `pm-prioritize` | 做 MVP 裁剪、优先级排序与版本切分 |
| `pm-ux-copy` | 输出页面结构、微文案、空状态与错误状态 |
| `pm-launch-loop` | 补齐上线清单、埋点、反馈与首周迭代 |
| `pm-portfolio` | 把项目包装成案例、简历与面试回答 |

## 来源映射

这个蓝图主要来自 `vibevibe-all-sections-export` 里的四条主线：
- 基础篇：零基础、MVP、从作品到上线闭环
- 进阶篇第三章：产品思维、想法验证、PRD、文档驱动
- 进阶篇第五章：UI/UX、组件、交互、页面表达
- 进阶篇第十六章：真实用户、反馈分类、迭代节奏

实战案例篇与优质文章篇作为案例补强与延伸阅读来源。

## 内容边界

这个仓库发布的是：
- Skill 结构
- 提示词工作流
- 模板
- 示例输出
- 对 VibeVibe 内容的模块化映射

这个仓库默认不直接再发布原教程全文。若后续要补充更细的章节引用或原文片段，请先确认内容版权与再发布权限。

## 下一步

1. 先看 [skill-map.md](C:/Users/34456/Documents/New%20project/pm-vibe-skills/docs/skill-map.md)
2. 选一个模块试用
3. 把示例输出接到你的项目里
4. 逐步补 tests、examples 和 Actions
