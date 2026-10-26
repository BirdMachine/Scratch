# 🦜 Living README Laboratory

Three experiments in making a **GitHub README feel like an animated application** without script tags, injected CSS or iframes.

[🏠 Main Scratch README](../../README.md) · [💎 Glass](#01-holographic-glass) · [🐟 Terrarium](#02-a-little-living-terrarium) · [🖥️ Desktop](#03-a-readme-disguised-as-a-desktop)

> [!IMPORTANT]
> These visuals are **SVG/SMIL render experiments**. Browser, GitHub image proxy and reduced-motion settings can change animation behavior. The aquarium is animated but **not yet a persistent GitHub Issues-controlled game**. The desktop is a visual metaphor with *real Markdown links* underneath.

## 01 · Holographic glass

<p align="center">
  <img src="./assets/holographic-glass.svg" width="960" alt="Shimmering holographic crystal over a gridded purple and cyan background">
</p>

A GitHub-friendly approach to a floating refractive-looking prism: translucent polygon faces, chromatic gradient strokes, background glow, overlapping waves and self-contained SVG animation.

<details>
<summary>💎 Open the prism's instrument panel</summary>

| Material | Technique | Notes |
|---|---|---|
| Faceted glass | SVG paths + opacity | Simulated refraction; *not* physical refraction |
| Chromatic edge | Multistop gradient | Pink → cyan → violet |
| Floating motion | SMIL `animateTransform` | Fallback is static |
| Haze | Gaussian blur + radial gradient | Small blur region for performance |
| Scope | Image only | Does not restyle GitHub's page |

[Inspect the prism SVG](./assets/holographic-glass.svg)

</details>

## 02 · A little living terrarium

<p align="center">
  <img src="./assets/readme-terrarium.svg" width="960" alt="Cute betta fish swimming among sea plants with drifting bubbles">
</p>

Our aquarium lives entirely inside one SVG. The betta glides, its tail deforms, and bubbles rise. This is **visual phase one**: no external API, Action, or write permission required.

<details>
<summary>🐟 Open the fishkeeper's notebook</summary>

**Future optional phase**: a GitHub Issue Form could accept `feed`, `decorate`, or `lights` commands; an Action could validate the command, update a JSON habitat state and regenerate an SVG. Avoid triggering workflows from untrusted issue text without validation and minimal permissions.

**Today:** This version is a looping animation, not an interactable pet.

[Inspect the terrarium SVG](./assets/readme-terrarium.svg)

</details>

## 03 · A README disguised as a desktop

<p align="center">
  <img src="./assets/birdmachine-desktop.svg" width="960" alt="Faux holographic operating system with project explorer, system monitor and terminal">
</p>

This is a mock OS shell made from SVG. For **actual clicks**, use Markdown links and GitHub-native `details` immediately below the visual: GitHub strips arbitrary JavaScript and most styling.

| ◈ Dock | Launch |
|:---|:---|
| 💎 Prism | [Open the glass module](#01-holographic-glass) |
| 🐟 Habitat | [Open the aquarium module](#02-a-little-living-terrarium) |
| 🧪 Scratch | [Return to the original laboratory](../../README.md) |

<details>
<summary>🗔 TERMINAL.EXE · click to open</summary>

```text
bird@machine:~$ cat /etc/motd
WELCOME TO BIRDMACHINE OS
  renderer: GitHub-flavored Markdown
  animations: SVG / SMIL (viewer-dependent)
  executable JS in README: denied
  practical weirdness: unlimited
bird@machine:~$ _
```

</details>

<details>
<summary>🗔 SYSTEM SETTINGS · click to open</summary>

- **Theme:** cyber-glass, raspberry plasma, aqueous cyan
- **Surface:** simulated transparency within the image, not through GitHub UI
- **Controls:** native links and disclosure widgets
- **Accessibility:** captions and alt text; motion-sensitive users can open static content or use browser motion preferences

</details>

---

### Experimental checklist

- [x] Three authored standalone SVG specimens
- [x] Animated primitive shapes with static fallback
- [x] A GitHub-native navigation / disclosure layer
- [ ] Verify SVG animations against GitHub's live README image rendering
- [ ] Explore dark/light-specific `picture` variants
- [ ] Optionally add a controlled GitHub Actions-backed habitat

> [!TIP]
> A README cannot host an arbitrary web app. If we eventually want drag-and-drop windows, live sliders and physically accurate shaders, put that component on **GitHub Pages** and embed a still/animated preview with a link to launch the experience.
