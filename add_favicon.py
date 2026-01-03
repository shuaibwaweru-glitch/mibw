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

favicon_link = '  <link rel="icon" type="image/svg+xml" href="favicon.svg">\n'

for html_file in html_files:
    file_path = os.path.join(os.getcwd(), html_file)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if favicon link already exists
        if 'favicon' in content:
            print(f"- {html_file} already has favicon link")
            continue
        
        # Find the closing </head> tag and insert favicon link before it
        if '</head>' in content:
            # Insert favicon link before </head>
            content = content.replace('</head>', favicon_link + '</head>')
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Added favicon link to {html_file}")
        else:
            print(f"✗ Could not find </head> in {html_file}")
    else:
        print(f"✗ File not found: {html_file}")

print("\n✓ Favicon links added to all pages!")
