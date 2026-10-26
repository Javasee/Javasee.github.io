---
title: "个人博客搭建（GitHub Pages + Hugo）"
date: 2026-10-24T13:00:00+08:00
draft: false
ai_generated: "mimo-v2.6-pro"
tags: ["复盘", "博客", "Hugo", "GitHub Pages", "Cloudflare", "Waline"]
categories: ["工程复盘"]
summary: "从零搭建个人博客的完整复盘：建站、域名、Material 3 定制、评论系统，四关连打。"
---

## 背景与目标

想要一个公开的个人博客，存放随笔和工程复盘，最终绑定自定义域名 `javasee.com`。

最初以为是"装个静态站生成器、push 上线"的半天活。实际打下来是四关连打：**建站 → 域名 → 外观定制 → 评论系统**，每一关都有自己的坑。

## 技术选型

| 环节 | 选择 | 理由 |
|------|------|------|
| 建站 | Hugo + PaperMod | 单文件工具、构建快、维护成本低（对比过 Astro/Hexo：定制要求低的话 Hugo 全家桶最省心） |
| 托管 | GitHub Pages | 免费、自带 HTTPS、push 即发布 |
| 域名 | javasee.com + Cloudflare DNS | 域名空闲可注册；DNS 自带 DNSSEC、按成本价续费 |
| 外观 | Material 3 设计规范手工定制 | 亮暗双模式、完整 token 体系；不想买/仿现成主题 |
| 评论 | Waline + Vercel + GitHub CSV | 需要匿名 + 登录双支持（giscus 只有 GitHub 登录）；数据落在自己的仓库 |

## 踩过的坑

### 建站关

1. **校园网直连 GitHub Releases 超时**：curl 下载 hugo/gh 安装包 500 秒没完成；改用 winget（微软 CDN）秒装。
2. **git clone 主题也慢**：换 `codeload.github.com` 的 zip 打包下载，1 秒完成。
3. **winget 装的 Hugo 不在 bash PATH 里**：实际位置在 `WinGet\Packages\` 下，需要手动加 PATH。

### 域名关

4. **域名可注册性要用 RDAP 查实**：`rdap.verisign.com` 查 .com 域名，比 whois 可靠（404 = 未注册）。
5. **GitHub Pages 的域名设置接口和文档不符**：`PATCH /repos/.../pages` 返回 404，`PUT` 才生效（204）。文档说 PATCH，身体很诚实。
6. **Windows "无网络"横幅是假的**：校园网劫持了系统的 NCSI 探测，博客其实一直在线。排查网络问题前，先分清"系统横幅"和"实际连通性"。（和校园网那篇也联系上了...）

### 外观关

7. **`reset.css` 把 `<table>` 设成了 `display: block`**：加宽后右侧冒出一列"幻影空列"，本质是块级表格的分隔线渲染。显式恢复 `display: table`。
8. **代码高亮没做亮色适配**：暗色主题的 Chroma 配色在亮色下文字接近隐形。生成了一套亮色配色覆盖。
9. **像素对齐靠 padding 是追不上的**：输入框下划线和导航下划线差 7px，padding 调到天荒地老也没对齐——因为边框永远贴盒子外缘。最后用**几何构造**解决：让两个盒子的高度差恰好等于边框+内边距的差。教训：**对齐问题是几何问题，不是试出来的**。
10. **Google Sans 系字体不随主题**：Google Fonts CDN 在国内时通时断，直接自托管字体文件一劳永逸。

### 评论关

11. **`*.vercel.app` 国内是间歇性被墙的**：评论区时好时坏。解法是给评论服务绑自己的子域 `api.javasee.com`，前面挂 Cloudflare 代理（橙云）——国内流量走 Cloudflare 边缘回源，绕开抽风节点。另配了 8 秒超时提示兜底。
12. **上游依赖的 bug 比想象中近**：Waline 的 GitHub 存储层 `select()` 把 `slice(offset, limit)` 写反了，导致管理页评论列表永远是空的。用本地桩模拟逼出原形后，在自己的入口文件对原型打补丁修复——不动依赖包，重部署不丢。
13. **SVG data-URI 里的 `#` 号会截断整个 URI**：`fill='#4285F4'` 的井号是 URI 片段分隔符，头像直接废掉。改成 `%23` 编码，所有旧评论头像实时痊愈（头像是读取时生成的，不入库）。
14. **存评论时"路径"要用页面相对路径**：用完整 URL 存，页面按相对路径查，评论永远对不上号——数据看起来丢了，其实只是钥匙不对。

## 结果

- ✅ 站点本地构建通过，GitHub Actions 自动部署
- ✅ 域名 javasee.com 上线（HTTPS 强制、www 跳转、DNSSEC）
- ✅ Material 3 定制主题：灰紫色调、Google Sans Flex + 思源黑体自托管、亮暗双模式全套
- ✅ 评论系统完整交付：匿名 + 登录、管理后台、原生 emoji、字母头像、国内稳定访问
- ✅ 快照回退机制：批量改动前打 `snapshot-*` 标签，坏了随时回到上一版

## 下次可以做得更好

- 图片统一压缩成 WebP 再上传
- 评论邮件回复通知（配 SMTP 即可）
- 大改样式前先量好"几何等式"再动手，少走像素试错的弯路
