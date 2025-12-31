# Manwell Development Workflow

A guide for developers working on the Manwell project.

---

## Project Philosophy

**Manwell is a static website built for speed, control, and emotional impact.**

- No frameworks or dependencies beyond vanilla HTML, CSS, and JavaScript
- Every design choice serves the brand message
- The code should feel like "a monastic text illuminated by firelight"
- Quality > Quantity. Simplicity > Complexity.

---

## Development Environment Setup

### 1. Clone & Install

```bash
# Clone repository
git clone https://github.com/manwell/manwell.git
cd manwell

# No npm install needed! This is a static site.
# Optional: Install dev tools if extending the project
npm install (optional for future build tools)
```

### 2. Run Locally

```bash
# Option A: Python built-in server
python -m http.server 8000

# Option B: Node.js HTTP Server
npx http-server

# Option C: VS Code Live Server
# Right-click index.html > "Open with Live Server"
```

Then visit: `http://localhost:8000`

### 3. Verify Everything Works

- [ ] `index.html` loads and displays correctly
- [ ] Navigation links work
- [ ] No console errors (F12)
- [ ] Mobile responsiveness (DevTools F12)
- [ ] All videos embed correctly

---

## File Structure Overview

```
manwell/
├── index.html              # Landing page (hero + triptych + videos)
├── mission.html            # Mission & foundational texts
├── community.html          # Newsletter signup
├── 404.html                # Error page
├── css/
│   └── styles.css          # All styling (no Tailwind/Bootstrap)
├── js/
│   └── script.js           # All interactivity (vanilla JS)
├── assets/
│   ├── images/             # .webp optimized images
│   └── videos/             # Hero video backdrop
├── data/
│   └── content.json        # Dynamic content (optional)
├── docs/
│   ├── README.md           # Project overview
│   ├── SETUP.md            # Integration guide
│   ├── DEPLOYMENT.md       # Deployment instructions
│   └── WORKFLOW.md         # This file
├── .gitignore
├── package.json            # Meta info + optional scripts
├── robots.txt              # SEO: crawler directives
└── sitemap.xml             # SEO: page index
```

---

## Adding New Pages

### 1. Create HTML File

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Page description">
  <title>Page Title - Manwell</title>
  
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <!-- Header (copy from existing page) -->
  <header>
    <!-- ... -->
  </header>

  <!-- Your content -->
  <section class="content-section">
    <!-- ... -->
  </section>

  <!-- Footer (copy from existing page) -->
  <footer>
    <!-- ... -->
  </footer>

  <script src="js/script.js"></script>
</body>
</html>
```

### 2. Update Navigation Links

In `<header>`, update all `<nav>` elements to include link to new page:
```html
<li><a href="newpage.html">Page Title</a></li>
```

### 3. Add to Sitemap

Update `sitemap.xml`:
```xml
<url>
  <loc>https://manwell.com/newpage.html</loc>
  <lastmod>2025-12-31</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.7</priority>
</url>
```

### 4. Commit

```bash
git add newpage.html sitemap.xml
git commit -m "feat: Add new page - page title"
```

---

## Modifying Styles

All styles are in `css/styles.css`. Organization:

```css
/* 1. Global reset & typography */
/* 2. Header & navigation */
/* 3. Hero section */
/* 4. Content sections */
/* 5. Forms */
/* 6. Animations */
/* 7. Responsive design */
```

### Example: Changing Accent Color

```css
/* Find and replace #ff5a09 (Forge Orange) */
.cta-button {
  background-color: #ff5a09;  /* Change this */
}

.pillar:hover {
  border-color: rgba(255, 90, 9, 0.5);  /* And this */
}
```

### Testing Responsive Design

- Desktop: Full width (1200px+)
- Tablet: 768px - 1024px
- Mobile: 480px - 767px

DevTools: F12 > Toggle Device Toolbar (Ctrl+Shift+M)

---

## Adding Interactivity

All JavaScript in `js/script.js`. Structure:

```javascript
// 1. Mobile menu toggle
// 2. Reveal on scroll
// 3. Smooth scroll
// 4. Form handling
// 5. Lazy loading
// 6. Header effects
// 7. Parallax
// 8. Social links
```

### Example: Add Click Handler

```javascript
// In js/script.js
document.querySelector('.my-button').addEventListener('click', () => {
  console.log('Button clicked!');
  // Do something
});
```

### Example: Add Scroll Effect

```javascript
window.addEventListener('scroll', () => {
  const scrollTop = window.pageYOffset;
  console.log('Scroll position:', scrollTop);
  // Do something based on scroll
});
```

**Note:** All JS is vanilla. No jQuery, React, Vue, etc.

---

## Content Updates

### Update Text Content

Edit HTML directly in the `.html` files. Example:

```html
<!-- Before -->
<h1>Old Heading</h1>

<!-- After -->
<h1>New Heading</h1>
```

### Update Dynamic Content

Use `data/content.json` for content that changes frequently:

```json
{
  "brand": {
    "tagline": "Not healed. Forged."
  }
}
```

Then load in JS:
```javascript
fetch('data/content.json')
  .then(res => res.json())
  .then(data => {
    document.querySelector('.tagline').textContent = data.brand.tagline;
  });
```

### Update Social Links

Find in `community.html` or `index.html`:
```html
<a href="https://instagram.com/YOUR_USERNAME">...</a>
```

---

## Working with Images

### Optimization Requirements

All images should be:
1. Optimized (compressed)
2. In `.webp` format (best) or `.jpg` (acceptable)
3. Responsive (multiple sizes if needed)
4. Lazy loaded (use `data-src` attribute)

### Converting to WebP

```bash
# Using ImageMagick
convert image.jpg -quality 85 image.webp

# Using online tools
# https://cloudconvert.com/jpg-to-webp
```

### Using Images in HTML

```html
<!-- Regular image -->
<img src="assets/images/logo.webp" alt="Manwell Logo" width="200" height="100">

<!-- Lazy loaded image -->
<img src="placeholder.webp" data-src="assets/images/real-image.webp" class="lazy-load" alt="Description">
```

---

## Working with Videos

### Don't Host Videos Locally

**Instead:** Host on YouTube/TikTok and embed via API.

Benefits:
- Faster (CDN delivery)
- Better monetization (YouTube)
- Reduced server load
- Analytics included

### Embedding YouTube

```html
<iframe 
  src="https://www.youtube.com/embed/VIDEO_ID?modestbranding=1&rel=0"
  title="Video Title"
  allowfullscreen=""
  loading="lazy"
></iframe>
```

### Hero Video Fallback

If you need a background video, keep it short (<5MB):

```html
<video class="hero-video" autoplay muted loop playsinline>
  <source src="assets/videos/hero.mp4" type="video/mp4">
</video>
```

---

## Version Control (Git)

### Basic Workflow

```bash
# 1. Make changes to files
# Edit index.html, css/styles.css, etc.

# 2. Check what changed
git status

# 3. Stage changes
git add index.html css/styles.css

# Or stage everything
git add .

# 4. Commit with message
git commit -m "feat: Update hero headline"

# 5. Push to remote
git push origin main
```

### Commit Message Format

```
<type>: <short description>

<optional longer description>
```

Types:
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `style` - CSS/formatting only
- `refactor` - Code restructuring (no feature change)
- `perf` - Performance improvement

Examples:
```bash
git commit -m "feat: Add reveal-on-scroll animation"
git commit -m "fix: Mobile menu not closing properly"
git commit -m "docs: Update README with API endpoints"
git commit -m "style: Improve button hover effect"
```

### Viewing History

```bash
# View recent commits
git log --oneline -10

# View detailed commit
git show <commit-hash>

# View changes between commits
git diff <commit1> <commit2>

# View all branches
git branch -a
```

---

## Testing

### Manual Testing Checklist

- [ ] **Desktop**: All pages load, no console errors
- [ ] **Mobile**: Responsive, touch-friendly, readable
- [ ] **Navigation**: All links work
- [ ] **Videos**: All embeds play correctly
- [ ] **Forms**: Can submit newsletter form
- [ ] **Performance**: PageSpeed >90
- [ ] **Accessibility**: Text readable, colors contrasting
- [ ] **Cross-browser**: Chrome, Firefox, Safari, Edge

### Browser Testing

```bash
# Chrome DevTools
F12 > Console (check for errors)

# Toggle mobile view
Ctrl+Shift+M (Windows) or Cmd+Shift+M (Mac)

# Lighthouse audit
F12 > Lighthouse > Generate report
```

### Performance Testing

1. **Google PageSpeed Insights**
   - https://pagespeed.web.dev
   - Aim for >90 on both mobile and desktop

2. **WebPageTest**
   - https://webpagetest.org
   - Detailed waterfall analysis

3. **Lighthouse (Built-in)**
   - F12 > Lighthouse
   - Performance, Accessibility, SEO, Best Practices

---

## Debugging

### Console Debugging

```javascript
console.log('Value:', someVariable);
console.error('Error message:', error);
console.warn('Warning:', issue);
console.table(arrayOfObjects);
```

### Browser DevTools (F12)

- **Console**: See errors and logs
- **Elements**: Inspect HTML structure
- **Styles**: See applied CSS
- **Network**: Check file downloads
- **Performance**: See render times
- **Accessibility**: Check contrast, labels

### Common Issues

**Issue:** Styles not applying
- Solution: Hard refresh (Ctrl+Shift+Delete) or check file path

**Issue:** JavaScript not running
- Solution: Check console for errors, verify file is linked

**Issue:** Mobile menu not closing
- Solution: Check z-index and event listeners

**Issue:** Videos not loading
- Solution: Check embed URL, verify YouTube/TikTok video exists

---

## Creating Features

### Feature Checklist

1. **Plan**
   - What should it do?
   - Where should it go?
   - How will it look?

2. **Develop**
   - Create HTML structure
   - Add CSS styles
   - Add JavaScript interactivity

3. **Test**
   - Manual browser testing
   - Mobile responsiveness
   - Performance check
   - Cross-browser compatibility

4. **Document**
   - Update README if needed
   - Add comments to complex code

5. **Commit**
   ```bash
   git add .
   git commit -m "feat: Description of feature"
   ```

---

## Performance Optimization

### Key Metrics

- **PageSpeed**: >90
- **Time to First Byte (TTFB)**: <200ms
- **Largest Contentful Paint (LCP)**: <2.5s
- **Cumulative Layout Shift (CLS)**: <0.1

### Optimization Techniques

1. **Images**
   - Convert to `.webp`
   - Compress ruthlessly
   - Use correct dimensions
   - Lazy load

2. **JavaScript**
   - Minimize HTTP requests
   - Defer non-critical scripts
   - Remove unused code

3. **CSS**
   - Avoid heavy selectors
   - Minimize repaints/reflows
   - Use hardware acceleration

4. **Server**
   - Enable GZIP compression
   - Use CDN
   - Cache static assets
   - Minimize redirects

---

## Deployment Process

### Before Deploying

```bash
# 1. Test locally
python -m http.server 8000

# 2. Check console
# F12 > Console (no errors?)

# 3. Run PageSpeed
# https://pagespeed.web.dev

# 4. Verify all links work

# 5. Commit changes
git add .
git commit -m "release: v1.0.0 - Ready for deployment"

# 6. Push to GitHub
git push origin main
```

### Deploy to Netlify

1. Connect GitHub repository
2. Automatic deployment on push

### Deploy to GitHub Pages

1. Push to `main` branch
2. Site updates automatically

---

## Communication & Updates

### Updating the Team

When making significant changes:

```bash
# Write descriptive commit messages
git commit -m "feat: Add dark mode toggle

- New CSS class for light mode
- Persists preference in localStorage
- Works on all pages
"

# Push and share
git push origin main
```

### Documenting Changes

Update relevant documentation:
- README.md (if project structure changes)
- SETUP.md (if integration instructions change)
- DEPLOYMENT.md (if deployment process changes)
- Code comments (for complex logic)

---

## Resources

- [HTML Reference](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS Reference](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Git Guide](https://git-scm.com/doc)
- [Web.dev Best Practices](https://web.dev/)

---

## Questions?

Refer to:
1. README.md - Project overview
2. SETUP.md - Integration guide
3. DEPLOYMENT.md - Deployment instructions
4. Code comments - Inline documentation
5. Git log - Recent changes

---

**Manwell. Father Yourself.**

Code with intention. Every line serves the mission.
