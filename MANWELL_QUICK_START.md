# MANWELL QUICK START GUIDE

## 🎯 What You Need to Know

Your website has been completely transformed from **MiBW** to **Manwell** with a modern, professional, image-heavy design. Here's everything you need to know to manage it going forward.

---

## 📍 WHAT CHANGED

### Brand
- **Old Name:** MiBW (Men In Black & White)
- **New Name:** Manwell
- **Old Logo:** "MiBW" text
- **New Logo:** Simple "M" with gradient (Navy→Teal)
- **New Tagline:** "Manwell - Where Men's Mental Health Matters"

### Homepage (index.html)
- **Old:** Basic text content
- **New:** Modern image-heavy design with:
  - Large hero section with background image
  - 6-item community photo gallery
  - 6 "Why Manwell" reason cards
  - 6 program showcase cards with images
  - 4 member testimonials with circular avatars
  - Professional footer with social links

### All 13 Pages
- Updated logo and navigation
- Consistent Manwell branding
- Professional color scheme (Navy, Teal, Gold, Red)
- Responsive design on all devices

---

## 🎨 COLORS & DESIGN

### Brand Colors
```
Navy:   #1a3a52  (Primary - headers, text, backgrounds)
Teal:   #4a9b8e  (Secondary - accents, links)
Gold:   #d4af37  (Action - buttons, highlights)
Red:    #d32f2f  (Crisis - urgent calls to action)
```

### How to Change Colors
1. Open `css/styles.css`
2. Use Find & Replace:
   - Find: `#1a3a52` Replace: `#yourcolor`
   - Find: `#4a9b8e` Replace: `#yourcolor`
   - Find: `#d4af37` Replace: `#yourcolor`
   - Find: `#d32f2f` Replace: `#yourcolor`
3. Save file
4. Deploy: `git push origin main`

---

## 📸 IMAGES & PHOTOS

### Current Setup
- All images use **Unsplash** (free stock photos)
- Images automatically loaded from URLs
- No image files stored locally
- Color overlay applied for text readability

### To Add Your Own Images
1. **Get Photos:**
   - Use Unsplash, Pexels, Pixabay (free)
   - Or upload your own photos
   - Minimum quality: 1200px wide

2. **Optimize Photos:**
   - Recommended size: 75-150KB
   - Aspect ratios:
     - Gallery: Square (1:1)
     - Cards: 4:3 (400×300)
     - Avatars: Square (80-100px)
   - Use online tools to compress

3. **Replace URLs in HTML:**
   - Find Unsplash URL in HTML
   - Replace with your image URL
   - Save and test locally

4. **Deploy:**
   - `git add -A`
   - `git commit -m "Updated images"`
   - `git push origin main`

---

## 🔗 NAVIGATION STRUCTURE

### Main Menu (9 Items)
1. **Home** → index.html
2. **About Us** → mission.html
3. **Programs** → activities.html
4. **Education** → mental-health-hub.html
5. **Assessments** → assessments.html
6. **Community** → community.html
7. **Find Help** → therapist-directory.html
8. **Crisis Support** → crisis.html
9. **Donate** → Redirect to your donation platform

### Footer Links
- About, Quick Links, Resources, Support sections
- Social media icons (Facebook, Twitter, Instagram, LinkedIn)
- All customizable in footer section

---

## 📝 EDITING CONTENT

### To Update Text on Pages
1. Open HTML file (e.g., mission.html)
2. Find the text you want to change
3. Edit directly in VS Code
4. Save file
5. Test locally: refresh browser
6. Deploy: `git push origin main`

### Example: Homepage Headline
```html
<!-- Find this line -->
<h1 class="hero-main-title">Your Journey to Wellness</h1>

<!-- Change to your text -->
<h1 class="hero-main-title">Your New Headline Here</h1>
```

### Important: Keep These Consistent
- Logo text: "Manwell"
- Social links in footer
- "Donate" button color (should be red)
- Crisis hotline number (if added)

---

## 🚀 HOW TO DEPLOY CHANGES

### Quick Deployment Steps
```bash
# 1. Open terminal in VS Code or PowerShell
cd f:\Manwell

# 2. Check what changed
git status

# 3. Add all changes
git add -A

# 4. Commit with message
git commit -m "Updated [what changed]"

# 5. Push to GitHub (auto-deploys to Vercel)
git push origin main

# 6. Wait 1-2 minutes for Vercel to update
# 7. Visit https://www.manwell.org to see changes live
```

### Example Commits
- `git commit -m "Updated mission page content"`
- `git commit -m "Added new therapist photos"`
- `git commit -m "Changed button colors to new brand color"`
- `git commit -m "Fixed navigation on mobile"`

---

## 📱 RESPONSIVE DESIGN

### How It Works
- **Desktop (1024px+):** 3-column layouts, full features
- **Tablet (768-1024px):** 2-column layouts
- **Mobile (<768px):** 1-column, full-width
- **Small Phone (<480px):** Optimized for touch

### How to Test
1. Open website in browser
2. Press F12 to open Developer Tools
3. Click "Toggle Device Toolbar" (top left)
4. Select different devices
5. Test all interactive features

---

## 🔧 COMMON CUSTOMIZATIONS

### Change Donation Button Link
Find in `index.html` footer:
```html
<a href="#" class="cta-primary" style="background: #d4af37;">Donate Now</a>
```
Change `href="#"` to your donation URL:
```html
<a href="https://your-donation-platform.com" class="cta-primary">Donate Now</a>
```

### Add New Social Media Link
Find footer social links:
```html
<a href="#" title="Facebook">f</a>
<a href="#" title="Twitter">𝕏</a>
```
Replace `#` with your social media URLs:
```html
<a href="https://facebook.com/yourpage" title="Facebook">f</a>
<a href="https://twitter.com/yourhandle" title="Twitter">𝕏</a>
```

### Change Crisis Hotline
Find and update:
```html
<a href="tel:988">Call 988</a>
```

### Update Copyright Year
Find in footer:
```html
<p>&copy; 2025 Manwell. All rights reserved.</p>
```

---

## 🎓 FILE STRUCTURE GUIDE

```
f:\Manwell\
├── index.html                    ← HOMEPAGE (main page)
├── mission.html                  ← About Us page
├── activities.html               ← Programs page
├── therapist-directory.html      ← Find Help page
├── crisis.html                   ← Crisis Support page
├── community.html                ← Community Forum
├── mental-health-hub.html        ← Education page
├── assessments.html              ← Assessment tools
├── experts.html                  ← Expert board
├── gallery.html                  ← Photo gallery
├── stories.html                  ← Testimonials
├── videos.html                   ← Video library
├── resources.html                ← Resources/downloads
│
├── css/
│   ├── styles.css               ← MAIN STYLESHEET (edit for colors)
│   └── styles-image-heavy.css   ← Image component library
│
├── js/
│   └── script.js                ← Navigation/menu functionality
│
├── assets/
│   ├── favicon.svg              ← Browser tab icon
│   ├── images/                  ← Your image folder
│   └── videos/                  ← Your video folder
│
└── [Documentation files]
```

---

## ✅ TESTING CHECKLIST

After making changes, test:

- [ ] All pages load without errors
- [ ] Images display correctly
- [ ] Links work (click each link)
- [ ] Mobile design looks good (F12 → Device toggle)
- [ ] Buttons are clickable
- [ ] Navigation menu works
- [ ] Donation button goes to right place
- [ ] Social media links work
- [ ] No broken text or overlaps
- [ ] Page loads in <2 seconds

### How to Test Locally
1. Keep local server running: `python -m http.server 8000`
2. Open browser: `http://localhost:8000`
3. Test all changes before deploying
4. Check F12 Console for errors

---

## 🆘 COMMON ISSUES & SOLUTIONS

### Issue: Page looks broken
**Solution:** Clear browser cache
- Press Ctrl+Shift+Del → Clear all data → Refresh page

### Issue: Images not showing
**Solution:** Check image URLs
- Make sure URLs start with `https://` (not `http://`)
- Verify image exists (try clicking link in new tab)
- Check image format (JPG, PNG, WEBP all work)

### Issue: Changes not showing on live site
**Solution:** Wait for Vercel to rebuild
- Commits take 1-2 minutes to appear live
- Check GitHub to confirm commit was pushed
- Hard refresh browser (Ctrl+Shift+R)

### Issue: Can't push to GitHub
**Solution:** Check credentials
- Make sure you have Git installed
- Configure Git with your credentials
- Check internet connection

### Issue: Styling looks different locally vs live
**Solution:** CSS caching issue
- Clear browser cache (Ctrl+Shift+Del)
- Verify css/styles.css is loading (F12 → Network tab)
- Check for CSS typos

---

## 📈 NEXT STEPS (ENHANCEMENT IDEAS)

### Phase 2 - Image Enhancement (1-2 weeks)
- Add professional therapist photos
- Add expert headshots
- Expand photo gallery to 40+ images
- Add member avatars to community page
- Add event photography

### Phase 3 - Content Expansion (2-4 weeks)
- Add blog/news section
- Create video tutorials
- Add member success stories
- Implement event calendar
- Add testimonial videos

### Phase 4 - Functionality (1-2 months)
- Online program registration
- Member login portal
- Live chat support
- Email newsletter signup
- Analytics integration

See **IMAGE_HEAVY_REDESIGN_COMPLETE.md** for detailed page-by-page plan.

---

## 📞 SUPPORT RESOURCES

### Documentation Files
1. **MANWELL_REBRAND_COMPLETE.md** ← Full overview
2. **IMAGE_HEAVY_REDESIGN_COMPLETE.md** ← Enhancement plan
3. **CUSTOMIZATION_GUIDE.md** ← Detailed customization
4. **This File** ← Quick reference guide

### Getting Help
- Check documentation first
- Review git commit history: `git log`
- Check CSS comments for component details
- Ask AI for help with specific code questions

---

## 🎊 REMEMBER

✨ **Your website is now professional and modern**
✨ **Manwell brand is strong and memorable**
✨ **Image-heavy design makes great impressions**
✨ **All pages are responsive and accessible**
✨ **Changes deploy automatically with git push**

**Most importantly: Your website is ready to make a real difference in men's mental health support!**

---

**Version:** 1.0 - January 3, 2026  
**Status:** Production Ready  
**Website:** https://www.manwell.org
