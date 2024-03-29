# egomedia-django

This is the repository for the egomedia project at [Kings Digital Lab](https://kdl.kcl.ac.uk)

This project uses the technologies outlined in our [Technology Stack](https://stackshare.io/kings-digital-lab/django) and is configured to use [Vagrant](https://www.vagrantup.com/) for local development and [Fabric](http://www.fabfile.org/) for deployment.

## Release notes

### 1.0.0

- Create specific page for browsing the data.
- Add content separator tiles to the browse page.
- Remove contributors dimension from the visualisation.
- Refine display of keywords/tags.
- Enable visited links.
- Make breadcrumbs more visible.

### 0.2.4

- Added live filter to Table of Contents in project pages
- Updated pip package django-kdl-wagtail

### 0.2.3

### 0.2.2 Increment #8

- Replaced logo with new version
- Improved responsive menu on smaller screens
- CSS clean up

### 0.2.1 Increment #8

- Homepage

  - Implemented new visualisation (interactive)
  - Added toggle to expand/collapse viz section

- Merged Pillow dependency (security)
- Bug and typo fixes

### 0.2 Increment #8

- Homepage

  - Styling (content separation)
  - Sticky block for filtering
  - Nested project filters
  - Changed order of cards to: themes, projects, researchers

- New cards styling

  - Show/hide path, description, tags
  - Style differentiation between parent and child cards
  - Seethrough title block over image

- Project page

  - Sidebar restyled to match child pages in cards
  - Tags are sorted alphabetically

- Sitemap page
- Text search
- Accessibility improvements
- Colour palette changes
- Removed capitalisation from tags
- Google analytics set up (ready but not active)
- Bug fixes and performance improvements

### 0.1.1 Increment #7

- First draft of visualization
- Fixed modal size (now large)
- Fixed modal overlap issue with close button
- Fixes bibliography missing from ToC
- Back to home page after clicking on a search result re-applies the previous filters
- Added `lang` attribute to the site
- Issue fixes
- Display sub-project tags in project cards on the home page
- Fixed bug for videos added within richtext editor
- Reduced max-width for embedded objects (now 640px)
- Fixed bug: anchor link was display before content rather than on the side
- Fixed bug: margin-bottom on floating elements
- Added breadcrumbs to project pages
- Nested list for Projects index page (all level display)
- Refactor facet model: new facet types and items can be added via the admin interface
- Themes are no longer mandatory for Researchers

### 0.1 Increment #6

- Bug fixes
- Changed wording in ToC
- ERC and KCL logos in the footer
- Expose block anchor links
- Replacing floating content with flexbox
- Zotero bibliography
- Option to choose which blocks display in the TOC
- Endnotes
- Markdown foonote/endnote syntax
- Static site generation via the wagtail bakery package
- Modified sticky sidebar to allow for internal scrolling
- Reduce session duration to one hour

### 0.0.9

- Bug fixes
- Introduction display on theme pages
- Markdown links
- Styling improvements

### 0.0.8

- Bug fixes
- Styled nested ordered lists
- Image gallery with links to pages and external URLs
- Image gallery modal styling

### 0.0.7

- Fixed floating content issue
- Style for default ToC
- Faceted search on homepage
- Align classes for images
- Feed image in the promote tab
- Researcher page
- Adding sticky function to project sidebar

### 0.0.6

- Image gallery behaviour and styling

### 0.0.5

- Blockquote styling
- Embed blocks
- Map block
- Timeline styling

### 0.0.4

- Fixed dropdown menus functionality
- Fixed nested modals

### 0.0.3

- Added dropdown menus
- Removed testing tags

### 0.0.2

- Added error page templates

### 0.0.1

First minor release.

- Cards
- Content blocks
- Fixed Font Awesome Pro 5 issue
- Initial styling
- Page types

## Getting started

1. Enter the project directory: `cd egomedia-django`
2. Start the virtual machine: `vagrant up`
3. SSH into the virtual machine: `vagrant ssh`
4. Run the local development server: `./manage.py runserver 0:8000`

You can then access the site locally at [http://localhost:8000](http://localhost:8000)

If the project is ldap-enabled, you can login using your LDAP credentials. Note: LDAP authentication will only work within the college firewall. Alternatively, use the default superuser login:

username: `vagrant`
password: `vagrant`

Note: This login will only work on a locally deployed virtual machine.

## Requirements

- Ansible >= 2.3
- NodeJS
- Vagrant >= 1.9
- VirtualBox >= 5.0
