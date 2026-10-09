# CSS 完全指南 · 示例代码

[English](README.md) | **简体中文**

《CSS 完全指南》（5 篇 40 章）的配套示例，部署在 GitHub Pages：

**https://createagle.github.io/css-guide/**

## 目录约定

```text
index.html                     # 示例总目录（按篇、章导航），由 tools/build_index.py 生成
assets/
  style.css                    # 公共样式：亮/暗色主题、居中演示布局、prefers-reduced-motion
  fonts/                       # Roboto Flex 可变字体（woff2，拉丁字符子集）及其 OFL 许可证
chapters/
  01-intro/
    README.md                  # 本章示例说明
    01-stylesheets.html        # 一个示例一个独立页面
    exercises/                 # 练习的初始代码（NN-start）与成品代码（NN-final）
  02-selectors/
  ...
tools/
  build_index.py               # 根据各章 README 重新生成 index.html
  reading_time.py              # 按章节 Markdown 导出估算阅读时长
.github/workflows/
  pages.yml                    # push 到 main 即自动部署
  sync-main.yml                # claude/** 分支自动快进到 main 并部署
```

- 示例链接：`https://createagle.github.io/css-guide/chapters/<章目录>/<示例>.html`
- 查看源码：`https://github.com/createagle/css-guide/blob/main/chapters/<章目录>/<示例>.html`
- 示例页只放演示本身（英文文案，无说明），可直接 iframe 内嵌；讲解在教程文档里。
- 示例都是零依赖的 HTML 页面，双击即可打开（第 29 章的跨文档视图过渡需要本地服务器或线上地址）；统一支持暗色模式和 `prefers-reduced-motion`。
- 所有 Markdown 文件都有英文（`README.md`）和中文（`README.zh-CN.md`）两个版本，顶部互相链接切换。

### 新增示例

1. 复制一个现有示例页，修改英文 `<title>`、控件和 `.stage` 里的代码。
2. 在本章 `README.md` 和 `README.zh-CN.md` 的表格里各加一行。
3. 运行 `python3 tools/build_index.py` 重新生成 `index.html`。

## 部署

- `.github/workflows/sync-main.yml`：推送到 `claude/**` 分支后，自动快进合并到 `main` 并触发部署。
- `.github/workflows/pages.yml`：推送到 `main`（或被上面的 workflow 触发）时部署到 GitHub Pages。

首次使用需在仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**，并把 `main` 设为默认分支。

本地预览：

```sh
python3 -m http.server 8000
# 打开 http://localhost:8000/
```

## 许可证

[MIT](LICENSE)。`assets/fonts/` 里的 Roboto Flex 字体采用 [SIL Open Font License 1.1](assets/fonts/OFL.txt)。
