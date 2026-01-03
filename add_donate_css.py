import os

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

donate_css = '''    /* ========== DONATE BUTTON ========== */
    .donate-btn {
      display: inline-block;
      padding: 0.7rem 1.5rem;
      background: #E8B356;
      color: white;
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 700;
      border: none;
      cursor: pointer;
      border-radius: 4px;
      transition: all 0.3s ease;
      margin-left: 1rem;
    }

    .donate-btn:hover {
      background: #d4a051;
      box-shadow: 0 4px 12px rgba(232, 179, 86, 0.4);
      transform: translateY(-2px);
    }

    .donate-btn:active {
      transform: translateY(0);
    }

'''

for html_file in html_files:
    file_path = os.path.join(os.getcwd(), html_file)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if donate-btn CSS already exists
        if '.donate-btn {' in content:
            print(f"- {html_file} already has donate button CSS")
            continue
        
        # Find the logo-icon CSS and insert donate-btn CSS after it
        if '.logo-icon {' in content:
            # Find the closing brace of logo-icon
            start_pos = content.find('.logo-icon {')
            if start_pos != -1:
                # Find the closing brace
                brace_count = 0
                i = start_pos
                while i < len(content):
                    if content[i] == '{':
                        brace_count += 1
                    elif content[i] == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            # Insert after this closing brace
                            insert_pos = i + 1
                            content = content[:insert_pos] + '\n\n' + donate_css + content[insert_pos:]
                            
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(content)
                            print(f"✓ Added donate button CSS to {html_file}")
                            break
                    i += 1
        else:
            print(f"✗ Could not find .logo-icon in {html_file}")
    else:
        print(f"✗ File not found: {html_file}")

print("\n✓ Donate button CSS added to all pages!")
