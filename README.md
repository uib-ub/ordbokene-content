# ordbokene-content
Source for text content at ordbokene.no

## Add a locale
Create a subdirectory in content/ with the three letter [ISO 639-2 code](https://www.loc.gov/standards/iso639-2/php/code_changes.php) as folder name.
Add your text files as seen in the existing locales. Preceding numbers in the filenames decide the order of the sections, and the first section of "help" and "about" will be shown as the introduction.

## Override text in the welcome page articles
Add a .md file in welcome/bm or welcome/nn with the article ID as filename, e. g. 40922.md

## Security: sanitation of html tags
Html tags not found in the list found in the list in md2vue.py will be removed

