from flask import Flask
from analyzer.repo_parser import clone_repo, get_structure

app = Flask(__name__)

@app.route("/")
def home():
    repo_url = "https://github.com/pallets/flask"

    repo_path = clone_repo(repo_url)
    folders, files = get_structure(repo_path)

    return f"""
    <h1>Codebase Storyteller</h1>

    <h2>Repository</h2>
    <p>{repo_url}</p>

    <h2>Folders</h2>
    <ul>
        {''.join([f'<li>{folder}</li>' for folder in folders])}
    </ul>

    <h2>Files</h2>
    <ul>
        {''.join([f'<li>{file}</li>' for file in files])}
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)