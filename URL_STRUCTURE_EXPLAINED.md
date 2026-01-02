# URL Structure Solution - Why .html Appears

## The Problem
Your site URLs show `.html` extensions like:
- www.mibw.org/gallery.html
- www.mibw.org/activities.html
- www.mibw.org/therapist-directory.html

This is because you're hosting static HTML files. While this works perfectly, it's not as clean as modern web apps which use "clean URLs".

## Solution Options

### Option 1: Vercel URL Rewriting (EASIEST - No code changes needed)
Vercel automatically handles clean URLs for you. Just create a `vercel.json` file:

```json
{
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

But even better - Vercel treats `.html` files as static assets, so clean URLs should work automatically. Try:
- www.mibw.org/gallery (without .html)
- www.mibw.org/activities (without .html)

### Option 2: Update All Internal Links (What we're doing)
Change all links throughout the site to NOT include `.html`:

```html
<!-- Old -->
<a href="gallery.html">Gallery</a>

<!-- New -->
<a href="/gallery">Gallery</a>
```

### Option 3: Use Root-Relative Paths
```html
<a href="/gallery.html">Gallery</a>
```

This makes all links work whether you have `.html` or not.

## What We're Implementing
We've updated the new design to use cleaner paths. Since you're on Vercel, the platform should handle clean URLs automatically. You can test:

**With .html (always works):**
- https://www.mibw.org/gallery.html

**Without .html (modern, cleaner):**
- https://www.mibw.org/gallery

## Recommendation
Keep the `.html` in your actual files (gallery.html, etc.) but let Vercel handle the URL display. Most modern hosting platforms automatically strip extensions from file-based sites. Your site is working correctly either way!
