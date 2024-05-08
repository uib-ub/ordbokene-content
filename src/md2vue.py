import os
import re
import markdown

# Initialize a dictionary to store the content of the markdown files
content = {}

# Traverse the content directory
for root, dirs, files in os.walk('content'):
    # Skip the locale directories
    if os.path.dirname(root) == 'content':
        continue
    # Find all .md files
    md_files = [f for f in files if f.endswith('.md')]
    for md_file in md_files:
        # Extract the locale, directory, and slug from the root path and file name
        locale = os.path.relpath(root, 'content').split(os.sep)[0]
        directory = os.path.basename(root)
        slug = os.path.splitext(md_file)[0]
        # Strip the preceding numbers from the slug
        slug = re.sub(r'^\d+\.', '', slug)
        # If there is no slug, set it to 'index'
        if not slug:
            slug = 'index'
        with open(os.path.join(root, md_file), 'r', encoding="utf8") as f:
            md_content = f.read()
            # Convert markdown to HTML
            html_content = markdown.markdown(md_content)
            # Store the HTML content in the dictionary
            if directory not in content:
                content[directory] = {}
            if locale not in content[directory]:
                content[directory][locale] = {}
            content[directory][locale][slug] = html_content

# Create the Vue components
for directory, locales in content.items():
    vue_component = "<template>\n  <div>\n"
    subheadings = {}
    headings = {}
    
    for locale, slugs in locales.items():
        subheadings[locale] = {}
        
        for slug, html_content in slugs.items():
            condition = '!$route.params.slug' if slug == 'index' else f"$route.params.slug === '{slug}'"
            vue_component += f"    <template v-if=\"$route.params.locale === '{locale}' && { condition } \">\n"
            vue_component += f"      {html_content}\n"
            vue_component += "    </template>\n"

            # Extract the first heading from the HTML content
            match = re.search(r'<h1>(.*?)</h1>', html_content)
            if match:
                if slug == 'index':
                    headings[locale] = match.group(1)
                else:
                    subheadings[locale][slug] = match.group(1)
            

        # Add the navigation links
    
    for locale in headings:
        vue_component += f"<ContentNavigation v-if=\"$route.params.locale === '{locale}'\" :headings=\"{headings}\" :subheadings=\"{subheadings[locale]}\"/>\n"
                
    vue_component += "  </div>\n</template>\n\n"


    # Write the Vue component to the content-components directory
    output_file = os.path.join('content-components', f"{directory}.vue")
    with open(output_file, 'w', encoding="utf8") as f:
        f.write(vue_component)

