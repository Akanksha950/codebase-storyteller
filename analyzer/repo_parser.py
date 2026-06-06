# import os
# import git

# def clone_repo(repo_url):
#     repo_name = repo_url.rstrip("/").split("/")[-1]
#     clone_path = os.path.join("repos", repo_name)

#     os.makedirs("repos", exist_ok=True)

#     if not os.path.exists(clone_path):
#         git.Repo.clone_from(repo_url, clone_path)

#     return clone_path


# def get_structure(repo_path):
#     folders = []
#     files = []

#     for item in os.listdir(repo_path):
#         full_path = os.path.join(repo_path, item)

#         if os.path.isdir(full_path):
#             folders.append(item)
#         else:
#             files.append(item)

#     return sorted(folders), sorted(files)


import os
import git

def clone_repo(repo_url):
    repo_name = repo_url.rstrip("/").split("/")[-1]
    clone_path = os.path.join("/tmp", "repos", repo_name)

    os.makedirs(os.path.join("/tmp", "repos"), exist_ok=True)

    if not os.path.exists(clone_path):
        git.Repo.clone_from(repo_url, clone_path)

    return clone_path


def get_structure(repo_path):
    folders = []
    files = []

    if not os.path.exists(repo_path):
        return folders, files

    for item in os.listdir(repo_path):
        full_path = os.path.join(repo_path, item)
        if os.path.isdir(full_path):
            folders.append(item)
        else:
            files.append(item)

    return sorted(folders), sorted(files)