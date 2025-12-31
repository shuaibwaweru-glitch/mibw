# Manwell Website - Design Overview

## 🎨 Brand Colors

### Primary Colors
- **Navy Blue (Primary Dark):** `#1a3a52` - Headers, footer background
- **Teal (Accent):** `#4a9b8e` - Buttons, links, accents
- **White (Background):** `#ffffff` - Main background

### Secondary Colors
- **Slate Gray (Text):** `#2c3e50` - Primary text color
- **Medium Gray (Secondary Text):** `#6b7a8a` - Descriptive text
- **Light Gray (Secondary Text):** `#4a5568` - Body text
- **Off-White (Light Background):** `#f8f9fa` - Card backgrounds
- **Border Gray:** `#e8f0f5` - Borders and dividers

---

## 📐 Design System

### Typography

**Font Stack:** Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| H1 (Page Title) | 3.5rem (56px) | 800 | Navy #1a3a52 |
| H2 (Section) | 2.2rem (35px) | 700 | Navy #1a3a52 |
| H3 (Subsection) | 1.5rem (24px) | 600 | Navy #1a3a52 |
| Body Text | 1rem (16px) | 400 | Slate #2c3e50 |
| Small Text | 0.95rem (15px) | 400 | Medium #6b7a8a |

**Line Height:** 1.7-1.8 for body text, 1.25 for headings

---

## 🎯 Component Styling

### Buttons (CTA)
- **Background:** Teal (#4a9b8e)
- **Text:** White
- **Padding:** 1rem 2.5rem
- **Border Radius:** 4px
- **Hover:** Navy (#1a3a52) background, shadow effect
- **Transition:** 0.4s ease

### Cards & Containers
- **Background:** White or Off-White (#f8f9fa)
- **Border:** 1px solid #e8f0f5
- **Border Radius:** 8px (cards), 4px (sections)
- **Padding:** 2-2.5rem
- **Shadow:** Subtle on hover
- **Transition:** 0.4-0.5s ease

### Links
- **Color:** Teal (#4a9b8e)
- **Hover:** Navy (#1a3a52)
- **Text Decoration:** None → Underline on hover
- **Transition:** 0.3s ease

### Form Inputs
- **Border:** 1px solid #e8f0f5
- **Background:** White
- **Text Color:** Navy #1a3a52
- **Focus Border:** Teal (#4a9b8e)
- **Focus Background:** Light Off-White (#f8f9fa)
- **Focus Shadow:** `0 0 8px rgba(74, 155, 142, 0.15)`
- **Border Radius:** 4px

### Navigation
- **Background:** White
- **Border Bottom:** 1px solid #e8f0f5
- **Link Color:** Slate #4a5568
- **Hover Color:** Navy #1a3a52
- **Underline Accent:** Teal (#4a9b8e)

### Footer
- **Background:** Navy Blue (#1a3a52)
- **Text:** Light (#b8c5d6)
- **Accent:** Teal (#4a9b8e)

---

## 🏗️ Layout Grid

- **Max Width:** 1400px (full width)
- **Container Max:** 1200px (content sections)
- **Padding:** 2rem (standard)
- **Padding Large:** 6rem (section vertical)
- **Gap:** 2-3rem (grid items)

### Responsive Breakpoints
- **Desktop:** 1024px+
- **Tablet:** 768px - 1023px
- **Mobile:** 480px - 767px
- **Small Mobile:** <480px

---

## 🎬 Animations & Transitions

### Hover Effects
- **Buttons:** `translateY(-2px)` + shadow
- **Cards:** `translateY(-5px)` + shadow increase
- **Links:** Underline width increase (0 → 100%)
- **Social Icons:** `translateY(-3px)` + shadow

### Page Load
- **Fade In Up:** 1.5s ease-out
- **Reveal on Scroll:** 0.8s ease

### Transitions
- Default timing: `0.3s-0.5s ease`
- Button hover: `0.4s ease`
- Card hover: `0.5s ease`

---

## 📱 Responsive Design

### Header
- **Desktop:** Fixed position, full navigation
- **Tablet:** Fixed, slightly reduced padding
- **Mobile:** Fixed, hamburger menu toggle

### Hero Section
- **Desktop:** 100vh height, full viewport
- **Tablet:** 80vh height
- **Mobile:** 60vh height, larger padding

### Triptych (3 Columns)
- **Desktop:** 3 columns (`repeat(3, 1fr)`)
- **Tablet/Mobile:** 1 column (stacked)
- **Gap:** 2rem → 2.5rem on desktop

### Video Grid
- **Desktop:** Auto-fit (`minmax(300px, 1fr)`)
- **Mobile:** 1 column

---

## 🖼️ Logo Specifications

### Logo File
- **Format:** SVG (scalable)
- **Path:** `assets/images/logo.svg`
- **Size in Header:** 40px height
- **Colors:** Navy (#1a3a52) + Teal (#4a9b8e)

### Usage
- Appears in header on all pages
- Next to or before "Manwell" text
- Maintained aspect ratio
- Can scale to any size without loss

---

## 📊 Spacing System

**Vertical Spacing:**
- XS: 0.5rem
- S: 1rem
- M: 1.5rem
- L: 2rem
- XL: 3rem
- XXL: 6rem (section padding)

**Horizontal Spacing:**
- Padding: 2rem (standard)
- Section max width: 900px
- Container max width: 1200px

---

## 🎨 Minimalist Principles

1. **Whitespace First** - Generous negative space
2. **One Accent Color** - Teal used consistently
3. **Limited Typography** - Single font family
4. **Clean Lines** - Minimal borders (light gray)
5. **Subtle Shadows** - No dramatic effects
6. **Simple Icons** - Emoji or simple symbols
7. **No Gradients** - Solid colors only
8. **Clear Hierarchy** - Typography and spacing

---

## ✅ Best Practices

### Color Usage
- Navy (#1a3a52): Headlines, footer, primary UI
- Teal (#4a9b8e): CTAs, links, accents
- Gray (#6b7a8a): Body text
- White/Off-White: Backgrounds

### Typography
- Headlines: Sans-serif, Navy, Bold
- Body: Sans-serif, Gray, Regular
- Small text: Sans-serif, Medium Gray, Regular

### Spacing
- Consistent padding (2rem standard)
- Generous whitespace
- Breathing room around elements
- Balanced margins

### Interactions
- Smooth transitions (0.3-0.5s)
- Subtle shadow effects
- Consistent hover states
- Clear focus states for inputs

---

## 🚀 Development Reference

### CSS Custom Properties (Recommended)
```css
:root {
  --color-navy: #1a3a52;
  --color-teal: #4a9b8e;
  --color-text: #2c3e50;
  --color-gray: #6b7a8a;
  --color-border: #e8f0f5;
  --color-bg-light: #f8f9fa;
  
  --font-family: 'Inter', sans-serif;
  --font-size-base: 1rem;
  --line-height-base: 1.7;
  
  --spacing-xs: 0.5rem;
  --spacing-s: 1rem;
  --spacing-m: 1.5rem;
  --spacing-l: 2rem;
  --spacing-xl: 3rem;
  --spacing-xxl: 6rem;
  
  --radius-sm: 4px;
  --radius-md: 8px;
  
  --transition: 0.3s ease;
  --transition-slow: 0.5s ease;
}
```

### Hex Color Reference
```
Navy:           #1a3a52
Teal:           #4a9b8e
Slate:          #2c3e50
Medium Gray:    #4a5568
Light Gray:     #6b7a8a
Border:         #e8f0f5
Light BG:       #f8f9fa
White:          #ffffff
```

---

## 📋 Checklist for New Components

When adding new components, ensure:
- ✅ Uses Navy, Teal, or Gray colors
- ✅ Sans-serif typography (Inter)
- ✅ Proper spacing (2rem standard)
- ✅ Soft borders (#e8f0f5)
- ✅ Light backgrounds (#f8f9fa or white)
- ✅ Smooth transitions (0.3-0.5s)
- ✅ Responsive design (mobile-first)
- ✅ Accessible contrast ratios
- ✅ No unnecessary gradients
- ✅ Minimalist aesthetic

---

**Design Status:** ✅ Complete and implemented  
**Last Updated:** December 31, 2025  
**Version:** 1.0 (Modern Minimalist Redesign)
