---
name: taste
description: UI design taste, visual aesthetics, typography harmony, and design system intelligence for modern web applications.
---

# Design Taste & Visual Excellence Guidelines

A specialized skill for building high-taste, visually wowed web user interfaces with curated typography, harmonious color palettes, micro-animations, and responsive layout math.

---

## 🎨 Core Design System Principles

### 1. Typography Hierarchy & Google Fonts
- **Display & Headline Font**: `Syne` (Weights: 500, 700, 800) — Used for page titles, card headers, metric numbers, and section headlines.
- **Telemetry & Data Font**: `JetBrains Mono` (Weights: 300, 400, 500, 700) — Used for audit IDs, verification hashes, status badges, code, and transformation parameters.

### 2. Color Palette & Dark Obsidian Theme
- **Background**: `#06080f` (Deep Obsidian Black) with `#0d121f` container surfaces.
- **Accents**: `#f59e0b` (Amber Gold), `#6366f1` (Indigo Glow).
- **Status Indicators**:
  - `Flagged Defect`: `#f43f5e` (Rose Red) with `bg-rose-500/10` tint.
  - `Resolved & Verified`: `#10b981` (Emerald Green) with `bg-emerald-500/10` tint.
  - `Inspection Pending`: `#f59e0b` (Amber Gold) with `bg-amber-500/10` tint.
  - `Cloudinary AI`: `#a855f7` (Purple) with `bg-purple-500/10` tint.

### 3. Glassmorphism & Micro-Animations
- Use subtle backdrop blurs (`backdrop-blur-md`, `backdrop-blur-lg`) over semi-transparent container surfaces (`bg-slate-900/90`, `bg-slate-950/80`).
- Apply interactive hover scale effects (`group-hover:scale-105 transition-transform duration-500`).
- Use smooth transition states (`transition-all duration-300`).

---

## 🚫 Anti-Patterns to Avoid

- ❌ **No Plain Default Colors**: Avoid raw red (`#ff0000`), blue (`#0000ff`), or plain white backgrounds without ambient contrast.
- ❌ **No Static Placeholders**: Use real or generated images/components with aspect ratio preserving containers.
- ❌ **No Corporate "Enterprise" Framing**: Let functional features, live data optimization studio, and audit verification badges speak for themselves.

---

## 🛠 Next.js & Cloudinary Design Integration

- Use `CloudinaryMediaImage` or `CldImage` for automatic responsive sizing, `f_auto` format switching, `q_auto` compression, and dynamic text overlays (`l_text`).
- Display live payload savings badges (e.g. `73.2% Bandwidth Saved`) to make media performance visible to users and judges.
