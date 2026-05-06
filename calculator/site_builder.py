"""Simple static site builder for the calculator demo.

Generates a `site/` directory with an `index.html` and static assets.
"""
import os
import shutil

ROOT = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(ROOT, "templates")


def build_site(output_dir: str = "site") -> None:
    """Render templates and copy static files to `output_dir`.

    This is intentionally simple: it copies `index.html.tpl` to
    `site/index.html` and copies the `static/` folder.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Copy index
    tpl_path = os.path.join(TEMPLATES_DIR, "index.html.tpl")
    out_path = os.path.join(output_dir, "index.html")
    with open(tpl_path, "r", encoding="utf-8") as f:
        content = f.read()
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Copy static files
    static_src = os.path.join(TEMPLATES_DIR, "static")
    static_dst = os.path.join(output_dir, "static")
    if os.path.exists(static_dst):
        shutil.rmtree(static_dst)
    shutil.copytree(static_src, static_dst)


if __name__ == "__main__":
    build_site()
