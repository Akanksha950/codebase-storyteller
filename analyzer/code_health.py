import os

def calculate_health(repo_path, folders, files):
    score = 0
    breakdown = {}

    has_readme = any(f.lower().startswith("readme") for f in files)
    breakdown["README"] = 100 if has_readme else 0
    score += breakdown["README"]

    has_license = any(f.lower().startswith("license") for f in files)
    breakdown["License"] = 100 if has_license else 0
    score += breakdown["License"]

    has_tests = any("test" in f.lower() for f in folders + files)
    breakdown["Tests"] = 80 if has_tests else 20
    score += breakdown["Tests"]

    has_docs = any("doc" in f.lower() for f in folders + files)
    breakdown["Docs"] = 80 if has_docs else 20
    score += breakdown["Docs"]

    total = round(score / 4)
    return total, breakdown