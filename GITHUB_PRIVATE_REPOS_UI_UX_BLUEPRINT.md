# GitHub Private Repositories: UI/UX Architecture & Professional Website Design Blueprint

> **Account**: `@jai1aiger` (Pedini Sanjai Kumar)  
> **Status**: Comprehensive Analysis & Implementation Guide  
> **Generated**: September 2026  
> **Scope**: Extraction, analysis, and cross-application blueprint of all authenticated GitHub private repositories for crafting world-class, responsive, and interactive UI/UX across diverse website genres.

---

## 1. Executive Summary & Repository Ecosystem

An inspection of the authenticated GitHub account reveals **three private repositories**, each addressing a distinct and complementary tier of modern digital product design:

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                               GITHUB PRIVATE REPOSITORIES                               │
├───────────────────────────────┬───────────────────────────────┬─────────────────────────┤
│    jai1aiger/studio           │jai1aiger/v0-url-intelligence  │    jai1aiger/NORM       │
│    (Private)                  │-dashboard (Private)           │    (Private)            │
├───────────────────────────────┼───────────────────────────────┼─────────────────────────┤
│ • Production Design System    │ • 3D WebGL & Particle FX      │ • Conversational UX     │
│ • 25+ Shadcn / Radix UI Kits  │ • Cyber / Futuristic HUD      │ • Transaction Recovery  │
│ • App Router & Responsive Nav │ • Animated SVG Metric Rings   │ • Contextual Messaging  │
│ • Recharts Data Visualization │ • Skewed 3D Perspective Cards │ • Razorpay Paylinks API │
│ • Genkit AI & Multi-lang i18n │ • Glassmorphism & Framer Mtn  │ • State Machine Guard   │
└───────────────────────────────┴───────────────────────────────┴─────────────────────────┘
                                           │
                                           ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                      UNIFIED PROFESSIONAL UI/UX ARCHITECTURE                            │
├──────────────────────────────┬──────────────────────────────┬───────────────────────────┤
│ • SaaS & Enterprise Apps     │ • AI Landing Pages & HUDs    │ • E-Commerce & Checkout   │
│ • 3D Portfolios & Agencies   │ • Healthcare & Clinics       │ • FinTech & Dashboards    │
└──────────────────────────────┴──────────────────────────────┴───────────────────────────┘
```

When combined, these repositories provide a **complete, production-grade frontend and UX engineering stack**:
1. **`jai1aiger/studio`** provides the **foundational UI infrastructure**: layout shells, accessible primitives, typography hierarchy, data charts, and design tokens.
2. **`jai1aiger/v0-url-intelligence-dashboard`** provides the **visual spectacle and micro-interactions**: GPU-accelerated 3D WebGL particle physics, animated circular gauges, glowing glassmorphic controls, and 3D card tilt transformations.
3. **`jai1aiger/NORM`** provides the **conversational & transactional UX**: turn-by-turn recovery messaging, humanized error resolution, and friction-free payment flows.

---

## 2. In-Depth Breakdown of Private Repositories

---

### Repo 1: `jai1aiger/studio`
* **Visibility**: `Private`
* **Default Branch**: `main`
* **Primary Role**: Full-Stack Enterprise Design System & AI Advisory SaaS Platform
* **Live Framework**: Next.js 15.5.9 (Turbopack, App Router), React 19.2.1, TypeScript 5, Tailwind CSS 3.4.1

#### A. Tech Stack & Key Dependencies
| Package | Version | Purpose in UI/UX |
| :--- | :--- | :--- |
| `next` | `15.5.9` | App Router, Server/Client components, dynamic layout nesting |
| `react` & `react-dom` | `19.2.1` | Next-gen React concurrent rendering |
| `@radix-ui/*` | `^1.1.x - ^2.1.x` | Headless, accessible primitives (WAI-ARIA compliant) |
| `recharts` | `^2.15.1` | Responsive SVG charts with custom gradient fills and tooltips |
| `lucide-react` | `^0.475.0` | Consistent vector iconography with uniform stroke weights |
| `embla-carousel-react`| `^8.6.0` | Touch-friendly, momentum-based content carousels |
| `react-hook-form` + `zod` | `^7.54` / `^3.24` | Schema-validated forms with inline error feedback |
| `@genkit-ai/google-genai` | `^1.20.0` | Google GenAI / Gemini backend for streaming AI responses |
| `tailwindcss-animate` | `^1.0.7` | Keyframe entrance, exit, and pulse animation utilities |

#### B. Component Catalog (25+ Production-Grade Primitives)
The repository contains an enterprise-grade component suite located at `src/components/ui/`:
1. **Layout & Containers**:
   * `sidebar.tsx`: Collapsible multi-tier navigation drawer with mobile touch triggers.
   * `card.tsx`: Modular card structure (`CardHeader`, `CardTitle`, `CardDescription`, `CardContent`, `CardFooter`).
   * `scroll-area.tsx`: Custom styled cross-browser scrollbars using Radix Scroll Area.
   * `separator.tsx`: Semantic horizontal and vertical dividers with subtle opacity.
   * `sheet.tsx`: Slide-over drawer panel for secondary actions and mobile drawers.
2. **Interactive Controls & Inputs**:
   * `button.tsx`: Variant-driven buttons (`default`, `secondary`, `outline`, `ghost`, `link`, `destructive`) with size scales (`sm`, `default`, `lg`, `icon`).
   * `input.tsx` & `textarea.tsx`: Form fields styled with smooth focus rings and placeholder states.
   * `select.tsx`, `dropdown-menu.tsx`, `menubar.tsx`: Accessible overlay menus with keyboard navigation.
   * `checkbox.tsx`, `radio-group.tsx`, `switch.tsx`: Accessible binary and multi-choice switches.
   * `slider.tsx`: Continuous and stepped draggable range sliders.
3. **Data Display & Feedback**:
   * `table.tsx`: Data tables with sticky headers, zebra striping, and cell alignments.
   * `chart.tsx`: Configurable chart wrappers with CSS variable theme bindings.
   * `badge.tsx`: Pill badges for status indicators (`default`, `secondary`, `destructive`, `outline`).
   * `avatar.tsx`: Image avatars with automatic fallback initials.
   * `progress.tsx`: Linear animated progress bars.
   * `skeleton.tsx`: Shimmer placeholder loaders for asynchronous content fetching.
4. **Overlays & Dialogs**:
   * `dialog.tsx` & `alert-dialog.tsx`: Accessible modal dialogs with backdrop blur and focus traps.
   * `popover.tsx` & `tooltip.tsx`: Contextual floating popups with animated arrows.
   * `toast.tsx` & `toaster.tsx`: Toast notification dispatchers with action buttons.
   * `calendar.tsx`: Full-month date pickers integrated with `date-fns`.

#### C. Key UI/UX Implementations
* **Dashboard Layout (`src/app/dashboard/layout.tsx` & `page.tsx`)**:
  * Metric cards with hover-lift micro-interactions (`transition-all hover:shadow-md hover:-translate-y-1`).
  * Recharts Area Chart with custom dual-gradient fills (`#colorIncome` and `#colorExpenses`), responsive container scaling, and HSL-bound tooltips.
  * AI Companion CTA Card: High-contrast primary surface (`bg-primary text-primary-foreground`) directing users to the "Spark" conversational assistant.
* **Internationalization (`src/components/translations-provider.tsx`)**:
  * Global translation context providing instant language switching without page reloads.

---

### Repo 2: `jai1aiger/v0-url-intelligence-dashboard`
* **Visibility**: `Private`
* **Default Branch**: `main`
* **Primary Role**: 3D GPU Particle Canvas, Futuristic AI HUD & Website Intelligence Platform
* **Live Deployment**: Deployed on Vercel (`v0-url-intelligence-dashboard`)
* **Live Framework**: Next.js 16.0.7, React 19.2.0, Tailwind CSS v4 (`@tailwindcss/postcss: ^4.1.9`), Three.js, React Three Fiber

#### A. Tech Stack & Key Dependencies
| Package | Version | Purpose in UI/UX |
| :--- | :--- | :--- |
| `three` | `latest` | Direct WebGL rendering engine for 3D shaders and particle fields |
| `@react-three/fiber` | `latest` | Declarative Three.js wrapper inside the React 19 component tree |
| `@react-three/drei` | `10.7.7` | Pre-built 3D shaders, cameras, and geometry helpers |
| `framer-motion` | `latest` | Spring physics, staggered entry variants, and SVG path animations |
| `cmdk` | `1.0.4` | Spotlight-style instant command palette search |
| `sonner` | `^1.7.4` | Sleek toast alerts with stacking animations |
| `vaul` | `^1.1.2` | Mobile-friendly iOS-style bottom drawer |
| `next-themes` | `^0.4.6` | Flawless dark/light theme switching with zero flash |
| `react-resizable-panels` | `^2.1.7` | Draggable split-screen layout panels |

#### B. Highlighted UI/UX Components & Innovations

1. **GPU 3D Particle Simulation (`components/three-background.tsx`)**:
   * **Mechanism**: Custom WebGL buffer geometry with **3,000 ascending particles** simulating blue ethereal flames.
   * **Performance Features**: Runs inside a `<Canvas>` configured with `style={{ pointerEvents: "none" }}`, allowing zero interference with foreground clicks and inputs.
   * **Visual Blend**: Uses `THREE.AdditiveBlending` with vertex coloring (cyan `#00ccff`, blue `#0066ff`, and white highlights) and dual point lights.

2. **Cyber-Hero Section (`components/hero.tsx`)**:
   * **Gradient Text**: Clipping text with `bg-clip-text text-transparent bg-gradient-to-r from-purple-400 via-cyan-400 to-purple-400`.
   * **Pulsing Halo**: Ambient glow behind inputs using `absolute inset-0 bg-gradient-to-r from-purple-500 to-cyan-500 rounded-full blur opacity-75 animate-pulse`.
   * **Glassmorphic Input**: `bg-white/5 backdrop-blur-xl border border-white/10 rounded-full text-white`.
   * **Shimmer Button**: Framer Motion animated shine overlay cycling infinitely across the CTA.

3. **Circular SVG Metric Gauge (`components/performance-card.tsx`)**:
   * **SVG Animation**: Animates `strokeDasharray` using Framer Motion with ease-out physics.
   * **Color Logic**:
     * Score $>90$: Emerald Green gradient (`#10b981` ➜ `#34d399`) + Green glow.
     * Score $50-90$: Amber Yellow gradient (`#f59e0b` ➜ `#fbbf24`) + Yellow glow.
     * Score $<50$: Rose Red gradient (`#ef4444` ➜ `#f87171`) + Red glow.
   * **Backdrop**: Dual-layer glass card with radial gradient back-glow matching the score tier.

4. **3D Perspective Showcase (`components/results-grid.tsx`)**:
   * **CSS 3D Transform**: Applies real 3D isometric tilt to screenshot previews:
     ```tsx
     style={{
       perspective: "1000px",
       transform: "rotateY(12deg) rotateX(-5deg)",
     }}
     ```
   * **Staggered Animations**: Uses Framer Motion `variants` (`containerVariants` with `staggerChildren: 0.2` and `itemVariants`) to reveal cards sequentially.

---

### Repo 3: `jai1aiger/NORM`
* **Visibility**: `Private`
* **Default Branch**: `main`
* **Primary Role**: Conversational Revenue Recovery & Humanized FinTech Outreach Engine
* **Platform**: Built for the Razorpay AI Buildathon (Track 3: AI Revenue Recovery)
* **Live Framework**: Python 3.10+, FastAPI, SQLAlchemy, SQLite, Google Gemini Flash, Razorpay API, Twilio API

#### A. Tech Stack & Integration Architecture
| Module | Component | UX Value |
| :--- | :--- | :--- |
| `FastAPI` | Webhook receiver & REST endpoints | Sub-second webhook ingestion upon checkout failures |
| `SQLAlchemy` | `Transaction`, `OutreachLog` models | Real-time state machine audit trail |
| `Gemini Flash` | Contextual Prompt Engine | Generates empathetic, code-switched Hinglish/English recovery copy |
| `Razorpay SDK` | Dynamic Payment Links API | Creates 1-click personalized checkout links with expiration |
| `Twilio WhatsApp`| Business Sandbox API | Delivers conversational cards directly to the user's phone |

#### B. UX Principles & Flow Engineering
1. **Converting Failure to Conversion**:
   * Standard checkout errors (e.g. `BAD_REQUEST_PAYMENT_TIMED_OUT`, `INSUFFICIENT_FUNDS`) cause cart abandonment.
   * `NORM` captures the payload, diagnoses the root cause, and generates personalized, non-intrusive messages offering alternative payment options (UPI, Netbanking, Cards) with a pre-configured recovery link.
2. **Ethical UX Guardrails ("Meeting the Bar")**:
   * **Hard Cap**: Maximum **3 outreach attempts** per transaction.
   * **Instant Stop Keyword Detection**: If the user replies with "stop", "nahi", "unsubscribe", or "cancel", the state transitions to `OPTED-OUT` and silences all future notifications immediately.
   * **Full Visibility**: Complete audit history of timestamps, channels, and message contents.

---

## 3. Master Blueprint: Crafting Professional UI/UX Across 5 Website Genres

Here is how to synthesize the code, components, and patterns from these private repositories to design best-in-class websites for different industries.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          UI/UX SYNTHESIS ARCHITECTURE                                  │
├───────────────────┬───────────────────────────────────┬────────────────────────────────┤
│ Website Genre     │ Primary Source Repositories       │ Key UI/UX Patterns             │
├───────────────────┼───────────────────────────────────┼────────────────────────────────┤
│ 1. SaaS & B2B     │ • studio (Layout, Nav, Recharts)  │ Nested sidebars, stat cards,   │
│    Enterprise     │ • v0-dashboard (Theme, Sonner)    │ data tables, modal forms       │
├───────────────────┼───────────────────────────────────┼────────────────────────────────┤
│ 2. AI Landing &   │ • v0-dashboard (Three.js, Hero)   │ 3D particle canvas, glowing    │
│    Cyber HUDs     │ • studio (Badges, Buttons)        │ inputs, 3D tilted card frames  │
├───────────────────┼───────────────────────────────────┼────────────────────────────────┤
│ 3. E-Commerce &   │ • studio (Embla, Dialog, Sheet)   │ Cart slide-over, product grid, │
│    Direct-to-Cons │ • NORM (Razorpay & Recovery)      │ 1-click recovery paylinks      │
├───────────────────┼───────────────────────────────────┼────────────────────────────────┤
│ 4. 3D Creative &  │ • v0-dashboard (R3F, Drei, Three) │ Real-time WebGL canvas,        │
│    Portfolios     │ • Workspace 3D Lanyard & Cards    │ interactive physics & badges   │
├───────────────────┼───────────────────────────────────┼────────────────────────────────┤
│ 5. Healthcare &   │ • studio (Calendar, Form, Zod)    │ Appointment scheduling, intake │
│    Clinic Booking │ • studio (Accordion, Table)       │ forms, FAQ disclosure panels   │
└───────────────────┴───────────────────────────────────┴────────────────────────────────┘
```

---

### Genre 1: Modern SaaS & Enterprise Analytics Platforms

#### Design Objective
Build a dashboard that feels fast, clean, informative, and authoritative, handling complex datasets while maintaining visual clarity.

#### Implementation Architecture
1. **Shell & Layout (`jai1aiger/studio`)**:
   * Use `sidebar.tsx` and `header.tsx` with dynamic breadcrumb trails and collapsible navigation.
   * Implement responsive breakpoints (`grid-cols-1 md:grid-cols-2 lg:grid-cols-4`).
2. **Key Metric KPI Cards (`jai1aiger/studio`)**:
   * Wrap metrics in `Card` with hover-lift micro-interactions:
     ```tsx
     <Card className="transition-all duration-200 hover:shadow-lg hover:-translate-y-1 border-border/50 bg-card/60 backdrop-blur-sm">
       <CardHeader className="flex flex-row items-center justify-between pb-2">
         <CardTitle className="text-sm font-medium text-muted-foreground">Monthly Recurring Revenue</CardTitle>
         <DollarSign className="h-4 w-4 text-emerald-500" />
       </CardHeader>
       <CardContent>
         <div className="text-3xl font-bold tracking-tight">$48,250</div>
         <p className="text-xs text-emerald-500 flex items-center mt-1">
           <ArrowUpRight className="h-3 w-3 mr-1" /> +12.4% from last month
         </p>
       </CardContent>
     </Card>
     ```
3. **Data Visualization (`jai1aiger/studio`)**:
   * Leverage Recharts Area / Bar charts with custom dual SVG gradient stops (`linearGradient` from `hsl(var(--primary))` to transparent).
   * Customize `<Tooltip>` using CSS variables for theme-aware dark/light popups.
4. **Data Management Tables (`jai1aiger/studio`)**:
   * Use `table.tsx` with sticky headers, `Avatar` for user records, `Badge` for status tags (`Active`, `Pending`, `Suspended`), and `DropdownMenu` for action rows.

---

### Genre 2: High-Converting AI Products & Developer Tool Landing Pages

#### Design Objective
Create an unforgettable first impression using futuristic cyber styling, dark aesthetics, glowing ambient lighting, and interactive WebGL elements.

#### Implementation Architecture
1. **GPU 3D Background (`jai1aiger/v0-url-intelligence-dashboard`)**:
   * Mount `<ThreeBackground />` behind the hero section with `pointer-events-none` so visitors can interact with buttons and forms while particles float behind them.
2. **Cyber Hero Typography & Input Bar (`jai1aiger/v0-url-intelligence-dashboard`)**:
   * Heading with gradient clip text:
     ```tsx
     <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight">
       <span className="bg-clip-text text-transparent bg-gradient-to-r from-purple-400 via-cyan-400 to-indigo-400">
         Next-Generation AI Intelligence
       </span>
     </h1>
     ```
   * Glassmorphism search / prompt bar with animated gradient glow aura (`bg-white/5 backdrop-blur-xl border border-white/10 rounded-full focus-within:ring-2 focus-within:ring-cyan-400`).
3. **Product Showcase with 3D Skew Perspective (`jai1aiger/v0-url-intelligence-dashboard`)**:
   * Present application screenshots in an isometric 3D angled container (`perspective: 1000px`, `transform: rotateY(12deg) rotateX(-5deg)`) with frosted glass borders and drop shadows.
4. **Circular Animated Performance Gauges (`jai1aiger/v0-url-intelligence-dashboard`)**:
   * Display real-time AI metrics (e.g. latency, throughput, accuracy score) using Framer Motion SVG path stroke animations.
5. **Instant Quick-Action Palette (`cmdk` from `v0-dashboard`)**:
   * Trigger modal command search with `Ctrl+K` / `Cmd+K` for instant navigation and action execution.

---

### Genre 3: E-Commerce & Direct-to-Consumer (D2C) Storefronts

#### Design Objective
Maximize conversions, eliminate friction in product exploration, provide smooth checkout experiences, and automatically recover lost revenue.

#### Implementation Architecture
1. **Interactive Product Showcases (`jai1aiger/studio`)**:
   * Implement `embla-carousel-react` (`carousel.tsx`) for fluid swipeable image galleries on mobile and desktop.
   * Use `badge.tsx` for discount tags (`Save 25%`), stock alerts (`Only 3 Left`), and new arrival tags.
2. **Product Configuration & Quick View (`jai1aiger/studio`)**:
   * `radio-group.tsx` for size / color / variant selections.
   * `dialog.tsx` for modal instant previews without leaving the catalog page.
   * `sheet.tsx` for a slide-over slide-in shopping bag (`CartSheet`) with instant item counter and total calculations.
3. **Cart Abandonment & Payment Recovery (`jai1aiger/NORM`)**:
   * Connect checkout failure events to `NORM` webhook listeners.
   * When a payment drops due to network or gateway glitches, generate an instant Razorpay dynamic recovery link.
   * Dispatch a friendly WhatsApp message with the exact product summary and single-tap checkout button, boosting checkout completion rates by 15–30%.

---

### Genre 4: Creative 3D Interactive Agency & Developer Portfolios

#### Design Objective
Showcase technical prowess, interactive creativity, and high-end visual design with real-time 3D models, smooth physics, and interactive cards.

#### Implementation Architecture
1. **3D WebGL Canvas & Physics (`jai1aiger/v0-url-intelligence-dashboard` + Workspace Assets)**:
   * Combine React Three Fiber (`Canvas`, `useFrame`, `BufferGeometry`) with interactive 3D elements (such as the 3D visiting card / lanyard badge shader from the current workspace).
   * Render custom materials with matcap textures, specular reflections, and responsive camera controls.
2. **Project Case Study Grid (`jai1aiger/v0-url-intelligence-dashboard`)**:
   * Cards with Framer Motion staggered entrance animations (`staggerChildren: 0.15`).
   * Hover scale micro-interactions (`whileHover={{ scale: 1.03, y: -4 }}`).
3. **Interactive Tech Stack Badges (`jai1aiger/v0-url-intelligence-dashboard` + `studio`)**:
   * Floating tech badges displaying icons (React, Three.js, Next.js, Python, Tailwind) with translucent pill styling (`bg-white/10 backdrop-blur-md border border-white/20 px-4 py-2 rounded-full`).
4. **Theme Switcher & Audio/Visual Toggles (`next-themes`)**:
   * Zero-flash dark and light theme toggle with smooth CSS transitions.

---

### Genre 5: Healthcare, Clinic & Appointment Booking Portals

#### Design Objective
Convey trust, medical professionalism, clarity of services, and effortless appointment booking (synergizing with `jai1aiger/sri-jjr-physiotherapy-clinic` and `studio`).

#### Implementation Architecture
1. **Appointment Booking Calendar (`jai1aiger/studio`)**:
   * Embed `calendar.tsx` with date availability highlighting and slot booking.
   * Combine with `select.tsx` for choosing treatment categories (e.g. Orthopedic Rehab, Sports Injury, Post-Op Care).
2. **Patient Intake & Consultation Form (`jai1aiger/studio`)**:
   * Schema-validated multi-step form using `react-hook-form` + `zod` (`form.tsx`, `input.tsx`, `textarea.tsx`, `radio-group.tsx`).
   * Real-time client-side validation preventing incomplete submissions.
3. **FAQ & Treatment Accordions (`jai1aiger/studio`)**:
   * Implement `accordion.tsx` using Radix UI primitives for smooth expandable sections detailing treatment protocols, session timings, and insurance coverage.
4. **Doctor & Clinic Trust Profiles (`jai1aiger/studio`)**:
   * `card.tsx` with doctor credentials, clinic certifications, and verified patient reviews with star ratings and avatar badges.

---

## 4. Production-Ready UI Recipes & Code Templates

The following modular code snippets are extracted and refined directly from the private repositories for instant reuse in any modern project.

---

### Recipe 1: 3D WebGL Ethereal Particle Canvas
*Source: Extracted and generalized from `jai1aiger/v0-url-intelligence-dashboard/components/three-background.tsx`*

```tsx
"use client";

import React, { useEffect, useRef, useState } from "react";
import { Canvas } from "@react-three/fiber";
import * as THREE from "three";

interface ParticleCanvasProps {
  particleCount?: number;
  primaryColor?: string;
  secondaryColor?: string;
}

function ParticleField({
  particleCount = 2500,
  primaryColor = "#0066ff",
  secondaryColor = "#00ccff",
}: ParticleCanvasProps) {
  const [mounted, setMounted] = useState(false);
  const particlesRef = useRef<THREE.Points>(null);

  useEffect(() => {
    setMounted(true);
  }, []);

  useEffect(() => {
    if (!particlesRef.current) return;
    const geometry = particlesRef.current.geometry;
    const positionAttribute = geometry.getAttribute("position");
    const positions = positionAttribute.array as Float32Array;

    const animate = () => {
      for (let i = 0; i < positions.length; i += 3) {
        positions[i + 1] += (Math.random() - 0.5) * 0.4 + 0.05; // upward drift
        positions[i] += (Math.random() - 0.5) * 0.15;
        positions[i + 2] += (Math.random() - 0.5) * 0.15;

        // Reset boundary
        if (positions[i + 1] > 45) {
          positions[i + 1] = -45;
        }
      }
      positionAttribute.needsUpdate = true;
    };

    const interval = setInterval(animate, 16);
    return () => clearInterval(interval);
  }, [mounted]);

  if (!mounted) return null;

  const geometry = new THREE.BufferGeometry();
  const positions = new Float32Array(particleCount * 3);
  const colors = new Float32Array(particleCount * 3);

  const c1 = new THREE.Color(primaryColor);
  const c2 = new THREE.Color(secondaryColor);

  for (let i = 0; i < particleCount * 3; i += 3) {
    positions[i] = (Math.random() - 0.5) * 50;
    positions[i + 1] = Math.random() * 90 - 45;
    positions[i + 2] = (Math.random() - 0.5) * 30;

    const mixRatio = Math.random();
    const mixed = c1.clone().lerp(c2, mixRatio);
    colors[i] = mixed.r;
    colors[i + 1] = mixed.g;
    colors[i + 2] = mixed.b;
  }

  geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
  geometry.setAttribute("color", new THREE.BufferAttribute(colors, 3));

  return (
    <Canvas
      className="absolute inset-0"
      camera={{ position: [0, 0, 50], fov: 75 }}
      style={{ pointerEvents: "none" }}
    >
      <color attach="background" args={["#030712"]} />
      <ambientLight intensity={0.3} />
      <pointLight position={[25, 25, 25]} intensity={0.9} color={secondaryColor} />
      <points ref={particlesRef}>
        <bufferGeometry attach="geometry" {...geometry} />
        <pointsMaterial
          attach="material"
          size={0.6}
          sizeAttenuation={true}
          transparent={true}
          opacity={0.75}
          vertexColors={true}
          blending={THREE.AdditiveBlending}
        />
      </points>
    </Canvas>
  );
}

export function AmbientThreeBackground(props: ParticleCanvasProps) {
  return (
    <div className="absolute inset-0 -z-10 overflow-hidden">
      <ParticleField {...props} />
    </div>
  );
}
```

---

### Recipe 2: Glassmorphic Search Bar with Traveling Shimmer Button
*Source: Refined from `jai1aiger/v0-url-intelligence-dashboard/components/hero.tsx`*

```tsx
"use client";

import React from "react";
import { motion } from "framer-motion";
import { Sparkles, ArrowRight } from "lucide-react";

interface SearchBarProps {
  value: string;
  onChange: (val: string) => void;
  onSubmit: () => void;
  placeholder?: string;
  loading?: boolean;
}

export function GlassmorphicSearchInput({
  value,
  onChange,
  onSubmit,
  placeholder = "Search or enter query...",
  loading = false,
}: SearchBarProps) {
  return (
    <div className="relative w-full max-w-2xl mx-auto">
      {/* Ambient Pulsing Glow Underlay */}
      <div className="absolute inset-0 bg-gradient-to-r from-purple-600/40 via-cyan-500/40 to-indigo-600/40 rounded-full blur-xl opacity-75 transition duration-1000 animate-pulse" />

      {/* Glassmorphism Input Field Container */}
      <div className="relative flex items-center bg-gray-950/70 backdrop-blur-2xl border border-white/15 rounded-full p-2 shadow-2xl">
        <Sparkles className="h-5 w-5 text-cyan-400 ml-4 mr-2 shrink-0 animate-spin" style={{ animationDuration: "12s" }} />
        <input
          type="text"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && !loading && onSubmit()}
          placeholder={placeholder}
          disabled={loading}
          className="w-full bg-transparent px-3 py-2 text-white placeholder-gray-400 focus:outline-none text-base"
        />

        {/* Shimmering Action CTA Button */}
        <motion.button
          onClick={onSubmit}
          disabled={loading || !value.trim()}
          whileHover={{ scale: 1.03 }}
          whileTap={{ scale: 0.97 }}
          className="relative px-6 py-2.5 bg-gradient-to-r from-purple-600 to-cyan-500 text-white font-medium rounded-full shrink-0 overflow-hidden shadow-md disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
        >
          <span className="relative z-10 text-sm">
            {loading ? "Processing..." : "Generate"}
          </span>
          {!loading && <ArrowRight className="h-4 w-4 relative z-10" />}

          {/* Continuous Traveling Shimmer Reflection */}
          <motion.div
            className="absolute inset-0 bg-gradient-to-r from-transparent via-white/35 to-transparent pointer-events-none"
            animate={{ x: ["100%", "-100%"] }}
            transition={{ duration: 2.8, repeat: Infinity, ease: "linear" }}
          />
        </motion.button>
      </div>
    </div>
  );
}
```

---

### Recipe 3: Animated SVG Circular Metric Gauge
*Source: Refined from `jai1aiger/v0-url-intelligence-dashboard/components/performance-card.tsx`*

```tsx
"use client";

import React from "react";
import { motion } from "framer-motion";

interface MetricGaugeProps {
  score: number; // 0 to 100
  title?: string;
  subtitle?: string;
}

export function AnimatedCircularMetric({
  score,
  title = "Performance Index",
  subtitle = "Optimized via Edge CDN",
}: MetricGaugeProps) {
  const clampedScore = Math.min(100, Math.max(0, score));

  // Determine dynamic color gradient based on health threshold
  const isOptimal = clampedScore >= 90;
  const isWarning = clampedScore >= 60 && clampedScore < 90;

  const colorStart = isOptimal ? "#10b981" : isWarning ? "#f59e0b" : "#ef4444";
  const colorEnd = isOptimal ? "#34d399" : isWarning ? "#fbbf24" : "#f87171";
  const gradientClass = isOptimal
    ? "from-emerald-500 to-teal-400"
    : isWarning
    ? "from-amber-500 to-yellow-400"
    : "from-rose-500 to-red-400";

  const radius = 80;
  const circumference = 2 * Math.PI * radius; // ~502.65
  const strokeOffset = ((100 - clampedScore) / 100) * circumference;

  return (
    <div className="relative flex flex-col items-center justify-center p-6 bg-gray-900/60 backdrop-blur-xl border border-white/10 rounded-2xl shadow-xl overflow-hidden">
      {/* Background Radial Glow */}
      <div
        className={`absolute inset-0 bg-gradient-to-br ${gradientClass} opacity-10 blur-3xl`}
      />

      <div className="relative w-44 h-44 my-2">
        <svg className="w-full h-full -rotate-90" viewBox="0 0 200 200">
          {/* Base Background Track */}
          <circle
            cx="100"
            cy="100"
            r={radius}
            fill="none"
            stroke="rgba(255, 255, 255, 0.08)"
            strokeWidth="10"
          />
          {/* Animated Value Ring */}
          <motion.circle
            cx="100"
            cy="100"
            r={radius}
            fill="none"
            stroke="url(#metricGradient)"
            strokeWidth="10"
            strokeLinecap="round"
            strokeDasharray={circumference}
            initial={{ strokeDashoffset: circumference }}
            animate={{ strokeDashoffset: strokeOffset }}
            transition={{ duration: 1.4, ease: "easeOut" }}
          />
          <defs>
            <linearGradient id="metricGradient" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor={colorStart} />
              <stop offset="100%" stopColor={colorEnd} />
            </linearGradient>
          </defs>
        </svg>

        {/* Center Numeric Metric */}
        <div className="absolute inset-0 flex flex-col items-center justify-center text-center">
          <motion.span
            initial={{ scale: 0.5, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ delay: 0.2, duration: 0.4 }}
            className={`text-4xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r ${gradientClass}`}
          >
            {clampedScore}
          </motion.span>
          <span className="text-[11px] font-medium tracking-wider uppercase text-gray-400 mt-1">
            Score / 100
          </span>
        </div>
      </div>

      <h4 className="text-base font-semibold text-white mt-1">{title}</h4>
      <p className="text-xs text-gray-400 mt-0.5">{subtitle}</p>
    </div>
  );
}
```

---

### Recipe 4: 3D Skewed Isometric Showcase Card
*Source: Refined from `jai1aiger/v0-url-intelligence-dashboard/components/results-grid.tsx`*

```tsx
"use client";

import React from "react";
import { motion } from "framer-motion";

interface IsometricShowcaseProps {
  imageSrc: string;
  title: string;
  badgeText?: string;
  category?: string;
}

export function IsometricPerspectiveCard({
  imageSrc,
  title,
  badgeText = "Live Preview",
  category = "Web Application",
}: IsometricShowcaseProps) {
  return (
    <motion.div
      whileHover={{ scale: 1.03, rotateY: 8, rotateX: -2 }}
      transition={{ type: "spring", stiffness: 260, damping: 20 }}
      className="h-full bg-gradient-to-br from-white/10 to-white/5 backdrop-blur-xl border border-white/15 rounded-3xl p-6 shadow-2xl overflow-hidden"
      style={{
        perspective: "1200px",
        transform: "rotateY(14deg) rotateX(-6deg)",
      }}
    >
      <div className="relative w-full aspect-[4/3] rounded-xl overflow-hidden border border-white/20 shadow-inner group">
        <img
          src={imageSrc}
          alt={title}
          className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent" />

        <div className="absolute top-3 left-3">
          <span className="px-3 py-1 text-xs font-semibold bg-white/20 backdrop-blur-md border border-white/30 rounded-full text-white">
            {badgeText}
          </span>
        </div>

        <div className="absolute bottom-4 left-4 right-4">
          <p className="text-xs font-medium text-cyan-400 uppercase tracking-widest">
            {category}
          </p>
          <h3 className="text-lg font-bold text-white mt-0.5">{title}</h3>
        </div>
      </div>
    </motion.div>
  );
}
```

---

### Recipe 5: Responsive Theme-Aware Gradient AreaChart
*Source: Refined from `jai1aiger/studio/src/app/dashboard/page.tsx`*

```tsx
"use client";

import React from "react";
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from "recharts";

interface ChartDataPoint {
  date: string;
  primaryMetric: number;
  secondaryMetric: number;
}

interface AnalyticsChartProps {
  data: ChartDataPoint[];
  primaryLabel?: string;
  secondaryLabel?: string;
}

export function ThemeAwareAnalyticsChart({
  data,
  primaryLabel = "Revenue",
  secondaryLabel = "Operating Costs",
}: AnalyticsChartProps) {
  return (
    <div className="w-full h-[360px] p-6 bg-card/60 backdrop-blur-md border border-border/60 rounded-2xl shadow-sm">
      <div className="mb-4">
        <h3 className="text-lg font-semibold tracking-tight">Financial Trajectory</h3>
        <p className="text-xs text-muted-foreground">Historical comparison over the selected billing period</p>
      </div>
      <ResponsiveContainer width="100%" height="85%">
        <AreaChart data={data} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
          <defs>
            <linearGradient id="primaryGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="hsl(var(--primary))" stopOpacity={0.4} />
              <stop offset="95%" stopColor="hsl(var(--primary))" stopOpacity={0.0} />
            </linearGradient>
            <linearGradient id="secondaryGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#06b6d4" stopOpacity={0.4} />
              <stop offset="95%" stopColor="#06b6d4" stopOpacity={0.0} />
            </linearGradient>
          </defs>
          <CartesianGrid strokeDasharray="3 3" stroke="hsl(var(--border))" opacity={0.5} />
          <XAxis dataKey="date" stroke="hsl(var(--muted-foreground))" fontSize={12} tickLine={false} />
          <YAxis stroke="hsl(var(--muted-foreground))" fontSize={12} tickLine={false} tickFormatter={(val) => `$${val}`} />
          <Tooltip
            contentStyle={{
              backgroundColor: "hsl(var(--card))",
              borderColor: "hsl(var(--border))",
              borderRadius: "0.75rem",
              boxShadow: "0 10px 25px -5px rgba(0, 0, 0, 0.2)",
              color: "hsl(var(--foreground))",
            }}
          />
          <Legend />
          <Area
            type="monotone"
            dataKey="primaryMetric"
            name={primaryLabel}
            stroke="hsl(var(--primary))"
            strokeWidth={2.5}
            fillOpacity={1}
            fill="url(#primaryGrad)"
          />
          <Area
            type="monotone"
            dataKey="secondaryMetric"
            name={secondaryLabel}
            stroke="#06b6d4"
            strokeWidth={2}
            fillOpacity={1}
            fill="url(#secondaryGrad)"
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}
```

---

## 5. Professional UI/UX Standards Checklist for Implementation

When utilizing the code and assets from these repositories to construct new websites, ensure compliance with these standard practices:

### 1. Typography & Hierarchy
* **Primary Headings**: Use high-contrast fonts (`Poppins`, `Montserrat`, or `Inter`) with tight tracking (`tracking-tight`) and balanced line-heights.
* **Body Copy**: Set readable sizes (`text-sm` or `text-base`), ample line-spacing (`leading-relaxed`), and muted foreground colors (`text-muted-foreground` / `text-gray-400`) to prevent eye fatigue.

### 2. Micro-Interactions & Haptics
* **Hover States**: Apply slight vertical offsets (`hover:-translate-y-1` or `hover:scale-[1.02]`) and soft shadow growth (`hover:shadow-lg`).
* **Active / Tap States**: Provide immediate visual confirmation using Framer Motion `whileTap={{ scale: 0.98 }}` or Tailwind `active:scale-95`.
* **Transitions**: Use consistent durations (`transition-all duration-200 ease-out`).

### 3. Accessible Color Systems & Contrast
* Maintain a minimum contrast ratio of **4.5:1** for normal text and **3:1** for large text against backgrounds (WCAG 2.1 AA).
* Define colors using **HSL CSS variables** (`--primary: 221.2 83.2% 53.3%`) to allow dynamic runtime theme switching without rewriting class rules.

### 4. GPU & WebGL Performance
* Set `pointer-events: none` on ambient 3D canvases to avoid capturing cursor inputs.
* Throttle WebGL rendering when elements leave the viewport using `IntersectionObserver`.
* Enable `sizeAttenuation` and vertex color buffers to minimize draw calls on mobile devices.

### 5. Conversational & Transactional Friction Reduction
* Never display raw HTTP or payment gateway error codes (`ERR_TXN_TIMED_OUT`) to end users. Translate them into empathetic, humanized guidance with single-click resolution actions.
* Preserve cart state and offer multi-channel recovery links (SMS / WhatsApp) for high-ticket transactions.

---

## 6. Summary Matrix: Repository Assets & Use Cases

| Capability | `jai1aiger/studio` | `jai1aiger/v0-url-intelligence-dashboard` | `jai1aiger/NORM` |
| :--- | :---: | :---: | :---: |
| **Component Suite (25+ UI Items)** | ✅ Primary Engine | ❌ (Selected components) | ❌ |
| **3D WebGL Particle Simulation** | ❌ | ✅ Primary Engine | ❌ |
| **Data Analytics (Recharts)** | ✅ Primary Engine | ❌ | ❌ |
| **Circular Animated Progress Gauges**| ❌ | ✅ Primary Engine | ❌ |
| **3D Perspective Isometric Previews** | ❌ | ✅ Primary Engine | ❌ |
| **Internationalization (i18n)** | ✅ Primary Engine | ❌ | ❌ |
| **Forms & Zod Validation** | ✅ Primary Engine | ❌ | ❌ |
| **Conversational Recovery UX** | ❌ | ❌ | ✅ Primary Engine |
| **Razorpay Instant Paylinks** | ❌ | ❌ | ✅ Primary Engine |
| **Mobile Slide Drawers & Command Palettes**| ✅ Sheet / Drawer | ✅ Vaul / cmdk | ❌ |

---

*Document compiled from live GitHub repository code and repository metadata for Pedini Sanjai Kumar (`@jai1aiger`).*
