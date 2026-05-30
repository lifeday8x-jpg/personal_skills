---
name: q-version-xianxia-mobile-art
description: Create art direction, production briefs, asset lists, character proportions, style rules, and AI image prompts for a chibi Q-version xianxia/wuxia mobile game with ink-wash aesthetics. Use when Codex needs to design or specify mobile game characters, sects, NPCs, monsters, bosses, spirit pets, mounts, weapons, magic treasures, costumes, scenes, UI icons, skill effects, gacha cards, splash art, turnarounds, sprites, or outsourcing briefs in a cute Chinese fantasy cultivation style.
---

# Q-Version Xianxia Mobile Art

## Core Approach

Treat the project as a mobile game art-direction task, not only as an image prompt task. Always convert vague style requests into usable production structure: asset type, role in game, silhouette, head-body proportion, view angle, rendering level, animation needs, UI readability, and delivery notes.

Default to a cute but readable 3-head chibi proportion unless the user asks otherwise. Use 2-head for mascot-like pets and very young comic characters, 2.5-head for casual NPCs, 3-head for playable characters and most monsters, and 3.5-head for elegant heroes, bosses, and premium splash art.

Prefer Chinese-language outputs when the user writes in Chinese. Include English AI image prompts only when useful for image models or when the user requests them.

## Workflow

1. Identify the requested asset category: character, monster, pet, mount, weapon, magic treasure, scene, UI, icon, skill effect, card art, or full style guide.
2. Pick the production format:
   - Concept brief for early design.
   - Asset specification for outsourcing or implementation.
   - Prompt pack for AI image generation.
   - Style guide for repeated production.
3. Define the mobile constraints: small-screen silhouette, clear faction identity, limited visual noise, readable weapon/prop shape, and animation-friendly layers.
4. Choose a proportion and view:
   - 3-head front/three-quarter view for playable characters.
   - 2 to 2.5-head for pets, mascots, minor NPCs, and item-shop figures.
   - 3.5-head for premium heroes, bosses, title art, and card illustrations.
5. Produce structured output with concise headings and concrete deliverables.

## Output Templates

### Character or NPC

Use this structure:

- 角色定位
- 头身比例
- 门派/阵营气质
- 轮廓关键词
- 发型与五官
- 服装结构
- 武器/法宝
- 色彩方案
- 姿态与表情
- 手游落地注意
- AI绘图提示词
- 负面提示词

### Monster, Boss, Spirit Pet, or Mount

Use this structure:

- 类型与战斗定位
- 头身/体型比例
- 轮廓识别点
- 修仙元素
- 材质与纹样
- 色彩方案
- 动作/待机设定
- 技能视觉方向
- 手游落地注意
- AI绘图提示词
- 负面提示词

### Scene or Map Area

Use this structure:

- 场景功能
- 时代与修仙层级
- 构图视角
- 核心建筑/自然元素
- 水墨表现
- 可交互物件
- 氛围色彩
- UI遮挡安全区
- 分层建议
- AI绘图提示词
- 负面提示词

### UI, Icon, or Item

Use this structure:

- 功能定位
- 形状语言
- 主图案
- 颜色与稀有度
- 材质表现
- 小尺寸可读性
- 套装一致性
- AI绘图提示词
- 负面提示词

## Style Rules

Use these defaults unless the user provides a different art direction:

- Style: Q版, 修仙, 武侠, 水墨, 东方幻想, cute but refined.
- Shape: large head, compact body, strong silhouette, soft rounded facial features, readable costume layers.
- Ink: light ink wash edges, xuan paper texture, brush gradients, restrained ornamental lines.
- Color: low-to-medium saturation with one clear accent color per faction or character.
- Materials: silk, cloud brocade, jade, bamboo, bronze, cinnabar talismans, lacquer, mist, spiritual light.
- Xianxia motifs: flying swords, talismans, pills, gourds, jade pendants, clouds, cranes, lotus, mountains, sect seals, spiritual rings.
- Avoid: hyper-realistic anatomy, horror gore, cluttered costume fragments, unreadable tiny ornaments, Western medieval armor unless requested, heavy cyberpunk elements unless requested.

## Reference Loading

Load `references/mobile-art-spec.md` when the user needs:

- a fuller style guide,
- decisions about head-body proportions,
- complete mobile game asset categories,
- outsourcing-ready specifications,
- faction systems,
- prompt formulas,
- or help deciding what a mobile game should include.
