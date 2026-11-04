# Meld Mobile

**A portable design system for expressive, native-feeling mobile applications.**

Version **1.0.0** · Prepared **4 November 2026** · iOS, Android, and responsive mobile web

Inspired by [rit3zh's portfolio on X](https://x.com/rit3zh). This is a new, consolidated system for your applications, not an official system published or endorsed by the creator.

## Start here

Copy this **one file** into each application's repository as `DESIGN_SYSTEM.md`. Give it to your designer, developer, or coding agent before implementation. The document contains the visual direction, portable tokens, component behavior, motion recipes, screen patterns, and a source ledger. It has no required companion assets or remote fonts.

**Visual companion:** the repository's [README gallery](https://github.com/itsakbarov/mobile-design-system#readme-ov-file) shows light and dark components, three mobile screen examples, forms and overlays, and a matched-expansion motion example. Its [rendering source](https://github.com/itsakbarov/mobile-design-system/blob/main/examples/render.py) reads the tokens in this file. The specification remains usable by itself when copied into another project.

For the default app, use **neutral surfaces + native sans typography + restrained violet + one meaningful signature interaction per task area**. Choose light or dark according to the use context and the user's system setting. Keep all behavior available with reduced motion and opaque materials.

**Reading order:** [Design language](#design-language) → [Foundations](#foundations) → [Portable tokens](#portable-tokens) → [Components](#components) → [Signature interactions](#signature-interactions) → [Screen recipes](#screen-recipes) → [Adoption](#adoption) → [Evidence and coverage](#evidence-and-coverage).

### What the labels mean

- **Observed:** visible in reviewed video playback or its presentation. Video review uses sampled playback states; it is not a frame-by-frame measurement or usability test.
- **Source-exact:** a literal value or documented behavior read in the creator's linked repository. Exact source values are collected in the evidence appendix, separate from the implementation defaults.
- **Meld specification:** an original production choice for a consistent, reusable system. All requirements and token values below are Meld specifications unless explicitly labeled otherwise.

The portfolio contains different apps, platform experiments, and promotional videos. Its strongest common thread is **continuity of interaction**, rather than a single repeated brand palette. This system preserves that thread while standardizing the parts that applications need to share.

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

**Presentation is not product UI.** The account often places a phone inside a simulator frame over a wallpaper. Device bezels, simulator toolbars, macOS windows, recording backgrounds, and promotional captions are presentation assets. Do not reproduce them inside your app.

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

The spacing scale is **0, 4, 8, 12, 16, 24, 32, 40, 48, 64**. The creator's streaming example publishes the 4–64 scale; zero and the semantic role assignments are Meld additions.

Design on a compact phone first. Validate at **320, 360, 390, and 430** logical units, landscape, tablet, and split screen. These are review widths, not fixed canvas sizes. Above approximately 600 available units, use a bounded reading pane or list/detail structure; do not stretch phone cards to fill the display. Breakpoints respond to available space and content.

Use runtime safe-area and keyboard insets. A bottom action region includes its own content height plus the current bottom inset. Ensure the last list row and focused form field can scroll above sticky controls. Do not hard-code a notch, Dynamic Island, home indicator, status bar, or keyboard height.

### Typography

Use the native system family through platform APIs. Do not bundle SF fonts for Android or the web. The Editorial profile may use the platform serif for one display role; it must not affect navigation, form labels, or data.

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

The neutral/violet family is source-informed; the specific semantic assignments and accessible status pairs are Meld specifications. Use the complete light or dark theme. Do not implement dark mode as a simple inversion.

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

Use a single accent family across an app. Do not interpret the portfolio's different demo palettes as a requirement to mix violet, neon green, red, cyan, and pastels in one product.

Meld deliberately darkens the source's light secondary gray from `#6E6E73` to `#64646A` so ordinary secondary text also works on inset and accent surfaces. The source-exact original remains in the evidence appendix.

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

The creator's longer 700–900 ms carousel focus and 1500–2000 ms text trail are named showcase effects, not global transition tokens. Keep them optional and content-specific. Do not simulate slow operations just to finish an animation.

With **Reduce Motion**, disable parallax, refraction movement, zoom, perspective, elastic deformation, and ambient loops. Change state instantly or crossfade for at most 120 ms. With **Reduce Transparency**, use solid surfaces. Preserve labels, value changes, next/previous controls, and all routes through the task.

## Portable tokens

The following JSON is the authoritative machine-readable contract for Meld v1.0. It is plain application data, not a claimed standards-compliant interchange format. Resolve `{path.to.token}` aliases recursively. Replace `$theme` with `light` or `dark` before resolving color aliases. A generator should reject missing references and cycles. In native code, semantic names should become theme properties rather than being retyped as hex literals throughout screens.

```json
{
  "meta": {
    "name": "Meld Mobile",
    "version": "1.0.0",
    "reviewedOn": "2026-11-04",
    "specification": "Meld portable token contract; not a DTCG interchange file",
    "units": {
      "dimension": "logical unit: iOS pt, Android dp, web CSS px at 1x",
      "font": "iOS scalable pt, Android sp, web rem equivalent",
      "duration": "ms"
    },
    "provenance": "Source-informed production adaptation; see evidence appendix. Values are Meld specifications unless explicitly labeled source-exact."
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
      "ios": "system / SF through platform APIs",
      "android": "platform system sans",
      "web": "system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
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

All values here are Meld specifications. Every interactive component has default, pressed, focused where relevant, disabled, and loading states where meaningful. Data-driven content also needs empty, partial, stale/offline, and failure/retry states. State changes must preserve the user's context.

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

These recipes are optional. Use the ordinary components above whenever they serve the task. The recipe specifications are Meld adaptations; exact source values are listed separately in the evidence appendix.

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

Hardware cutouts and native modules are optional enhancement paths. Feature-detect them. The creator's Siri island example is iOS-specific and the profile/metaball example requires a development build rather than Expo Go; these are implementation constraints of those examples, not requirements for using Meld.

Measure gesture-heavy screens on a representative lower-performance device. Keep motion on the native/UI rendering path where practical, reuse expensive effects, and disable costly shader/blur work if it interferes with input. A smooth ordinary surface is an acceptable supported variant of every expressive recipe.

## Adoption

### Paste this into the next application brief

> Use the attached MELD_MOBILE_DESIGN_SYSTEM.md as this application's design source of truth. Build the [app purpose] for [audience] on [platforms], using the [Core / Media / Assistant / Editorial] profile. Follow its semantic theme, type and spacing tokens, component states, screen patterns, keyboard/safe-area behavior, accessibility, and reduced-motion fallbacks. Reuse shared components before adding new ones. Choose one meaningful signature interaction per task area. Treat the evidence appendix as inspiration and the explicitly defined Meld specifications as implementation defaults. Deliver the complete task flow with loading, empty, error, offline/partial-data, large-text, and interruption behavior where applicable. If a needed pattern is missing, add the smallest consistent extension and document it.

### App configuration

```yaml
designSystem: Meld Mobile
version: 1.0.0
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
- [ ] No simulator frames, fixed hardware cutouts, copied creator assets, or promotional wallpaper leaked into product UI.

### Governance

**Owner:** the application's design-system maintainer. **Versioning:** patch for clarification/correction, minor for compatible components/tokens, major for changes to existing semantics or visual behavior. An app may pin an older major during migration.

For an extension, record its user problem, chosen semantic role, component states, accessibility/fallback, source if any, and affected screens. Promote it into the shared library after it proves reusable in multiple real contexts. Keep experiments feature-local until then. When changing a token, document the before/after result and migration instead of silently restyling every application.

**Change log — 1.0.0, 4 November 2026:** first consolidated Meld system, derived from the reviewed portfolio and linked source examples; adds complete production states, cross-platform fallbacks, a checked theme palette, and a portable token contract.

## Evidence and coverage

**Review snapshot: 4 November 2026.** The signed-in Videos feed was traversed from newest to its visible oldest endpoint, then cross-checked against author threads and a focused X Latest search (`from:rit3zh filter:videos`). The combined review contains **55 main video posts + 9 additional author-posted reply videos = 64 video reviews**, spanning 20 June 2025–3 November 2026. Each listed video was visually sampled during playback.

**Method:** accessibility metadata plus multiple playback screenshot moments where feasible, not uninterrupted viewing of every frame. Durations below are approximate player totals. The longer filter/audio demos were sampled for interface behavior rather than audited for every effect, sound quality, or performance. Limited montage, promotional, and code-demo evidence is labeled in the ledger.

**Scope:** includes every main video surfaced by the current Videos feed and the additional original reply clips found through threads/search. It does not guarantee access to hidden, unindexed, deleted, or private posts, or establish every frame within a montage. Separate uploads of similar-looking clips are separate reviewed posts. Quoted third-party reference videos are attributed rather than counted as rit3zh-created clips. Mixed image/video galleries count once for their reviewed video.

**Reading the ledger:** each row is a sampled visual finding followed by the rule carried into Meld. The four Slice rows are desktop/presentation references; their mobile contribution is explicitly limited.

| Date / video | Approx. length | Sampled finding | Rule for reuse |
|---|---:|---|---|
| 2026-11-03 · [Profile header / metaball merge](https://x.com/rit3zh/status/2117568716607246450) | ~16s | A pale profile list keeps a circular avatar identifiable as it merges into compact top chrome and returns on reverse scroll. | Preserve identity across scroll-linked expanded/compact states; use a normal toolbar fallback. |
| 2026-11-02 · [Liquid glass carousel](https://x.com/rit3zh/status/2117171219644776651) | ~8s | Portrait event invitations browse over a blurred image-derived backdrop, with one centered item and controlled white caption text. | Use localized media depth and clear selection; keep a plain snapping pager alternative. |
| 2026-10-31 · [Animated streaming text](https://x.com/rit3zh/status/2116511633224900995) | ~18s | Black chat canvas, quiet input pill, stable markdown reading structure, and a temporary violet/gray arrival trail. | Append new content without reanimating history or overriding the reader’s scroll position. |
| 2026-10-29 · [Siri-AI inspired animation](https://x.com/rit3zh/status/2115565941128102250) | ~15s | A compact luminous top region expands into a labeled processing status while music artwork stays visible. | Tie compact/expanded status to real operations and provide an ordinary in-app status fallback. |
| 2026-10-27 · [Small interaction collection](https://x.com/rit3zh/status/2115026517998842173) | ~15s | Sampled montage states show badge morph, active violet slider, and an expanded red delete confirmation. | Coordinate label, glyph, size, and tint as one state; do not apply every effect simultaneously. |
| 2026-10-21 · [Slice MacBook mockups](https://x.com/rit3zh/status/2112863870134165521) | ~16s | Angled 3D MacBook staging changes to a readable front-facing screen preview. | Desktop presentation only: borrow focal hierarchy, not device staging or desktop density. |
| 2026-10-20 · [Slice annotation while recording](https://x.com/rit3zh/status/2112473154417578290) | ~10s | A compact contextual drawing toolbar produces editable arrows, freehand marks, and rectangles over recorded content. | Desktop reference: adapt contextual tools to reachable, adequately sized mobile controls. |
| 2026-10-17 · [Slice v0.2.0 focus, privacy and export](https://x.com/rit3zh/status/2111480143923515727) | ~31s | Spotlight, magnification, and surrounding blur focus a recording on a selected region. | Desktop editor reference: guide attention while preserving context; blur is not a security boundary. |
| 2026-10-17 · [Slice first release](https://x.com/rit3zh/status/2111343045266596102) | ~10s | A restrained dark launch clip pairs concise “record.” typography with compact recording chrome. | Limited promotional evidence: use clear task language; infer no mobile dimensions or theme mandate. |
| 2026-10-05 · [Reply · Morphlet Android stack](https://x.com/rit3zh/status/2107107795271397544) | ~9s | An amount-entry surface proceeds to a success surface in the same contained region, retaining prior context. | Preserve task identity, focus, back behavior, and explicit outcomes through short contained flows. |
| 2026-10-05 · [Reply · Morphlet Android](https://x.com/rit3zh/status/2107107791429357839) | ~7s | Light Android action sheet uses grouped neutral options, explicit close, and a separately styled destructive row. | Keep overlay anatomy consistent while adapting platform rendering and action semantics. |
| 2026-10-05 · [Morphlet v0.1.2](https://x.com/rit3zh/status/2107107787293753694) | ~22s | Dark rounded direction, ticket, and checkout surfaces retain the event imagery and previous task context. | Make the active layer, close/back route, keyboard accommodation, and final outcome clear. |
| 2026-10-05 · [Reply · Android stack, earlier separate upload](https://x.com/rit3zh/status/2107107314222411835) | ~9s | Light rounded Send/asset-selection and Amount sheets occupy the same contained task region over a dimmed playground; percentage shortcuts sit above a stable pale-blue Continue action. | Preserve contained task continuity from selection to entry, with a stable primary-action position and an explicit close/back path. |
| 2026-09-24 · [Reply · Android composer and image picker](https://x.com/rit3zh/status/2103139131811656188) | ~14s | A light ChatGPT-inspired composer coordinates with the Android keyboard, selected-photo preview and expanding thumbnail chooser; picker focus blurs the inactive composer/keyboard layer and exposes close. | Coordinate input, attachments, picker and keyboard geometry while preserving draft/media state and an explicit dismissal path. |
| 2026-09-24 · [Reply · Motion blur Android](https://x.com/rit3zh/status/2102847371071852898) | ~7s | Android comparison clears from a dark authentication sheet to its underlying chat composer. | Keep the interaction intent while adapting platform controls; experimental blur remains optional. |
| 2026-09-24 · [Experimental motion blur](https://x.com/rit3zh/status/2102847366856683645) | ~5s | Fast-moving authentication-sheet content smears directionally, then becomes sharp at rest. | Experimental opt-in only; keep content available immediately and disable blur under reduced motion. |
| 2026-09-22 · [Reply · Progressive blur Android](https://x.com/rit3zh/status/2102423256636735678) | ~11s | Android feed scrolls beneath a stable avatar/search header with the same localized material boundary. | Preserve fixed-chrome readability without promising identical rendering across devices. |
| 2026-09-22 · [Progressive blur](https://x.com/rit3zh/status/2102423249909146040) | ~8s | A fixed avatar/search header stays crisp as social photographs soften beneath its overlap boundary. | Give progressive blur one separation role and a solid high-contrast alternative. |
| 2026-09-19 · [Matched native popover transitions](https://x.com/rit3zh/status/2101309683378348340) | ~9s | An invoice-folder item remains recognizable as a rounded detail surface; the surrounding grid dims. | Match the selected object into readable detail. Visual inspiration credited to @proskuaaa. |
| 2026-09-18 · [Dynamic Island style in-app notifications](https://x.com/rit3zh/status/2100920008406864311) | ~11s | A contextual action resolves into a compact top notification and then a readable confirmation banner over the feed. | Tie feedback to the action without losing place; credits include @onyx__albert and @revmpstudio. |
| 2026-09-05 · [Reacticx V2 launch montage](https://x.com/rit3zh/status/2096016566290895031) | ~34s | Sampled launch-montage moments isolate lettering, arranged pill controls, and closing product typography. | Promotional montage: evaluate each component independently; it does not define one screen or palette. |
| 2026-08-10 · [Native content transitions](https://x.com/rit3zh/status/2086546601783484860) | ~15s | Large wallet balances update inside a stable dark summary while controls and the lighter asset list stay anchored. | Reserve value space and align changing numbers; visual inspiration credited to @Onimicee_Design. |
| 2026-07-28 · [Native blur views](https://x.com/rit3zh/status/2081988176131072354) | ~16s | Place photographs and editorial titles sit beneath crisp circular navigation controls and blurred overlapping chrome. | Let content supply personality; verify every material state and provide an opaque alternative. |
| 2026-07-27 · [Native iOS tab bar / segmented control](https://x.com/rit3zh/status/2081472010287558677) | ~11s | A floating bottom capsule changes between book browsing and editing controls while covers remain visible behind it. | Distinguish destination selection from edit mode, retain names, and respect safe areas. |
| Jul 12 2026 · [Morphing keyboard-aware composer + picker](https://x.com/rit3zh/status/2076236737232400711) | ~23s | Black ChatGPT-like screen; compact rounded input stays immediately above the keyboard. Later sampled state shows file tiles with round selection controls; the caption explicitly describes a morph between composer and picker. Samples include keyboard/composer and file-selection states. | Treat keyboard, composer, attachment menu, and selected attachment as one coordinated layout state. Preserve the input and selection while changing mode. |
| Jul 8 2026 · [Cover-flow carousel](https://x.com/rit3zh/status/2074827499243291106) | ~12s | Music player has frontal active artwork, angled neighboring covers, a reflected lower edge, and artwork-related blur behind conventional title/progress/transport controls. Different artwork is centered across samples. | Selected media gets one stable focal position; neighboring items communicate browse direction. Keep transport conventional and separate from decorative depth. |
| Jul 2 2026 · [Dynamic keyboard-aware tray](https://x.com/rit3zh/status/2072571729848029486) | ~13s | Dark social screen with a rounded utility tray over it; a later state contains a Boost Post form, region/payment rows, and white primary action. Tray contents and height change while the underlying post remains context. Caption explicitly says keyboard-aware. | Size trays to their content, coordinate their detents with editing, and keep the primary action reachable above keyboard/safe area. |
| Jun 25 2026 · [Stackable toasts](https://x.com/rit3zh/status/2070161176663830996) | ~20s | Dark task screen; a compact birthday notification appears over the list. Later sample shows several rounded feedback rows stacked, each with leading identity, title/detail, close, and sometimes Open action. | Notifications share a consistent anchor, limited stack depth, and clear dismissal/action hierarchy. New messages should not rearrange the task itself. |
| 2026-06-12 · [Reply · Vector icon liquid-lens examples](https://x.com/rit3zh/status/2065185006386049122) | ~16s | Opened directly after finding it in the parent thread. Two screenshot moments during playback show three rows on black: icon-only, label-only, icon+label; the active compact pill changes between Home/Browse/Saved. | Support the same selection primitive across icon/label configurations, but default mobile product navigation to visible labels. Lens effects and accents may be theme-specific; do not turn the red example into a global semantic selection color. |
| Jun 12 2026 · [Refractive liquid-lens pill switcher](https://x.com/rit3zh/status/2065185002682466744) | ~24s | Light browse screen with horizontal text categories above media cards. Different categories are active in the two samples; active emphasis stays compact rather than tinting the whole screen. Caption identifies refractive liquid lens and WebGPU. | Keep selection localized to the active item; use stable category labels and a clear selected state. Optional lens material follows the indicator only. |
| Jun 11 2026 · [Curved liquid-glass tab bar](https://x.com/rit3zh/status/2064804053008445678) | ~9s | Light image/list screens behind a floating curved translucent bottom bar with five icons; a bright capsule highlights one position as screen content changes. | Persistent navigation may float above content if safe areas and bottom content inset are explicit. The selected region must remain easy to locate. |
| Jun 9 2026 · [Avatar tooltip](https://x.com/rit3zh/status/2064288911065776592) | ~9s | Warm event screen, overlapping circular avatars, dark pill name tooltip above the active avatar. Across samples a different avatar enlarges slightly and receives the name pill. Large serif page heading is specific to this example. | A compact avatar cluster can reveal identity while maintaining group context; pair local emphasis with a readable name. |
| May 17 2026 · [Motion tabs](https://x.com/rit3zh/status/2055991350336934000) | ~6s | Dark audiobook screen; a compact bottom tab region expands into a translucent accessory panel with playback continuation and menu/list content. Samples show different panel content tied to the compact bottom origin. | A bottom accessory can carry contextual controls without losing current screen context. Give expansion a useful task, retain explicit selection. |
| May 2 2026 · [Toastiva morphing toasts](https://x.com/rit3zh/status/2050518196730597811) | ~10s | Light finance screen; small top-centered sending/status pill grows into a wider notification containing sentence-length information. Neutral white rounded feedback remains distinct from the dashboard behind it. | Update one feedback object's shape and content as its information grows; keep anchoring stable and reserve readable multiline space. |
| Apr 21 2026 · [iOS-inspired swipe actions](https://x.com/rit3zh/status/2046563570436260307) | ~11s | Light mail inbox, avatar/name/preview rows. One sample exposes blue Read on a leading swipe; another exposes trailing gray More, orange Flag, red Trash blocks with text and icons. | Gesture reveal should preserve row identity and expose clearly labeled contextual actions. Destructive and neutral actions have different semantic styles. |
| Apr 16 2026 · [iOS-inspired date picker](https://x.com/rit3zh/status/2044521474741178500) | ~13s | Dark rounded calendar popover over a form; month heading and directional controls. Later sample switches the same container to month/year wheels with an emphasized selected row. Android emulator controls appear in the recording. | Allow a nearby date field to expand into focused selection, with quick navigation across months/years and an unambiguous selected value. |
| Apr 7 2026 · [Smooth morphing toasts](https://x.com/rit3zh/status/2041278099195916367) | ~13s | Dark account screen; small top feedback labels join a larger white/light card, later expanding to a detail/action surface. Context remains visible beneath; top anchoring is stable across different sizes. | Status-to-detail expansion can preserve object continuity. Content determines the final size; the headline remains a stable anchor. |
| Feb 22 2026 · [Apple Intelligence visual component](https://x.com/rit3zh/status/2025622342844682466) | ~5s | Black fruit shopping screen. One sample shows multicolor screen-edge glow and a dark assistant prompt panel; another shows the ordinary compact input and product screen without the expanded panel. | Temporary assistant mode can be signaled locally and reversibly while preserving the task screen. Provide textual state and explicit entry/exit. |
| Feb 3 2026 · [Reacticx component montage](https://x.com/rit3zh/status/2018451865030344704) | ~17s | Sampled moments show a purple rounded project card on a black Projects screen and a multicolor assistant orb; a later frame is promotional title text. Multiple unrelated component demos are edited together. | Keep reusable foundations neutral and admit optional themed components. One montage can demonstrate breadth without defining a single product's palette. |
| Nov 23 2025 · [Morphing text](https://x.com/rit3zh/status/1992630188069601722) | ~10s | Minimal black screen with large centered serif word, progress/position indicator, and a paired previous/next capsule. Samples show Pure and Timeless with changed position values. | Decorative display-word changes can retain a stable baseline and navigation origin; reserve them for short, nonessential display content. |
| Nov 15 2025 · [Linear-inspired bottom tabs](https://x.com/rit3zh/status/1989659598299828675) | ~26s | Dark project/issue screens shown on iOS and Android emulators. A compact bottom icon bar expands upward into a labeled vertical destination menu; current menu row gets a neutral pill. | Use an anchored overflow destination menu when destinations exceed the sensible persistent tab count. Preserve selection and screen context. |
| Nov 9 2025 · [Apple Maps-style bottom sheet](https://x.com/rit3zh/status/1987428381986820198) | ~28s | Sampled collapsed search tray above map, full map state, and later device-list content with a compact bottom tab/accessory surface. Rounded dark sheet, small drag handle, and retained underlying map/device context. | Native sheets need meaningful detents, coordinated scrolling, retained context, explicit controls, and keyboard-aware search. |
| Oct 11 2025 · [Progressive blur header](https://x.com/rit3zh/status/1976908455777911011) | ~13s | Dark dashboard; compact Overview header stays legible while underlying large text/content becomes progressively blurred near the top. Later wide shot retains the same compact header over scrolled content. | Use progressive blur only at an overlapping system/navigation edge; keep current title and essential actions sharp, and provide an opaque header alternative. |
| 2 October 2025 · [Native iOS Popovers](https://x.com/rit3zh/status/1973824375255347635) | ~7s | dark travel app with bold left-aligned title, search field, compact destination controls and photography. A small rounded dark popover appears immediately above the originating destination control, with icon/title/detail content and a directional relationship to its anchor. | contextual detail should remain spatially attached to its trigger, size to content, and dismiss without changing the underlying task. Prefer native adaptive popovers, with a sheet fallback where space is insufficient. |
| 21 August 2025 · [Morphing SF Symbols](https://x.com/rit3zh/status/1958488197287006549) | ~14s | dark onboarding canvas, a centered white symbol inside a subdued circular enclosure, centered display title and short supporting copy, a progress line/step indicator, and a large white Continue button. Multiple samples showed the same stable layout during the symbol/title sequence. | maintain the symbol's visual center and container across related onboarding states; preserve the Continue/Skip affordances while content changes. Morph only related meanings. |
| 13 August 2025 · [SwiftUI Core Image Filters](https://x.com/rit3zh/status/1955627555811426527) | ~88s | native photo picker followed by a dark image editor. A large preview stays above the adjustment region. The active adjustment uses yellow, a horizontal slider updates the image, and a centered numerical overlay reports the active value (one sample showed saturation +48). | image manipulation should expose a live preview, a numerical value when useful, an obvious selected tool, and a reversible reset/confirm path. Keep editing controls in a consistent bottom zone. |
| 12 August 2025 · [Minimal Glass Morphing Transition](https://x.com/rit3zh/status/1955035908303962325) | ~25s | an explicitly WIP component showcase with translucent dark rounded panels over a textured surface. A central plus control expands into a horizontal group of colored action symbols, while the outer panel and section header remain recognizable. | preserve a common origin and enclosing geometry when revealing a compact action group. Use material changes to explain expansion, and keep a clear close path. |
| 9 August 2025 · [Native Progressive Blur](https://x.com/rit3zh/status/1954186364297093247) | ~12s | an App Store-like dark catalog with bold heading, search, rows containing icons/title/metadata, and blue capsule actions. Scrolling content softens gradually beneath persistent chrome and near the lower edge rather than meeting a hard blur boundary. | progressive blur can separate scrollable content from persistent controls while preserving continuity. Keep control labels crisp; apply blur to the content behind the chrome. |
| 8 August 2025 · [Stackable Bottom Sheets](https://x.com/rit3zh/status/1953814827639394726) | ~14s | dark project/task dashboard with compact statistics and action rows. A Projects sheet presents over the existing screen with a top drag handle/title/close control; a later sample shows another Options layer while previous task content remains visible behind it. | nested temporary tasks should retain context, expose a clear top layer, and return to the previous state on dismissal. Keep sheet headers and dismissal controls consistent. |
| 5 August 2025 · [Parallax Header](https://x.com/rit3zh/status/1952702271118098660) | ~11s | dark profile screen with a large illustrated cover, summary/metrics and Follow action. Samples showed both the expanded image-led header and a scrolled feed with a compact centered identity in persistent top chrome. | large profile imagery may compress into a compact identity as content scrolls; preserve the same person/title and maintain back/menu actions. Scrolling should reveal more usable content, not merely trigger decoration. |
| 4 August 2025 · [Native TipKit Popover](https://x.com/rit3zh/status/1952317517482868887) | ~10s | a dark utility home uses a small help trigger. Its rounded contextual tip contains a blue question icon, prominent Need Help? title, short guidance, a blue primary action, secondary support action, and a close control. A later sample shows the uncluttered home after the tip has gone. | teach one relevant capability in context, anchor the explanation to its source, and make it dismissible. Keep tips concise and suppress them once dismissed or completed. |
| 2 August 2025 · [Animated Toast](https://x.com/rit3zh/status/1951606651934343179) | ~13s | dark task screen with status chips and task cards. A compact rounded toast sits above the bottom safe area, with a green status icon, title, short supporting text and an Undo action. Multiple samples retained the underlying task and showed its completed state. | feedback should acknowledge the operation without replacing the screen; align icon, copy, and optional recovery action. Put the toast above bottom navigation and keyboard obstruction. |
| 1 August 2025 · [Reply · Refined Liquid Glass Aquarium](https://x.com/rit3zh/status/1951205220991807523) | ~17s | An aquarium orb carries the scene’s richness; glass is limited to a small statistics strip and three circular controls. | Selective material is stronger than all-screen glass; the author offers this as a refined follow-up. |
| 1 August 2025 · [Floating Action Menu](https://x.com/rit3zh/status/1951024643302891536) | ~25s | a dark finance screen uses a circular floating trigger. When expanded, a small vertical group of actions (including Add Money and Filter) appears while the underlying screen becomes blurred. A later sample shows the menu closed and the full finance layout restored. | keep a floating action menu close to its origin, group only related actions, and visually separate the active layer while preserving underlying context. Restore focus to the trigger when dismissed. |
| 31 July 2025 · [Native Liquid Glass](https://x.com/rit3zh/status/1950929182449447092) | ~22s | glass-effect showcase using a finance dashboard over highly animated red and later silver/black imagery. Transparent panels and cards inherit substantial background color/distortion. Text remains in a familiar dashboard arrangement while the surrounding material changes. | glass can communicate a layer's connection to imagery, but meaningful data requires a reliable contrast layer. The source of motion should not overwhelm reading. |
| 29 July 2025 · [Early Metaball/Island Animation](https://x.com/rit3zh/status/1950228775649890535) | ~14s | light account/settings interface with grouped white rows, subdued iconography and blue native toggles. A circular profile/avatar element visually joins the top island area as the screen scrolls; a later compact state keeps the person's identity in the header. | a collapsed header should preserve the identity of its expanded state. Use shape continuity to connect the two rather than removing/recreating unrelated elements. |
| 28 July 2025 · [Native Mesh Gradient](https://x.com/rit3zh/status/1949849412944957509) | ~61s | a gradient customization demo uses a saturated green/teal/yellow mesh inside the device, white title, and grouped controls including animation speed and blur sliders. | a mesh background is a deliberate expressive surface for a focused experience or preview. Expose adjustment values and keep control positions stable. |
| 27 July 2025 · [Native Animated Text View](https://x.com/rit3zh/status/1949425572485947829) | ~26s | sparse dark canvas with a short centered white phrase. Samples show glyphs partly blurred/displaced and a later more readable phrase while the Pause and Next Animation controls remain stable below. The caption lists typing, blur, drop and twist variants. | reserve expressive glyph animation for short display or optional status text; preserve the text's baseline/center and never move the operational controls with it. Permit pause/skip where animation is sustained. |
| 25 July 2025 · [SwiftUI-Native Popover Code Demo](https://x.com/rit3zh/status/1948767376058843410) | ~33s | Code/bridge demonstration with sparse device preview; sampled frames provide limited popover-anatomy evidence. | Use stronger popover recordings for visual guidance. Victor Mono mentioned in the thread is an editor font. |
| 23 July 2025 · [Glow UI OTP Input](https://x.com/rit3zh/status/1947947674197807278) | ~15s | dark centered verification panel, a small identity/shield cue, title and helper copy, four evenly spaced digit cells, inline verifying indicator, Resend and Clear actions, and numeric keyboard. | make the OTP feel like one input with clear progress, support paste/autofill and backspace, retain context during verification, and expose resend/recovery. Use color plus text/icon for validation. |
| 18 July 2025 · [iOS Sonic Player](https://x.com/rit3zh/status/1946192174036476150) | ~144s | Dark player separates track/artwork, elapsed/remaining scrubber, central transport, and Player/EQ/Effects/Presets sections. | Keep transport stable, settings grouped, current values readable, and platform playback integration conventional. |
| 11 July 2025 · [Audio Filters and EQ WIP](https://x.com/rit3zh/status/1943668327131267455) | ~98s | A dark WIP player keeps track context and transport above grouped audio effects and adjustment controls. | Separate current playback from configuration; expose understandable selected values and reset behavior. |
| 29 June 2025 · [Custom Spotify Player](https://x.com/rit3zh/status/1939248633372946661) | ~26s | A full artwork player collapses into a bottom mini-player retaining thumbnail, track identity, and transport. | Preserve track, playback position, and fixed play/pause targets across compact/expanded modes. |
| 2025-06-20 · [Reply · Glow UI mixed-gallery promotional video](https://x.com/rit3zh/status/1935987210559410240) | ~8s | Dark library launch montage frames three phone previews—music player, profile/content and search/settings—with curved promotional lettering and changing screen imagery. The post also contains one image sibling. | Limited foundation evidence: use real content and clear type hierarchy to distinguish related screens while keeping ordinary controls recognizable. |

### Credits retained from the portfolio

The posts themselves cite multiple design references. Meld draws on the recurring interaction ideas and is not presented as a proprietary visual invention of one author.

| Pattern | Attribution / reference |
|---|---|
| Keyboard-aware composer | [ChatGPT inspiration stated in the post](https://x.com/rit3zh/status/2076236737232400711) |
| Curved glass navigation | [Creator’s Kann attribution](https://x.com/rit3zh/status/2064804136143724831) and [Kann reference](https://60fps.design/apps/kann) |
| Toastiva layout | [Creator’s Sileo / hiaaryan attribution](https://x.com/rit3zh/status/2050591865586803008) |
| Bottom navigation and map sheet | [Linear-inspired tabs](https://x.com/rit3zh/status/1989659598299828675), [Apple Maps-style sheet](https://x.com/rit3zh/status/1987428381986820198) |
| Matched invoice detail | [Post/thread crediting @proskuaaa](https://x.com/rit3zh/status/2101309683378348340) |
| In-app island notifications | [Post/thread crediting @onyx__albert and @revmpstudio](https://x.com/rit3zh/status/2100920008406864311) |
| Native changing-value demo | [Post/thread crediting @Onimicee_Design](https://x.com/rit3zh/status/2086546601783484860) |


### Checked token pairs

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

### Exact source anchors

These values are evidence, not additional implementation defaults. Live `main` links may change after the review date.

| Source | Source-exact evidence | How Meld uses it |
|---|---|---|
| [Streaming primitive scale](https://github.com/rit3zh/expo-animated-streaming-text/blob/main/src/constants/radix.const.ts) | Space4/8/12/16/24/32/40/48/64; radii3/4/6/8/12/16/full; font sizes12/14/16/18/20/24/28/35/60 | Uses the space scale and a smaller semantic type/radius set; body17 and sheet28 are deliberate adaptations |
| [Streaming colors and timing](https://github.com/rit3zh/expo-animated-streaming-text/blob/main/src/constants/components/streaming-text.const.ts) | Light text#1D1D1F, muted#6E6E73, code#F6F6F8; trail#8E7FD6→#8E8E93; fade1500ms, trail2000ms, follow200ms | Anchors neutral palette; reserves arrival trail for streaming rather than permanent text |
| [Streaming theme primitives](https://github.com/rit3zh/expo-animated-streaming-text/blob/main/src/constants/radix.const.ts) | Dark#000000/#0A0A0A/#131313, text#F5F5F5/#B4B4B4; violet#6E56CF/#BAA7FF | Anchors light/dark neutral and violet roles; adds tested pressed/status/border pairs |
| [Profile layout](https://github.com/rit3zh/expo-scroll-metaball/blob/main/src/constants/layout.const.ts) and [screen](https://github.com/rit3zh/expo-scroll-metaball/blob/main/src/constants/components/metaball-screen.const.ts) | Avatar120, gap16/24, skeleton gutter20, shelf gap12; spring260/30/1; calm fade180ms | Preserves scroll-linked identity and spacing rhythm; does not standardize cutout dimensions |
| [Glass carousel](https://github.com/rit3zh/expo-glass-carousel/blob/main/src/constants/components/glass-carousel.const.ts) | Card height450, aspect3:4, gap12, radius10, backdrop blur26, focus700–900ms, lens fade850ms | Treats geometry/timing as a showcase recipe; uses adaptive sizing and shorter ordinary transitions |
| [Carousel behavior](https://github.com/rit3zh/expo-glass-carousel/blob/main/README.md) | Swipe/flick, side tap centers, center tap focuses, second tap closes; next/previous/focus/close accessibility actions; reduced motion; static-child snapshot assumptions | Carries direct manipulation and explicit action alternatives into the recipe |
| [Siri state machine](https://github.com/rit3zh/expo-siri-ai-animations/blob/main/README.md) | Idle/listening/thinking/searching/reasoning/answer; demo phase durations4200/2400/2600/3200/5500ms; island module iOS16.4+ | Uses real operation states and platform fallbacks; never copies simulated phase delays |
| [Siri springs](https://github.com/rit3zh/expo-siri-ai-animations/blob/main/modules/expo-siri-island/src/constants/island-spring.constant.ts) | Pop220/21/1, orb220/28/1, settle420/40/1, stretch160/16/1, grow190/22/1, dismiss300/33/1 | Keeps component-specific expressive settings separate from standard motion |
| [Interaction index](https://github.com/rit3zh/interactions/blob/main/src/components/ui/example-list/constants.ts) | Eight demos: paper crumple, shine card, stretch carousel, step player, reveal to copy, status badge, glow slider, delete button | Supplies optional tactile patterns; does not require applying every effect |

Spring triples above mean stiffness/damping/mass in their source model. The glass carousel's separate custom `damping:0.92` is not a Reanimated `withSpring` damping coefficient. Do not copy it into a different physics API.

### The eight-demo interaction collection

| Demo and source | Source-exact details | Production adaptation |
|---|---|---|
| [Paper crumple](https://github.com/rit3zh/interactions/blob/main/src/components/paper-crumple/constants.ts) | Hold/crumple/drag; restores on release; springs120/20/1 and150/24/1; tilt10° | Optional tactile media object; never the only delete route |
| [Shine card](https://github.com/rit3zh/interactions/blob/main/src/components/shine-card/constants.ts) | Radius28, tilt8°, press scale0.98, glare0.35 | Subtle local object feedback with a stationary readable/accessible representation |
| [Stretch carousel](https://github.com/rit3zh/interactions/blob/main/src/components/stretch-carousel/constants.ts) | Width0.62×available, radius32, gap16, spring180/22/0.9 | A media variant with direct selection and low-motion paging |
| [Step player](https://github.com/rit3zh/interactions/blob/main/src/components/step-player/constants.ts) | Dot8, bar36, gap8, move520ms, stagger55ms | Expose pause and direct step selection; do not force waiting |
| [Reveal to copy](https://github.com/rit3zh/interactions/blob/main/src/components/reveal-to-copy/constants.ts) | Height52, visual button36/ring44, type17, reveal5000ms, copied hold500ms | Enlarge targets to48; preserve real value and conventional Copy action |
| [Status badge](https://github.com/rit3zh/interactions/blob/main/src/components/status-badge/constants.ts) | Height36, radius14, padding14, icon18, type16/22; label280/tint320/glyph220ms | Standardize compact semantic badge; replace weak pastel text with readable status pairs |
| [Glow slider](https://github.com/rit3zh/interactions/blob/main/src/components/glow-slider/constants.ts) | Height44, inset5, tint#8C72E0; follow520/26/0.5, snap240/18/0.7 | Keep value/track stable, use target48, expose increment/decrement |
| [Delete button](https://github.com/rit3zh/interactions/blob/main/src/components/delete-button/constants.ts) | Pill54/button48/radius40; unfolds to confirmation; hold1400ms; min pending1100ms/done hold2200ms | Prefer consequence-based confirmation or undo; do not import artificial waiting |

### Provenance boundary

Video observations establish visible patterns; source reads establish implemented constants and documented behavior. They do not prove exact screenshot font metrics, universal creator intent, accessibility conformance, or current package support. Meld's production rules and tokens are independent design decisions made for consistent reuse.

The linked code files were read from each repository's default `main` branch on the review date. This document does not copy the source implementations or redistribute the creator's images, music, logos, or videos. If importing an implementation later, check that repository's current license and platform requirements.
