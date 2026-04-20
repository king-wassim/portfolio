# Design System Specification: The Kinetic Engineer

## 1. Overview & Creative North Star
**Creative North Star: "The Digital Blueprint"**
This design system moves away from the static, template-driven nature of traditional portfolios. Instead, it treats the browser as a high-precision drafting table. By blending the technical rigor of engineering with the sophisticated editorial layout of a high-end journal, we create an environment that feels both industrial and premium.

The system breaks the "standard grid" through **intentional asymmetry**. We utilize heavy horizontal padding and offset typography to lead the eye through a narrative of technical expertise. It is not just a list of projects; it is a curated exhibition of problem-solving.

---

## 2. Colors & Tonal Depth
The palette is rooted in a deep, nocturnal foundation, using vibrant accents to represent "live" data or active systems.

### The "No-Line" Rule
Traditional 1px borders are strictly prohibited for sectioning. Structural boundaries must be defined solely through background shifts using the `surface-container` tiers or subtle tonal transitions. This creates a more sophisticated, "machined" look where components feel carved out of the interface rather than pasted onto it.

### Surface Hierarchy & Nesting
To create depth without shadows, we utilize a "Nested Surface" logic:
*   **Base Layer:** `surface` (#00142b) – The primary canvas.
*   **Sectioning:** `surface-container-low` (#001c3a) – Large layout blocks (e.g., Project details).
*   **Component Level:** `surface-container-high` (#0e2b4b) – The most prominent interactive elements.

### Glass & Texture
*   **The Glass Rule:** For navigation bars or floating action menus, use `surface-container` colors at 70% opacity with a `20px` backdrop-blur. This allows the high-tech blue background to "bleed" through, creating an integrated, liquid feel.
*   **Signature Gradients:** For primary CTAs and hero headlines, use a subtle linear gradient: `primary-container` (#0074d9) to `primary` (#a7c8ff). This mimics the glow of a high-resolution display.

---

## 3. Typography
We use a high-contrast scale to differentiate between "Technical Metadata" and "Narrative Headlines."

*   **Display & Headline (Space Grotesk):** This is our "Drafting" font. Its geometric, slightly wide proportions suggest precision engineering. Use `display-lg` for project titles to create an authoritative, editorial impact.
*   **Body & Label (Inter):** Our "Functional" font. Inter provides maximum readability for technical documentation and project descriptions. 
*   **The Hierarchy Intent:** Use `label-md` in `tertiary` (#3ce368) for all technical tags (e.g., "Python," "CAD," "AWS"). This color-coding immediately signals "Active Skills" to the viewer.

---

## 4. Elevation & Depth
In this system, elevation is a product of light and layering, not heavy dropshadows.

*   **Tonal Layering:** Achieve "lift" by stacking. A `surface-container-highest` card placed on a `surface-container-low` background creates a natural, sharp elevation change.
*   **Ambient Shadows:** If a floating effect is required (e.g., a hovered project card), use a tinted shadow: `0px 20px 40px rgba(0, 31, 63, 0.4)`. The shadow must be the color of the background, never pure black.
*   **The Ghost Border:** For accessibility on interactive inputs, use `outline-variant` at 20% opacity. It should be felt, not seen.

---

## 5. Components

### Buttons
*   **Primary:** Solid `primary-container`. No border. `xl` (0.75rem) roundedness. On hover, transition to `primary` with a subtle glow.
*   **Secondary:** Ghost style. No background, `outline` at 30% opacity. Text in `primary`.
*   **Tertiary (The "Action Link"):** Underlined with a 2px `tertiary` (#3ce368) stroke that expands on hover.

### Project Cards
*   **Structure:** No dividers. Use `16` (4rem) vertical spacing to separate the image from the description.
*   **Background:** Use `surface-container-low`. 
*   **Interaction:** On hover, the card should scale by 1.02x and the background should shift to `surface-container-high`.

### Skills Chips
*   **Visual:** `surface-container-highest` background, `label-md` typography.
*   **Accent:** Use a `1x1` dot of `tertiary` (#3ce368) next to the text to signify a "Status: Active" engineering aesthetic.

### Input Fields
*   **Style:** Underline-only or subtle `surface-container-lowest` fill. Forbid the "box" look. Labels should be `label-sm` and permanently visible above the input to maintain a "form/schematic" feel.

---

## 6. Do’s and Don’ts

### Do:
*   **Embrace Negative Space:** Use the `20` (5rem) and `24` (6rem) spacing tokens between major sections. Engineering is about clarity; the layout should reflect that.
*   **Use Asymmetric Grids:** Align your text to a 12-column grid, but leave the first 2 columns empty for "Display" headings to create an editorial look.
*   **Animate Transitions:** Use `cubic-bezier(0.2, 0, 0, 1)` for all hover states—it feels "mechanical" and precise.

### Don’t:
*   **Don't use 1px Solid Lines:** Never use a high-contrast line to separate content. Use a background shift or white space.
*   **Don't use Standard Grays:** Every "gray" in this system must be tinted with blue (`#8b919e`). Pure gray feels "dead"; tinted blue feels "technological."
*   **Don't Over-round:** Stick to `md` (0.375rem) or `lg` (0.5rem) for most components. `full` roundedness should be reserved exclusively for pills/chips. Excessive rounding loses the "engineering" edge.