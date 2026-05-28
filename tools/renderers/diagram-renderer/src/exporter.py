from pathlib import Path
import re

from playwright.sync_api import sync_playwright


def extract_svg_size(
    svg_content: str
):

    width_match = re.search(
        r'<svg[^>]*width="(\d+)"',
        svg_content
    )

    height_match = re.search(
        r'<svg[^>]*height="(\d+)"',
        svg_content
    )

    if not width_match or not height_match:

        raise ValueError(
            "SVG width/height not found."
        )

    return int(width_match.group(1)), int(height_match.group(1))


def export_png(
    svg_path: Path
):

    png_path = svg_path.with_suffix(
        ".png"
    )

    svg_content = svg_path.read_text(
        encoding="utf-8"
    )

    width, height = extract_svg_size(
        svg_content
    )

    html = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
html, body {{
    margin: 0;
    padding: 0;
    width: {width}px;
    height: {height}px;
    overflow: hidden;
    background: #0f172a;
}}
svg {{
    display: block;
    width: {width}px;
    height: {height}px;
}}
</style>
</head>
<body>
{svg_content}
</body>
</html>
"""

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch()

        page = browser.new_page(
            viewport={
                "width": width,
                "height": height
            },
            device_scale_factor=1
        )

        page.set_content(
            html,
            wait_until="load"
        )

        page.screenshot(
            path=str(
                png_path
            ),
            full_page=False,
            omit_background=False
        )

        browser.close()

    print(
        f"Generated PNG: {png_path}"
    )
