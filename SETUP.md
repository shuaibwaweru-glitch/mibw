# Manwell Setup & Integration Guide

This guide covers integrating external services and configuring Manwell for production use.

---

## 1. Newsletter Integration (Email Signup)

The `community.html` form currently logs data to the browser console. To collect emails, integrate with one of these platforms:

### Option A: Mailchimp (Recommended for Beginners)

1. **Create Account**
   - Sign up at [mailchimp.com](https://mailchimp.com) (free tier available)
   - Create an audience/list

2. **Get API Credentials**
   - Go to Settings > API Keys
   - Copy your API Key and List ID

3. **Update Form in `js/script.js`**
   ```javascript
   const form = document.getElementById('newsletter-form');
   if (form) {
     form.addEventListener('submit', async (e) => {
       e.preventDefault();
       const formData = new FormData(form);
       const name = formData.get('name');
       const email = formData.get('email');

       // Replace with your actual Mailchimp API endpoint
       const response = await fetch('https://YOUR_DOMAIN.us1.api.mailchimp.com/3.0/lists/YOUR_LIST_ID/members', {
         method: 'POST',
         headers: {
           'Authorization': 'Bearer YOUR_API_KEY',
           'Content-Type': 'application/json',
         },
         body: JSON.stringify({
           email_address: email,
           status: 'subscribed',
           merge_fields: {
             FNAME: name
           }
         })
       });

       if (response.ok) {
         // Show confirmation
         form.style.display = 'none';
         // ... rest of code
       }
     });
   }
   ```

### Option B: ConvertKit (Creator-Friendly)

1. **Sign up** at [convertkit.com](https://convertkit.com)
2. **Create Form** in ConvertKit dashboard
3. **Embed Form** - Use ConvertKit's embed code in `community.html`

### Option C: EmailJS (No Backend Needed)

1. **Sign up** at [emailjs.com](https://emailjs.com)
2. **Install EmailJS**
   ```bash
   npm install @emailjs/browser
   ```
3. **Initialize in `js/script.js`**
   ```javascript
   import emailjs from '@emailjs/browser';
   emailjs.init('YOUR_PUBLIC_KEY');
   ```
4. **Send Emails**
   ```javascript
   emailjs.send('service_id', 'template_id', {
     from_name: name,
     from_email: email,
     message: 'New subscriber'
   });
   ```

---

## 2. Social Media Integration

### Instagram Embed
Add to HTML where you want Instagram feed:
```html
<script async src="//www.instagram.com/embed.js"></script>
<blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/p/POST_ID/"></blockquote>
```

### TikTok Embed
```html
<script async src="https://www.tiktok.com/embed.js"></script>
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@username/video/POST_ID">
  <section></section>
</blockquote>
```

### YouTube Embed (Already Implemented)
Videos are embedded via IFrame API - just update video IDs in `index.html`

---

## 3. Analytics Setup

### Google Analytics 4

1. **Create Account**
   - Go to [analytics.google.com](https://analytics.google.com)
   - Create new GA4 property

2. **Get Measurement ID**
   - In Admin > Data Streams > Web
   - Copy your Measurement ID (G-XXXXXXXXXX)

3. **Add to All HTML Pages**
   ```html
   <!-- In <head> -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-XXXXXXXXXX');
   </script>
   ```

### Plausible Analytics (Privacy-Friendly Alternative)

1. **Sign up** at [plausible.io](https://plausible.io)
2. **Add one line to `<head>`**
   ```html
   <script defer data-domain="yourdomain.com" src="https://plausible.io/js/script.js"></script>
   ```

---

## 4. Email Contact Form

For direct email inquiries (separate from newsletter), use:

### EmailJS Setup
```html
<!-- Add to community.html -->
<form id="contact-form">
  <input type="text" name="from_name" placeholder="Your Name" required>
  <input type="email" name="from_email" placeholder="Your Email" required>
  <textarea name="message" placeholder="Your Message" required></textarea>
  <button type="submit">Send Message</button>
</form>

<script type="text/javascript">
  (function(){
    emailjs.init("YOUR_PUBLIC_KEY");
  })();
  
  document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    emailjs.sendForm('service_id', 'template_id', this);
  });
</script>
```

---

## 5. SEO Optimization

### Meta Tags (Add to `<head>` of each page)

```html
<!-- index.html -->
<meta name="description" content="Manwell. A digital forge for modern masculinity. Confront the silent crisis. Father yourself.">
<meta name="keywords" content="masculinity, sovereignty, self-improvement, personal development">
<meta name="author" content="Manwell">
<meta property="og:title" content="Manwell - The Digital Forge">
<meta property="og:description" content="A digital sanctuary for men forging sovereignty.">
<meta property="og:image" content="https://yourdomain.com/assets/images/og-image.jpg">
<meta property="og:url" content="https://yourdomain.com">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Manwell - The Digital Forge">
<meta name="twitter:description" content="A digital sanctuary for men forging sovereignty.">
<meta name="twitter:image" content="https://yourdomain.com/assets/images/og-image.jpg">
```

### Structured Data (Schema.org)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Manwell",
  "url": "https://manwell.com",
  "logo": "https://manwell.com/assets/images/logo.png",
  "sameAs": [
    "https://instagram.com/manwell_",
    "https://tiktok.com/@manwell_",
    "https://youtube.com/manwell"
  ]
}
</script>
```

### XML Sitemap
Create `sitemap.xml`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://manwell.com/</loc>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://manwell.com/mission.html</loc>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://manwell.com/community.html</loc>
    <priority>0.8</priority>
  </url>
</urlset>
```

### robots.txt
Create `robots.txt`:
```
User-agent: *
Allow: /
Disallow: /admin/
Sitemap: https://manwell.com/sitemap.xml
```

---

## 6. Favicon & Web App Configuration

### Favicon
1. Create a 32x32 and 512x512 PNG icon
2. Convert to `.ico` format
3. Add to root directory and reference in `<head>`:
   ```html
   <link rel="icon" type="image/x-icon" href="/favicon.ico">
   <link rel="apple-touch-icon" href="/apple-touch-icon.png">
   <link rel="manifest" href="/site.webmanifest">
   ```

### Web Manifest (`site.webmanifest`)
```json
{
  "name": "Manwell",
  "short_name": "Manwell",
  "description": "Digital forge for modern masculinity",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#1a1a1a",
  "theme_color": "#ff5a09",
  "icons": [
    {
      "src": "/assets/images/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/assets/images/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

---

## 7. Environment Variables (for API Keys)

Create `.env.example`:
```
MAILCHIMP_API_KEY=your_api_key_here
MAILCHIMP_LIST_ID=your_list_id_here
EMAILJS_PUBLIC_KEY=your_public_key_here
GA_ID=G-XXXXXXXXXX
```

Never commit `.env` with real keys. Ignore in `.gitignore`:
```
.env
.env.local
```

---

## 8. Performance Monitoring

### Google PageSpeed Insights
- Test at [pagespeed.web.dev](https://pagespeed.web.dev)
- Aim for >90 on desktop and mobile

### WebPageTest
- Advanced testing at [webpagetest.org](https://webpagetest.org)

### Lighthouse (Built into Chrome DevTools)
- F12 > Lighthouse tab
- Run audit

---

## 9. Security Checklist

- [ ] HTTPS enabled (automatic on most hosts)
- [ ] CSP headers configured (Content-Security-Policy)
- [ ] No sensitive keys in code
- [ ] `.env` files not committed
- [ ] Regular security updates
- [ ] Form validation on client and server
- [ ] Rate limiting on email form

---

## 10. Environment-Specific Configuration

### Local Development
```bash
# Use local API endpoints
const API_URL = 'http://localhost:8000/api';
```

### Production
```bash
# Use production API endpoints
const API_URL = 'https://api.manwell.com';
```

Use environment variables to switch:
```javascript
const API_URL = process.env.NODE_ENV === 'production' 
  ? 'https://api.manwell.com'
  : 'http://localhost:8000/api';
```

---

## Implementation Priority

1. **Essential** (Before Launch)
   - Newsletter integration
   - Google Analytics
   - Meta tags & SEO
   - HTTPS/Custom domain

2. **Important** (First Month)
   - Email contact form
   - Sitemap & robots.txt
   - Favicon

3. **Nice-to-Have** (Ongoing)
   - Social media embeds
   - Advanced analytics
   - A/B testing

---

## Troubleshooting

### CORS Errors
- Common with email forms
- Solution: Use CORS proxy or backend server

### Email Not Sending
- Check API keys are correct
- Verify email format
- Check rate limiting

### Analytics Not Tracking
- Ensure GA/Plausible script is in `<head>`
- Check measurement ID is correct
- Wait 24 hours for data to appear

---

## Testing Integrations Locally

```bash
# For email form testing
npm install -D dotenv

# Create .env.test with test credentials
# Use test API keys from Mailchimp/EmailJS
```

---

## Additional Resources

- [Mailchimp API Docs](https://mailchimp.com/developer/)
- [ConvertKit API Docs](https://developers.convertkit.com/)
- [Google Analytics Docs](https://support.google.com/analytics/)
- [Schema.org Documentation](https://schema.org/)
- [Web.dev SEO Guide](https://web.dev/lighthouse-seo/)

---

**Manwell. Father Yourself.**

Complete integration and you're ready to forge your digital presence.
