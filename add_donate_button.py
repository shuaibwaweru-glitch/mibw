import os
import re

# List of HTML files to update
html_files = [
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

donate_button = '        <a href="/donate" class="donate-btn">💚 Donate</a>'

for html_file in html_files:
    file_path = os.path.join(os.getcwd(), html_file)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if donate button already exists
        if 'donate-btn' in content:
            print(f"- {html_file} already has donate button")
            continue
        
        # Find the closing </nav> tag and insert donate button before it
        if '</nav>' in content:
            # Insert donate button before </nav>
            content = content.replace('</nav>', donate_button + '\n      </nav>')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Added donate button to {html_file}")
        else:
            print(f"✗ Could not find </nav> in {html_file}")
    else:
        print(f"✗ File not found: {html_file}")

print("\n✓ Donate button added to all pages!")
