---
name: eastern-mystic-ui-skill
description: Generate and refine AI image prompts, art briefs, and game-ready asset direction for an eastern mystic mobile game UI style centered on a Lingjian spirit-diagnostic device, Shanhai ink landscapes, jade/brass astrolabe UI, glowing talisman glyphs, root-bone result cards, ritual buttons, spiritual energy effects, and translucent human bone/meridian silhouettes. Use when Codex needs to create or critique concept art prompts, mobile UI concept screens, image generation batches, asset lists, style profiles, or production checklists for this specific eastern fantasy modern ritual interface direction.
---

# Eastern Mystic UI Skill

## Core Intent

Produce assets for a vertical mobile game where the player does not feel they are answering a questionnaire. They are operating a mysterious Lingjian device that scans the body, reads root-bone fate, and presents the result through a modern ritual UI.

Keep the visual thesis stable:

- Core object: Lingjian device, bone-reading platform, fate astrolabe, jade/brass scanning ring.
- Environment: Shanhai ink mountains, mist, moon, cloud sea, floating pavilions, quiet ritual space.
- Interaction language: jade buttons, rotating star dials, luminous talisman rings, meridian/bone imaging, fine gold measurement lines.
- Mood: immortal, arcane, calm, diagnostic, mysterious; avoid noisy page-game grandeur.

## Workflow

1. Identify the requested asset type.
   - For complete screens, read `references/asset-types.md` and `references/mobile-game-adaptation.md`.
   - For style or prompt details, read `references/style-profile.md`.
   - For batch prompt generation, use `scripts/generate_asset_brief.py`.

2. Convert the user request into a game asset brief.
   Include purpose, aspect ratio, foreground object, background depth, UI interaction zone, material palette, negative direction, and expected deliverables.

3. Separate concept appeal from mobile usability.
   A concept image may be ornate; a game asset must reserve readable touch zones, keep symbols large enough, and avoid over-rendering the lower navigation/buttons.

4. Generate prompts in layers.
   Use one prompt for the whole screen only when exploring mood. For production, create separate prompts for background, device, UI ornaments, result card, button states, effects, and silhouettes.

5. Add constraints for cleanup.
   Ask for transparent background, isolated object, centered orthographic view, consistent lighting, simple silhouette, or atlas-friendly spacing when the asset will be cut into a game container.

6. Review output with the checklist in `references/mobile-game-adaptation.md`.
   Reject outputs that look like ordinary quiz cards, red/gold page-game UI, generic tarot, sci-fi hospital scanner, or character illustration first.

## Asset Families

- `vertical-main-screen`: full 9:16 home or ritual interaction concept.
- `lingjian-device`: circular jade/brass apparatus, scanning mirror, bone-reading stage.
- `root-bone-result-card`: result background, frame, title plaque, grade emblem, glow layer.
- `ritual-button`: jade round button, talisman tab, held/disabled/active states.
- `astrolabe-ui`: rotating ring, star dial, compass ticks, constellation lines.
- `energy-effect`: thunder, wood, water, fire, star, shadow, qi, meridian glow.
- `ink-shanhai-background`: layered mist mountains and ritual terrace.
- `spirit-bone-silhouette`: translucent human, bones, meridians, chakra-like points.

## Prompt Shape

Use this structure unless the user provides a better one:

```text
[asset type], [game function], vertical mobile game UI asset,
Lingjian spirit diagnostic device, Shanhai ink fantasy environment,
jade and aged brass astrolabe interface, luminous talisman glyphs,
calm mysterious ritual mood, readable touch zones, layered game asset,
[specific composition], [material/lighting constraints],
avoid questionnaire card, avoid red gold webgame style, avoid generic tarot,
avoid character-poster composition, avoid cluttered tiny UI text
```

For production batches, prefer multiple focused prompts over one overloaded prompt.

## Reference Images

Use the bundled reference images only as visual direction, not as files to reproduce exactly:

- `assets/reference-images/lingjian-device-human-scan.png`: strongest for the core Lingjian scanner and spiritual body imaging.
- `assets/reference-images/shanhai-oracle-stage-cards.png`: strongest for game screen composition, stage depth, and bottom card/button placement.
- `assets/reference-images/ink-star-dial-ui.png`: strongest for ink motion, star dial ornament, and ritual UI geometry.

## Output Expectations

When asked for prompts, return:

- A concise art brief.
- 3-6 generation prompts grouped by asset family.
- Negative prompt / avoid list.
- Mobile-game adaptation notes.
- Optional export specs such as `PNG`, transparent background, `9:16`, `1024x1792`, `2048x2048`, or sprite atlas padding.

When asked to critique images, return:

- What matches the intended direction.
- What harms game usability.
- What to regenerate separately.
- A revised prompt or production split.
