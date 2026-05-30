# Bug Guardrails

Apply this checklist before and after UrhoX UI edits.

## Highest Priority Rules

- Call `UI.SetRoot()` once in `Start()` for normal UI creation.
- Never call `UI.SetRoot()` or create new widgets inside `HandleUpdate`.
- Never rebuild the whole root after a button click.
- Switch pages with `visible`, not destroy/recreate.
- Use `flexBasis = 0` with `flexGrow = 1` on ScrollViews and flexible central regions.
- Cache widget references that need updates, but treat every reference inside a destroyed subtree as invalid.
- Do not redeclare callback-captured locals with `local` later. Assign to the existing variable instead.
- Use `overflow = "visible"` for icon-over-border containers and parent tab bars.
- Bind the same click handler to every visual part of a single interactive control.

## Common Failures

### Click Causes Scroll To Top

Cause: click handler rebuilds root or ScrollView.

Fix: cache the label/button/page reference and update only changed properties.

### Slider Value Does Not Display

Cause: `onChange` stores the value but does not update visible text.

Fix: update the paired label inside `onChange`.

### ScrollView Does Not Scroll

Cause: ScrollView expands to full content height.

Fix: add `flexGrow = 1, flexBasis = 0`.

### Multi-Page UI Loses State

Cause: inactive pages are destroyed.

Fix: build page panels once and toggle `visible`.

### VirtualList Jumps To Top

Cause: using `SetData()` when only one item changed.

Fix: mutate the data item in place and call `Refresh()` when possible.

### Destroyed Reference Crash

Cause: Lua variable still points to a widget whose underlying node was destroyed.

Fix: do not access cached refs after destroying their subtree. If unavoidable, check `ref.node`.

### ClearChildren Leak Or Layout Issue

Cause: `ClearChildren()` removes children without destroying them.

Fix:

```lua
local oldChildren = panel:GetChildren()
panel:ClearChildren()
for _, child in ipairs(oldChildren) do
    child:Destroy()
end
```

Then add new children.

### Icon Overflow Is Clipped

Cause: the cell, tab bar, or parent container clips overflow.

Fix: set `overflow = "visible"` on the icon cell and relevant parent containers. For ScrollViews, add enough content padding.

### Selected Tab Tint Has No Effect

Cause: cached ref points to wrapper panel, not the actual icon panel.

Fix: component factories should return refs such as `{ root, icon, border, label }`; update `refs.icon`.

### Two Visual Controls Navigate Differently

Cause: border and icon use separate closures or stale captured variables.

Fix: create one `handler` per tab and assign it to both border and icon.

## Final Self-Check

Before finishing, verify:

- There is no `UI.SetRoot(CreateUI())` pattern in callbacks.
- `HandleUpdate` only updates existing refs/timers.
- Every ScrollView or central flexible panel has `flexBasis = 0`.
- All pages are prebuilt and switched by `visible`.
- Modal/Toast layers are built once and appended last.
- Icon-over-border components use sibling layers, absolute icon positioning, and visible overflow.
- Callback functions are defined before loop closures use them.
- Image paths have color fallbacks.
