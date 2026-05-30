# Q-Version Urban Mobile Art Specification

## Proportion Guide

| Proportion | Best For | Notes |
| --- | --- | --- |
| 2-head | mascots, sticker figures, brand animals, emoji packs | Very cute, simple shapes, weak clothing detail. |
| 2.5-head | shop NPCs, interns, clerks, side characters, casual pedestrians | Balanced cuteness and readable outfit identity. |
| 3-head | playable characters, main NPCs, standard rivals, office/social roles | Recommended default for mobile RPG/simulation production. |
| 3.5-head | CEOs, celebrities, premium rivals, gacha cards, story illustrations | More elegant, better for dramatic pose and luxury styling. |

Use larger hands, hair shapes, bags, phones, glasses, ties, jackets, and props to improve small-screen recognition. Keep legs and shoe details simplified for sprites.

## Mobile Game Asset Categories

### Characters

- Playable urban archetypes: finance elite, tech founder, idol, designer, lawyer, student, detective, entrepreneur.
- Workplace NPCs: assistant, receptionist, HR, manager, investor, security guard, courier, barista.
- Lifestyle NPCs: gym coach, stylist, live streamer, influencer, DJ, chef, bookstore owner.
- Story roles: rival CEO, childhood friend, mysterious investor, celebrity client, street-smart hacker, luxury villain.

### Props and Equipment

- Personal props: smartphone, tablet, laptop, smartwatch, headphones, coffee cup, office badge.
- Business props: briefcase, contract folder, pen, credit card, stock chart screen, trophy, company seal.
- Fashion props: sunglasses, tie clip, handbag, sneakers, watch, scarf, perfume bottle.
- Vehicles: sports car, scooter, business sedan, city bike, subway train, helicopter for premium scenes.

### Scenes

- Office lobby, CEO office, meeting room, trading desk, coworking space.
- Cafe, convenience store, mall atrium, fashion street, rooftop bar, luxury apartment.
- Subway station, night city street, riverside promenade, airport VIP lounge.
- School gate, campus path, gym, livestream room, backstage dressing room.

### UI and Icons

- Avatar frames, rarity frames, role badges, relationship icons, task markers.
- Item icons, currency icons, stock/wealth icons, fashion tags, property badges.
- Gacha cards, reward panels, event banners, city map nodes, chapter covers.
- Skill icons for negotiation, charm, investment, creativity, fitness, tech, insight.

## Visual Language

### Silhouette

Give each asset one strong read at thumbnail size:

- business elite: sharp suit shoulders, tie, briefcase, confident stance.
- finance trader: phone/chart screen, gold highlight, focused expression.
- tech founder: hoodie or minimalist jacket, laptop/tablet, clean glasses.
- idol: soft hair volume, stage accessory, sparkling outline, elegant hand pose.
- student: backpack, school jacket, badge, energetic posture.
- street fashion: oversized jacket, sneakers, headphones, asymmetrical shape.
- luxury rival: long coat or tailored suit, cold gaze, expensive watch or cane.

### Color

Use one main color, one support color, and one accent:

- business elite: charcoal, white, deep red or gold.
- tech founder: slate gray, white, electric blue.
- finance trader: black, warm gold, chart green/red.
- idol/celebrity: pearl white, rose pink, champagne gold.
- student: navy, cream, bright yellow or red badge.
- street fashion: black, denim blue, signal orange or lime.
- luxury rival: deep wine, black, cold silver.

Avoid palettes dominated by only one hue. Gold and glow effects should frame the character or important prop, not cover every surface.

## Rendering Levels

### Sprite-Level

Use simplified shading, large shapes, clean edges, and limited accessories. Design clothing in separable layers: hair, head accessory, torso, jacket, hands, held prop, back ornament.

### Concept-Level

Use more clothing detail, clear material notes, front/side/back or three-quarter view, and call out animation-critical parts such as hair, jacket hem, tie, bag strap, screen glow, and loose accessories.

### Splash/Card-Level

Use dynamic pose, stronger studio lighting or city atmosphere, richer glow, and more background context. Still preserve Q-version proportions if the game style requires it.

## Prompt Formula

For Chinese prompt packs, use:

`主题 + 头身比例 + 角色定位 + 都市身份/阵营 + 服装/道具 + 姿态表情 + 渲染风格 + 色彩 + 手游资产要求 + 视角/背景 + 质量词`

Example:

`Q版三头身都市金融男主，商业精英角色，圆润脸型，大眼睛，黑色西装与白衬衫，深红领带，手持显示股票K线图的手机，另一只手提黑色公文包，自信严肃表情，柔和高级3D手办质感，金色环形光效背景，炭黑与暖金配色，手游角色立绘，正面三分之二视角，干净背景，高辨识度，精致但不过度复杂`

For English image models, use:

`chibi 3-head proportion urban mobile game character, premium modern city style, [role], [outfit], [signature prop], cute rounded face, expressive eyes, clear silhouette, polished 2.5D or soft 3D toy rendering, low-to-medium saturation palette with [accent color], three-quarter front view, clean background, mobile game concept art, readable at small size`

## Negative Prompt Defaults

Use these unless the task needs a different boundary:

`realistic adult anatomy, long realistic body, horror gore, dirty gritty realism, western medieval armor, heavy cyberpunk armor, overly complex fashion details, unreadable tiny logos, messy background, photorealistic skin, harsh plastic render, dark muddy colors, extra fingers, malformed hands, text, watermark, logo`

## Outsourcing Brief Checklist

For outsource-ready requests, include:

- asset name and use case,
- canvas ratio or approximate resolution if known,
- head-body proportion,
- view count,
- required expressions or poses,
- animation-sensitive parts,
- color palette,
- role or faction identifiers,
- forbidden elements,
- export needs such as transparent background, layered PSD, or icon-safe crop.

If the user does not know the game structure, propose a starter scope:

- 4 playable archetypes,
- 4 urban factions or role groups,
- 16 NPCs,
- 8 rivals or premium characters,
- 8 mascots/pets,
- 8 vehicles,
- 60 item/fashion/business icons,
- 24 skill icons,
- 8 major city scenes,
- 1 UI visual direction sheet.
