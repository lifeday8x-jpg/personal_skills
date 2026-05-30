# Q-Version Xianxia Mobile Art Specification

## Proportion Guide

| Proportion | Best For | Notes |
| --- | --- | --- |
| 2-head | mascots, spirit pets, baby monsters, comic expressions | Very cute, simple shapes, weak costume detail. |
| 2.5-head | shop NPCs, minor disciples, casual townsfolk, small monsters | Balanced cuteness and readable clothing. |
| 3-head | playable heroes, main NPCs, standard monsters, combat sprites | Recommended default for mobile RPG production. |
| 3.5-head | premium characters, bosses, gacha cards, story illustrations | More elegant, less toy-like, better for dramatic poses. |

Use larger hands, sleeves, weapons, hats, tails, and props to improve small-screen recognition. Keep the waist and legs simplified for sprites.

## Mobile Game Asset Categories

### Characters

- Playable male/female cultivators.
- Sect disciples by rank: outer disciple, inner disciple, elder, sect master.
- NPCs: merchant, alchemist, blacksmith, storyteller, innkeeper, wandering swordsman.
- Story roles: childhood friend, rival, mysterious master, demon cultivator, immortal envoy.

### Creatures

- Spirit pets: fox, crane, deer, koi, rabbit, cat-like beast, little dragon.
- Monsters: bamboo demon, paper talisman spirit, mountain goblet spirit, cloud beast, sword wraith.
- Bosses: demon lord, ancient dragon, fallen immortal, corrupted sect elder, abyssal lotus.
- Mounts: flying sword, cloud deer, crane, gourd, qilin-inspired mount.

### Equipment and Props

- Weapons: flying sword, fan, flute, spear, umbrella, ribbon, brush, guqin.
- Magic treasures: jade seal, spirit gourd, alchemy furnace, lotus lamp, talisman bell.
- Items: pills, herbs, ores, scrolls, sect tokens, formation flags.

### Scenes

- Newbie village, sect gate, training ground, scripture pavilion, alchemy room.
- Bamboo forest, misty mountain, immortal cave, lotus pond, sword tomb.
- Market street, tea house, ferry crossing, river town.
- Demon valley, ancient battlefield, thunder peak, heavenly palace.

### UI and Icons

- Avatar frames, rarity frames, skill icons, item icons, quest markers.
- Sect badges, currency icons, bag tabs, combat buttons, minimap markers.
- Gacha cards, reward panels, event banners, chapter maps.

## Visual Language

### Silhouette

Give each asset one strong read at thumbnail size:

- sword sect: long sword, sharp sleeves, straight posture.
- alchemy sect: gourd, pill furnace, round motifs.
- talisman sect: paper charms, cinnabar lines, square seals.
- music sect: flute, guqin, ribbon, flowing sleeves.
- beast sect: ears, tails, claws, fur collars.
- demon faction: asymmetric horns, dark jade, broken halos, smoky edges.

### Color

Use one main color, one support color, and one accent:

- sword sect: moon white, dark teal, silver light.
- alchemy sect: warm ivory, herb green, cinnabar.
- talisman sect: ink black, paper yellow, vermilion.
- lotus/healing sect: pale green, lotus pink, soft gold.
- demon faction: charcoal, deep red, poisonous green or violet.
- heavenly faction: white jade, pale gold, sky cyan.

Avoid palettes dominated by only one hue. Keep ink and paper textures present but do not make every asset beige.

## Rendering Levels

### Sprite-Level

Use simplified shading, large shapes, clear edges, and limited accessories. Design clothing in separable layers: hair, head accessory, torso, sleeves, weapon, back ornament.

### Concept-Level

Use more garment detail, clear material notes, front/side/back or three-quarter view, and call out animation-critical parts.

### Splash/Card-Level

Use dynamic pose, stronger atmosphere, richer ink wash, dramatic spiritual effects, and more background context. Still preserve chibi proportions if the game style requires it.

## Prompt Formula

For Chinese prompt packs, use:

`主题 + 头身比例 + 角色定位 + 门派/阵营 + 服装/武器/法宝 + 姿态表情 + 水墨表现 + 色彩 + 手游资产要求 + 视角/背景 + 质量词`

Example:

`Q版三头身修仙少女，剑宗内门弟子，圆润脸型，大眼睛，月白短袍与青色披帛，背负小飞剑，手持竹简，轻盈站姿，微笑，水墨晕染边缘，宣纸纹理，淡青与银白配色，手游角色立绘，正面三分之二视角，干净浅色背景，高辨识度，精致但不过度复杂`

For English image models, use:

`chibi 3-head proportion xianxia mobile game character, ink wash Chinese fantasy style, [role], [costume], [weapon/treasure], cute rounded face, clear silhouette, xuan paper texture, soft brush edges, low saturation palette with [accent color], three-quarter front view, clean light background, mobile game concept art, readable at small size`

## Negative Prompt Defaults

Use these unless the task needs a different boundary:

`realistic adult anatomy, long realistic body, western medieval armor, sci-fi armor, cyberpunk, horror gore, overly complex ornaments, unreadable details, messy background, photorealistic skin, harsh 3D render, dark muddy colors, extra fingers, malformed hands, text, watermark, logo`

## Outsourcing Brief Checklist

For outsource-ready requests, include:

- asset name and use case,
- canvas ratio or approximate resolution if known,
- head-body proportion,
- view count,
- required expressions or poses,
- animation-sensitive parts,
- color palette,
- faction identifiers,
- forbidden elements,
- export needs such as transparent background, layered PSD, or icon-safe crop.

If the user does not know the game structure, propose a starter scope:

- 4 playable archetypes,
- 3 sect factions,
- 12 NPCs,
- 16 monsters,
- 4 bosses,
- 6 spirit pets,
- 6 mounts,
- 40 item/equipment icons,
- 20 skill icons,
- 6 major scenes,
- 1 UI visual direction sheet.
