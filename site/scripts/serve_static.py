"""Serve the built Pages artifact under its project base path for browser QA.

This deliberately serves ``dist/`` instead of starting an Astro runtime: the
public deployment is static, and loading every generated person page into a
preview process needlessly increases local test memory use.
"""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


BASE_PATH = "/before-oss"


class PagesHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        pathname = urlsplit(self.path).path
        if pathname != BASE_PATH and not pathname.startswith(f"{BASE_PATH}/"):
            self.send_error(404, "Outside the project base path")
            return None
        return super().send_head()

    def translate_path(self, path: str) -> str:
        pathname = urlsplit(path).path
        if pathname == BASE_PATH:
            pathname = "/"
        elif pathname.startswith(f"{BASE_PATH}/"):
            pathname = pathname[len(BASE_PATH) :]
        return super().translate_path(pathname)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=4321)
    args = parser.parse_args()
    dist = Path(__file__).resolve().parents[1] / "dist"
    if not (dist / "index.html").is_file():
        raise SystemExit("Build the static site before browser tests: npm run build")
    handler = partial(PagesHandler, directory=str(dist))
    server = ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    print(f"Serving {dist} at http://127.0.0.1:{args.port}{BASE_PATH}/", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
