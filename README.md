# Manwell - Digital Forge for Modern Masculinity

A digital sanctuary and portal for men confronting the silent crisis of modern masculinity. Not a self-help brand, but a call to sovereignty.

## Project Overview

**Manwell** is a static website serving as the digital home for a movement focused on authentic masculinity, inner work, and fathering oneself. The website establishes brand ethos, showcases video content, builds email community, and directs traffic to social channels.

## Core Brand Attributes

- **Tone**: Deep, unfiltered, poetic, sovereign. No "bro" energy or toxic positivity.
- **Visual Style**: High-contrast, textured, atmospheric (shadows, raw materials, dawn/dusk light).
- **Philosophy**: Not healed. **Forged.**

## Tech Stack

- **HTML5** - Semantic, clean markup
- **CSS3** - Custom styling with CSS Grid/Flexbox
- **Vanilla JavaScript** - No frameworks, focus on performance
- **Git** - Version control from day one

## Directory Structure

```
manwell/
├── index.html              # Landing page - "The Confrontation"
├── mission.html            # Mission page - "The Blueprint"
├── community.html          # Newsletter signup - "The Séance"
├── css/
│   └── styles.css          # Main stylesheet
├── js/
│   └── script.js           # Core interactivity
├── assets/
│   ├── images/             # Images (compressed .webp format)
│   └── videos/             # Hero video backdrops
├── data/
│   └── content.json        # Dynamic content (optional)
├── .gitignore
└── README.md
```

## Pages

### 1. Landing Page (`index.html`)
The Confrontation. Hero section with video backdrop, triptych (The Performance, Transactional Worth, The Unfought War), and video portal.

### 2. Mission Page (`mission.html`)
The Blueprint. Deep foundational texts and mission statement. Explains the "why" behind Manwell.

### 3. Community Page (`community.html`)
The Séance. Weekly email signup. One deep text. One hard truth. One question.

## Getting Started

### Prerequisites
- A modern web browser
- Optional: A local server (e.g., `python -m http.server` or VS Code Live Server)

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd manwell
   ```

2. Open `index.html` in your browser or run a local server:
   ```bash
   python -m http.server 8000
   ```
   Then visit `http://localhost:8000`

## Development

### Adding Content

- **Texts**: Edit HTML sections directly in the `.html` files
- **Videos**: Replace YouTube embed URLs in the video grid section
- **Colors & Typography**: Modify CSS variables in `css/styles.css`
- **Interactivity**: Extend `js/script.js` as needed

### Performance Optimization

- All images should be compressed and converted to `.webp` format
- Videos should be optimized for web (consider hosting on YouTube/TikTok)
- Lazy loading is implemented for images
- PageSpeed target: >90

### Responsive Design

The site is fully responsive from mobile (480px) to desktop and beyond. Media queries are defined in `css/styles.css`.

## Brand Colors

- **Charcoal Black**: `#1a1a1a` - Primary background
- **Stone Gray**: `#4a4a4a` - Secondary text
- **Ash**: `#c0c0c0` - Body text
- **Forge Orange**: `#ff5a09` - CTA accents
- **Deep Ember Red**: `#B22222` - Alternative accent (optional)

## Typography

- **Headlines**: Playfair Display (serif) - Bold, strong presence
- **Body**: Inter (sans-serif) - Clean, readable

## Integration Points

### Newsletter
- Email form is currently a placeholder
- **Next Step**: Integrate with Mailchimp, ConvertKit, or similar API
- Form submission handled in `js/script.js`

### Social Links
- Update social media URLs in footer and video section
- Current placeholders: Instagram, TikTok, YouTube, Email

### Video Embeds
- Uses YouTube IFrame API for unified player
- Can be extended with Instagram/TikTok embeds using their official APIs

## Git Workflow

Initialize and track all changes:
```bash
git status                    # See current state
git add <file>               # Stage files
git commit -m "message"      # Commit with message
git log                       # View history
```

Example commits:
```bash
git commit -m "init: Set up project structure and core pages"
git commit -m "feat: Add hero section with video backdrop"
git commit -m "style: Implement brand color palette and typography"
git commit -m "feat: Add reveal-on-scroll animation"
```

## Deployment

This is a static site and can be deployed to:

- **GitHub Pages** - Free, simple
- **Netlify** - Fast, automatic deployments
- **Vercel** - Optimized for static content
- **AWS S3 + CloudFront** - Scalable

Example for GitHub Pages:
1. Push to a GitHub repository
2. Go to Settings > Pages
3. Select `main` branch as source

## Future Enhancements

- [ ] Newsletter API integration (Mailchimp/ConvertKit)
- [ ] Instagram/TikTok embed APIs for dynamic video feed
- [ ] Blog section with markdown-based content
- [ ] SEO optimization (meta tags, structured data)
- [ ] Analytics integration (Google Analytics, Plausible)
- [ ] Dark/Light mode toggle
- [ ] Multi-language support

## Philosophy

Every design choice serves the core message: **sovereignty through confrontation and inner work.** The site should feel like a "monastic text illuminated by firelight"—substantial, quiet, and powerful.

## Contact & Links

- **Email**: contact@manwell.com
- **Instagram**: @manwell_
- **TikTok**: @manwell_
- **YouTube**: Manwell Channel

---

**Manwell. © 2025. Father Yourself.**

*A digital forge for men who refuse to perform.*
