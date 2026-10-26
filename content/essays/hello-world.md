---
title: "Hello World：博客开张了"
date: 2026-10-24T12:00:00+08:00
draft: false
tags: ["随笔", "开张"]
categories: ["随笔"]
summary: "第一篇随笔，试试水～"
---

这是博客的第一篇文章，欢迎光临～ ★

## 这个博客长什么样

- **随笔**：想到什么写什么
- **工程复盘**：项目结束后写总结

## 图片怎么放

两种方式：

**方式一（推荐）**：整篇文章的图片和 Markdown 放同一个文件夹（页面资源包）：

```text
content/essays/my-post/
├── index.md      ← 文章正文
├── photo1.jpg    ← 图片放在同目录
└── photo2.png
```

正文里直接写 `![说明](photo1.jpg)` 就行。

**方式二**：放到 `static/images/` 目录，正文里用 `/images/xxx.png` 引用。比如下面这张：

![示例图片](/images/hello.svg)

## 一段代码试试

```python
print("Hello, Javasee's Blog!")
```

写作流程就是：**本地写 Markdown → git push → 自动发布**。就这么简单 (≧▽≦)ﾉ


---

*本篇博客由 mimo-v2.6-pro 生成*
