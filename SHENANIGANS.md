# 🦜 README SHENANIGANS LAB

<p align="center"><img src="./assets/myspace-terminal.svg" width="100%" alt="Neon personal-web-page styled README banner"></p>

> This page is a specimen jar for **image-map-era instincts applied to GitHub Markdown**. Some tricks are robust. Some are goblin engineering. That is the point.

## 01 — The README Is The Image

The first cheat is gloriously simple: stop asking Markdown to lay things out. Make a giant SVG *be* the layout.

<p align="center"><img src="./assets/fake-window.svg" width="760" alt="Fake retro application window rendered as SVG"></p>

SVG gives us typography, gradients, fake chrome, overlapping objects, arbitrary positioning, scanlines, diagrams, fake interfaces, ornamental borders, etc. GitHub only has to place one rectangle.

---

## 02 — Fake 2004 Microbutton Shrine

<p align="center">
<a href="#03--table-layout-is-not-dead-it-was-merely-sleeping"><img src="./assets/micro-button.svg" width="132" alt="Bird Web button"></a>
<a href="./README.md"><img src="./assets/micro-button.svg" width="105" alt="Bird Web button"></a>
<a href="#06--collapsible-secret-level"><img src="./assets/micro-button.svg" width="158" alt="Bird Web button"></a>
<a href="./assets/myspace-terminal.svg"><img src="./assets/micro-button.svg" width="88" alt="Bird Web button"></a>
</p>

Same asset, intentionally inconsistent widths. Instant janky-web mosaic. Each image can independently be a link, so a row of ornamental graphics can secretly be navigation.

---

## 03 — Table Layout Is Not Dead, It Was Merely Sleeping

<table><tr>
<td width="38%" align="center"><img src="./assets/micro-button.svg" width="140"><br><b>LEFT SHRINE</b><br><sub>tiny little web artifact</sub></td>
<td width="62%"><img src="./assets/fake-window.svg" width="100%"><br><code>&lt;td&gt;</code> has entered its second life.</td>
</tr></table>

Nested-ish visual composition via HTML tables is extremely MySpace. GitHub controls plenty of the styling, but images do the visual heavy lifting.

---

## 04 — Fake UI Controls That Are Actually Links

<a href="./README.md"><img src="https://img.shields.io/badge/%E2%97%80_BACK-README-ff3fb4?style=for-the-badge" alt="Back to README"></a>
<a href="./assets/fake-window.svg"><img src="https://img.shields.io/badge/OPEN-WINDOW.EXE-54f7e8?style=for-the-badge" alt="Open window SVG"></a>
<a href="#top"><img src="https://img.shields.io/badge/%E2%86%91-ESCAPE-fff45c?style=for-the-badge" alt="Back to top"></a>

Buttons aren't buttons. Windows aren't windows. The README is a stage set. 😌

---

## 05 — Theme-Sensitive Parallel Universes

GitHub supports `<picture>`, so the same location can swap art according to light/dark preference.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/myspace-terminal.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/fake-window.svg">
  <img src="./assets/myspace-terminal.svg" width="100%" alt="Theme-sensitive experimental banner">
</picture>

This can go way beyond palette swapping: light mode can show one entire composition and dark mode another.

---

## 06 — Collapsible Secret Level

<details>
<summary><b>🗝️ OPEN THE SUSPICIOUS DOOR</b></summary>

<br>

<p align="center"><img src="./assets/myspace-terminal.svg" width="88%" alt="Secret neon terminal"></p>

<table><tr><td>

### YOU FOUND THE UNDER-README

`README.md` can have optional rooms. Put huge art, lore, debug info, screenshots, joke endings, or alternate interfaces behind `<details>`.

</td><td align="center">

<img src="./assets/micro-button.svg" width="150">

**+37 BIRD**

</td></tr></table>

</details>

---

## 07 — Faux Full-Bleed / Cropped Panorama

<p align="center"><img src="./assets/myspace-terminal.svg" width="9999" alt="Oversized neon banner"></p>

The browser/GitHub container still wins, but deliberately absurd dimensions are worth probing across desktop/mobile. Width handling, intrinsic SVG dimensions, tables, and image scaling occasionally create wonderfully cursed edge cases.

---

## 08 — README Dollhouse

<table>
<tr><td colspan="3" align="center"><img src="./assets/myspace-terminal.svg" width="100%"></td></tr>
<tr>
<td align="center"><img src="./assets/micro-button.svg" width="100"><br>ATTIC</td>
<td rowspan="2" align="center"><img src="./assets/fake-window.svg" width="420"><br><b>MAIN CHAMBER</b></td>
<td align="center"><img src="./assets/micro-button.svg" width="100"><br>TURRET</td>
</tr>
<tr><td align="center">🦜<br><sub>bird room</sub></td><td align="center">✨<br><sub>forbidden glitter</sub></td></tr>
</table>

A README doesn't need to look like a document. It can look like a little illustrated object with Markdown hiding between the floorboards.

---

## 09 — Invisible Structure / Visible Art

<!--
THIS COMMENT IS PART OF THE PIECE.
SOURCE-VIEW EXPLORERS GET A SECOND LAYER.

         .-.
        (o o)  YOU LOOKED BEHIND THE WALL
        | O \
         \   \
          `~~~'

Idea: make rendered README and source README tell different jokes.
-->

The rendered view can be the glossy facade; comments make the raw source a second easter-egg surface. **Two audiences, one file.**

---

## 10 — The Image-Map Ghost

Actual HTML `<map>/<area>` support is not something I'd build a README around, so the reliable GitHub-ish descendant is: **slice one composition into several adjacent linked images**. Each slice gets its own destination, visually pretending to be one interactive illustration.

<table><tr>
<td><a href="./README.md"><img src="./assets/micro-button.svg" width="176"></a></td>
<td><a href="./assets/myspace-terminal.svg"><img src="./assets/micro-button.svg" width="176"></a></td>
<td><a href="./assets/fake-window.svg"><img src="./assets/micro-button.svg" width="176"></a></td>
</tr></table>

Next mutation: draw a single 900px scene, export 3–5 perfectly matching SVG slices, then make the slices separate links. **Image map by dismemberment.** 💖

---

## 11 — Deliberately Broken Reality

| NORMAL | WRONG | WORSE |
|:--:|:--:|:--:|
| <img src="./assets/micro-button.svg" width="176"> | <img src="./assets/micro-button.svg" width="90"> | <img src="./assets/micro-button.svg" width="260"> |
| one asset | same asset | still same asset |

Repeated assets at incompatible scales feel like browser corruption without requiring animation or scripting. Mix that with abrupt alignment changes, giant transparent margins inside SVGs, fake clipping, duplicated UI, and deliberately misregistered layers.

---

## 12 — Things To Probe Next

- sliced panoramic SVG navigation / pseudo image-map
- transparent SVG overlays simulated by separate stacked-looking rows
- fake browser scrollbar / fake GitHub UI that bleeds into README content
- SVG spritesheet fragments using `viewBox` variants
- SVG text laid out like magazine typography
- faux desktop with clickable icon-images beneath it
- README choose-your-own-adventure using anchors + `<details>`
- optical illusions that exploit GitHub light/dark backgrounds
- enormous transparent padding to create impossible-looking whitespace
- SVG-as-infographic where the *documentation itself* is illustrated
- intentional raster + SVG mismatch for crunchy 2000s compositing

<p align="center"><img src="./assets/rainbow-divider.svg" width="100%" alt="Rainbow divider"></p>

<p align="center"><b>THE WEB WAS NEVER SUPPOSED TO BECOME THIS TIDY.</b><br><sub>we can put a little 2006 back in it. as a treat.</sub></p>
