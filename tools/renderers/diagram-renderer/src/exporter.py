from pathlib import Path

from playwright.sync_api import (
    sync_playwright
)


def export_svg(
    output_path: Path,
    svg_content: str
):

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(svg_content)


def export_png(
    svg_path: Path,
    png_path: Path
):

    png_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch()

        page = browser.new_page()

        page.goto(
            f"file:///{svg_path.resolve()}"
        )

        page.screenshot(
            path=str(png_path)
        )

        browser.close()
