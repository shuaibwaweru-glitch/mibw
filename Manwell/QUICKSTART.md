# Manwell - Quick Start Guide

**Welcome to the forge.** This quick start will get you up and running in under 5 minutes.

---

## 1. Start Development Server

```bash
cd f:\Manwell

# Option A: Python (most common)
python -m http.server 8000

# Option B: Node.js (if installed)
npx http-server

# Option C: VS Code
# Right-click index.html > "Open with Live Server"
```

**Then open:** `http://localhost:8000`

---

## 2. File Structure at a Glance

```
Manwell/
├── index.html              ← Landing page (START HERE)
├── mission.html            ← Mission & philosophy
├── community.html          ← Newsletter signup
├── 404.html                ← Error page
├── css/styles.css          ← All styling
├── js/script.js            ← All interactivity
├── data/content.json       ← Dynamic content
├── assets/                 ← Images, videos
├── README.md               ← Project overview
├── SETUP.md                ← Integration guide
├── DEPLOYMENT.md           ← Deployment instructions
└── WORKFLOW.md             ← Development guide
```

---

## 3. Key Technologies

- **HTML5** - Semantic markup
- **CSS3** - Grid, Flexbox, animations
- **JavaScript** - Vanilla (no frameworks)
- **Git** - Version control

**No frameworks. No build step. Pure, fast, focused.**

---

## 4. Brand Colors

```
Charcoal Black:   #1a1a1a   (backgrounds)
Stone Gray:       #4a4a4a   (secondary text)
Ash:              #c0c0c0   (body text)
Forge Orange:     #ff5a09   (CTAs & accents)
```

---

## 5. Typography

```
Headings:  Playfair Display (serif) - Bold, strong
Body:      Inter (sans-serif) - Clean, readable
```

---

## 6. Making Changes

### Update Text
Edit `.html` files directly.

### Update Styles
Edit `css/styles.css` and refresh browser (Ctrl+Shift+Delete hard refresh).

### Add Interactivity
Edit `js/script.js` - vanilla JavaScript only.

### Add Images
Save to `assets/images/`, optimize as `.webp`, use lazy loading.

### Add Videos
Embed from YouTube/TikTok, don't host locally.

---

## 7. Version Control

```bash
# Check status
git status

# Add changes
git add .

# Commit
git commit -m "feat: Your change description"

# View history
git log --oneline
```

**Commit Message Format:**
```
feat: New feature
fix: Bug fix
docs: Documentation
style: CSS/formatting
```

---

## 8. Testing

### Desktop
- Open in browser
- F12 Console (check for errors)
- Check all links work

### Mobile
- F12 > Toggle Device Toolbar (Ctrl+Shift+M)
- Test on actual phone if possible

### Performance
- PageSpeed Insights: https://pagespeed.web.dev
- Target: >90 score

---

## 9. Deploy When Ready

When you're ready to go live:

### Option A: GitHub Pages (Free)
```bash
git push origin main
# Site auto-deploys
```

### Option B: Netlify (Recommended)
1. Sign up at netlify.com
2. Connect GitHub repository
3. Auto-deploys on push

### Option C: Traditional Hosting
Upload files via FTP to your host.

**See DEPLOYMENT.md for full guide.**

---

## 10. Integrations to Add

These are optional but recommended:

- [ ] **Newsletter Email** - Mailchimp/ConvertKit (SETUP.md)
- [ ] **Analytics** - Google Analytics (SETUP.md)
- [ ] **SEO** - Meta tags & structured data (SETUP.md)
- [ ] **Domain** - Custom domain name (DEPLOYMENT.md)

---

## 11. File Sizes & Performance

Current project is **~80KB** uncompressed:
- HTML: ~23KB
- CSS: ~10.8KB
- JavaScript: ~4.7KB
- Documentation: ~36KB

**Goal:** Keep total site <500KB with all assets.

---

## 12. Next Steps

1. **Explore**
   - Open `index.html` in browser
   - Click around, test responsiveness
   - Read the content

2. **Customize**
   - Update social links
   - Change hero video URL
   - Update email contact
   - Adjust colors if desired

3. **Test**
   - F12 > Console (no errors?)
   - Test on mobile
   - Run PageSpeed Insights

4. **Deploy**
   - Choose hosting platform
   - Follow DEPLOYMENT.md
   - Test live site

---

## 13. Helpful Resources

| Resource | Purpose |
|----------|---------|
| README.md | Project overview & structure |
| SETUP.md | API integrations & configuration |
| DEPLOYMENT.md | Hosting & deployment options |
| WORKFLOW.md | Developer workflow & best practices |
| css/styles.css | Design tokens & theming |
| js/script.js | Reusable utility functions |

---

## 14. Common Questions

**Q: Can I use React/Vue/Tailwind?**  
A: This project intentionally avoids frameworks for speed and control. Use vanilla HTML/CSS/JS.

**Q: How do I add a blog?**  
A: Create blog posts as HTML files, or use `data/content.json` to load dynamic content.

**Q: How do I change the accent color?**  
A: Replace `#ff5a09` (Forge Orange) throughout `css/styles.css`.

**Q: How do I host videos?**  
A: Don't. Use YouTube, TikTok, or Instagram embeds instead.

**Q: How do I collect emails?**  
A: Integrate with Mailchimp/ConvertKit (see SETUP.md).

---

## 15. Support

- Check the relevant documentation file (README, SETUP, DEPLOYMENT, WORKFLOW)
- Search code comments for `TODO` or `NOTE`
- View git history: `git log --oneline`
- Read browser console (F12) for errors

---

## 16. Philosophy

> "Manwell is not a healing. It is a forge."

Every design choice serves this mission:
- **Deep**, not shallow
- **Sovereign**, not performing
- **Poetic**, not promotional
- **Real**, not fake
- **Forged**, not healed

Code with intention.

---

## You're Ready!

```bash
# 1. Start development server
python -m http.server 8000

# 2. Open browser
# http://localhost:8000

# 3. Make changes
# Edit HTML/CSS/JS

# 4. Test
# F12 Console, responsive testing

# 5. Commit
# git add . && git commit -m "your message"

# 6. Deploy
# Follow DEPLOYMENT.md
```

**Manwell. Father Yourself.**

The forge is open. Get to work.
