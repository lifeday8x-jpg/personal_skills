#!/usr/bin/env python3
"""Generate a compact art brief and prompt scaffold for the ritual UI asset skill."""

from __future__ import annotations

import argparse
from textwrap import dedent


ASSET_PRESETS = {
    "vertical-main-screen": {
        "purpose": "first playable ritual interaction screen",
        "canvas": "9:16, 1024x1792 or 1080x1920",
        "composition": "centered Lingjian scanner, Shanhai ink depth, lower third reserved for controls",
    },
    "lingjian-device": {
        "purpose": "reusable central spirit diagnostic apparatus",
        "canvas": "square or transparent isolated PNG",
        "composition": "front-facing jade/brass circular device with simple maskable silhouette",
    },
    "root-bone-result-card": {
        "purpose": "post-scan result card background and frame",
        "canvas": "vertical card or transparent frame",
        "composition": "jade panel, brass rim, empty title areas, restrained glow",
    },
    "ritual-button": {
        "purpose": "tappable control set",
        "canvas": "512x512 or atlas-friendly transparent PNG",
        "composition": "round jade button states with simple glyph icons",
    },
    "astrolabe-ui": {
        "purpose": "rotating rings, scan overlays, star dial components",
        "canvas": "square transparent PNG",
        "composition": "concentric rings, compass ticks, constellation nodes, talisman glyph circle",
    },
    "energy-effect": {
        "purpose": "elemental VFX source",
        "canvas": "transparent PNG or dark preview sheet",
        "composition": "disciplined spiritual glow, particles, ink or meridian motion",
    },
    "ink-shanhai-background": {
        "purpose": "background plate",
        "canvas": "9:16 or wider parallax plate",
        "composition": "mist mountains, cloud sea, ritual terrace, open center and lower UI space",
    },
    "spirit-bone-silhouette": {
        "purpose": "human root-bone scanning overlay",
        "canvas": "transparent PNG",
        "composition": "androgynous translucent body, meridians, bones, light nodes",
    },
}


def build_prompt(asset_type: str, focus: str) -> str:
    preset = ASSET_PRESETS[asset_type]
    return dedent(
        f"""
        ART BRIEF
        Asset type: {asset_type}
        Purpose: {preset["purpose"]}
        Canvas: {preset["canvas"]}
        Composition: {preset["composition"]}
        Focus: {focus}

        GENERATION PROMPT
        {asset_type}, {preset["purpose"]}, eastern fantasy modern ritual mobile game UI asset,
        Lingjian spirit diagnostic device language, Shanhai ink atmosphere, jade and aged brass materials,
        luminous teal talisman glyphs, fine gold astrolabe measurement lines, calm mysterious immortal mood,
        {preset["composition"]}, layered game asset, readable phone-scale shapes, no baked text

        NEGATIVE DIRECTION
        avoid ordinary questionnaire UI, avoid red gold webgame style, avoid generic tarot,
        avoid medical sci-fi scanner, avoid character poster composition, avoid tiny unreadable text,
        avoid cluttered lower touch zone
        """
    ).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an eastern mystic ritual UI asset brief.")
    parser.add_argument("asset_type", choices=sorted(ASSET_PRESETS))
    parser.add_argument("--focus", default="production-ready visual direction")
    args = parser.parse_args()
    print(build_prompt(args.asset_type, args.focus))


if __name__ == "__main__":
    main()
