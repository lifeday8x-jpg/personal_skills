---
name: q-version-urban-mobile-art
description: Create art direction, production briefs, asset lists, character proportions, style rules, and AI image prompts for a chibi Q-version urban modern mobile game. Use when Codex needs to design or specify mobile game business elites, office workers, students, streamers, idols, entrepreneurs, urban NPCs, city scenes, props, UI icons, avatar frames, splash art, turnarounds, sprites, or outsourcing briefs in a cute premium contemporary style with clean silhouettes and mobile readability.
---

# Q-Version Urban Mobile Art

## Core Approach

Treat the request as mobile game art direction, not only as an image prompt task. Convert vague urban style ideas into usable production structure: asset type, role in game, silhouette, head-body proportion, view angle, rendering level, animation needs, UI readability, and delivery notes.

Default to a cute but premium 3-head chibi proportion unless the user asks otherwise. Use 2-head for mascot-like brand figures and emoji stickers, 2.5-head for casual NPCs and shop staff, 3-head for playable characters and standard NPCs, and 3.5-head for premium heroes, bosses, card art, and promotional illustrations.

Prefer Chinese-language outputs when the user writes in Chinese. Include English AI image prompts when useful for image models or when the user requests them.

## Workflow

1. Identify the requested asset category: character, NPC, rival, pet, vehicle, prop, city scene, UI, icon, card art, splash art, or full style guide.
2. Pick the production format:
   - Concept brief for early design.
   - Asset specification for outsourcing or implementation.
   - Prompt pack for AI image generation.
   - Style guide for repeated production.
3. Define the mobile constraints: small-screen silhouette, clear role identity, limited visual noise, readable prop shape, and animation-friendly layers.
4. Choose a proportion and view:
   - 3-head front/three-quarter view for playable urban characters.
   - 2 to 2.5-head for mascots, shop NPCs, comic side characters, and item figures.
   - 3.5-head for CEOs, idols, rivals, rare cards, title art, and story illustrations.
5. Produce structured output with concise headings and concrete deliverables.

## Output Templates

### Character or NPC

Use this structure:

- 角色定位
- 头身比例
- 都市身份/阵营气质
- 轮廓关键词
- 发型与五官
- 服装结构
- 标志道具
- 色彩方案
- 姿态与表情
- 手游落地注意
- AI绘图提示词
- 负面提示词

### Rival, Boss, Celebrity, or Premium Card

Use this structure:

- 类型与剧情/玩法定位
- 头身比例
- 第一眼识别点
- 服装与身份符号
- 材质与光效
- 色彩方案
- 动作/表情设定
- 卡面氛围
- 手游落地注意
- AI绘图提示词
- 负面提示词

### Scene or City Area

Use this structure:

- 场景功能
- 城市层级与生活气质
- 构图视角
- 核心建筑/设施
- 光影与氛围
- 可交互物件
- UI遮挡安全区
- 分层建议
- AI绘图提示词
- 负面提示词

### UI, Icon, or Prop

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

- Style: Q版, 都市现代, 商业精英, 潮流生活, cute but polished, premium mobile game art.
- Shape: large head, compact body, expressive eyes, clean face, strong silhouette, readable clothing layers.
- Rendering: soft 3D-toy feel or polished 2.5D illustration, smooth skin, controlled highlights, clean edge lighting.
- Color: low-to-medium saturation base with one clear accent color per role or faction.
- Materials: wool suit fabric, cotton shirt, silk tie, leather bag, polished shoes, glass, metal, phone screen glow, warm studio light.
- Urban motifs: smartphone, stock chart, briefcase, coffee cup, subway card, office badge, luxury mall, skyline, neon sign, sports car, headphones.
- Avoid: realistic adult anatomy, horror gore, dirty gritty realism, overly dense fashion details, unreadable tiny logos, medieval fantasy armor, heavy cyberpunk unless requested, watermark or text baked into the image.

## Urban Role Palette

Use role-based color coding when the user has no existing palette:

- business elite: charcoal, white shirt, deep red or gold accent.
- tech founder: slate gray, clean white, electric blue accent.
- finance trader: black, warm gold, green/red chart accent.
- idol/celebrity: pearl white, rose pink, champagne gold.
- student: navy, cream, bright badge accent.
- street fashion: black, denim blue, signal orange or lime.
- luxury villain/rival: deep wine, black, cold silver.

## Reference Loading

Load `references/mobile-art-spec.md` when the user needs:

- a fuller style guide,
- decisions about head-body proportions,
- complete mobile game asset categories,
- outsourcing-ready specifications,
- urban role palettes,
- prompt formulas,
- or help deciding what a modern city mobile game should include.
