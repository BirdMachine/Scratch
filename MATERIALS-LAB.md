# 🧪 ADVANCED MATERIALS / RENDERING LAB

<p align="center"><sub>SVG is not merely vector drawing. SVG is a tiny procedural compositor we can sneak into a README.</sub></p>

The interesting step beyond gradients + drop shadows is to fake **material response**: refraction, surface roughness, chromatic dispersion, anisotropic-ish highlights, procedural wrinkles, specular lighting, translucent volume, and optical depth.

---

## 01 — Prismatic / Refractive Glass

<p align="center"><img src="./assets/materials/prismatic-glass.svg" width="100%" alt="Prismatic glass material experiment"></p>

This one uses `feTurbulence` as a synthetic irregular surface, then `feDisplacementMap` to distort the colored scene beneath the pane. A second filter offsets color channels around highlights to fake **chromatic aberration / dispersion**.

It is not physically correct refraction—SVG filters do not give us a real ray tracer—but perceptually it moves beyond “transparent rectangle with blur.” The pane appears to have an *optically imperfect thickness*.

**Probe:** whether GitHub's SVG rendering path preserves the full filter chain consistently on desktop/mobile.

---

## 02 — Iridescent / Anodized Metal

<p align="center"><img src="./assets/materials/iridescent-metal.svg" width="100%" alt="Iridescent anodized metal material experiment"></p>

Here the trick is a deliberately nonlinear spectral gradient plus broad dark/light bands and procedural high-frequency noise blended over the surface. The gradient implies thin-film color shift; the highlight bands imply a curved polished object; noise breaks the mathematically perfect vector surface enough to suggest a manufactured finish.

The useful lesson: **material identity comes from several spatial frequencies at once.** Large gradients establish form, medium highlights establish gloss, tiny noise establishes surface.

---

## 03 — Holographic Foil

<p align="center"><img src="./assets/materials/holographic-foil.svg" width="100%" alt="Holographic foil material experiment"></p>

This one gets considerably sillier. A rainbow substrate is distorted by procedural turbulence; then `feSpecularLighting` treats the turbulence map approximately like surface relief. A fine diagonal pattern supplies the microstructure cue our brains associate with diffraction film.

So: **procedural bump map + fake illumination + spectral palette + micro-lines = surprisingly foil-ish rectangle.**

If `feSpecularLighting` survives GitHub reliably, that opens a whole family of embossed plastic, hammered metal, satin, pearl, wet surfaces and molded UI chrome.

---

## 04 — Soft Gel / Liquid UI

<p align="center"><img src="./assets/materials/gel-bubble.svg" width="100%" alt="Translucent gel bubble material experiment"></p>

The shape itself is intentionally imperfect and then displaced again with turbulence. A radial translucent fill suggests volume; a broad internal highlight suggests a curved interface; the cast shadow grounds it away from the page.

This is the **Frutiger Aero candy-object direction**: controls that look less like rectangles and more like things you could poke. 🫧

---

## 05 — Rendering Stack / Mental Model

Instead of “draw a pretty SVG,” treat each asset like a miniature material shader assembled from 2D operations:

```text
SILHOUETTE / FORM
       ↓
BASE ALBEDO / SPECTRAL COLOR
       ↓
MACRO LIGHTING GRADIENT
       ↓
SURFACE NORMAL FAKE (turbulence / displacement)
       ↓
SPECULAR RESPONSE
       ↓
MICROTEXTURE / GRAIN
       ↓
EDGE / FRESNEL-ISH HIGHLIGHT
       ↓
CAST SHADOW + ENVIRONMENT CUES
       ↓
THE HUMAN VISUAL SYSTEM DOES THE REST
```

That is the avenue I want to push: **shader thinking without shaders.**

---

## 06 — Particularly Juicy Next Materials

| Material | SVG fakery to try |
|---|---|
| frosted glass | displacement + noisy opacity + edge clarity |
| dichroic glass | angle-implied spectral rims + layered transparency |
| mother-of-pearl | low-frequency turbulence + pastel spectral interference |
| opal | cloudy volume + embedded spectral fire flecks |
| brushed aluminum | directional procedural grain + long specular streak |
| machined CD metal | radial micro-grooves + rainbow interference |
| satin | directional soft highlight + fibrous noise |
| velvet | edge-bright / center-dark grazing-light illusion |
| wet acrylic | hard specular + internal color + contact shadow |
| translucent resin | cloudy depth + embedded inclusions / bubbles |
| mercury glass | mirrored dark/light patches + mottled backing |
| soap bubble | almost-transparent body + spectral edge film |
| pearlescent car paint | metallic base + broad color-shift highlight |
| CRT glass | curved highlight + scanline phosphor layer + vignette |
| water | displacement/refraction + caustic-ish procedural highlights |

---

## 07 — Important Constraint That Is Actually Fun

None of these materials need to be *physically* correct. They need to survive GitHub's image pipeline and produce the right perceptual read at README scale.

That turns the restriction into an aesthetic: tiny fake material shaders, frozen into portable SVG objects, living inside a Markdown document.

> **We are not rendering reality. We are rendering enough evidence that the brain volunteers to render reality for us.**

[← return to the Non-Euclidean Glasshouse](./NON-EUCLIDEAN-GEOCITIES.md)
