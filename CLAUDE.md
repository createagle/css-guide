# CSS 完全指南 · 协作约定

本仓库是《CSS 完全指南》（5 篇 40 章）的配套示例。教程正文写在 Claude Docs 文档里，
示例代码放在这里并部署到 https://createagle.github.io/css-guide/ ，正文引用线上地址。
约定与姊妹项目《HTML 完全指南》（createagle/html-guide）、《SVG 完全指南》（createagle/svg-complete-guide）保持一致。

## 提交与部署（每次改动都要做）

1. 改完代码后先本地验证：`python3 -m http.server` 起服务，用 Playwright（Chromium 已预装）打开页面截图，
   亮色、暗色都看一遍，交互控件实际操作一次，并确认控制台没有报错。
2. 提交并推送到当前会话指定的 `claude/**` 分支：`git push -u origin <分支>`。
3. 推送会触发 `.github/workflows/sync-main.yml`：把分支快进合并到 `main`（没有 `main` 时直接创建），
   再触发 `pages.yml` 部署。不需要手动开 PR 或合并。
4. 推送后检查两个 workflow 是否成功；失败要排查修复，不要把失败的部署留着。
5. 文档里引用的示例链接只写已部署成功的页面。

快进失败说明 `main` 上有分支没有的提交（例如有人在网页上直接改了 main）：
先 `git fetch origin main && git merge origin/main`，解决冲突后再推送。

## 示例约定

- 目录：`chapters/<NN-slug>/<NN-name>.html`，每章一个 `README.md`（及 `README.zh-CN.md`）。
- 练习：`exercises/` 放每道题的初始版本 `NN-start.html` 和成品版本 `NN-final.html`（没有代码的题不放）。
  **两个版本都必须能在 GitHub Pages 上直接预览**（`body.demo` + 公共样式，英文文案）。
  README 用表格列出每题的在线预览链接和源码文件。题目与参考答案写在文档里：每道题一个三级标题，题目下写
  `初始效果：[在线预览](Pages 地址) · [查看源码](GitHub 地址)`；参考答案用可折叠 widget
  （`<details>` + `<summary>参考答案</summary>`，默认收起，不加 text id），末尾写
  `最终效果：在线预览 · 查看源码` 两个链接。
- **示例页只放演示本身**：不写标题、说明文字、面包屑、源码面板。讲解全部写在 Claude Docs 文档里。
  页面要能直接作为 iframe 内嵌。演示本身就是「样式作用在一段内容上的结果」时，页面里出现的标题、段落属于演示内容，可以保留。
- **GitHub Pages 上的页面文案一律用英文**（`<title>`、控件标签、图注、`alt`、`aria-label`）；
  演示中文排版、国际化等必须出现中文的地方除外。
- **仓库里的 Markdown 一律中英双语**：英文写在 `README.md`，中文写在同目录的 `README.zh-CN.md`，
  两个文件 H1 下第一行放语言切换：英文版 `**English** | [简体中文](README.zh-CN.md)`，
  中文版 `[English](README.md) | **简体中文**`。两版内容保持一致，改一版就同步改另一版；
  中文版里指向其他 README 的链接指向 `README.zh-CN.md`。`CLAUDE.md` 是协作约定，不需要双语。
- 页面结构：`<body class="demo">` 内放可选的 `<div class="controls">` 控件和 `<div class="stage">` 演示区，
  引用 `../../assets/style.css`（练习页是 `../../../assets/style.css`）。演示需要的样式写在页面 `<head>` 的 `<style>` 里。
  公共样式提供 `.panel`（带边框的结果区）、`.label`（小标题）、`pre.code`（代码读数）、`.good` / `.bad`。
- 零依赖、双击可打开；支持暗色模式和 `prefers-reduced-motion`。
- 示例本身要符合本书讲的写法：HTML 语义正确、能用键盘操作、表单控件有 label；CSS 用现代写法（逻辑属性、`oklch()`、自定义属性），
  演示较新的特性时用 `@supports` 给出降级，页面在不支持的浏览器里也不能坏掉。
- 新增示例后同步更新本章 `README.md`、`README.zh-CN.md`，再运行 `python3 tools/build_index.py` 重新生成根目录 `index.html`（它读取各章英文 README 的示例表格）。
- 文档里引用的代码片段要与页面源码一致；改了页面就同步改文档。

## 文档约定（Claude Docs）

- 文档结构：「教学大纲」标签页在最前；五个「第 N 篇」标签页按顺序排列，每章是所属篇下的子标签页，
  名为「第 N 章 标题」。
- 小标题带序号，每个标签页内从 1 开始逐级编号：二级标题 `1.`、`2.`…，三级标题 `1.1`、`1.2`…，
  四级标题 `1.1.1`…。不要把章号带进小标题。
- 每章按大纲的 7 段式结构写，每个示例配「在线演示」「查看源码」两个链接。
- 阅读时长：只在章标题下一行写 `*全章阅读约 N 分钟，不含练习动手时间*`，各节不单独标注。
  必须用 `tools/reading_time.py` 实测，不要凭印象估：用 Claude Docs `export`（format=markdown）导出该章，
  把返回的 `bytes_b64` 原样存成文件，先核对解码后的字节数与导出结果的 `bytes` 一致，再运行
  `python3 tools/reading_time.py --b64 <文件>`。估算标准写在脚本开头（正文 400 字/分钟、代码 10 行/分钟、
  表格 3 行/分钟、每张图 0.5 分钟、每个在线演示 1 分钟，每节向上取整后相加）。内容改动后重新实测并更新。

## 链接格式

- 在线演示：`https://createagle.github.io/css-guide/chapters/<章目录>/<示例>.html`
- 查看源码：`https://github.com/createagle/css-guide/blob/main/chapters/<章目录>/<示例>.html`
