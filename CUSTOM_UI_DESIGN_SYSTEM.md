# Custom UI Design System

**A portable design system for expressive, native-feeling mobile applications.**

Version **1.0.1** · Prepared **4 November 2026** · iOS, Android, and responsive mobile web

A centralized reference for the visual language, components, and interaction behavior shared across your mobile applications.

## Start here

Copy this **one file** into each application's repository as `DESIGN_SYSTEM.md`. Give it to your designer, developer, or coding agent before implementation. The document contains the visual direction, portable tokens, component behavior, motion recipes, screen patterns, and implementation guidance. It has no required companion assets or remote fonts.

**Visual companion:** the repository's [README gallery](https://github.com/itsakbarov/mobile-design-system#readme-ov-file) shows light and dark components, three mobile screen examples, forms and overlays, and a matched-expansion motion example. Its [rendering source](https://github.com/itsakbarov/mobile-design-system/blob/main/examples/render.py) reads the tokens in this file. The specification remains usable by itself when copied into another project.

For the default app, use **neutral surfaces + native sans typography + restrained violet + one meaningful signature interaction per task area**. Choose light or dark according to the use context and the user's system setting. Keep all behavior available with reduced motion and opaque materials.

**Reading order:** [Design language](#design-language) → [Foundations](#foundations) → [Portable tokens](#portable-tokens) → [Components](#components) → [Signature interactions](#signature-interactions) → [Screen recipes](#screen-recipes) → [Adoption](#adoption) → [Contrast checks](#contrast-checks) → [References](#references).

### Reading the specification

The tokens and requirements below are the system's implementation defaults. Optional signature patterns build on the shared components and include conventional, reduced-motion, and opaque-material alternatives.

The design language centers on **continuity of interaction**: keep the active object recognizable as its state, size, or context changes. Research notes and original source credits are maintained in the separate reference appendix.

## Design language

### Quiet structure, expressive response

| Principle | Apply it | Avoid |
|---|---|---|
| Make the active object feel continuous | Let a selected tab, expanding composer, status badge, or detail surface visibly retain its identity | Replace the whole screen with unrelated entrance animations |
| Let the finger lead | Track drag position directly; settle calmly after release | Add an artificial delay between touch and response |
| Use material to explain depth | Put local translucency on floating controls above media or scrolled content | Blur every card, field, and background |
| Let content supply richness | Use artwork, photography, and one focal interaction within clear native structure | Turn the entire interface into competing effects |
| Keep the task familiar | Preserve labels, back behavior, scrolling, and conventional inputs | Require a novel gesture to reach a basic action |

**Default appearance:** generous spacing, neutral canvases, compact controls with soft corners, clear typographic hierarchy, thin separators, and minimal elevation. Violet indicates a primary action or selected state. Semantic colors indicate outcomes. Background photography may determine a media screen's mood without redefining the application's action colors.

**Signature budget:** one dominant moving object per task area. A media carousel may be expressive while its toolbar and playback controls remain quiet. Do not combine a refracting tab bar, parallax header, glowing slider, streaming title, and morphing toast on the same screen.

**Presentation context:** device bezels, simulator toolbars, desktop windows, recording backgrounds, and promotional captions belong to documentation previews. Product screens use their own layout, navigation, and runtime safe areas.

### App profiles

Use one profile per product or clearly bounded feature. All profiles share tokens and component behavior.

| Profile | Suitable applications | Allowed expression |
|---|---|---|
| **Core** — default | Utilities, productivity, account flows, lists, forms | Neutral surfaces, violet selection, small tactile responses, matched local transitions |
| **Media** | Music, events, galleries, discovery | Artwork-derived backdrops, image-led hero, local glass controls, one carousel or expanding player |
| **Assistant** | AI chat, voice, live processing | Stable composer, restrained streaming trail, compact labeled status that expands when needed |
| **Editorial** — optional | Social discovery, reading, event storytelling | One platform serif display style for a large content title; all controls and body copy keep the native sans |

An app may replace the accent with its brand color after checking every contrast pair. Keep the semantic role names, spacing, type hierarchy, target sizes, and state behavior. Do not recolor success or danger to match the brand.

## Foundations

### Layout and spacing

Use logical units, not screenshot pixels. A value of 24 maps to 24 pt on iOS, 24 dp on Android, or the equivalent CSS length at a 1× web baseline. Font scaling is separate from layout scaling.

| Role | Default | Behavior |
|---|---:|---|
| Phone page inset | 24 | Use 16 when the available width is under 360 logical units |
| Major section gap | 32 | Between distinct decisions or content groups |
| Related group gap | 24 | Between a group heading and a separate block |
| Repeated item gap | 12 | Lists of compact surfaces or related controls |
| Inline gap | 8 | Icon + label, adjacent related metadata |
| Primary control minimum height | 52 | Grow with text and multiline content |
| Minimum interactive target | 48 × 48 | Visual icons may be 20–24; the target remains larger |
| Reading column maximum | 560 | Center long prose within wide panes |
| Expanded content pane maximum | 680 | Use extra width for a second pane where useful |

The spacing scale is **0, 4, 8, 12, 16, 24, 32, 40, 48, 64**. Use the semantic roles above to give repeated layouts a consistent rhythm.

Design on a compact phone first. Validate at **320, 360, 390, and 430** logical units, landscape, tablet, and split screen. These are review widths, not fixed canvas sizes. Above approximately 600 available units, use a bounded reading pane or list/detail structure; do not stretch phone cards to fill the display. Breakpoints respond to available space and content.

Use runtime safe-area and keyboard insets. A bottom action region includes its own content height plus the current bottom inset. Ensure the last list row and focused form field can scroll above sticky controls. Do not hard-code a notch, sensor cutout, home indicator, status bar, or keyboard height.

### Typography

Use the native system family through platform APIs and preserve platform text scaling. The Editorial profile may use the platform serif for one display role; it must not affect navigation, form labels, or data.

| Token | Size / line height | Weight | Purpose |
|---|---|---:|---|
| `type.display` | 35 / 40 | 600 | Short, content-led hero title; usually one per screen |
| `type.title` | 28 / 36 | 600 | Main screen heading |
| `type.heading` | 20 / 28 | 600 | Section heading |
| `type.body` | 17 / 24 | 400 | Reading, input, list content |
| `type.bodyStrong` | 17 / 24 | 600 | Emphasis within ordinary UI |
| `type.label` | 14 / 20 | 500 | Button, short control label, supporting metadata |
| `type.caption` | 12 / 16 | 400 | Secondary nonessential context; never the only label for an action |

Use sentence case. Avoid long all-caps labels. Keep prose near 45–70 characters per line where space allows. Use tabular numerals for changing timers, amounts, and equalizer values. Never make a number's animation obscure its final value.

Support platform text scaling, including approximately 200% text size in acceptance review. Controls, rows, and sheets grow; navigation may reflow. Critical text wraps. Truncate only noncritical repeated context, with the full value available in a detail view. Do not shrink fonts to preserve a mockup.

### Color and contrast

The neutral/violet palette uses semantic roles for surfaces, text, actions, selection, and status. Use the complete light or dark theme. Do not implement dark mode as a simple inversion.

| Semantic role | Light | Dark |
|---|---|---|
| Canvas | `#F6F6F8` | `#000000` |
| Surface | `#FFFFFF` | `#0A0A0A` |
| Raised surface | `#FFFFFF` | `#131313` |
| Primary text | `#1D1D1F` | `#F5F5F5` |
| Secondary text | `#64646A` | `#B4B4B4` |
| Primary action | `#6E56CF` | `#BAA7FF` |
| Text on primary action | `#FFFFFF` | `#21183C` |
| Selected/accent surface | `#EEE9FC` | `#252034` |
| Accent text | `#5940AE` | `#BAA7FF` |
| Essential control border | `#85858F` | `#777780` |

Use a single accent family across an app. Keep inactive surfaces neutral and reserve semantic colors for meaningful status.

Light secondary text uses `#64646A` so it remains readable on inset and accent surfaces as well as the canvas.

Text must achieve **4.5:1** contrast in ordinary roles; qualifying large text may use **3:1**. Essential boundaries and focus indicators need **3:1** against adjacent surfaces. The lighter `divider` token only separates already-understandable content; it is not the sole boundary of an input. Status uses a label or icon as well as color. The token appendix contains complete success, warning, danger, and information pairs. Use an offset or two-tone focus treatment over variable media so the focus ring remains distinguishable.

For text on artwork, first use a sufficiently opaque scrim or solid caption surface. Check actual bright, dark, and busy images. Blur alone does not guarantee contrast. Placeholder text uses `textSecondary`; do not reduce its opacity. Disabled controls remain understandable, with an explanation when the reason is not obvious.

### Shape, depth, icons, and media

- **Radii:** 6 for small labels, 12 for fields, 16 for ordinary surfaces/controls, 28 for sheet corners, 32 for an occasional media hero. Use half-height rounding for intentional pills. Do not put rounded cards inside rounded cards by default.
- **Depth:** create hierarchy with layout and surface tone first. Use a soft shadow for floating elements in light mode; raised fill and separation in dark mode. Two visible elevation levels are usually enough.
- **Icons:** use one family per platform, with consistent apparent weight. Prefer platform symbols on native surfaces, consistent equivalents elsewhere. Icon drawings are generally 20–24; interactive targets remain at least 48. Provide action names and toggle states.
- **Images:** retain aspect ratio and focal subject. Use one consistent crop within a repeated collection. Media can be vivid while controls stay legible and neutral. Reserve space during loading; provide a meaningful failed-image state.
- **Glass:** local floating navigation, media transport, or anchored menus only. Use the platform material when available. Provide a solid raised surface for reduced transparency, insufficient contrast, unsupported hardware, or weak performance. A shader's blur radius is not a portable opacity specification.

### Motion

Gesture feedback begins immediately. During a drag, progress follows the finger rather than running a timed animation. After release, use a damped settle. Preserve a stable reading anchor and let the user interrupt a transition.

| Token | Duration | Use |
|---|---:|---|
| `motion.feedback` | 120 ms | Press tint, small confirmation, reduced-motion crossfade |
| `motion.control` | 180 ms | Selected state, icon/label swap |
| `motion.content` | 240 ms | Small local content replacement |
| `motion.overlay` | 320 ms | Sheet/popover transition when native behavior is unavailable |
| `motion.signature` | 480 ms | Optional matched expansion; never delay access to the action |

Use `easeOut = cubic-bezier(0.22, 1, 0.36, 1)`. The proposed settle spring is **stiffness 260 / damping 34 / mass 1** in a physics model with those meanings. Platform-native spring parameters may not map numerically; match the behavior. A press may scale to **0.98** only when it does not move adjacent content. Typical non-gesture entrance travel is at most **12** logical units.

Long media-focus or streaming-trail effects are optional, content-specific recipes. Keep ordinary controls on the shared transition scale and never simulate slow operations just to finish an animation.

With **Reduce Motion**, disable parallax, refraction movement, zoom, perspective, elastic deformation, and ambient loops. Change state instantly or crossfade for at most 120 ms. With **Reduce Transparency**, use solid surfaces. Preserve labels, value changes, next/previous controls, and all routes through the task.

## Portable tokens

The following JSON is the authoritative machine-readable contract for Custom UI Design System v1.0.1. It is plain application data, not a claimed standards-compliant interchange format. Resolve `{path.to.token}` aliases recursively. Replace `$theme` with `light` or `dark` before resolving color aliases. A generator should reject missing references and cycles. In native code, semantic names should become theme properties rather than being retyped as hex literals throughout screens.

```json
{
  "meta": {
    "name": "Custom UI Design System",
    "version": "1.0.1",
    "reviewedOn": "2026-11-04",
    "specification": "Portable token contract; not a DTCG interchange file",
    "units": {
      "dimension": "logical unit: iOS pt, Android dp, web CSS px at 1x",
      "font": "iOS scalable pt, Android sp, web rem equivalent",
      "duration": "ms"
    },
    "provenance": "Production specifications maintained in this repository. Historical research and source credits are documented separately in docs/REFERENCES.md."
  },
  "space": {
    "0": 0,
    "1": 4,
    "2": 8,
    "3": 12,
    "4": 16,
    "6": 24,
    "8": 32,
    "10": 40,
    "12": 48,
    "16": 64
  },
  "radius": {
    "small": 6,
    "field": 12,
    "surface": 16,
    "sheet": 28,
    "hero": 32,
    "pill": "half the rendered height"
  },
  "layout": {
    "pageInset": 24,
    "compactInset": 16,
    "sectionGap": 32,
    "groupGap": 24,
    "itemGap": 12,
    "inlineGap": 8,
    "readingMaxWidth": 560,
    "expandedPaneMaxWidth": 680
  },
  "size": {
    "controlMinHeight": 52,
    "targetMin": 48,
    "icon": 24,
    "smallIcon": 20,
    "rowMinHeight": 64,
    "tabBarContentMinHeight": 64,
    "focusRing": 2,
    "focusOffset": 2
  },
  "type": {
    "family": {
      "ios": "platform system font through native APIs",
      "android": "platform system sans",
      "web": "system-ui, sans-serif"
    },
    "display": {
      "size": 35,
      "lineHeight": 40,
      "weight": 600,
      "trackingEm": -0.025
    },
    "title": {
      "size": 28,
      "lineHeight": 36,
      "weight": 600,
      "trackingEm": -0.02
    },
    "heading": {
      "size": 20,
      "lineHeight": 28,
      "weight": 600,
      "trackingEm": -0.01
    },
    "body": {
      "size": 17,
      "lineHeight": 24,
      "weight": 400,
      "trackingEm": 0
    },
    "bodyStrong": {
      "size": 17,
      "lineHeight": 24,
      "weight": 600,
      "trackingEm": 0
    },
    "label": {
      "size": 14,
      "lineHeight": 20,
      "weight": 500,
      "trackingEm": 0
    },
    "caption": {
      "size": 12,
      "lineHeight": 16,
      "weight": 400,
      "trackingEm": 0
    }
  },
  "color": {
    "light": {
      "canvas": "#F6F6F8",
      "surface": "#FFFFFF",
      "surfaceRaised": "#FFFFFF",
      "surfaceInset": "#EEEEF2",
      "textPrimary": "#1D1D1F",
      "textSecondary": "#64646A",
      "textOnMedia": "#FFFFFF",
      "divider": "#DEDEE3",
      "controlBorder": "#85858F",
      "focus": "#6E56CF",
      "action": "#6E56CF",
      "actionPressed": "#5C43BE",
      "onAction": "#FFFFFF",
      "accentSurface": "#EEE9FC",
      "accentText": "#5940AE",
      "selectedSurface": "#EEE9FC",
      "disabledSurface": "#E8E8ED",
      "disabledText": "#64646A",
      "successSurface": "#E8F7ED",
      "successText": "#216E42",
      "warningSurface": "#FFF4D6",
      "warningText": "#7A4B00",
      "dangerSurface": "#FCEBEC",
      "dangerText": "#9E2B2B",
      "infoSurface": "#EAF2FF",
      "infoText": "#204F9B",
      "scrim": "#00000066"
    },
    "dark": {
      "canvas": "#000000",
      "surface": "#0A0A0A",
      "surfaceRaised": "#131313",
      "surfaceInset": "#1C1C20",
      "textPrimary": "#F5F5F5",
      "textSecondary": "#B4B4B4",
      "textOnMedia": "#FFFFFF",
      "divider": "#34343A",
      "controlBorder": "#777780",
      "focus": "#BAA7FF",
      "action": "#BAA7FF",
      "actionPressed": "#A58DEB",
      "onAction": "#21183C",
      "accentSurface": "#252034",
      "accentText": "#BAA7FF",
      "selectedSurface": "#252034",
      "disabledSurface": "#25252A",
      "disabledText": "#B4B4B4",
      "successSurface": "#10291B",
      "successText": "#A3E5BC",
      "warningSurface": "#30250E",
      "warningText": "#F4D48C",
      "dangerSurface": "#33181C",
      "dangerText": "#FFB4AC",
      "infoSurface": "#15243A",
      "infoText": "#B1CCFF",
      "scrim": "#00000099"
    }
  },
  "motion": {
    "instant": 0,
    "feedback": 120,
    "control": 180,
    "content": 240,
    "overlay": 320,
    "signature": 480,
    "easeOut": [
      0.22,
      1,
      0.36,
      1
    ],
    "easeInOut": [
      0.65,
      0,
      0.35,
      1
    ],
    "settleSpring": {
      "stiffness": 260,
      "damping": 34,
      "mass": 1
    },
    "pressScale": 0.98,
    "enterDistanceMax": 12,
    "reduced": {
      "duration": 120,
      "translation": 0,
      "scale": 1,
      "refraction": false,
      "ambientLoops": false
    }
  },
  "layer": {
    "content": 0,
    "sticky": 10,
    "floating": 20,
    "popover": 30,
    "modalScrim": 40,
    "modal": 50,
    "toast": 60,
    "tooltip": 70
  },
  "elevation": {
    "floatingLight": {
      "color": "#0000001A",
      "x": 0,
      "y": 4,
      "blur": 16,
      "spread": 0
    },
    "overlayLight": {
      "color": "#00000024",
      "x": 0,
      "y": 12,
      "blur": 32,
      "spread": 0
    },
    "dark": "Use surfaceRaised plus divider; do not rely on a black shadow for separation."
  },
  "component": {
    "button": {
      "minHeight": "{size.controlMinHeight}",
      "radius": "{radius.surface}",
      "paddingX": "{space.6}",
      "gap": "{space.2}",
      "type": "{type.label}",
      "background": "{color.$theme.action}",
      "foreground": "{color.$theme.onAction}"
    },
    "field": {
      "minHeight": "{size.controlMinHeight}",
      "radius": "{radius.field}",
      "paddingX": "{space.4}",
      "type": "{type.body}",
      "background": "{color.$theme.surface}",
      "border": "{color.$theme.controlBorder}"
    },
    "sheet": {
      "radiusTop": "{radius.sheet}",
      "padding": "{layout.pageInset}",
      "background": "{color.$theme.surfaceRaised}"
    },
    "badge": {
      "type": "{type.label}",
      "radius": "{radius.small}",
      "paddingX": "{space.2}",
      "paddingY": "{space.1}"
    }
  }
}
```

**Mapping convention:** `color.light.textPrimary` → `theme.color.textPrimary`; `type.body` → one complete text style; `component.button` → a shared component recipe. Web implementations convert type sizes to `rem`, preserve user zoom, and use native focus behavior. Native implementations use platform scalable text styles and safe-area APIs. Elevation values are visual targets; Android elevation and iOS shadows are not numerically interchangeable.

## Components

All values here are the system's production specifications. Every interactive component has default, pressed, focused where relevant, disabled, and loading states where meaningful. Data-driven content also needs empty, partial, stale/offline, and failure/retry states. State changes must preserve the user's context.

| Component | Anatomy and default size | Required behavior |
|---|---|---|
| **Action button** | Minimum 52 high, radius 16, padding 24, label 14/20, optional icon24 + gap8 | Primary, secondary, quiet, and destructive variants. Keep width and label stable while busy; prevent duplicate submission. Show a real recoverable error. One main action per decision group. |
| **Icon button** | Icon24 in target48; optional neutral filled surface | Stable accessible action name. Toggle exposes selected state. Do not rely on a tooltip as its only name. |
| **Text field** | Persistent label14/20, gap8, field min52/radius12/padding16, text17/24, helper gap8 | Appropriate keyboard/autofill/return action; empty, focused, invalid, populated, disabled, read-only. Preserve input after failure. Show the correction in text. |
| **List row** | Minimum64, content gap16, title17/24, support14/20 | Wrap long content; distinguish navigation, switch, and separate trailing action. Use spacing/separators instead of enclosing every row in a card. |
| **Content surface** | Radius16, padding16 or24, gaps12 or16 | Static and actionable variants are separate. Reserve media space. Show loading/empty/failure. Avoid a full-card action with competing nested buttons. |
| **Segmented control** | Minimum56 high, inset4, segment target48, radius16 | Two to four short related views. Selected background plus selected semantics. Preserve panel state. Reflow or use a menu when labels cannot fit. |
| **Bottom navigation** | Minimum64 content region + runtime safe area, icon24 + label14/20 | Three to five actual top-level destinations. Keep labels visible and restore each destination's scroll/navigation state. A badge has a meaningful spoken description. |
| **Bottom sheet** | Top radius28, inset24, content-driven height | Explicit close, system back, focus management, keyboard-aware content. Dragging is supplementary. Use medium/full detents only when the task benefits. Push a complex child task rather than accumulating modal layers. |
| **Toast/banner** | Radius12 or16, padding16, icon24 + gap12, readable text | Brief noncritical feedback may toast. Persistent failure or required action stays inline/in a banner. Undo/dismiss targets48; reading time and accessibility settings take priority over a fixed timeout. |
| **Confirmation dialog** | Radius28, inset24, clear object/consequence, actions min52 | Use explicit verbs such as “Delete recording.” Safe exit, busy/failure state, and focus restoration. Reversible routine actions generally favor undo. |
| **Switch / choice** | Platform-native visual control within target48 | Label and value are exposed together. Show pending/error when a remote change can fail. Never imply success before confirmation unless rollback is supported. |
| **Slider** | Minimum48 interaction region, clear label/current value | Steps, endpoints, increment/decrement accessibility actions, and editable value when precision matters. Glow/stretch are optional; the actual value and target stay stable. |
| **Date/time picker** | Platform-native picker by default | Locale-aware format, explicit timezone where relevant, constraints and invalid-date feedback. Preserve selected values across sheet changes. Never replace a usable native picker solely for visual novelty. |
| **OTP input** | One logical code field with an optional segmented visual representation | Paste and platform autofill work for the complete code. Handle incomplete, invalid, expired, resend pending, and retry. Announce the field coherently rather than six unrelated unnamed cells. |

### Shared interaction rules

The entire target responds, not only its glyph. Maintain at least 8 units of separation where adjacent controls would otherwise overlap. Larger text can grow every minimum-height component. Focus is visible, follows logical reading order, enters modal content, and returns to its trigger or a meaningful successor after removal.

Use clear, short outcome-oriented copy: **Save changes**, **Try again**, **Copy link**, **Delete recording**. Errors state what happened and how to continue. Empty states explain the next useful action. Do not add playful text to serious failures.

For async work: `idle → pending → success OR error`; cancellation and interruption are explicit when supported. A small optimistic change is acceptable only with reliable rollback. Preserve scroll position and content during refresh. Skeletons match the eventual layout; an old screen does not blank out for a background refresh.

## Signature interactions

These recipes are optional. Use the ordinary components above whenever they serve the task. The recipes use the shared foundations and define their own state behavior and fallbacks.

### Morphing header and progressive blur

Use for a profile, artist, or detail page whose large identity header becomes a compact toolbar. Bind transition progress to scroll offset. Preserve one semantic title/avatar identity and keep back/share available throughout. A local blur may separate content moving behind a fixed header; it must not blur the text the user is reading.

Expanded → scrolling → compact → expanded is reversible at any point. Preserve the top inset at large text sizes. Offer a normal compact-header fallback on non-island devices. A pull-to-expand media banner must not compete with refresh or system gestures; provide an explicit **Expand media** action.

**Low-motion fallback:** switch between expanded and compact layouts, retaining the same title and controls. Never emulate an OS cutout with a fixed black pill across every device.

### Media carousel and expanding player

Use for a small collection of artwork, events, or media where one item has focus. Maintain a clear centered item and a visible neighbor only when it helps explain horizontal browsing. Preserve the media ratio; use the container width, not a hard-coded device width. The active item alone owns playback.

Dragging → settling → focused → expanded → focused must keep the selected item identifiable. Match the expanding media surface to its destination. Place captions and transport controls on legible local material. Expose next/previous, item count, activate, pause, and close actions. Stop autoplay when content leaves the active context. An explicitly playing audio session may continue in a compact player containing thumbnail, track title, and play/pause. Preserve the track, playback position, and fixed transport targets when expanding or collapsing it.

**Low-motion fallback:** horizontal list/pager with direct selection and a normal detail screen. Avoid shader snapshots for cards containing independently interactive or live content unless their interaction/accessibility tree is preserved.

### Keyboard-aware composer and tray

Use a persistent text composer that rises with the keyboard. Give it min52 height, body17/24, and `radius.pill` for a single line (26 at height52). Use radius28 for a taller multiline container and bound its expansion. Keep draft content and attachment state stable as the picker opens. Input, send/stop, and attachment actions remain distinct accessible controls.

Collapsed → editing → attachment tray → selected attachments → sending → sent/error. Derive tray height and keyboard transitions from runtime metrics. Avoid a gap or double bottom inset during keyboard swaps. Keep stop/retry available during streaming. Request photo/microphone access when the user invokes that function, with a useful denied-permission path.

**Low-motion/unsupported-material fallback:** ordinary solid composer plus native attachment sheet. Keyboard correctness is required in every theme and platform.

### Matched popover, sheet, and local action menu

Anchor a short contextual menu to its trigger. Preserve spatial origin when it expands into a richer panel. Use a portal/native presentation so clipping containers do not cut off the popover. Keep focus, background interaction, outside dismissal, and system back consistent with whether the surface is modal.

Choose a popover for a few contextual actions; a sheet for a bounded task; a pushed screen for a complex flow. If a second sheet is unavoidable, expose the parent context and a clear back route; never build an unbounded stack of translucent panels.

**Low-motion fallback:** directly open the destination surface. The anchor relationship remains visually clear through placement and labeling.

### Morphing status and notifications

A status component may change icon, label, width, and semantic tint together as one object: queued → active → complete/error. Keep labels readable during transition, and announce meaningful state changes once. Do not announce each animation frame.

Use a compact badge for the object's status, a banner for persistent problems, and a toast for brief feedback. A stackable toast recipe may show up to three visible entries, newest first, with older messages accessible in context; important actions do not disappear underneath the stack. An island-style notification remains within app-owned safe content and does not impersonate system privacy indicators.

**Low-motion fallback:** replace the labeled state immediately or crossfade. Never use a morph to delay real completion.

### Streaming text and assistant state

Append actual incoming words/chunks without reanimating prior content. Use the body text style, stable paragraph spacing, and normal headings. A temporary accent trail may mark arrival, but text must quickly resolve to a readable foreground. Do not use low-contrast violet as the permanent body text.

Auto-follow only while the reader is at the latest content. Scrolling away suspends auto-follow and exposes **Jump to latest**. Keep partial content after interruption. Provide stop and retry/resume when supported. Screen readers receive an appropriate progress summary and one completion announcement, not one announcement per token.

Assistant states reflect real activity: idle → listening → processing → speaking/answer, with cancellation, disconnect, and error exits. Label each state. A visual orb/waveform is supplementary; a loop must never imply microphone use when no capture is taking place.

**Low-motion fallback:** static state label/icon and immediate incoming text. No forced breathing, edge glow, or moving refraction. Unsupported island platforms use an inline status or ordinary banner.

### Tactile controls, copy, and deliberate deletion

Press feedback may use tint and a 0.98 scale, returning without a bounce. Glare, tilt, and stretch belong to a media/object demonstration, not every button. A copy interaction exposes **Copy**, confirms **Copied**, and offers the actual value; animated masking is never a security boundary.

For deletion, reveal a labeled action through a menu or optional swipe, then use undo for reversible removal or a specific confirmation for irreversible consequences. Preserve context during pending work. On failure, restore the item and explain recovery. Hold-to-confirm, crumpling, and disintegration must have ordinary accessible alternatives and must not impose demo-length waiting.

**Low-motion fallback:** immediate/tint feedback and a conventional confirmation/undo path.

### Focused editing

For photo, sound, or other media editing, keep the preview/current item visible, the selected tool obvious, and the current numeric value readable when precision matters. Tool selection does not move reset, cancel, confirm, or core transport controls. Work on a reversible draft; reset returns to a defined baseline, cancel discards the draft, and confirm commits it. Preserve edits after a failed save/export and explain the retry route. A value slider has increment/decrement alternatives and a direct value input where needed.

## Screen recipes

| Screen | Recommended composition | Signature allowance | Essential non-happy-path behavior |
|---|---|---|---|
| **Home / library** | Title, search, concise filter, content list/grid, bottom navigation | Moving selected filter OR compact matched detail transition | Loading placeholders, empty library, offline cached content, retry |
| **Media / event detail** | Artwork header, title/metadata, one main action, related content | Morphing header OR expanding player/carousel | Missing image, unavailable item, long title, playback failure |
| **Player / editor** | Stable preview/current item, familiar transport or tool controls, labeled values, separate grouped settings | One local material or selected-tool transition | Loading media, interrupted playback, reset/undo, failed save/export |
| **Chat / assistant** | Readable transcript, stable composer, optional attachment tray | Streaming trail OR compact state island | Stop, partial response, reconnect, attachment/permission failure |
| **Create / edit** | Clear title, labeled fields, contextual help, persistent submit region | Small local status confirmation | Validation, keyboard, unsaved changes, submit failure, restoration |
| **Settings / account** | Grouped rows, native switches, clear destructive section | Ordinary local control feedback | Failed remote toggle, disabled reason, sign-in expiry |
| **Search / discovery** | Search field, filters, results, detail route | One media-focused carousel where it improves discovery | No results, partial results, stale query, loading/retry |
| **Onboarding** | One purpose per step, useful preview, clear continue/back | Small step indicator or matched preview | Skip where valid, permission later, interruption/resume |

Do not force all applications into the same dashboard. A task list, media player, and chat share the design grammar while retaining different information architecture.

### A concrete default screen

For a new app, begin with: runtime safe top inset → toolbar with back or app context → title28/36 → 24 gap → primary content → 32 gap → next content group. Use 24 side insets. Put bottom navigation in a min64 region plus runtime safe area. A form's primary button is min52 and remains reachable above the keyboard. Add one signature only after the ordinary flow works.

## Accessibility and platform behavior

Respect system theme, increased text size, reduced motion, reduced transparency, screen readers, and keyboard/switch access. Provide a color-independent selected state, error text, meaningful image alternatives, correct reading order, and visible focus. Review long translations and RTL layouts using logical start/end spacing. Do not mirror album art, numbers, or media playback symbols indiscriminately.

On iOS, keep native back/swipe-back, permission flows, sheets, pickers, and safe areas. On Android, keep system/predictive back, native keyboard behavior, appropriate system bars, and accessible equivalents for iOS-only effects. On mobile web, preserve browser zoom, keyboard focus, semantic controls, and viewport/keyboard behavior. Use conventional controls when a platform cannot reproduce a material or morph reliably.

Hardware cutouts and native modules are optional enhancement paths. Feature-detect support, verify the requirements of the chosen implementation, and provide a conventional toolbar or inline status on other devices.

Measure gesture-heavy screens on a representative lower-performance device. Keep motion on the native/UI rendering path where practical, reuse expensive effects, and disable costly shader/blur work if it interferes with input. A smooth ordinary surface is an acceptable supported variant of every expressive recipe.

## Adoption

### Paste this into the next application brief

> Use the attached CUSTOM_UI_DESIGN_SYSTEM.md as this application's design source of truth. Build the [app purpose] for [audience] on [platforms], using the [Core / Media / Assistant / Editorial] profile. Follow its semantic theme, type and spacing tokens, component states, screen patterns, keyboard/safe-area behavior, accessibility, and reduced-motion fallbacks. Reuse shared components before adding new ones. Choose one meaningful signature interaction per task area. Use the production specifications in this document as the implementation defaults. Deliver the complete task flow with loading, empty, error, offline/partial-data, large-text, and interruption behavior where applicable. If a needed pattern is missing, add the smallest consistent extension and document it.

### App configuration

```yaml
designSystem: Custom UI Design System
version: 1.0.1
profile: Core
theme: system
accentOverride: null
signaturePattern: null # choose deliberately after the core flow works
platforms: [ios, android]
```

Keep shared foundations in one theme module, ordinary components in one library, and signature effects in optional feature modules. Screens consume semantic tokens rather than raw colors. A change to a shared alias must be reviewed in light/dark, large text, and every app profile that uses it.

### Definition of done

- [ ] The main task works end to end with native back and keyboard behavior.
- [ ] Compact width, large text, long content, RTL where supported, and split-screen layouts remain usable.
- [ ] Light/dark contrast pairs and real media overlays are checked; essential controls have visible boundaries/focus.
- [ ] Targets remain at least 48 × 48 logical units; labels, roles, values, and reading order work with assistive technology.
- [ ] Loading, empty, validation, failure, offline/partial data, cancellation, and recovery are covered where relevant.
- [ ] Reduced motion and opaque-material fallbacks retain every action and meaning.
- [ ] A signature adds clarity or tactile feedback without adding waiting or competing with another effect.
- [ ] No simulator frames, fixed hardware cutouts, third-party assets without the appropriate usage rights, or promotional wallpaper leaked into product UI.

### Governance

**Owner:** the application's design-system maintainer. **Versioning:** patch for clarification/correction, minor for compatible components/tokens, major for changes to existing semantics or visual behavior. An app may pin an older major during migration.

For an extension, record its user problem, chosen semantic role, component states, accessibility/fallback, source if any, and affected screens. Promote it into the shared library after it proves reusable in multiple real contexts. Keep experiments feature-local until then. When changing a token, document the before/after result and migration instead of silently restyling every application.

**Change log**

- **1.0.1, 4 November 2026:** adopts the Custom UI Design System identity, updates documentation and rendered examples, and separates historical research into a reference appendix. Geometry, color, and motion values remain unchanged.
- **1.0.0, 4 November 2026:** establishes the mobile foundations, component states, cross-platform fallbacks, checked theme palette, and portable token contract.

## Contrast checks

Computed using sRGB relative luminance. These checks cover opaque token pairs, not arbitrary media/glass combinations.

| Theme | Foreground / background | Ratio |
|---|---|---:|
| Light | `textPrimary` / `canvas` | 15.59:1 |
| Light | `textPrimary` / `surfaceRaised` | 16.83:1 |
| Light | `textSecondary` / `canvas` | 5.45:1 |
| Light | `textSecondary` / `surfaceRaised` | 5.88:1 |
| Light | `textSecondary` / `surfaceInset` | 5.08:1 |
| Light | `textSecondary` / `accentSurface` | 4.95:1 |
| Light | `onAction` / `action` | 5.39:1 |
| Light | `onAction` / `actionPressed` | 7.00:1 |
| Light | `accentText` / `accentSurface` | 6.39:1 |
| Light | `disabledText` / `disabledSurface` | 4.81:1 |
| Light | `successText` / `successSurface` | 5.62:1 |
| Light | `warningText` / `warningSurface` | 6.76:1 |
| Light | `dangerText` / `dangerSurface` | 6.43:1 |
| Light | `infoText` / `infoSurface` | 7.03:1 |
| Light | `controlBorder` / `surface` | 3.65:1 |
| Light | `controlBorder` / `surfaceInset` | 3.16:1 |
| Light | `focus` / `canvas` | 5.00:1 |
| Light | `focus` / `surfaceRaised` | 5.39:1 |
| Dark | `textPrimary` / `canvas` | 19.26:1 |
| Dark | `textPrimary` / `surfaceRaised` | 17.04:1 |
| Dark | `textSecondary` / `canvas` | 10.13:1 |
| Dark | `textSecondary` / `surfaceRaised` | 8.96:1 |
| Dark | `textSecondary` / `surfaceInset` | 8.19:1 |
| Dark | `textSecondary` / `accentSurface` | 7.59:1 |
| Dark | `onAction` / `action` | 7.98:1 |
| Dark | `onAction` / `actionPressed` | 6.04:1 |
| Dark | `accentText` / `accentSurface` | 7.54:1 |
| Dark | `disabledText` / `disabledSurface` | 7.36:1 |
| Dark | `successText` / `successSurface` | 10.69:1 |
| Dark | `warningText` / `warningSurface` | 10.48:1 |
| Dark | `dangerText` / `dangerSurface` | 9.61:1 |
| Dark | `infoText` / `infoSurface` | 9.63:1 |
| Dark | `controlBorder` / `surface` | 4.46:1 |
| Dark | `controlBorder` / `surfaceInset` | 3.83:1 |
| Dark | `focus` / `canvas` | 10.06:1 |
| Dark | `focus` / `surfaceRaised` | 8.90:1 |

## References

Historical design research, reviewed examples, and original source credits are preserved in the repository's [reference appendix](https://github.com/itsakbarov/mobile-design-system/blob/main/docs/REFERENCES.md).
