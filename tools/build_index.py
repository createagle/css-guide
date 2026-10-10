#!/usr/bin/env python3
"""Regenerate the root index.html from each chapter's README.md demo table.

Run after adding or renaming a demo:  python3 tools/build_index.py
A demo row in chapters/<dir>/README.md looks like:
| 5-1 OKLCH vs HSL | [01-oklch.html](https://createagle.github.io/css-guide/chapters/05-color/01-oklch.html) | ... |
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

PARTS = [
    ('Part 1 · Basics', [
        ('01-intro', 'Meet CSS'),
        ('02-selectors', 'Selector Basics'),
        ('03-cascade', 'Cascade, Specificity & Inheritance'),
        ('04-values-units', 'Values & Units'),
        ('05-color', 'Color'),
        ('06-box-model', 'The Box Model'),
        ('07-typography', 'Text & Fonts'),
        ('08-backgrounds', 'Backgrounds, Borders & Shadows'),
    ]),
    ('Part 2 · Layout', [
        ('09-flow', 'Normal Flow & Formatting Contexts'),
        ('10-positioning', 'Positioning & Stacking Contexts'),
        ('11-flexbox', 'Flexbox Basics'),
        ('12-flexbox-advanced', 'Flexbox in Depth'),
        ('13-grid', 'Grid Basics'),
        ('14-grid-advanced', 'Grid in Depth'),
        ('15-float-multicol', 'Floats, Multi-column & More'),
        ('16-overflow-scroll', 'Overflow & Scrolling'),
    ]),
    ('Part 3 · Responsive & Modern CSS', [
        ('17-media-queries', 'Responsive Design & Media Queries'),
        ('18-container-queries', 'Container Queries'),
        ('19-intrinsic', 'Fluid Sizing & Intrinsic Design'),
        ('20-custom-properties', 'Custom Properties'),
        ('21-nesting-scope', 'Nesting & @scope'),
        ('22-layers', 'Cascade Layers'),
        ('23-selectors', 'Modern Selectors'),
        ('24-pseudo-elements', 'Pseudo-elements & Generated Content'),
    ]),
    ('Part 4 · Visuals & Motion', [
        ('25-transitions', 'Transitions'),
        ('26-transforms', 'Transforms'),
        ('27-keyframes', 'Keyframe Animations'),
        ('28-scroll-driven', 'Scroll-driven Animations'),
        ('29-view-transitions', 'View Transitions'),
        ('30-filters-masks', 'Filters, Blending & Masks'),
        ('31-anchor-positioning', 'Anchor Positioning & Top-layer UI'),
        ('32-form-styling', 'Styling Forms & Components'),
    ]),
    ('Part 5 · Engineering & Practice', [
        ('33-architecture', 'CSS Architecture & Naming'),
        ('34-theming', 'Theming & Dark Mode'),
        ('35-a11y', 'Accessibility & CSS'),
        ('36-performance', 'Rendering Performance'),
        ('37-debugging', 'Debugging, Compatibility & Tooling'),
        ('38-frameworks', 'CSS in Frameworks & Components'),
        ('39-capstone', 'Capstone Project'),
        ('40-tools-future', 'Resources & the Future'),
    ]),
]

ROW = re.compile(r'^\|\s*(\d+-\d+)\s+(.+?)\s*\|\s*\[([^\]]+?\.html)\]')


def demos(slug):
    readme = ROOT / 'chapters' / slug / 'README.md'
    if not readme.exists():
        return []
    out = []
    for line in readme.read_text(encoding='utf-8').splitlines():
        m = ROW.match(line)
        if m:
            out.append((m.group(1), m.group(2), f'chapters/{slug}/{m.group(3)}'))
    return out


def main():
    parts = []
    n = 0
    for title, chapters in PARTS:
        first, last = n + 1, n + len(chapters)
        items = []
        for slug, name in chapters:
            n += 1
            links = ' · '.join(f'<a href="{html.escape(href)}">{num} {html.escape(label)}</a>' for num, label, href in demos(slug))
            ex = f'\n      <div class="examples">{links}</div>' if links else '\n      <div class="examples">Coming soon</div>'
            items.append(f'    <li>{n}. {html.escape(name)}{ex}\n    </li>')
        parts.append(f'  <h2>{html.escape(title)} (Ch. {first}–{last})</h2>\n  <ul class="chapters">\n' + '\n'.join(items) + '\n  </ul>')
    page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CSS Complete Guide · Demos</title>
  <meta name="description" content="Runnable demos for the CSS Complete Guide, 5 parts and 40 chapters.">
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
<main>
  <h1>CSS Complete Guide · Demos</h1>
  <p><a href="https://github.com/createagle/css-guide">Source on GitHub</a></p>

{chr(10).join(parts)}
</main>
</body>
</html>
'''
    (ROOT / 'index.html').write_text(page, encoding='utf-8')
    print('index.html written')


if __name__ == '__main__':
    main()
