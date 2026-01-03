import os
import re

# List of HTML files to update
html_files = [
    'index.html',
    'mission.html',
    'pillars.html',
    'mental-health-hub.html',
    'assessments.html',
    'therapist-directory.html',
    'crisis.html',
    'community.html',
    'resources.html',
    'stories.html',
    'videos.html',
    'experts.html',
    'activities.html',
    'gallery.html',
    'therapy-marketplace.html',
    'contact.html'
]

# URL mappings - old href to new href
url_mappings = {
    'href="index.html"': 'href="/home"',
    'href="mission.html"': 'href="/about"',
    'href="pillars.html"': 'href="/strategy"',
    'href="mental-health-hub.html"': 'href="/mental-health"',
    'href="assessments.html"': 'href="/assessments"',
    'href="therapist-directory.html"': 'href="/find-therapist"',
    'href="crisis.html"': 'href="/crisis"',
    'href="community.html"': 'href="/community"',
    'href="resources.html"': 'href="/resources"',
    'href="stories.html"': 'href="/stories"',
    'href="videos.html"': 'href="/videos"',
    'href="experts.html"': 'href="/experts"',
    'href="activities.html"': 'href="/programs"',
    'href="gallery.html"': 'href="/gallery"',
    'href="therapy-marketplace.html"': 'href="/marketplace"',
    'href="contact.html"': 'href="/contact"',
}

for html_file in html_files:
    file_path = os.path.join(os.getcwd(), html_file)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply all replacements
        for old_href, new_href in url_mappings.items():
            content = content.replace(old_href, new_href)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated {html_file}")
        else:
            print(f"- No changes needed for {html_file}")
    else:
        print(f"✗ File not found: {html_file}")

print("\n✓ All internal links updated to clean URLs!")
