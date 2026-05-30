# UrhoX UI Patterns

Use these patterns for `urhox-libs/UI` portrait mobile game UI.

## Standard Portrait Structure

Build the UI once:

```lua
local UI = require("urhox-libs/UI")

local pages = {}
local tabRefs = {}
local activePage = "home"

local function ShowPage(id)
    if pages[activePage] then pages[activePage].visible = false end
    activePage = id
    if pages[activePage] then pages[activePage].visible = true end

    for tabId, refs in pairs(tabRefs) do
        local active = tabId == id
        if refs.icon then
            refs.icon.imageTint = active and {255,255,255,255} or {145,155,180,255}
        end
        if refs.label then
            refs.label.fontColor = active and {255,255,255,255} or {150,165,190,220}
        end
    end
end
```

Recommended root:

- `TopBar`: fixed height, resource counters, profile/settings buttons.
- `ContentStack`: `flexGrow = 1`, `flexBasis = 0`, contains all pages as overlapping absolute panels or same-position panels.
- `CTAZone`: optional quick action strip.
- `TabBar`: fixed bottom height, `overflow = "visible"` if icons protrude upward.
- `ModalLayer`: last child of root, absolute full screen, highest visual layer.

## Page Switching

Create all pages once and toggle `visible`.

```lua
local function BuildPages()
    pages.home = UI.Panel { width = "100%", height = "100%", visible = true, children = {} }
    pages.team = UI.Panel { width = "100%", height = "100%", visible = false, children = {} }
    pages.battle = UI.Panel { width = "100%", height = "100%", visible = false, children = {} }
    pages.bag = UI.Panel { width = "100%", height = "100%", visible = false, children = {} }
    pages.shop = UI.Panel { width = "100%", height = "100%", visible = false, children = {} }

    return UI.Panel {
        flexGrow = 1,
        flexBasis = 0,
        width = "100%",
        children = { pages.home, pages.team, pages.battle, pages.bag, pages.shop },
    }
end
```

## Icon With Border

Use sibling layers inside a visible-overflow cell. The icon and border must call the same handler.

```lua
local function IconWithBorder(cfg)
    local bW = cfg.borderW or 76
    local bH = cfg.borderH or 76
    local iW = cfg.iconW or math.floor(bW * 1.25)
    local iH = cfg.iconH or math.floor(bH * 1.25)
    local handler = cfg.onPress or function() end

    local borderPanel = UI.Panel {
        width = "100%", height = "100%",
        backgroundImage = cfg.borderImage,
        backgroundColor = cfg.borderColor or {36, 50, 82, 255},
        backgroundFit = "fill",
        pointerEvents = "auto",
        onClick = handler,
    }

    local iconPanel = UI.Panel {
        position = "absolute",
        left = (bW - iW) / 2,
        top = (bH - iH) / 2,
        width = iW, height = iH,
        backgroundImage = cfg.iconImage,
        backgroundColor = cfg.iconColor or {70, 110, 180, 255},
        backgroundFit = "contain",
        pointerEvents = "auto",
        onClick = handler,
        zIndex = 1,
    }

    local cell = UI.Panel {
        width = bW, height = bH,
        overflow = "visible",
        children = { borderPanel, iconPanel },
    }

    if not cfg.label then
        return cell, { root = cell, icon = iconPanel, border = borderPanel }
    end

    local label = UI.Label {
        text = cfg.label,
        fontSize = cfg.labelSize or 22,
        fontColor = cfg.labelColor or {180, 197, 220, 220},
        pointerEvents = "none",
        marginTop = 6,
    }

    local root = UI.Panel {
        flexDirection = "column",
        alignItems = "center",
        overflow = "visible",
        children = { cell, label },
    }

    return root, { root = root, cell = cell, icon = iconPanel, border = borderPanel, label = label }
end
```

## Tab Bar

Define tab metadata in a table. Define `ShowPage` before closures that call it.

```lua
local TABS = {
    { id = "home", label = "Home", icon = "UI/icons/home.png", border = "UI/frames/normal.png" },
    { id = "team", label = "Team", icon = "UI/icons/team.png", border = "UI/frames/normal.png" },
    { id = "battle", label = "Battle", icon = "UI/icons/battle.png", border = "UI/frames/rare.png" },
    { id = "bag", label = "Bag", icon = "UI/icons/bag.png", border = "UI/frames/normal.png" },
    { id = "shop", label = "Shop", icon = "UI/icons/shop.png", border = "UI/frames/normal.png" },
}
```

The tab bar should have `overflow = "visible"`, fixed height, and `justifyContent = "space-around"`.

## Scroll Views

Always constrain scroll views:

```lua
UI.ScrollView {
    flexGrow = 1,
    flexBasis = 0,
    width = "100%",
    children = {}
}
```

If icons inside a ScrollView need visual overflow, add padding to the scroll content. Do not rely only on child overflow because scroll clipping may still hide protruding visuals.

## Modal And Toast

Create modal layers once and append them last in root children.

- Reward/confirm modals: full-screen overlay, centered content, toggle `visible`.
- Toast: transparent full-screen wrapper or top absolute bar, `visible` toggled by timer.
- Update Toast timers in `HandleUpdate`; do not rebuild Toast nodes.

## Background Images

Use image and fallback together. For AI-generated placeholder assets, prefer `.png` paths because image generation tools normally output PNG files.

```lua
UI.Panel {
    width = "100%",
    height = "100%",
    backgroundImage = "Textures/Backgrounds/home_bg.png",
    backgroundSize = "cover",
    backgroundPosition = "center",
    backgroundColor = {8, 12, 22, 255},
}
```

Overlay gradients can improve text readability, but keep them subtle and do not obscure key art.
