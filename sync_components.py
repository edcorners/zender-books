import os
import re
import glob

def sync_components():
    print("Syncing HTML components...")
    
    if not os.path.exists('components/nav.html') or not os.path.exists('components/footer.html'):
        print("Error: components/nav.html or components/footer.html not found.")
        return

    with open('components/nav.html', 'r', encoding='utf-8') as f:
        nav_content = f.read().strip('\n')
        
    with open('components/footer.html', 'r', encoding='utf-8') as f:
        footer_content = f.read().strip('\n')

    # Regex patterns to find content between markers
    nav_pattern = re.compile(r'(<!-- COMPONENT:NAV -->\n).*?([ \t]*<!-- /COMPONENT:NAV -->)', re.DOTALL | re.IGNORECASE)
    footer_pattern = re.compile(r'(<!-- COMPONENT:FOOTER -->\n).*?([ \t]*<!-- /COMPONENT:FOOTER -->)', re.DOTALL | re.IGNORECASE)

    html_files = glob.glob('*.html')
    count = 0
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        
        # Replace the contents using lambda to avoid regex escape issues
        content = nav_pattern.sub(lambda m: m.group(1) + nav_content + '\n' + m.group(2), content)
        content = footer_pattern.sub(lambda m: m.group(1) + footer_content + '\n' + m.group(2), content)

        if content != original_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")
            count += 1
        else:
            print(f"Verified {file}")
            
    print(f"Sync complete. Updated {count} file(s).")

if __name__ == '__main__':
    sync_components()
