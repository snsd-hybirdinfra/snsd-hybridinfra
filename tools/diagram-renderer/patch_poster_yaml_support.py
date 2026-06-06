from pathlib import Path

target = Path(r".\tools\diagram-renderer\orchestration_entrypoint.py")

text = target.read_text(encoding="utf-8")

old = '''def render_scenario(
    metadata_path: Path
):

    metadata = load_yaml(
        metadata_path
    )

    data = build_poster_data_from_scenario_metadata(
        metadata_path,
        metadata
    )

    svg = build_poster_svg(
        data
    )

    svg_path, png_path = resolve_scenario_output_paths(
        metadata_path
    )

    write_svg(
        svg_path,
        svg
    )

    convert_svg_to_png(
        svg_path,
        png_path
    )

    print(
        f"[OK] Rendered scenario SVG: {svg_path}"
    )

    print(
        f"[OK] Rendered scenario PNG: {png_path}"
    )

    return {
        "svg": svg_path,
        "png": png_path
    }
'''

new = '''def render_scenario(
    metadata_path: Path
):

    poster_path = metadata_path.parent / "poster.yaml"

    if poster_path.exists():

        data = load_yaml(
            poster_path
        )

        print(
            f"[INFO] Using poster.yaml: {poster_path}"
        )

    else:

        metadata = load_yaml(
            metadata_path
        )

        data = build_poster_data_from_scenario_metadata(
            metadata_path,
            metadata
        )

        print(
            f"[INFO] Using metadata fallback: {metadata_path}"
        )

    svg = build_poster_svg(
        data
    )

    svg_path, png_path = resolve_scenario_output_paths(
        metadata_path
    )

    write_svg(
        svg_path,
        svg
    )

    convert_svg_to_png(
        svg_path,
        png_path
    )

    print(
        f"[OK] Rendered scenario SVG: {svg_path}"
    )

    print(
        f"[OK] Rendered scenario PNG: {png_path}"
    )

    return {
        "svg": svg_path,
        "png": png_path
    }
'''

if old not in text:
    raise SystemExit("Patch target block not found. render_scenario() structure may differ.")

text = text.replace(old, new)

target.write_text(text, encoding="utf-8")

print("Patched orchestration_entrypoint.py: poster.yaml priority enabled")
