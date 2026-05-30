# AI Asset Prompts / AI 美术资源 Prompt

当用户要求 AI 出图、占位图、图标、边框、按钮、背景图或 Prompt 包时读取本文件。一键生成 UI 时，也可以用这里的模板生成少量轻量占位资源。

使用原则：

- 中文负责表达题材和策划意图，例如“暗黑魔幻”“仙侠国风”“横屏战斗背景”。
- 英文 Prompt 负责稳定美术术语，例如 `cel shading`, `transparent background`, `ornate border`, `clean linework`。
- 按最小资源预算生成：优先 1 张背景、5 个 Tab 图标、1 个边框、1 个主按钮。
- 不要把文字烘焙进按钮或图标；按钮文字由 UI 代码渲染。

## 通用质量词 / General Quality Anchors

适合二游、商业手游、图标和 UI 资源：

```text
commercial mobile game UI asset, high quality game art, clean readable design, polished anime game style, crisp edges, clean linework, high contrast, professional UI illustration
```

图标常用：

```text
square format, 1:1 ratio, isolated subject, transparent background, cel shading, hard edge shadows, 2-3 shadow layers, 2px outline, readable at small size, 512x512
```

边框/按钮常用：

```text
transparent background, empty center area, no text, no logo, polished game UI asset, clean bevel, subtle highlight, readable silhouette
```

反向 Prompt / Negative prompt：

```text
photorealistic, 3D render, watercolor, sketch, emoji, text, watermark, blurry, low quality, western cartoon, oil painting, full body, cluttered background, unreadable details, messy composition
```

## 风格词库 / Style Keywords

将中文风格映射到英文 Prompt 片段。

### 二游蓝紫科技风 / Anime Blue-Violet Tech

用途：默认风格，适合主界面、抽卡、角色养成。

```text
anime blue-violet tech style, cool blue and violet palette, white highlights, glass panels, futuristic academy feeling, clean sci-fi ornaments, soft glow, elegant mobile gacha UI
```

### 暗黑魔幻风 / Dark Fantasy

用途：ARPG、地牢、恶魔、哥特、吸血鬼题材。

```text
dark fantasy mobile game UI style, black and crimson palette, dark gold trim, stone texture, black metal, glowing runes, ember light, gothic ornaments, heavy ornate frames
```

### 仙侠国风 / Xianxia Chinese Fantasy

用途：修仙、神话、国风 RPG。

```text
xianxia Chinese fantasy mobile game UI style, jade green and cyan palette, warm gold accents, ink wash mountains, cloud patterns, scroll texture, talisman ornaments, elegant jade borders
```

### 西幻 RPG 风 / Western Fantasy RPG

用途：冒险、公会、装备、任务。

```text
western fantasy RPG UI style, parchment texture, leather panels, carved wood, iron trim, gemstones, heraldic ornaments, readable quest board composition
```

### 科幻机甲风 / Sci-Fi Mecha

用途：机甲、太空、战术、射击。

```text
sci-fi mecha game UI style, dark metal panels, cyan and orange neon accents, HUD grid lines, energy bars, angular shapes, tactical interface, holographic glow
```

### 休闲卡通风 / Casual Cartoon

用途：经营、消除、农场、合成。

```text
casual cartoon mobile game UI style, bright friendly colors, rounded shapes, soft shadows, chunky readable icons, cheerful polished interface
```

### 赛博霓虹风 / Cyber Neon

用途：赛博朋克、黑客、未来都市。

```text
cyber neon UI style, black and purple base, magenta and cyan glow, neon outlines, glitch accents, futuristic city interface, high contrast
```

### 末日废土风 / Post-Apocalyptic Wasteland

用途：生存、丧尸、废土。

```text
post-apocalyptic wasteland UI style, rusty metal, worn panels, military green, hazard yellow accents, cracked surfaces, dusty atmosphere, survival game interface
```

## 背景图 / Background Prompts

### 竖屏主界面背景 / Portrait Home Background

把 `[style keywords]` 替换成上面的风格词库片段。

```text
vertical mobile game home screen background, [style keywords], clean readable composition, open center area for UI panels, clear top and bottom space for game UI, high quality game background art, 1080x1920, no text, no logo
```

二游示例：

```text
vertical mobile game home screen background, anime landscape, serene futuristic academy courtyard overlooking a blue city skyline, cool blue and violet palette, soft morning light, clean readable composition, open center area for UI panels, clear top and bottom space for game UI, high quality game background art, 1080x1920, no text, no logo
```

仙侠示例：

```text
vertical mobile xianxia RPG home screen background, floating jade mountain pavilion above clouds, ink wash distant mountains, cyan and jade green palette, warm gold sunlight, elegant fantasy atmosphere, open center area for UI panels, 1080x1920, no text, no logo
```

暗黑示例：

```text
vertical mobile dark fantasy home screen background, gothic castle gate, black stone, crimson moonlight, ember particles, dark gold accents, open center area for UI panels, dramatic but readable composition, 1080x1920, no text, no logo
```

### 横屏主界面/大厅背景 / Landscape Home Background

适合横版手游或横屏大厅。

```text
landscape mobile game lobby background, [style keywords], wide cinematic composition, clear center area for UI, safe empty space on left and right side panels, high quality game background art, 1920x1080, no text, no logo
```

### 横屏战斗占位背景 / Landscape Battle Placeholder

适合一键生成时的战斗/关卡占位界面。

```text
landscape mobile game battle scene background, [style keywords], wide side-scrolling composition, clear playable center lane, readable foreground and background separation, space for left joystick and right skill buttons, high quality game background art, 1920x1080, no text, no logo
```

## 图标 / Icon Prompt Template

通用模板：

```text
game UI icon, square format, 1:1 ratio, [subject], [style keywords], cel shading, hard edge shadows, 2-3 shadow layers, clean linework, 2px outline, isolated subject, transparent background, professional mobile game icon, high quality illustration, readable at small size, 512x512
```

默认 5 个 Tab 图标主题：

- 主页 / Home: `glowing home base emblem, small academy building silhouette, star particles`
- 编队 / Team: `stylized anime character bust silhouette with halo and team formation marks`
- 战斗 / Battle: `glowing tactical map, crossed energy blades, route lines and crystal marker`
- 背包 / Bag: `fantasy backpack with glowing rune stitched on it`
- 商店 / Shop: `ornate coin pouch with ribbon, magic seal, small gem accents`

额外常见图标：

- 抽卡 / Gacha: `glowing lottery ticket or summoning scroll with star particles`
- 任务 / Quest: `quest scroll with check mark and glowing seal`
- 设置 / Settings: `polished gear icon with small light core`
- 奖励 / Reward: `treasure chest or gift box with glowing gems`

## 边框 / Icon Frame Prompt Template

图标和边框必须分开生成。边框中心需要透明，不能含图标内容。

```text
game UI icon frame, square ornate border only, no icon content inside, transparent inner area, thick decorative border, [style keywords], transparent background, polished mobile game UI asset, 512x512
```

品质变体 / Rarity variants：

- 普通 / Normal: `simple metallic frame, thin line decoration, small corner gems`
- 稀有 / Rare: `ornate frame, glowing edge, rune symbols or elegant corner ornaments`
- 史诗 / Epic: `dark premium frame, gold trim, crystalline corner ornaments, glowing inscriptions`
- 传说 / Legendary: `ultra premium frame, intricate filigree, star medallions, radiant outer glow`

## 按钮 / Button Prompt Template

主按钮，不带文字：

```text
mobile game UI button asset, rounded rectangle, [style keywords], clean bevel, subtle highlight, empty center for text overlay, transparent background, high quality UI asset, 512x192, no text, no logo
```

确认/危险按钮，不带文字：

```text
mobile game UI confirm button asset, rounded rectangle, warm red-orange or crimson accent, clean bevel, subtle highlight, empty center for text overlay, transparent background, high quality UI asset, 512x192, no text, no logo
```

横屏技能按钮：

```text
mobile game circular skill button asset, [style keywords], round icon button frame, glowing rim, transparent center or subtle dark center, transparent background, high readability, 256x256, no text, no logo
```

横屏虚拟摇杆：

```text
mobile game virtual joystick UI asset, circular base ring and inner thumb pad, [style keywords], semi-transparent dark glass, subtle glow, transparent background, clean readable shape, 512x512, no text, no logo
```

## 资源接入规则 / Asset Integration Rules

- 保存到可预测路径，例如 `assets/UI/icons`, `assets/UI/frames`, `assets/UI/backgrounds`, 或项目已有资源目录。
- 图标和边框分开存储，不要合成一张。
- 代码中使用 `backgroundImage` + `backgroundColor` fallback。
- 背景使用 `backgroundSize = "cover"`，图标使用 `backgroundFit = "contain"` 或项目等价属性。
- 不要把中文按钮文字直接画进图片；用 UI Label/Button 渲染文字。
- 横屏资源命名建议带 `landscape`，竖屏资源命名建议带 `portrait`，例如 `home_bg_portrait.png`、`battle_bg_landscape.png`。
