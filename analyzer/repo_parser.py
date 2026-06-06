import os
import subprocess

def clone_repo(repo_url):
    repo_name = repo_url.rstrip("/").split("/")[-1]
    clone_path = os.path.join("/tmp", "repos", repo_name)

    os.makedirs(os.path.join("/tmp", "repos"), exist_ok=True)

    if not os.path.exists(clone_path):
        subprocess.run(
            ["git", "clone", repo_url, clone_path],
            check=True,
            capture_output=True
        )

    return clone_path


def get_structure(repo_path):
    folders = []
    files = []

    if not os.path.exists(repo_path):
        return folders, files

    for item in os.listdir(repo_path):
        if item == '.git':
            continue
        full_path = os.path.join(repo_path, item)
        if os.path.isdir(full_path):
            folders.append(item)
        else:
            files.append(item)

    return sorted(folders), sorted(files)