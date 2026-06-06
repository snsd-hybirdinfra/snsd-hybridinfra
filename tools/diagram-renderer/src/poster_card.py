from src.poster_theme import PANEL, BORDER, TEXT_PRIMARY, TEXT_SECONDARY, TEXT_MUTED, status_color
from src.text_utils import escape_truncated


def build_card_icon(cx, cy, color, card_type):
    icon_type = str(card_type).lower().strip()

    parts = [
        f'<circle cx="{cx}" cy="{cy}" r="22" fill="#020617" stroke="{color}" stroke-width="2" />'
    ]

    if icon_type == "gateway":
        parts.extend([
            f'<rect x="{cx - 11}" y="{cy - 9}" width="22" height="18" rx="4" fill="none" stroke="{color}" stroke-width="2" />',
            f'<line x1="{cx - 5}" y1="{cy}" x2="{cx + 5}" y2="{cy}" stroke="{color}" stroke-width="2" stroke-linecap="round" />',
            f'<line x1="{cx}" y1="{cy - 5}" x2="{cx}" y2="{cy + 5}" stroke="{color}" stroke-width="2" stroke-linecap="round" />'
        ])

    elif icon_type in ["routing", "traffic-path"]:
        parts.extend([
            f'<line x1="{cx - 13}" y1="{cy - 7}" x2="{cx + 7}" y2="{cy - 7}" stroke="{color}" stroke-width="2" stroke-linecap="round" />',
            f'<polyline points="{cx + 3},{cy - 12} {cx + 10},{cy - 7} {cx + 3},{cy - 2}" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />',
            f'<line x1="{cx - 13}" y1="{cy + 8}" x2="{cx + 7}" y2="{cy + 8}" stroke="{color}" stroke-width="2" stroke-linecap="round" />',
            f'<polyline points="{cx + 3},{cy + 3} {cx + 10},{cy + 8} {cx + 3},{cy + 13}" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />'
        ])

    elif icon_type == "service":
        parts.extend([
            f'<rect x="{cx - 11}" y="{cy - 11}" width="22" height="22" rx="5" fill="none" stroke="{color}" stroke-width="2" />',
            f'<circle cx="{cx}" cy="{cy}" r="4" fill="{color}" />',
            f'<line x1="{cx - 17}" y1="{cy}" x2="{cx - 11}" y2="{cy}" stroke="{color}" stroke-width="2" stroke-linecap="round" />',
            f'<line x1="{cx + 11}" y1="{cy}" x2="{cx + 17}" y2="{cy}" stroke="{color}" stroke-width="2" stroke-linecap="round" />'
        ])

    elif icon_type == "probe":
        parts.extend([
            f'<circle cx="{cx}" cy="{cy}" r="5" fill="{color}" />',
            f'<circle cx="{cx}" cy="{cy}" r="12" fill="none" stroke="{color}" stroke-width="2" opacity="0.65" />',
            f'<circle cx="{cx}" cy="{cy}" r="17" fill="none" stroke="{color}" stroke-width="1.5" opacity="0.35" />'
        ])

    elif icon_type in ["metric", "telemetry"]:
        parts.extend([
            f'<line x1="{cx - 12}" y1="{cy + 9}" x2="{cx - 12}" y2="{cy - 1}" stroke="{color}" stroke-width="3" stroke-linecap="round" />',
            f'<line x1="{cx - 4}" y1="{cy + 9}" x2="{cx - 4}" y2="{cy - 10}" stroke="{color}" stroke-width="3" stroke-linecap="round" />',
            f'<line x1="{cx + 4}" y1="{cy + 9}" x2="{cx + 4}" y2="{cy - 4}" stroke="{color}" stroke-width="3" stroke-linecap="round" />',
            f'<line x1="{cx + 12}" y1="{cy + 9}" x2="{cx + 12}" y2="{cy - 13}" stroke="{color}" stroke-width="3" stroke-linecap="round" />'
        ])

    elif icon_type in ["alert", "alert-view"]:
        parts.extend([
            f'<polygon points="{cx},{cy - 14} {cx + 14},{cy + 12} {cx - 14},{cy + 12}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round" />',
            f'<line x1="{cx}" y1="{cy - 4}" x2="{cx}" y2="{cy + 4}" stroke="{color}" stroke-width="2" stroke-linecap="round" />',
            f'<circle cx="{cx}" cy="{cy + 9}" r="2" fill="{color}" />'
        ])

    elif icon_type in ["dashboard", "dashboard-panel", "console"]:
        parts.extend([
            f'<rect x="{cx - 13}" y="{cy - 10}" width="26" height="20" rx="3" fill="none" stroke="{color}" stroke-width="2" />',
            f'<polyline points="{cx - 8},{cy + 4} {cx - 2},{cy - 2} {cx + 3},{cy + 2} {cx + 9},{cy - 6}" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />'
        ])

    elif icon_type == "evidence":
        parts.extend([
            f'<polygon points="{cx - 9},{cy - 13} {cx + 5},{cy - 13} {cx + 11},{cy - 7} {cx + 11},{cy + 13} {cx - 9},{cy + 13}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round" />',
            f'<line x1="{cx - 4}" y1="{cy}" x2="{cx + 5}" y2="{cy}" stroke="{color}" stroke-width="2" stroke-linecap="round" />',
            f'<line x1="{cx - 4}" y1="{cy + 6}" x2="{cx + 5}" y2="{cy + 6}" stroke="{color}" stroke-width="2" stroke-linecap="round" />'
        ])

    elif icon_type == "validation":
        parts.extend([
            f'<rect x="{cx - 12}" y="{cy - 12}" width="24" height="24" rx="5" fill="none" stroke="{color}" stroke-width="2" />',
            f'<polyline points="{cx - 7},{cy} {cx - 1},{cy + 6} {cx + 9},{cy - 7}" fill="none" stroke="{color}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />'
        ])

    else:
        parts.extend([
            f'<circle cx="{cx}" cy="{cy}" r="7" fill="{color}" />',
            f'<circle cx="{cx}" cy="{cy}" r="14" fill="none" stroke="{color}" stroke-width="2" opacity="0.35" />'
        ])

    return "\n".join(parts)


def render_card(card, x, y, width, height):
    title = escape_truncated(card.get("title", ""), 21)
    subtitle = escape_truncated(card.get("subtitle", ""), 28)

    raw_card_type = str(card.get("type", "")).strip()
    card_type = escape_truncated(raw_card_type, 21)

    status = escape_truncated(card.get("status", ""), 10)
    color = status_color(card.get("status", ""))

    emphasis = bool(card.get("emphasis", False))
    emphasis_label = escape_truncated(card.get("emphasis_label", "CORE"), 6)

    fill = "#172554" if emphasis else PANEL
    stroke = color if emphasis else BORDER
    stroke_width = 3 if emphasis else 2

    parts = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="22" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />',

        build_card_icon(
            x + 38,
            y + 40,
            color,
            raw_card_type
        ),

        f'<text x="{x + 72}" y="{y + 32}" fill="{TEXT_PRIMARY}" font-size="16" font-weight="bold">{title}</text>',
        f'<text x="{x + 72}" y="{y + 58}" fill="{TEXT_SECONDARY}" font-size="10">{subtitle}</text>',
        f'<text x="{x + 72}" y="{y + 84}" fill="{TEXT_MUTED}" font-size="10">{card_type}</text>',

        f'<rect x="{x + width - 118}" y="{y + height - 36}" width="96" height="22" rx="11" fill="#020617" stroke="{color}" stroke-width="1" />',
        f'<text x="{x + width - 70}" y="{y + height - 20}" fill="{color}" font-size="10" text-anchor="middle" font-weight="bold">{status}</text>'
    ]

    if emphasis:
        parts.extend([
            f'<rect x="{x + width - 132}" y="{y + 16}" width="92" height="22" rx="11" fill="#020617" stroke="{color}" stroke-width="1" />',
            f'<text x="{x + width - 86}" y="{y + 31}" fill="{color}" font-size="10" text-anchor="middle" font-weight="bold">{emphasis_label}</text>'
        ])

    return "\n".join(parts)

