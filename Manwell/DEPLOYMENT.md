# Deployment Guide - Manwell

This guide covers deploying Manwell to various hosting platforms.

## Quick Start (Local Development)

```bash
# Using Python 3
python -m http.server 8000

# Using Node.js (if installed)
npx http-server

# Using VS Code Live Server
# Right-click index.html > "Open with Live Server"
```

Visit `http://localhost:8000` in your browser.

---

## Deployment Options

### 1. GitHub Pages (Free, Simple)

**Steps:**
1. Create a GitHub repository called `manwell`
2. Push your code:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/manwell.git
   git branch -M main
   git push -u origin main
   ```
3. Go to repository Settings > Pages
4. Select `main` branch as source
5. Your site will be live at `https://YOUR_USERNAME.github.io/manwell`

**Pros:** Free, automatic deployments on git push  
**Cons:** Limited to GitHub infrastructure

---

### 2. Netlify (Recommended)

**Steps:**
1. Sign up at [netlify.com](https://netlify.com)
2. Connect your GitHub repository
3. Build settings:
   - Build command: (leave blank for static site)
   - Publish directory: `/` (root)
4. Deploy!

**Optional:**
- Set up custom domain (DNS settings)
- Add environment variables for API integrations
- Enable HTTPS (automatic)

**Pros:** Fast CDN, automatic HTTPS, good performance  
**Cons:** Requires GitHub connection (though manual upload option exists)

---

### 3. Vercel (Also Recommended)

**Steps:**
1. Sign up at [vercel.com](https://vercel.com)
2. Import your GitHub repository
3. No build configuration needed for static sites
4. Deploy!

**Pros:** Extremely fast, excellent analytics, edge functions support  
**Cons:** Requires GitHub connection

---

### 4. AWS S3 + CloudFront

**Steps:**
1. Create S3 bucket with same name as your domain
2. Upload files to S3
3. Enable static website hosting
4. Create CloudFront distribution
5. Point domain DNS to CloudFront

**Pros:** Scalable, highly available, good for high traffic  
**Cons:** Requires AWS knowledge, more setup

---

### 5. Traditional Web Hosting (cPanel/FTP)

**Steps:**
1. Upload files via FTP to your hosting provider's public directory
2. Ensure index.html is in the root
3. Test in browser

**Hosting options:**
- Bluehost, SiteGround, HostGator, etc.
- Usually $5-15/month

**Pros:** Full control, cheap  
**Cons:** Slower, less modern infrastructure

---

## Pre-Deployment Checklist

- [ ] All links point to correct files
- [ ] Social media URLs are updated
- [ ] Email contact form is configured (Mailchimp/ConvertKit)
- [ ] 404.html is present and accessible
- [ ] All images are optimized and use .webp format
- [ ] Meta descriptions are accurate
- [ ] Mobile responsiveness is tested
- [ ] Performance is tested (PageSpeed Insights)
- [ ] SSL/HTTPS is enabled
- [ ] Favicon is set (optional but recommended)

---

## Adding a Favicon

1. Create or download a 32x32 pixel icon
2. Save as `favicon.ico` in the root directory
3. Add to `<head>` in all HTML files:
   ```html
   <link rel="icon" type="image/x-icon" href="favicon.ico">
   ```

---

## Performance Optimization Before Deployment

### Image Optimization
```bash
# Using ImageMagick (install via package manager)
convert image.jpg -quality 85 image.webp
```

### Video Optimization
- Use YouTube/TikTok hosting instead of local files
- Keep hero video under 5MB for acceptable load times
- Use `.mp4` format with H.264 codec

### CSS & JS Minification
For production, consider minifying:
```bash
# CSS minification tools
sass --style=compressed css/styles.css > css/styles.min.css
```

### Lazy Loading Images
Already implemented in `js/script.js`. Use:
```html
<img src="placeholder.webp" data-src="real-image.webp" class="lazy-load">
```

---

## Setting Up a Custom Domain

### Domain Registrar (Google Domains, Namecheap, etc.)
1. Register your domain (e.g., `manwell.com`)
2. Point nameservers to your hosting provider
3. Update DNS records as per host instructions

### Common Hosting DNS Updates:
- **Netlify**: Add CNAME record pointing to your Netlify subdomain
- **GitHub Pages**: Add A records pointing to GitHub's IPs
- **AWS**: Point to CloudFront distribution

---

## SSL/HTTPS (CRITICAL)

All modern hosting providers offer free SSL certificates via Let's Encrypt:
- **Netlify**: Automatic
- **Vercel**: Automatic
- **GitHub Pages**: Automatic
- **Traditional Hosting**: Usually via cPanel > AutoSSL

Ensure your site is always served over HTTPS.

---

## Analytics & Monitoring

### Google Analytics
1. Create account at [analytics.google.com](https://analytics.google.com)
2. Add tracking code to `<head>`:
   ```html
   <script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'GA_ID');
   </script>
   ```

### Plausible Analytics (Privacy-Friendly)
```html
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/script.js"></script>
```

### PageSpeed Insights
Test at [pagespeed.web.dev](https://pagespeed.web.dev)

---

## Continuous Deployment

### Netlify (Auto-Deploy on Git Push)
- Connected to GitHub repository
- Every push to `main` branch triggers automatic build
- Preview deploys for pull requests

### GitHub Pages (Auto-Deploy on Git Push)
- Every push to `main` branch auto-deploys
- No build step needed for static sites

---

## Troubleshooting

### Site Looks Different Online
- Check file paths are relative (not absolute)
- Ensure all CSS/JS files are included
- Check browser cache (Ctrl+Shift+Delete)

### 404 Error on Some Pages
- Ensure `404.html` exists in root
- For GitHub Pages, custom 404 only works on main domain (not subfolders)

### Forms Not Working
- Check API endpoint is correct
- Verify CORS headers if using external API
- Use browser console (F12) to debug

### Slow Performance
- Optimize images
- Minimize HTTP requests
- Use CDN
- Enable compression
- Minify CSS/JS

---

## Rollback / Revert Deployment

If something goes wrong:

```bash
# View recent commits
git log --oneline

# Revert to previous commit
git revert HEAD

# Or hard reset (use carefully!)
git reset --hard <commit-hash>
```

---

## Next Steps

1. Choose your hosting platform
2. Set up custom domain
3. Configure email form API
4. Set up analytics
5. Monitor performance
6. Gather feedback from community

---

For questions or issues, refer to your host's documentation or open an issue in the repository.

**Manwell. Father Yourself.**
