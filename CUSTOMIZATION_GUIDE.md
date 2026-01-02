# MiBW Website - Maintenance & Customization Guide

## 🎯 Quick Access

**Live Website:** https://www.mibw.org  
**GitHub:** github.com/shuaibwaweru-glitch/mibw  
**Local Testing:** localhost:8000  

---

## 🎨 How to Customize

### Changing Colors

All colors are in `css/styles.css`. Search and replace:

```
Navy Blue (#1a3a52)   → Search for: #1a3a52 → Replace with: your-color
Teal (#4a9b8e)       → Search for: #4a9b8e → Replace with: your-color
Gold (#d4af37)       → Search for: #d4af37 → Replace with: your-color
Red (#d32f2f)        → Search for: #d32f2f → Replace with: your-color
```

### Changing Fonts

Edit the Google Fonts link in the `<head>` of any HTML file:

```html
<!-- Current fonts -->
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Inter:wght@400;500;700&display=swap" rel="stylesheet">

<!-- To change: visit fonts.google.com, select new fonts, and paste the link -->
```

### Adding Background Images

Edit hero section background in HTML (example from index.html):

```html
<!-- Current -->
<section class="ngo-hero" style="background: linear-gradient(...), url('https://images.unsplash.com/photo-...') center/cover;">

<!-- To change image: replace the URL with your image URL -->
<!-- Use your own images instead of Unsplash -->
```

### Updating Navigation

Navigation is consistent across all pages. To update menu items, edit:

```html
<nav>
  <ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="mission.html">About Us</a></li>
    <li><a href="activities.html">Programs</a></li>
    <!-- Add/remove/edit links here -->
  </ul>
</nav>
```

Make the same changes on ALL pages for consistency.

---

## 📝 Content Updates

### Homepage Updates
File: `index.html`
- Hero title: "Breaking the Silence"
- Hero subtitle: "Men's Mental Health Matters"
- Statistics: Update numbers in hero-stats section
- Why MiBW cards: Edit descriptions in why-grid section

### Activities/Programs Page
File: `activities.html`
- Program descriptions: Edit in large-program-card sections
- Success stories: Update in stories-grid section
- How to get started: Edit in steps-grid section

### Mission/About Page
File: `mission.html`
- Organization mission
- Core values
- Team information
- Contact details

---

## 🖼️ Image Management

### Current Images (Placeholder)
The site uses Unsplash images:
- Homepage hero: Community/team photo
- Activities hero: Meeting/workshop scene

### How to Replace with Your Images

1. Upload your image to your hosting (or use a CDN)
2. Find the hero section in HTML
3. Replace the Unsplash URL with your image URL

Example:
```html
<!-- Before -->
background: linear-gradient(...), url('https://images.unsplash.com/photo-...') center/cover;

<!-- After -->
background: linear-gradient(...), url('https://your-domain.com/images/your-photo.jpg') center/cover;
```

---

## 🚀 Deployment & Testing

### Local Testing
```bash
# Navigate to project directory
cd f:\Manwell

# Start Python HTTP server
python -m http.server 8000

# Visit in browser
http://localhost:8000
```

### Testing Checklist
- [ ] All pages load (HTTP 200)
- [ ] Navigation works on all pages
- [ ] Mobile responsive on all sizes
- [ ] Animations are smooth
- [ ] Images load properly
- [ ] Colors look right
- [ ] Favicon displays

### Pushing Changes to Live
```bash
# Add all changes
git add -A

# Commit with message
git commit -m "Update: Your changes here"

# Push to GitHub (auto-deploys to www.mibw.org)
git push origin main
```

---

## 📊 CSS Structure

### Main Stylesheet: `css/styles.css`

**Sections:**
1. Global Reset & Typography
2. Header & Navigation
3. Hero Sections & Animations
4. Component Styles (cards, buttons, etc.)
5. Program Section Styles
6. Footer Styles
7. Responsive Breakpoints
8. Utility Classes

### Key Classes to Know
```css
.ngo-hero              /* Hero section styling */
.section-container     /* Content wrapper (max-width 1400px) */
.why-grid              /* Reason cards grid */
.program-card          /* Individual program cards */
.cta-primary           /* Gold primary button */
.cta-secondary         /* Transparent secondary button */
.section-title         /* Section heading styling */
```

---

## 🎬 Animation Guide

### CSS Animations Available

**slideInLeft** - Content slides in from left
**slideInRight** - Content slides in from right
**float** - Continuous floating animation
**fadeInUp** - Fade in while moving up

### How to Add Animations

```css
/* Apply animation to element */
.your-element {
  animation: slideInLeft 0.8s ease-out;
  /* other styles */
}
```

---

## 📱 Responsive Design Breakpoints

```css
Desktop:     1024px+   (full layout)
Tablet:      768px-1023px (medium layout)
Mobile:      768px or less (mobile layout)
Small Phone: 480px or less (minimal layout)
```

### Testing Responsive Design
- Use browser DevTools (F12 → toggle device toolbar)
- Test on actual devices
- Check both portrait and landscape
- Verify touch interactions on mobile

---

## 🔐 Security & Performance

### Best Practices
1. **Keep images optimized** (compress before uploading)
2. **Use HTTPS** (Vercel handles this automatically)
3. **Don't store sensitive data** in client-side code
4. **Test changes locally** before pushing to GitHub
5. **Keep backups** of important changes

### Performance Tips
1. Optimize images (use tools like TinyPNG)
2. Use modern image formats (WebP, AVIF)
3. Minimize CSS/JS when ready for production
4. Cache-bust CSS if making style changes
5. Use CDN for images if possible

---

## 🐛 Troubleshooting

### Page Not Loading
- Check file path is correct
- Verify filename matches link (case-sensitive on servers)
- Clear browser cache (Ctrl+Shift+Delete)
- Check browser console for errors (F12)

### Styles Not Applying
- Make sure CSS file path is correct: `css/styles.css`
- Clear browser cache
- Check for CSS typos
- Verify selectors match HTML elements

### Mobile Not Responsive
- Check viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Test in browser DevTools
- Clear CSS cache
- Check media queries

### Images Not Showing
- Verify image URL is correct
- Check if image file exists
- Use full URLs (not relative paths) for external images
- Try different image formats

---

## 📞 Useful Resources

### Google Fonts
- Visit: fonts.google.com
- Choose fonts
- Copy the link
- Paste in HTML `<head>`

### Color Tools
- ColorHunt.co - Color palettes
- Coolors.co - Color schemes
- WebAIM - Color contrast checker

### Image Sources
- Unsplash.com - Free photos
- Pexels.com - Free photos
- Pixabay.com - Free photos
- Your own photos - Best option!

### CSS Tools
- CodePen.io - CSS experiments
- CSS-Tricks.com - CSS learning
- MDN Web Docs - Complete reference

---

## 📋 File Locations

```
f:\Manwell\
├── index.html                    (Homepage)
├── mission.html                  (About page)
├── activities.html               (Programs page) ← NEW
├── community.html                (Community forum)
├── therapist-directory.html      (Find therapist)
├── crisis.html                   (Crisis support)
├── assessments.html              (Self-assessment)
├── mental-health-hub.html        (Education)
├── experts.html                  (Expert board)
├── videos.html                   (Videos/podcasts)
├── resources.html                (Downloads)
├── gallery.html                  (Photos)
├── stories.html                  (Testimonials)
├── css/
│   ├── styles.css               (Modern design system)
│   └── styles-old.css           (Backup of old styles)
├── assets/
│   ├── favicon.svg              (Logo in tab)
│   ├── images/                  (Image files)
│   └── videos/                  (Video files)
├── data/
│   └── content.json             (Content data)
├── js/
│   └── script.js                (JavaScript)
├── .git/                        (Git repository)
└── README.md                    (Project info)
```

---

## ✅ Checklist Before Publishing Major Changes

- [ ] Test all pages locally
- [ ] Check on mobile devices
- [ ] Verify all links work
- [ ] Test forms and interactive elements
- [ ] Check image loading
- [ ] Verify animations are smooth
- [ ] Check color contrast (accessibility)
- [ ] Test on different browsers
- [ ] Commit changes to Git
- [ ] Push to GitHub
- [ ] Verify live at www.mibw.org
- [ ] Announce changes to team

---

## 🎓 Learning Resources

### Web Development
- MDN Web Docs: https://developer.mozilla.org
- W3Schools: https://w3schools.com
- FreeCodeCamp: https://freecodecamp.org

### Design
- Dribbble: https://dribbble.com (inspiration)
- Behance: https://behance.net (portfolios)
- Design Thinking Guide: https://nngroup.com

### Git & GitHub
- GitHub Docs: https://docs.github.com
- Git Tutorial: https://git-scm.com/doc
- GitHub Pages: https://pages.github.com

---

## 💬 Getting Help

### If Something Breaks
1. Check the error in browser console (F12)
2. Verify file paths are correct
3. Check Git status: `git status`
4. Review recent changes: `git log --oneline -5`
5. Revert changes if needed: `git revert [commit-hash]`

### Common Issues
- **CSS not updating?** Clear cache (Ctrl+Shift+Delete)
- **Page not found?** Check filename spelling
- **Image not showing?** Verify image URL and file exists
- **Animation jerky?** Check browser performance
- **Mobile broken?** Test viewport meta tag

---

## 🎉 You're All Set!

Your MiBW website is now a professional, modern NGO platform. Use this guide to customize, maintain, and improve it over time.

**Remember:** Always test locally before deploying to the live site!

---

*Last Updated: January 3, 2026*  
*Version: 1.0 - Complete Redesign*  
*Status: Production Ready*