# 生成 Catppuccin Latte（亮色）版的 chroma 高亮样式
# 读取主题的 mocha 配色文件，按风味名映射为 latte，选择器加亮色模式限定
import re

SRC = r"L:\Blog-Javasee\themes\PaperMod\assets\css\includes\chroma-styles.css"
DST = r"L:\Blog-Javasee\assets\css\extended\md3-chroma-light.css"

MOCHA_TO_LATTE = {
    "#f5a97f": "#fe640b",  # peach
    "#a6da95": "#40a02b",  # green
    "#6e738d": "#7c7f93",  # overlay2
    "#ed8796": "#d20f39",  # red
    "#8aadf4": "#1e66f5",  # blue
    "#f4dbd6": "#dc8a78",  # rosewater
    "#91d7e3": "#04a5e5",  # sky
    "#c6a0f6": "#8839ef",  # mauve
    "#8bd5ca": "#179299",  # teal
    "#eed49f": "#df8e1d",  # yellow
    "#cad3f5": "#4c4f69",  # text
    "#8087a2": "#8c8fa1",  # overlay1
    "#363a4f": "#ccd0da",  # surface0
    "#24273a": "#eff1f5",  # base
    "#474733": "#e6e9ef",  # line highlight -> mantle
}

src = open(SRC, encoding="utf-8").read()

def remap_hex(m):
    return MOCHA_TO_LATTE.get(m.group(0).lower(), m.group(0))

out_lines = []
for line in src.splitlines():
    if not line.strip():
        continue
    line = re.sub(r"#[0-9a-fA-F]{6}", remap_hex, line)
    # 给选择器加亮色模式限定（保留行首注释）
    line = re.sub(
        r"^(\s*(?:/\*.*?\*/\s*)?)(\.bg|\.chroma)",
        r"\1:root:not([data-theme=\"dark\"]) \2",
        line,
    )
    out_lines.append(line)

header = (
    "/* ===== Catppuccin Latte 亮色高亮（由 mocha 自动转译） =====\n"
    "   暗色模式沿用主题自带的 mocha 配色；本文件只在亮色模式生效 */\n"
)
open(DST, "w", encoding="utf-8").write(header + "\n".join(out_lines) + "\n")
print("written:", DST, len(out_lines), "rules")
