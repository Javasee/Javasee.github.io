---
title: "复盘：个人博客搭建（GitHub Pages + Hugo）"
date: 2026-10-24T13:00:00+08:00
draft: false
ai_generated: "mimo-v2.6-pro"
tags: ["复盘", "博客", "Hugo", "GitHub Pages"]
categories: ["工程复盘"]
summary: "从零搭建 javasee.com 个人博客的完整复盘。"
---

## 背景与目标

想要一个公开的个人博客，存放随笔和工程复盘，最终绑定自定义域名 `javasee.com`。

## 技术选型

| 环节 | 选择 | 理由 |
|------|------|------|
| 建站 | Hugo + PaperMod | 单文件工具、构建快、维护成本低 |
| 托管 | GitHub Pages | 免费、自带 HTTPS、push 即发布 |
| 域名 | javasee.com（待注册） | 域名空闲可注册 |

## 踩过的坑

1. **校园网直连 GitHub Releases 超时**：curl 下载 hugo/gh 安装包 500 秒没完成；改用 winget（微软 CDN）秒装。
2. **git clone 主题也慢**：换 `codeload.github.com` 的 zip 打包下载，1 秒完成。
3. **winget 装的 Hugo 不在 bash PATH 里**：实际位置在 `WinGet\Packages\` 下，需要手动加 PATH。

## 结果

- ✅ 站点本地构建通过
- ✅ GitHub Actions 自动部署
- ⏳ 域名 javasee.com 待注册绑定

## 下次可以做得更好

- 图片统一压缩成 WebP 再上传
- 上 giscus 评论区

