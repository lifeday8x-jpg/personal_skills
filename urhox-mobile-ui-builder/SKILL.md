---
name: urhox-mobile-ui-builder
description: Generate or refine UrhoX mobile game UI in Lua for portrait or landscape layouts. Use for 一键生成UI, 主界面, 游戏界面, 战斗界面, 战斗HUD, 结算界面, 开始界面, 商业手游UI, 二游UI, 竖屏游戏UI, 横屏游戏UI, 横版手游UI, UrhoX UI containers, tab bars, multi-page switching, buttons, popups, Toasts, ScrollViews, icon-with-border components, AI占位图, AI图标, or fixing/refining existing UrhoX UI while preserving state and avoiding common urhox-libs/UI bugs.
---

# UrhoX Mobile UI Builder

使用这个 skill 为 `urhox-libs/UI` 创建或修改手游 UI，支持竖屏 portrait 和横屏 landscape。优先做出**可运行、可切页、状态稳定**的 UI，再做视觉精修。

## 模式选择 / Mode Selection

根据用户请求选择模式：

- **一键生成 / One-click generation**：用户只说“做一套 UI”“生成主界面”“做个完整游戏界面”“二游首页”之类宽泛需求时使用。生成一套完整可运行的 UI 骨架和默认内容。
- **单点精修 / Focused refinement**：用户提到已有 UI 或具体目标时使用，例如“底栏改成 5 个按钮”“换背景”“修弹窗”“这个页面挤了”。只改相关模块，保留现有结构。
- **资源规划/生成 / Asset planning/generation**：用户要求真实图片、AI 出图、图标、按钮、边框、背景图、Prompt 时使用。一键生成可以默认生成少量 AI 占位图，但不要默认扩展成完整美术包。

如果用户说得很模糊，默认走“一键生成”，使用合理默认值，并简短说明采用了哪些默认范围。

## 风格预设 / Style Presets

如果用户给出题材或风格词，把它翻译成可执行的 UI 方向。用户没说风格时，默认使用**二游蓝紫科技风 / anime blue-violet tech**。

- **二游蓝紫科技风 / Anime blue-violet tech**：冷蓝、紫、白、玻璃面板、学院/未来感装饰、干净图标，适合抽卡、角色收集、养成游戏。
- **暗黑魔幻风 / Dark fantasy**：黑、猩红、暗金、石纹、金属、符文、火焰光、厚重边框，适合 ARPG、地牢、恶魔、吸血鬼、哥特题材。
- **仙侠国风 / Xianxia Chinese fantasy**：青绿、青蓝、金色、云纹、水墨、卷轴、山河、符箓、优雅边框，适合修仙、神话 RPG。
- **西幻 RPG 风 / Western fantasy RPG**：羊皮纸、皮革、木纹、铁边、宝石、徽章、任务面板，适合冒险、公会、装备、任务驱动游戏。
- **科幻机甲风 / Sci-fi mecha**：深色面板、青/橙霓虹、金属、HUD 网格、能量条、锐角按钮，适合机甲、太空、战术、射击题材。
- **休闲卡通风 / Casual cartoon**：高饱和、圆润按钮、软阴影、大图标，适合合成、农场、经营、消除、轻松题材。
- **像素复古风 / Pixel retro**：像素边框、有限色板、8-bit/16-bit 图标、粗颗粒字体，适合复古 RPG、街机。
- **赛博霓虹风 / Cyber neon**：黑紫底、粉/青发光、故障风、霓虹描边，适合赛博朋克、黑客、未来都市。
- **日式和风 / Japanese wa-style**：朱红、米白、墨黑、纸纹、灯笼、樱花、御守、木牌，适合神社、妖怪、武士、祭典题材。
- **末日废土风 / Post-apocalyptic wasteland**：锈铁、磨损金属、军绿、黄黑警示、裂纹面板、尘土，适合生存、丧尸、废土题材。
- **现代极简风 / Modern minimal**：白/炭黑底、克制配色、简单几何、强间距，适合策略、模拟、偏工具型游戏。

风格预设不能压过可用性：文字必须可读，主要按钮必须明显，导航必须可预测。

## 范围理解 / UI Scope Defaults

把常见策划口径翻译成实现范围：

- **主界面 / home / lobby / 大厅**：生成非战斗状态的大厅首页，包含资源栏、活动/Banner、功能入口、CTA 操作区、底部导航。
- **游戏界面 / game screen**：根据上下文判断。若用户提到战斗、关卡、HP、分数、暂停、敌人、计时器、摇杆、技能，则生成战斗 HUD。若说得模糊，则默认生成一个能从大厅进入的游戏/关卡占位界面。
- **完整 UI / complete UI**：默认生成基础闭环：开始界面、主界面/大厅、关卡或战斗占位界面、结算界面、设置弹窗、Toast、确认弹窗、奖励弹窗。

商城、抽卡、角色养成、背包、邮件、活动、好友、公会、排行榜、完整战斗 HUD 细节都视为可选模块，除非用户明确要求。

## 默认一键生成 / Default One-Click UI

先判断屏幕方向：

- **竖屏 / portrait**：用户没说方向、提到二游/抽卡/养成/主界面/大厅/背包/商城时默认使用。设计基准：1080 x 1920。
- **横屏 / landscape**：用户提到横屏、横版、横向、动作、射击、MOBA、横版闯关、战斗 HUD、虚拟摇杆、技能按钮时使用。设计基准：1920 x 1080。

用户没有指定页面时，生成这套默认 UI：

- 默认页面：`home`, `team`, `battle`, `bag`, `shop`。
- 竖屏根布局：顶部资源栏、内容页栈、CTA 操作区、底部 TabBar。
- 横屏根布局：顶部资源/状态栏、左侧任务/队伍信息区、中间游戏/大厅内容区、右侧快捷操作区、底部或侧边导航；战斗向横屏可加入左下摇杆占位、右下技能按钮占位。
- 首页内容：背景图或颜色 fallback、活动 Banner、快捷功能格子、状态/进度区域；横屏时改为更宽的横向 Banner 和左右信息栏。
- 导航：按钮用 `visible` 切换页面，不重建 root。竖屏优先底部 TabBar，横屏可使用底部 TabBar、顶部 TabBar 或侧边导航，按项目风格选择。
- 反馈：范围允许时包含至少一个确认弹窗和一个顶部 Toast。
- 资源：如果图像生成可用，一键生成允许少量 AI 占位图；代码必须保留 `backgroundColor` fallback 和可预测资源路径。

## 默认占位数据 / Default Placeholder Data

一键生成的 UI 不要是空壳。除非用户要求空模板，默认加入少量 mock data：

- 资源数值：金币、钻石、体力/能量。
- 玩家信息：占位昵称、等级、经验或进度。
- 任务：3 条简体中文任务。
- 奖励：3 个奖励项，带图标占位和数量。
- 角色卡片：3 到 5 个占位角色卡，带稀有度/等级标签。
- 关卡按钮：至少 1 个明确可点击的关卡或“开始战斗”按钮。

把 mock data 放在一个 local table 中，方便后续替换成真实游戏数据。

## 数值边界 / Numeric Boundaries

一键 UI 生成可以创建 mock 展示数值，让界面完整可读，但这些数值不能被当成最终玩法平衡。

允许作为 UI 占位：

- 资源展示值，例如金币、钻石、体力、仙玉、灵石。
- 玩家等级、经验条、战力、进度条。
- 奖励数量、道具数量、商品价格。
- 关卡推荐战力、简单难度标签。

除非用户明确要求，不要生成或定死：

- 最终经济平衡。
- 战斗公式、伤害公式、怪物血量和伤害。
- 掉落概率、抽卡概率。
- 升级经验曲线、养成消耗曲线。
- 离线收益公式。
- 商业化定价逻辑。

所有 mock 数值必须集中放在可替换的 local table，并用命名或注释标明是 mock/demo data，方便未来由策划或数值 skill 接管。

## 资源预算 / Asset Budget Defaults

一键生成时默认允许轻量 AI 占位资源，但只生成让 UI 立刻有完整感的最小集合：

- 1 张背景图，用于开始界面或主界面：竖屏用 1080 x 1920，横屏用 1920 x 1080。
- 5 个底部 Tab 图标，用于默认页面。
- 1 个通用普通品质图标边框。
- 1 个主按钮图片。
- 可选：如果有奖励弹窗，再生成 1 个奖励/道具图标。

不要默认生成大型完整资源包。多套背景、每页插画、多品质边框、大量道具图标、角色立绘、动画帧、按钮多状态图等，只有用户明确要求“完整美术包/完整资源包”时再做。

即使生成了图片，代码也必须能在图片缺失时运行：提供 `backgroundColor` fallback 和清晰的占位路径。

## 画风 Skill 协作 / Art Skill Collaboration

可以搭配其他专精画风 skill 使用，例如暗黑魔幻、仙侠国风、像素复古、角色头像、道具图标等。协作时，本 skill 负责 UI 工程契约，画风 skill 负责美术表现。

协作顺序：

1. 本 skill 先生成 Asset Spec，明确资源类型、尺寸、透明背景、主体占比、输出路径和 UI 接入方式。
2. 专精画风 skill 按 Asset Spec 生成图片或 Prompt，不得擅自改变画布尺寸、文件格式、透明要求、输出路径和是否允许文字。
3. 本 skill 接收资源后，按 UI 规范接入，并检查路径、`.png` 扩展名、fallback、容器尺寸、主体对齐和点击区域。

Asset Spec 至少包含：

- `asset_id`：资源唯一名，例如 `tab_shop`。
- `asset_type`：`background`, `tab_icon`, `item_icon`, `icon_frame`, `button`, `skill_button`, `joystick`。
- `target_style`：目标风格，例如 `xianxia`, `dark_fantasy`, `anime_blue_violet`。
- `canvas`：固定画布尺寸，例如 `[512, 512]`、`[1080, 1920]`、`[1920, 1080]`。
- `transparent_background`：图标、边框、按钮通常为 `true`；背景为 `false`。
- `subject`：中文或中英混合主体描述。
- `subject_ratio`：主体占画布比例，例如 Tab 图标 `0.70-0.82`。
- `anchor`：默认 `center`，特殊 HUD 资源可指定 `bottom_left`、`bottom_right`。
- `safe_padding`：建议透明安全边，例如 `12%`。
- `text_allowed`：按钮、图标默认 `false`，不要把文字画进图里。
- `output_path`：最终接入路径，优先 `.png`。

如果没有专精画风 skill，不要阻塞 UI 生成。回退到 `references/ai-asset-prompts.md`，使用最接近的内置风格预设先生成可用占位资源。

自动抠图/裁剪后必须归一化：只用裁剪检测主体 bbox，最终资源要重新放回固定 PNG 画布，保持统一主体占比、透明安全边和居中锚点。UI 容器只加载归一化后的标准画布资源，不直接使用裁剪后的裸图尺寸。

## 文案语言 / Text Language

默认所有玩家可见 UI 文案使用简体中文：标题、按钮、任务名、奖励名、弹窗文本、Toast 文案、玩家可见说明等。

技术变量名、资源路径、组件名可以继续使用英文，例如 `home`, `battle`, `shop`, `UI.SetRoot`, `ScrollView`, `Modal.Toast`。

只有用户明确要求其他语言，或现有项目已经统一使用其他语言时，才保持其他语言。

## UI 美化边界 / UI Polish Boundaries

一键生成应包含基础美化，让 UI 不像灰盒，但不要默认加入复杂动画系统或重特效。

一键生成默认允许：

- 清晰的间距、层级、字号和颜色层次。
- 半透明面板、边框、轻微阴影或描边。
- 按钮 `normal` / `pressed` / `disabled` 基础状态。
- Tab 选中态高亮。
- 弹窗遮罩和基础显示/隐藏反馈。
- Toast 显示/隐藏反馈。
- 统一的色板、字体大小和文本层级。

不要默认加入：

- 大量粒子。
- 复杂时间轴动画。
- 全屏转场。
- shader/glow 重特效。
- Live2D、Spine、角色看板动画。
- 动态背景。
- 复杂奖励飞行动画或大量循环特效。

当用户要求“美化”“加动态效果”“更精致”“按钮反馈更好”时，进入 polish 阶段：优先只改视觉层，不改变页面逻辑；保留原有布局和交互；高级动效需要考虑性能和项目已有动画系统。

## 屏幕适配护栏 / Screen Adaptation Guardrails

把 1080 x 1920 竖屏和 1920 x 1080 横屏当作设计参考，不要当成死板固定画布。UI 要能适应常见手机比例和安全区。

- 顶部栏和重要按钮要避开刘海/状态栏区域，保留合理 padding。
- 底部导航要避开手势条/home indicator 区域，保留底部 padding。
- 横屏 UI 左右两侧也要留安全 padding，避免被圆角、挖孔、系统手势区遮挡。
- 横屏战斗 HUD 中，左下摇杆、右下技能按钮、暂停/设置按钮都应放在安全区内。
- 中央内容区使用 `flexGrow = 1` 和 `flexBasis = 0`。
- 优先使用百分比宽度、flex 布局、padding、ScrollView，不要把所有纵向位置写死。
- 重要文本不能挤出按钮或面板。
- 内容可能超过高度时使用 `ScrollView`。
- 除非项目已有这种风格，不要把关键控件贴在屏幕极限角落。

这些是防裁剪、防重叠的护栏，不是要求所有游戏长成同一种布局。

## 验收清单 / Acceptance Checklist

一键生成后，检查基础流程是否打通：

- 开始界面可以进入主界面/大厅。
- 底部导航可以切换页面。
- 关卡/开始战斗按钮可以进入游戏界面或战斗占位界面。
- 游戏界面可以暂停、返回，或进入结算。
- 结算界面可以回到主界面/大厅。
- 确认弹窗、奖励弹窗可以打开和关闭。
- Toast 可以显示，并通过 update timer 自动隐藏。

如果本地环境无法运行 UrhoX UI，就手动检查代码路径，并在回复中说明没有做运行时验证。

## 已有布局修缮 / Existing UI Repair

当用户是在已有 UI 上要求“修一下”“优化”“改一处”“不对齐”“被裁剪”“点了没反应”“页面切换不对”“资源不显示”时，进入修缮模式。

修缮原则：

- 先阅读现有 Lua UI 文件、资源路径、组件命名、页面结构和回调写法。
- 不要因为局部问题重写整套 UI，除非用户明确说“重做/重构/全部替换”。
- 优先判断问题类型：布局问题、状态问题、交互问题、资源路径问题、视觉层级问题、性能/重建问题。
- 做最小 patch，保留已有页面结构、变量命名、资源目录和用户自定义风格。
- 保留旧行为，除非旧行为正是 bug 或与用户目标冲突。
- 如果发现同类问题重复出现，可以抽一个小 helper；不要为了单次修缮引入大抽象。
- 修改后只运行与改动相关的检查：例如 Tab 切页、弹窗开关、ScrollView 滚动、图标溢出、资源加载路径。

常见诊断方向：

- 被裁剪：检查父容器 `overflow`、ScrollView padding、横竖屏安全区。
- 点了没反应：检查 `pointerEvents`、`onClick/onPress`、图标和边框是否绑定同一个 handler。
- 切页丢状态：检查是否销毁重建页面，改为 `visible` 显隐。
- 滚动异常：检查 `ScrollView` 是否有 `flexGrow = 1, flexBasis = 0`。
- 资源不显示：检查资源路径、扩展名是否与实际文件一致；AI 生成占位图默认按 `.png` 接入。
- 选中态无效：检查缓存的是实际 icon/label 子控件，不是外层 wrapper。

## 工作流 / Workflow

1. 先检查现有项目：找到 Lua UI 入口、资源目录、已有组件和命名习惯。
2. 判断这是“一键生成”“单点精修”还是“资源规划/生成”。
3. 应用用户指定风格；用户没说时默认二游蓝紫科技风。
4. 需要 UrhoX 布局/组件模式时，读取 `references/urhox-ui-patterns.md`。
5. 修改前后都参考 `references/bug-guardrails.md` 做防坑检查。
6. 如果需要真实图标、边框、按钮、背景图，或一键生成需要 AI 占位资源，先按 `画风 Skill 协作 / Art Skill Collaboration` 生成 Asset Spec；没有专精画风 skill 时读取 `references/ai-asset-prompts.md` 兜底。
7. 执行最小但完整的实现：
   - 一键生成：创建完整可运行 UI 文件，或接入现有入口。
   - 单点精修/已有布局修缮：按 `已有布局修缮 / Existing UI Repair` 判断问题类型，只改目标组件/页面。
   - 一键生成只使用 mock 数值和基础美化；真实数值平衡与高级动效只有用户明确要求时才做。
8. 校验核心 guardrails：不要重复 `UI.SetRoot`，不要在 `Update` 重建 UI，页面切换用 `visible`，ScrollView 使用 `flexBasis = 0`，缓存 refs 有效，溢出图标容器使用 `overflow = "visible"`。
9. 一键生成后跑验收清单；不能运行时至少做代码路径检查。

## 实现规则 / Implementation Rules

- 正常 UI 创建只在启动时调用一次 `UI.SetRoot(root)`。
- 后续更新使用属性变化：`text`, `visible`, `backgroundColor`, `imageTint`, `value`，不要重建 widget。
- 回调或 update 需要访问的 widget 引用使用模块级 local 缓存。
- 页面切换不要销毁重建。一次性创建页面，用 `visible` 显隐。
- ScrollView 或中央弹性区域使用 `flexGrow = 1, flexBasis = 0`。
- 图标溢出边框组件及其父容器使用 `overflow = "visible"`。
- 图标和边框如果视觉上是同一个按钮，必须绑定同一个 handler。
- 需要改亮度/选中态时，缓存真实 icon 子控件，不要缓存外层 wrapper。
- 视觉资源保持可替换：`backgroundImage` 搭配 `backgroundColor` fallback。

## 输出要求 / Output Expectations

一键生成时交付：

- 可运行的 UrhoX Lua UI 实现。
- 清晰的页面、Tab、mock data 表。
- 导航函数、页面 visible 缓存、选中态更新。
- 可替换的图片路径和颜色 fallback。
- 简短说明生成了什么，以及哪些模块可继续精修。

单点精修时交付：

- 范围明确的 patch。
- 简短说明改了哪个组件，以及状态/交互如何保持。
- 可用的校验或测试结果。

## 参考资料 / Reference Map

- `references/urhox-ui-patterns.md`：布局、TabBar、图标溢出边框、多页面、Modal/Toast 模式。
- `references/bug-guardrails.md`：UrhoX/Yoga 高频坑和最终自查。
- `references/ai-asset-prompts.md`：背景、按钮、图标、边框的 AI Prompt 模板。
