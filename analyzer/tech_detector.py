import os

TECH_SIGNATURES = {
    "Python": ["requirements.txt", "setup.py", "pyproject.toml", ".py"],
    "JavaScript": ["package.json", ".js"],
    "TypeScript": [".ts", "tsconfig.json"],
    "React": [".jsx", ".tsx"],
    "Docker": ["Dockerfile", "docker-compose.yml"],
    "HTML/CSS": [".html", ".css"],
    "Java": [".java", "pom.xml"],
    "Go": ["go.mod", ".go"],
    "Rust": ["Cargo.toml", ".rs"],
    "C++": [".cpp", ".hpp"],
}

def detect_tech_stack(repo_path):
    detected = []
    all_files = []

    for root, dirs, files in os.walk(repo_path):
        for f in files:
            all_files.append(f)

    for tech, signatures in TECH_SIGNATURES.items():
        for sig in signatures:
            if any(f.endswith(sig) or f == sig for f in all_files):
                detected.append(tech)
                break

    return list(set(detected))