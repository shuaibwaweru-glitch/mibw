import re

dropdown_css = '''    /* ========== DROPDOWN NAVIGATION ========== */
    nav {
      display: flex;
      gap: 0.5rem;
      list-style: none;
    }

    .nav-item {
      position: relative;
    }

    .nav-item > a {
      display: block;
      padding: 0.5rem 1rem;
      text-decoration: none;
      color: #666;
      font-weight: 500;
      font-size: 0.9rem;
      transition: color 0.3s ease;
    }

    .nav-item > a:hover,
    .nav-item > a.active {
      color: #E8B356;
    }

    .dropdown-menu {
      display: none;
      position: absolute;
      top: 100%;
      left: 0;
      background: white;
      border: 1px solid #eee;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      border-radius: 4px;
      min-width: 220px;
      z-index: 1001;
    }

    .nav-item:hover .dropdown-menu {
      display: block;
    }

    .dropdown-menu a {
      display: block;
      padding: 0.8rem 1.2rem;
      text-decoration: none;
      color: #666;
      font-size: 0.9rem;
      transition: background-color 0.3s ease, color 0.3s ease;
      border-bottom: 1px solid #f0f0f0;
    }

    .dropdown-menu a:last-child {
      border-bottom: none;
    }

    .dropdown-menu a:hover {
      background-color: #f8f9fa;
      color: #E8B356;
    }

    .dropdown-menu .section-title {
      padding: 0.8rem 1.2rem;
      color: #1a5f66;
      font-weight: 600;
      font-size: 0.85rem;
      text-transform: uppercase;
      background-color: #f0f7f8;
      cursor: default;
    }'''

pages = ['index.html', 'mission.html', 'mental-health-hub.html', 'assessments.html', 'therapist-directory.html', 'crisis.html', 'community.html', 'resources.html', 'stories.html', 'videos.html', 'experts.html', 'activities.html', 'gallery.html', 'contact.html', 'therapy-marketplace.html']

for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove old nav CSS if it exists
        content = re.sub(r'    nav ul \{[\s\S]*?    \}', '', content)
        content = re.sub(r'    nav a \{[\s\S]*?    \}', '', content)
        
        # Find the position to insert the new CSS (right before the hero section or before closing style)
        pattern = r'(    \.menu-toggle \{[\s\S]*?\})'
        if re.search(pattern, content):
            content = re.sub(pattern, r'\1\n\n' + dropdown_css, content)
        else:
            # If menu-toggle doesn't exist, insert before closing style tag
            content = re.sub(r'(\n  </style>)', dropdown_css + r'\1', content)
        
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✓ Added dropdown CSS to {page}')
    except Exception as e:
        print(f'✗ Error {page}: {e}')

print("\n✓ All pages updated with dropdown CSS!")
