# 🧪 ADVANCED MATERIALS / RENDERING LAB

<p align="center"><sub>SVG is not merely vector drawing. SVG is a tiny procedural compositor we can sneak into a README.</sub></p>

The interesting step beyond gradients + drop shadows is to fake **material response**: refraction, surface roughness, chromatic dispersion, anisotropic-ish highlights, procedural wrinkles, specular lighting, translucent volume, optical depth, fibers, films, inclusions and interference.

## SHELF I — Optical Plastics, Metals & Gel

### 01 — Prismatic / Refractive Glass
<p align="center"><img src="./assets/materials/prismatic-glass.svg" width="100%"></p>
`feTurbulence` becomes a synthetic irregular surface; `feDisplacementMap` distorts the scene beneath it; offset color channels imply chromatic dispersion. Not a ray tracer—just enough evidence for the eye to infer optically imperfect thickness.

### 02 — Iridescent / Anodized Metal
<p align="center"><img src="./assets/materials/iridescent-metal.svg" width="100%"></p>
Nonlinear spectral bands imply thin-film color shift; macro highlights imply curvature; high-frequency noise implies manufactured surface. **Material identity happens at several spatial frequencies simultaneously.**

### 03 — Holographic Foil
<p align="center"><img src="./assets/materials/holographic-foil.svg" width="100%"></p>
Procedural wrinkles feed `feSpecularLighting`; a spectral substrate and diagonal microstructure sell diffraction-film behavior.

### 04 — Soft Gel / Liquid UI
<p align="center"><img src="./assets/materials/gel-bubble.svg" width="100%"></p>
Displaced silhouette + translucent radial volume + internal reflection + contact shadow. Frutiger Aero candy-object territory. 🫧

---

# SHELF II — THE MATERIALS CABINET HAS ESCAPED CONTAINMENT

### 05 — Dichroic Glass + Opal Fire
<p align="center"><img src="./assets/materials/dichroic-opal.svg" width="100%"></p>
The dichroic pane treats spectral color as an angle cue: a hard-edged transparent-ish slab whose color changes aggressively across its face. Beside it, the opal uses cloudy procedural structure with tiny saturated inclusions acting as **spectral fire**. One says *coated optical material*; the other says *light trapped inside a mineral*.

A future opal pass should make the fire itself procedural rather than hand-positioned, perhaps by thresholding turbulence into sparse colored islands.

### 06 — Satin + Velvet
<p align="center"><img src="./assets/materials/textiles.svg" width="100%"></p>
These are an especially useful pair because their geometry can be almost identical while their light response is opposite-ish. Satin wants a long directional traveling highlight. Velvet wants deep light absorption with tiny fibers catching grazing illumination. The velvet experiment uses procedural noise as a fake pile normal field.

**Same pigment ≠ same material. Light behavior is the identity.**

### 07 — Translucent Resin + Mercury Glass
<p align="center"><img src="./assets/materials/resin-mercury.svg" width="100%"></p>
The resin has visible objects suspended *inside* its volume: bubbles, colored inclusions, little geometric debris. That creates depth without actual 3D. Mercury glass goes the opposite direction: mirrored bands are dirtied with procedural mottling so the reflection feels chemically imperfect and backed rather than digitally chrome-perfect.

### 08 — Soap Film + Pearlescent Automotive Paint
<p align="center"><img src="./assets/materials/bubble-pearl.svg" width="100%"></p>
The soap film is almost nothing except its boundary: weak transparent body, strong spectral edge. Pearlescent paint is almost the inverse: opaque body with a broad color-shifting highlight that implies suspended mica-like flakes.

This is a lovely rendering lesson: sometimes **the material is primarily an edge condition**.

### 09 — CRT Glass + Water + Machined Metal
<p align="center"><img src="./assets/materials/crt-water-metal.svg" width="100%"></p>
Three surfaces with radically different information density. CRT glass gets curvature, vignette, reflection and scanline structure. Water uses turbulence as geometry and feeds it into displacement/specular lighting. Machined metal uses directional brush lines plus concentric tooling marks layered over a broad metallic response.

The CRT specimen also suggests a whole delicious subfield: phosphor masks, bloom, convergence error, scan curvature, ghosting, burned-in UI and faux analog signal damage.

---

## 10 — Rendering Stack / Mental Model

```text
SILHOUETTE / FORM
       ↓
BASE ALBEDO / SPECTRAL COLOR
       ↓
MACRO LIGHTING GRADIENT
       ↓
SURFACE NORMAL FAKE (turbulence / displacement)
       ↓
SPECULAR / DIFFUSE RESPONSE
       ↓
MICROTEXTURE / GRAIN / FIBER / GROOVE
       ↓
EDGE / FRESNEL-ISH / THIN-FILM CUES
       ↓
VOLUME CUES / INCLUSIONS
       ↓
CAST SHADOW + ENVIRONMENT CUES
       ↓
THE HUMAN VISUAL SYSTEM DOES THE REST
```

**Shader thinking without shaders.**

## 11 — Next Research Problems

Now I want to stop treating these as isolated swatches and investigate *composite objects*:

- a single glass window containing chrome hardware, resin controls and CRT displays
- realistic layered **mother-of-pearl / abalone** using turbulence at multiple scales
- procedural opal fire generated by thresholded noise
- true-looking frosted glass where silhouettes behind it remain perceptible but diffuse
- brushed aluminum with directionally stretched noise rather than a simple line pattern
- CD/DVD radial diffraction with polar/radial groove illusions
- embossed holographic security foil
- wet surfaces with meniscus/contact highlights
- water droplets sitting *on* another material
- scratched, fingerprinted, dusty and aged versions of pristine materials
- fake subsurface scattering for wax/jade/milky plastic
- caustic-light projection onto a second object
- material transitions: chrome dissolving into gel, glass frosting at an edge, pearl becoming oil slick
- animated optical response if SMIL survives: shimmer that moves without moving the object

## 12 — The Rule

> **We are not rendering reality. We are rendering enough evidence that the brain volunteers to render reality for us.**

And now we have enough individual material vocabulary to start making **objects whose components appear to be made of different substances**, rather than merely making fancy rectangles.

[← return to the Non-Euclidean Glasshouse](./NON-EUCLIDEAN-GEOCITIES.md)
