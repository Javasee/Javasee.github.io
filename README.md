# Javasee's Blog

基于 Hugo + PaperMod 的个人博客，托管于 GitHub Pages。

## 日常写文章

1. 新建文章：
   - 随笔：`content/essays/文章名.md`
   - 工程复盘：`content/retro/文章名.md`
2. 文章开头的 front matter 写好 `title`、`date`、`tags`，把 `draft: false`
3. 图片两种放法：
   - 推荐：整篇放一个文件夹 `content/essays/文章名/index.md` + 图片，正文直接 `![说明](图片.jpg)`
   - 或放 `static/images/`，正文引用 `/images/图片.png`
4. 发布：

```bash
git add .
git commit -m "new post: 文章名"
git push
```

GitHub Actions 会自动构建并发布（约 1 分钟）。

## 本地预览

```bash
hugo server -D
```

浏览器打开 http://localhost:1313

## 以后绑定域名 javasee.com

1. 注册域名后，在域名商 DNS 添加：
   - `A` 记录 `@` → `185.199.108.153` / `185.199.109.153` / `185.199.110.153` / `185.199.111.153`
   - `CNAME` 记录 `www` → `<用户名>.github.io`
2. 仓库 Settings → Pages → Custom domain 填 `javasee.com`，勾选 Enforce HTTPS
3. 把 `hugo.toml` 里 `baseURL` 改成 `https://javasee.com/`

（Actions 工作流会自动跟随 Pages 的域名配置，无需改动。）
