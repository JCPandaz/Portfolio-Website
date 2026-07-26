# Personal Portfolio Website

Coded using HTML, CSS, and JavaScript and designed with custom graphics. Highlights attributes about me, including my skills, experience, and education. Has links to all my socials and a contact field at the bottom.

## GitHub Pages Export

This project is written as a Flask app, but it can be exported to static files for GitHub Pages.

Build the static site:

```powershell
python build_static.py
```

GitHub Pages can then publish from the `docs/` folder.

If publishing under a project URL such as `https://username.github.io/repo-name/`, build with the repo path:

```powershell
python build_static.py --base-path /repo-name
```
