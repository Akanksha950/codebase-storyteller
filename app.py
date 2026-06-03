import os
from flask import Flask, render_template, request
from analyzer.repo_parser import clone_repo, get_structure
from analyzer.tech_detector import detect_tech_stack
from analyzer.storyteller import generate_summary
from analyzer.code_health import calculate_health

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        repo_url = request.form.get("repo_url", "").strip()
        try:
            repo_path = clone_repo(repo_url)
            folders, files = get_structure(repo_path)
            tech_stack = detect_tech_stack(repo_path)
            summary = generate_summary(repo_url, folders, files, tech_stack)
            health_score, breakdown = calculate_health(repo_path, folders, files)

            result = {
                "repo_url": repo_url,
                "folders": folders,
                "files": files,
                "tech_stack": tech_stack,
                "summary": summary,
                "health_score": health_score,
                "breakdown": breakdown,
            }
        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)