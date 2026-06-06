from pathlib import Path
import xml.etree.ElementTree as ET

svg = Path(r"..\..\scenarios\level-1-visibility\api-gateway-health-monitoring\diagrams\operational-poster.svg")

try:
    ET.parse(svg)
    print("[OK] SVG XML is valid")
except ET.ParseError as e:
    print("[FAILED]", e)
    line, col = e.position
    lines = svg.read_text(encoding="utf-8").splitlines()
    for idx in range(max(0, line - 4), min(len(lines), line + 3)):
        marker = ">>" if idx + 1 == line else "  "
        print(f"{marker} {idx + 1}: {lines[idx]}")
