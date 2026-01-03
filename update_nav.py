import re

nav_html = '''<nav>
        <div class="nav-item">
          <a href="index.html">Home</a>
        </div>
        <div class="nav-item">
          <a href="#">About ▼</a>
          <div class="dropdown-menu">
            <a href="mission.html">Our Mission & Values</a>
            <a href="experts.html">Our Experts</a>
            <a href="stories.html">Member Stories</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="#">Services ▼</a>
          <div class="dropdown-menu">
            <div class="section-title">Mental Health</div>
            <a href="mental-health-hub.html">Mental Health Hub</a>
            <a href="assessments.html">Assessments</a>
            <a href="crisis.html">Crisis Support</a>
            <div class="section-title">Programs</div>
            <a href="activities.html">Programs & Activities</a>
            <a href="therapy-marketplace.html">Therapy Marketplace</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="#">Community ▼</a>
          <div class="dropdown-menu">
            <a href="community.html">Community Programs</a>
            <a href="therapist-directory.html">Find a Therapist</a>
            <a href="gallery.html">Our Gallery</a>
            <a href="videos.html">Educational Videos</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="#">Resources ▼</a>
          <div class="dropdown-menu">
            <a href="resources.html">Resource Library</a>
            <a href="contact.html">Contact Us</a>
          </div>
        </div>
      </nav>'''

pages = ['index.html', 'mission.html', 'mental-health-hub.html', 'assessments.html', 'therapist-directory.html', 'crisis.html', 'community.html', 'resources.html', 'stories.html', 'videos.html', 'experts.html', 'activities.html', 'gallery.html', 'contact.html', 'therapy-marketplace.html']

for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = re.sub(r'<nav><ul>[\s\S]*?</ul></nav>', nav_html, content)
        
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'✓ Updated {page}')
    except Exception as e:
        print(f'✗ Error {page}: {e}')

print("\n✓ All pages updated with new dropdown navigation!")
