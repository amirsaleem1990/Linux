#!/home/amir/.venv_base/bin/python3

import os
import re
import requests
from urllib.parse import urlparse

TEST_PATH_RE = re.compile(r'(^|/)tests?(/|$)', re.IGNORECASE)

def _is_test_py(path: str) -> bool:
    """
    Heuristics for test files:
      - in a tests/ or test/ directory, OR
      - filename starts with test_ or ends with _test.py
    """
    if not path.endswith(".py"):
        return False
    name = path.split("/")[-1].lower()
    in_tests_dir = bool(TEST_PATH_RE.search(path))
    by_name = name.startswith("test_") or name.endswith("_test.py")
    return in_tests_dir or by_name

def _parse_github_pr_url(pr_url: str):
    """
    Accepts URLs like:
      https://github.com/<owner>/<repo>/pull/<number>
    Returns (owner, repo, number)
    """
    u = urlparse(pr_url)
    parts = [p for p in u.path.strip("/").split("/") if p]
    if len(parts) < 4 or parts[2] != "pull":
        raise ValueError("Not a valid GitHub PR URL: " + pr_url)
    owner, repo, _, number = parts[:4]
    return owner, repo, int(number)

def count_py_changes(
    pr_url: str,
    token: str | None = None,
    include_status: tuple[str, ...] = ("added", "modified"),
) -> dict:
    """
    Count .py test vs non-test files changed in a PR.
    Only counts files whose change 'status' is in include_status (default: added, modified).

    Returns:
      {
        "test_py_changed": <int>,
        "non_test_py_changed": <int>,
        "details": {
            "tests": [<paths>],
            "non_tests": [<paths>]
        }
      }
    """
    owner, repo, number = _parse_github_pr_url(pr_url)

    headers = {"Accept": "application/vnd.github+json"}
    token = token or os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    session = requests.Session()
    session.headers.update(headers)

    test_paths = []
    non_test_paths = []

    page = 1
    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{number}/files"
        resp = session.get(url, params={"page": page, "per_page": 100}, timeout=30)
        if resp.status_code == 404:
            raise RuntimeError("PR not found or repository is private without a valid token.")
        resp.raise_for_status()
        items = resp.json()
        if not items:
            break

        for f in items:
            status = f.get("status", "")
            path = f.get("filename", "")
            # Only count Python files with desired statuses
            if status not in include_status or not path.endswith(".py"):
                continue

            if _is_test_py(path):
                test_paths.append(path)
            else:
                non_test_paths.append(path)

        page += 1

    # Deduplicate paths in case of pagination overlap (shouldn't happen, but safe)
    test_paths = sorted(set(test_paths))
    non_test_paths = sorted(set(non_test_paths))

    return {
        "test_py_changed": len(test_paths),
        "non_test_py_changed": len(non_test_paths),
        "details": {
            "tests": test_paths,
            "non_tests": non_test_paths,
        },
    }

if __name__ == "__main__":
    # Example:

    pr = input("Enter you pr: ")
    result = count_py_changes(pr)  # optionally pass token=... or set GITHUB_TOKEN
    print(result)
