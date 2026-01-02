#!/usr/bin/env python3
"""
Apply Elderly Home template styling to all Manwell pages
Color scheme: Teal (#1a5f66), Orange (#E8B356)
"""

import os
import re

# Define the new comprehensive CSS
NEW_CSS = '''  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Source Sans Pro', sans-serif;
      line-height: 1.6;
      color: #2c3e50;
      background-color: #f8f9fa;
    }

    /* ========== HEADER ========== */
    header {
      background: white;
      border-bottom: 1px solid #e0e0e0;
      position: fixed;
      width: 100%;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    .header-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 1rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .logo {
      font-size: 1.5rem;
      font-weight: 700;
      color: #1a5f66;
      text-decoration: none;
      letter-spacing: -0.5px;
    }

    nav ul {
      list-style: none;
      display: flex;
      gap: 2.5rem;
    }

    nav a {
      text-decoration: none;
      color: #666;
      font-size: 0.95rem;
      font-weight: 500;
      transition: color 0.3s;
      border-bottom: 2px solid transparent;
      padding-bottom: 2px;
    }

    nav a:hover,
    nav a.active {
      color: #E8B356;
      border-bottom-color: #E8B356;
    }

    .menu-toggle {
      display: none;
      background: none;
      border: none;
      font-size: 1.5rem;
      cursor: pointer;
    }

    /* ========== CONTAINER ========== */
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 2rem;
    }

    /* ========== HERO SECTION ========== */
    .hero {
      background: linear-gradient(rgba(26, 95, 102, 0.7), rgba(26, 95, 102, 0.7)), url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600"><rect fill="%231a5f66" width="1200" height="600"/></svg>');
      background-size: cover;
      background-position: center;
      color: white;
      padding: 120px 2rem 80px;
      margin-top: 60px;
      text-align: center;
    }

    .hero-content {
      max-width: 900px;
      margin: 0 auto;
    }

    .hero h1 {
      font-family: 'Lora', serif;
      font-size: 3rem;
      font-weight: 600;
      margin-bottom: 1.5rem;
      line-height: 1.2;
      letter-spacing: -0.5px;
    }

    .hero p {
      font-size: 1.1rem;
      font-weight: 300;
      margin-bottom: 2rem;
      opacity: 0.95;
    }

    .cta-buttons {
      display: flex;
      gap: 1rem;
      justify-content: center;
      flex-wrap: wrap;
    }

    /* ========== BUTTONS ========== */
    .btn {
      padding: 12px 30px;
      border-radius: 0;
      text-decoration: none;
      font-weight: 600;
      transition: all 0.3s;
      border: none;
      cursor: pointer;
      font-size: 1rem;
      display: inline-block;
    }

    .btn-primary {
      background: #E8B356;
      color: white;
    }

    .btn-primary:hover {
      background: #d4a051;
      box-shadow: 0 4px 12px rgba(232, 179, 86, 0.3);
      transform: translateY(-2px);
    }

    .btn-secondary {
      background: transparent;
      color: white;
      border: 2px solid white;
    }

    .btn-secondary:hover {
      background: white;
      color: #1a5f66;
    }

    /* ========== SECTIONS ========== */
    section {
      padding: 4rem 2rem;
      background: white;
      margin: 0;
    }

    section.alt {
      background: #f8f9fa;
    }

    section h2 {
      font-family: 'Lora', serif;
      font-size: 2.2rem;
      color: #1a5f66;
      margin-bottom: 0.5rem;
      font-weight: 600;
      letter-spacing: -0.5px;
    }

    section h2:after {
      content: '';
      display: block;
      width: 60px;
      height: 3px;
      background: #E8B356;
      margin-top: 0.5rem;
      margin-bottom: 1.5rem;
    }

    section h3 {
      font-family: 'Lora', serif;
      color: #1a5f66;
      margin: 1.5rem 0 1rem;
      font-weight: 600;
    }

    /* ========== GRIDS ========== */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 2rem;
      margin: 2rem 0;
    }

    .stat-card {
      background: #1a5f66;
      color: white;
      padding: 2.5rem;
      border-radius: 0;
      text-align: center;
    }

    .stat-number {
      font-size: 2.8rem;
      font-weight: 700;
      color: #E8B356;
      margin-bottom: 0.5rem;
    }

    .stat-label {
      color: rgba(255,255,255,0.9);
      font-weight: 500;
      font-size: 0.95rem;
    }

    .features-grid,
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 2rem;
      margin: 2rem 0;
    }

    .feature-card,
    .card {
      background: #f8f9fa;
      border: none;
      border-left: 4px solid #E8B356;
      border-radius: 0;
      padding: 2.5rem;
      transition: all 0.3s;
    }

    .feature-card:hover,
    .card:hover {
      box-shadow: 0 6px 16px rgba(26, 95, 102, 0.12);
      transform: translateY(-2px);
    }

    .feature-icon {
      font-size: 2.5rem;
      margin-bottom: 1rem;
    }

    .feature-card h3,
    .card h3 {
      color: #1a5f66;
      margin-top: 0;
      margin-bottom: 0.5rem;
      font-size: 1.2rem;
    }

    .feature-card p,
    .card p {
      color: #666;
      font-size: 0.95rem;
    }

    /* ========== FOOTER ========== */
    footer {
      background: #1a5f66;
      color: white;
      padding: 4rem 0 1rem;
      margin-top: 0;
    }

    .footer-content {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 2rem;
      margin-bottom: 2rem;
    }

    .footer-section {
      padding: 0 2rem;
    }

    .footer-section h4 {
      color: #E8B356;
      margin-bottom: 1rem;
      font-size: 0.95rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .footer-section ul {
      list-style: none;
    }

    .footer-section a {
      color: rgba(255,255,255,0.85);
      text-decoration: none;
      line-height: 2;
      font-size: 0.9rem;
      transition: color 0.3s;
    }

    .footer-section a:hover {
      color: #E8B356;
    }

    .footer-bottom {
      border-top: 1px solid rgba(255,255,255,0.2);
      padding: 2rem;
      text-align: center;
      font-size: 0.85rem;
      opacity: 0.8;
    }

    /* ========== RESPONSIVE ========== */
    @media (max-width: 768px) {
      nav ul {
        display: none;
      }

      .menu-toggle {
        display: block;
      }

      .hero h1 {
        font-size: 1.8rem;
      }

      section h2 {
        font-size: 1.5rem;
      }

      .cta-buttons {
        flex-direction: column;
      }

      .btn {
        width: 100%;
      }
    }
  </style>'''

# Pages to update
PAGES = [
    'index.html',
    'mental-health-hub.html',
    'assessments.html',
    'therapist-directory.html',
    'crisis.html',
    'community.html',
    'resources.html',
    'mission.html',
    'stories.html',
    'videos.html',
    'experts.html',
    'activities.html',
    'gallery.html'
]

def apply_theme(filepath):
    """Apply theme colors to a page"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract the style section
        style_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
        if style_match:
            # Replace style section
            old_style = style_match.group(0)
            new_content = content.replace(old_style, NEW_CSS)
            
            # Replace color codes
            new_content = new_content.replace('#1a3a52', '#1a5f66')
            new_content = new_content.replace('#2d5a7f', '#1a5f66')
            new_content = new_content.replace('#b71c1c', '#1a5f66')
            
            # Update theme color meta tag
            new_content = new_content.replace('content="#1a3a52"', 'content="#1a5f66"')
            new_content = new_content.replace('content="#d32f2f"', 'content="#E8B356"')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

# Apply theme to all pages
os.chdir('f:\\Manwell')
success_count = 0
for page in PAGES:
    if apply_theme(page):
        print(f"✓ Updated {page}")
        success_count += 1
    else:
        print(f"✗ Failed {page}")

print(f"\n✓ Theme applied to {success_count}/{len(PAGES)} pages")
