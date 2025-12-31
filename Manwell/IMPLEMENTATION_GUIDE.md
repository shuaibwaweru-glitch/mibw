# Implementation Guide: Photo-Heavy Manwell Website

## Quick Start for Developers

### What Was Built

The Manwell website has been transformed into a **visually rich, East African-focused platform** with:
- ✅ New Stories page with expandable member narratives
- ✅ New Gallery page with image filtering
- ✅ Enhanced Homepage with featured stories preview
- ✅ Enhanced Mission page with image-text sections
- ✅ Enhanced Community page with profile testimonials

### File Changes Summary

| File | Changes | Status |
|------|---------|--------|
| `index.html` | Added featured stories preview section | ✅ Updated |
| `mission.html` | Added 3 image-text hybrid sections | ✅ Updated |
| `community.html` | Added 6 testimonials with profile images | ✅ Updated |
| `stories.html` | **NEW** - 6 stories with expandable modals | ✅ Created |
| `gallery.html` | **NEW** - 12-item gallery with filters | ✅ Created |
| `css/styles.css` | Story/gallery/modal styles included | ✅ Updated |
| `js/script.js` | Modal/filter logic in respective pages | ✅ Inline |

### Key New Features

#### 1. Stories Page (`stories.html`)
```html
<!-- Story Cards (clickable to expand) -->
<div class="story-card" onclick="openStory(0)">
  <img src="image.webp">
  <div class="story-content">
    <span class="story-tag">Sovereignty</span>
    <h3>The Performance Shattered</h3>
    <p class="excerpt">Preview text...</p>
  </div>
</div>

<!-- Expandable Modal -->
<div class="modal" id="story-modal">
  <div class="modal-content">
    <button class="modal-close" onclick="closeStory()">×</button>
    <img id="modal-image">
    <h2 id="modal-title"></h2>
    <div id="modal-story"></div>
    <iframe id="modal-video"></iframe>
  </div>
</div>
```

**JavaScript:**
```javascript
function openStory(index) {
  const story = stories[index];
  // Populate modal with story[index] data
  document.getElementById('story-modal').classList.add('active');
}

function closeStory() {
  document.getElementById('story-modal').classList.remove('active');
}
```

#### 2. Gallery Page (`gallery.html`)
```html
<!-- Filter Buttons -->
<button class="filter-btn active" data-filter="all">All</button>
<button class="filter-btn" data-filter="community">Community</button>

<!-- Gallery Grid -->
<div class="gallery-grid">
  <div class="gallery-item" data-filter="community,culture">
    <img src="image.webp">
    <div class="gallery-overlay">
      <h3>Title</h3>
    </div>
  </div>
</div>

<!-- Filter JavaScript -->
<script>
filterBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const filterValue = btn.getAttribute('data-filter');
    galleryItems.forEach(item => {
      const tags = item.getAttribute('data-filter').split(',');
      item.style.display = (filterValue === 'all' || tags.includes(filterValue)) ? 'block' : 'none';
    });
  });
});
</script>
```

#### 3. Image-Text Sections (Mission Page)
```html
<section>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center;">
    <div>
      <img src="image.webp" style="height: 400px; object-fit: cover; border-radius: 8px;">
    </div>
    <div>
      <h3>Section Title</h3>
      <p>Text content...</p>
      <div style="height: 3px; width: 40px; background: #4a9b8e; margin-top: 2rem;"></div>
    </div>
  </div>
</section>
```

#### 4. Testimonial Cards (Community Page)
```html
<div style="background: white; border: 1px solid #e8f0f5; border-radius: 8px; text-align: center;">
  <img src="profile.webp" style="width: 100%; height: 200px; object-fit: cover;">
  <div style="padding: 2rem;">
    <h3>Name</h3>
    <p style="color: #4a9b8e;">Location</p>
    <p style="font-style: italic;">Testimonial quote...</p>
  </div>
</div>
```

### Navigation Structure

All pages now include unified navigation:
```html
<nav>
  <ul>
    <li><a href="index.html">The Forge</a></li>
    <li><a href="mission.html">The Mission</a></li>
    <li><a href="gallery.html">Gallery</a></li>
    <li><a href="stories.html">Stories</a></li>
    <li><a href="community.html">Community</a></li>
  </ul>
</nav>
```

### CSS Class Reference

#### Modal System
```css
.modal { /* Full-screen overlay */ }
.modal.active { display: flex; }
.modal-content { /* Centered white box */ }
.modal-header { /* Hero image area */ }
.modal-body { /* Text and content area */ }
.modal-close { /* X button */ }
```

#### Stories
```css
.story-card { /* Preview card */ }
.story-card:hover { border-color: #4a9b8e; transform: translateY(-8px); }
.story-image { /* Image in card */ }
.story-content { /* Text section */ }
.story-tag { /* Category badge */ }
.read-more-btn { /* CTA text */ }
```

#### Gallery
```css
.gallery-grid { /* Responsive grid */ }
.gallery-item { /* Single image */ }
.gallery-overlay { /* Text overlay */ }
.gallery-item:hover .gallery-overlay { opacity: 1; }
.filter-btn { /* Filter button */ }
.filter-btn.active { /* Selected state */ }
.gallery-tag { /* Category badge */ }
```

#### Testimonials
```css
.testimonial-card { /* Testimonial container */ }
.testimonial-video { /* Video embed */ }
.testimonial-info { /* Name/quote area */ }
```

### Color Palette Reference

```
Navy Blue:     #1a3a52   (primary text, headlines)
Teal:          #4a9b8e   (accents, hovers, tags)
Off-White:     #f8f9fa   (background sections)
Border Gray:   #e8f0f5   (card borders)
Text Gray:     #6b7a8a   (secondary text)
Dark Text:     #4a5568   (body text)
```

### Responsive Breakpoints

```css
/* Mobile: < 480px */
/* Tablet: 480px - 768px */
/* Desktop: 768px+ */

/* Default: 1-column layouts, stacked sections */
/* Tablet: 2-column grids */
/* Desktop: 3+ columns, side-by-side layouts */
```

### Image Specifications

**Source:** Unsplash (free stock photos)

**Usage:**
```html
<!-- Story Cards -->
<img src="https://images.unsplash.com/photo-ID?w=500&h=250&fit=crop" alt="Description">

<!-- Full Images -->
<img src="https://images.unsplash.com/photo-ID?w=600&h=500&fit=crop" alt="Description">

<!-- Profile Photos -->
<img src="https://images.unsplash.com/photo-ID?w=400&h=300&fit=crop" alt="Name">
```

**Recommended Dimensions:**
- Story cards: 500×250px
- Full-width sections: 600×500px or 800×600px
- Profile photos: 400×300px
- Gallery items: 400×400px

### JavaScript Functions

#### Story Modal
```javascript
// Open a story by index
openStory(0);  // Opens first story

// Close the modal
closeStory();

// Keyboard: Escape key closes modal
// Mouse: Click background closes modal
```

#### Gallery Filter
```javascript
// Filter is automatic via data-filter attributes
// Click filter button → items show/hide automatically
```

#### Intersection Observer (Reveal Animation)
```javascript
// Already implemented in script.js
// Elements with .reveal class fade in on scroll
```

### Updating Content

#### Add a New Story
1. Edit `stories.html`
2. Add entry to `stories` array:
```javascript
{
  tag: 'Category',
  title: 'Story Title',
  subtitle: 'Name - Location',
  image: 'https://unsplash...',
  video: 'https://youtube.com/embed/...',
  excerpt: 'Short preview...',
  fullStory: 'Full narrative text...'
}
```
3. Add corresponding story card HTML
4. Commit changes

#### Add Gallery Items
1. Edit `gallery.html`
2. Add item to grid:
```html
<div class="gallery-item" data-filter="category1,category2">
  <img src="https://unsplash..." alt="Description">
  <div class="gallery-overlay">
    <h3>Title</h3>
    <span class="gallery-tag">Category</span>
  </div>
</div>
```
3. Update filter buttons if adding new category
4. Commit changes

#### Update Navigation
Edit the `<nav>` block in the header of each page:
```html
<nav>
  <ul>
    <li><a href="index.html">New Page 1</a></li>
    <!-- Update all 5 pages consistently -->
  </ul>
</nav>
```

### Performance Tips

1. **Images:** Unsplash URLs already serve optimized images via CDN
2. **Videos:** YouTube embeds use lazy loading (`loading="lazy"`)
3. **CSS:** All styles in single `styles.css` file
4. **JavaScript:** Modal/filter logic kept in respective pages
5. **Fonts:** Google Fonts (Inter) cached by browser

### Accessibility

✅ **Implemented:**
- Alt text on all images
- Semantic HTML (header, nav, section, footer)
- Color contrast meets WCAG AA
- Keyboard navigation (escape to close modal)
- Skip links in header (can be added)

### Browser Support

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers (iOS/Android)

### Deployment

1. Ensure all image URLs are accessible (Unsplash CDN is reliable)
2. Test responsive design on actual devices
3. Verify video embeds work (YouTube CDN)
4. Check navigation links across all pages
5. Test modal open/close on mobile
6. Verify gallery filters work

```bash
# Test locally
python -m http.server 8000
# Visit http://localhost:8000

# Deploy to hosting
# All files are static (no server required)
# Copy all files to web server
```

### Common Customizations

#### Change Colors
Edit `css/styles.css`:
```css
/* Find and replace */
#4a9b8e  /* Replace teal with brand color */
#1a3a52  /* Replace navy with primary color */
#f8f9fa  /* Replace off-white with background */
```

#### Change Story Count
1. Edit `stories.html` - change array length
2. Update HTML card count
3. Update story data array

#### Change Gallery Items
1. Edit `gallery.html`
2. Add/remove `.gallery-item` divs
3. Update filter categories as needed

#### Replace Images
1. Find Unsplash photo URLs
2. Replace in HTML files
3. Update alt text descriptions
4. Test responsive display

### Troubleshooting

**Modal not opening:**
- Check story card onclick handler: `onclick="openStory(0)"`
- Verify `stories` array is defined
- Check modal element ID: `id="story-modal"`

**Gallery filter not working:**
- Verify filter buttons have `data-filter` attribute
- Check gallery items have `data-filter` attribute
- Ensure categories match between buttons and items

**Images not loading:**
- Verify Unsplash URLs are correct
- Check image dimensions in query string
- Ensure alt text is present

**Responsive design issues:**
- Check media queries in `css/styles.css`
- Test on actual mobile device
- Verify viewport meta tag in `<head>`

### Support Resources

- **Design System:** See `DESIGN_SYSTEM.md`
- **Brand Guide:** See `BRAND_REDESIGN.md`
- **Setup Guide:** See `SETUP.md`
- **Deployment:** See `DEPLOYMENT.md`

---

**Last Updated:** 2025
**Status:** Production Ready
**Version:** 2.0 (Photo-Heavy Redesign)
