from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

from app import EDUCATION, EXPERIENCES, PROJECTS, app


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "docs"
STATIC_DIR = ROOT / "static"


def normalize_base_path(value: str) -> str:
    value = value.strip()
    if not value or value == "/":
        return ""
    return "/" + value.strip("/")


def apply_base_path(content: str, base_path: str) -> str:
    if not base_path:
        return content

    content = re.sub(r'(?P<attr>\b(?:href|src|action)=["\'])/', rf'\g<attr>{base_path}/', content)
    content = re.sub(r'url\(["\']/', f'url("{base_path}/', content)
    return content


def output_path_for_route(route: str) -> Path:
    clean_route = route.strip("/")
    if not clean_route:
        return OUTPUT_DIR / "index.html"
    return OUTPUT_DIR / clean_route / "index.html"


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_redirect(route: str, target: str, base_path: str) -> None:
    target_href = f"{base_path}{target}" if base_path else target
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url={target_href}">
    <link rel="canonical" href="{target_href}">
    <title>Redirecting...</title>
</head>
<body>
    <p><a href="{target_href}">Continue</a></p>
</body>
</html>
"""
    write_file(output_path_for_route(route), html)


def collect_routes() -> list[str]:
    routes = [
        "/",
        "/about",
        "/experience",
        "/education",
        "/projects",
        "/socials",
        "/contact",
    ]

    routes.extend(f"/experience/{item['slug']}" for item in EXPERIENCES)
    routes.extend(f"/education/{item['slug']}" for item in EDUCATION if item.get("detail_page"))
    routes.extend(f"/projects/{item['slug']}" for item in PROJECTS)
    return routes


def export_site(base_path: str) -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    OUTPUT_DIR.mkdir(parents=True)
    shutil.copytree(STATIC_DIR, OUTPUT_DIR / "static")
    write_file(OUTPUT_DIR / ".nojekyll", "")

    css_path = OUTPUT_DIR / "static" / "style.css"
    if css_path.exists():
        css_path.write_text(apply_base_path(css_path.read_text(encoding="utf-8"), base_path), encoding="utf-8")

    client = app.test_client()
    for route in collect_routes():
        response = client.get(route)
        if response.status_code != 200:
            raise RuntimeError(f"Could not export {route}: HTTP {response.status_code}")

        html = response.get_data(as_text=True)
        write_file(output_path_for_route(route), apply_base_path(html, base_path))

    write_redirect("/education/uiuc-computer-engineering", "/education/uiuc/", base_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export the Flask portfolio to static files for GitHub Pages.")
    parser.add_argument(
        "--base-path",
        default="",
        help="Optional GitHub Pages base path, for example /Personal-Portfolio. Leave blank for a custom domain or username.github.io root site.",
    )
    args = parser.parse_args()

    base_path = normalize_base_path(args.base_path)
    export_site(base_path)
    print(f"Exported static site to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
