# Infra Evidence Platform — Field Inspector Portal

An infrastructure evidence and verification platform designed for field inspectors evaluating roads, bridges, public health centers, and rural development schemes across regional India.

Integrated with **Qdrant Edge — Offline Field Memory** for vector search provenance and audit trail synchronization.

---

## 🌟 Key Features & Technical Highlights

### 1. Next.js Cloudinary Kit & Media Optimization
- **`CloudinaryMediaImage` & `CldImage`**: Dynamic image URL transformation engine leveraging Cloudinary's `f_auto` (automatic AVIF/WebP conversion) and `q_auto` (perceptual AI compression).
- **~73% to 84% Bandwidth Reduction**: Reduces high-resolution field photos from ~3.5 MB down to ~180 KB over low-bandwidth mobile networks.
- **Dynamic Watermark Overlays**: Automatically embeds tamper-evident text overlays (`l_text:Syne_20_bold:PWD-INSPECTED`) and verification badges.
- **Cloudinary Upload Widget (`CldUploadButton`)**: Direct evidence upload modal with AI auto-tagging.

### 2. JEV AI Change Verification Engine (`JevClient`)
- **Multimodal AI Gate**: Powered by Vercel AI Gateway / OpenRouter (`openai/gpt-4o-mini`) evaluating before/after inspection photos.
- **Automated Verification Badges**: Returns structured decision objects (`meaningful-change` vs `no-change` with confidence scores).
- **Deterministic Mock Mode**: Instant offline presentation mode (`NEXT_PUBLIC_JEV_MOCK=true`) for zero-latency hackathon demos.

### 3. Interactive Before/After Comparison Slider
- Powered by `react-compare-slider` to compare pre-repair defect states against restored infrastructure side-by-side.

### 4. Dual Design System & Qdrant Edge Partner Linkage
- **Typography Scale**: `Syne` (Display/Headlines) + `JetBrains Mono` (Telemetry & Hashes).
- **Obsidian Theme**: `#06080f` dark obsidian theme with `#f59e0b` amber accents.
- **Provenance Bridge**: Exposes `audit_id`, `verification_hash`, and vector collection linkages (`central_field_memories`).

---

## 🚀 Quick Start & Local Setup

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/Deadeye102000/Infra-Evidence-Platform.git
cd Infra-Evidence-Platform/cloudinary-infra-platform
npm install
```

### 2. Configure Environment Keys
Copy `.env.example` to `.env.local`:
```bash
cp .env.example .env.local
```

Edit `.env.local`:
```ini
# Cloudinary Keys
NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME=demo
CLOUDINARY_CLOUD_NAME=demo
CLOUDINARY_API_KEY=your_api_key_here
CLOUDINARY_API_SECRET=your_api_secret_here

# JEV Change Verification Engine (Set to false for live OpenRouter/Vercel AI calls)
NEXT_PUBLIC_JEV_MOCK=true
VERCEL_AI_GATEWAY_KEY=your_openrouter_api_key

# Partner Platform URL
NEXT_PUBLIC_QDRANT_EDGE_URL=http://localhost:3000
```

### 3. Start Development Server
```bash
# Starts dev server on port 3001 (http://localhost:3001)
npm run dev
```

### 4. Run Unit & Component Tests
```bash
# Runs 5 test suites (16 tests covering JevClient, Cloudinary helpers, & UI components)
npm test
```

---

## 🌐 Deployment to Vercel

```bash
cd cloudinary-infra-platform
npx vercel --prod
```

Or deploy directly via Vercel Dashboard by connecting `https://github.com/Deadeye102000/Infra-Evidence-Platform` (Root directory: `cloudinary-infra-platform`).

---

## 🛠 Tech Stack

- **Framework**: Next.js 14 App Router (TypeScript)
- **Image Cloud SDK**: `next-cloudinary` & `cloudinary` Node SDK (v2)
- **AI Gateway**: Vercel AI Gateway / OpenRouter Multimodal Vision API
- **Styling**: Tailwind CSS + shadcn/ui primitives (`Card`, `Badge`)
- **Typography**: Google Fonts (`Syne` + `JetBrains Mono`)
- **Comparison Slider**: `react-compare-slider`
- **Testing**: Jest + `@testing-library/react` (JSDOM)
- **Icons**: `lucide-react`
