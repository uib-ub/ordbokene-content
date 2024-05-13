# ordbokene-content
Source for text content at ordbokene.no

## Add a locale
Create a subdirectory in content/ with the three letter [ISO 639-2 code](https://www.loc.gov/standards/iso639-2/php/code_changes.php) as folder name.
Add your text files as seen in the existing locales. Preceding numbers in the filenames decide the order of the sections, and the first section of "help" and "about" will be shown as the introduction.

## Override text in the welcome page articles
Add a .md file in welcome/bm or welcome/nn with the article ID as filename, e. g. 40922.md

## Conversion to vue components
The markdown is sanitized and converted to vue componens by running src/md2vue.py
Html tags and attributes not found in ALLOWED_TAGS and ALLOWED_ATTRIBUTES in md2vue will be removed.
External contributors should not modify .gitlab-ci.yml or the files in src/

