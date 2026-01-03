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

# Replacements to make
replacements = [
    # Old phone to new phone
    (r'<a href="tel:\+?18001111111">1-800-MANWELL</a>', 
     '<a href="tel:+254754151315">+254 754 151 315</a>'),
    
    # Old email to new email
    (r'<a href="mailto:info@manwell\.org">info@manwell\.org</a>', 
     '<a href="mailto:hello@mibw.org">hello@mibw.org</a>'),
    
    # Old address (NYC) to new address (Nairobi)
    (r'123 Care Avenue(?:,)?\s*New York,\s*NY\s*10001',
     'Syscraft Place, Sports Road, Westlands, Nairobi'),
    (r'123 Care Avenue<br>New York, NY 10001',
     'Syscraft Place<br>Sports Road<br>Westlands, Nairobi'),
]

for html_file in html_files:
    file_path = os.path.join(os.getcwd(), html_file)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for old_pattern, new_text in replacements:
            content = re.sub(old_pattern, new_text, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated {html_file}")
        else:
            print(f"- No changes needed for {html_file}")
    else:
        print(f"✗ File not found: {html_file}")

print("\n✓ All footer contact information updated!")
