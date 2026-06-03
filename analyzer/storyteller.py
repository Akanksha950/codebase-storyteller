import os
from groq import Groq

def generate_summary(repo_url, folders, files, tech_stack):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    prompt = f"""
You are an expert developer who explains GitHub repositories in simple English.

Repository: {repo_url}
Tech Stack: {', '.join(tech_stack)}
Folders: {', '.join(folders)}
Files: {', '.join(files)}

Write a friendly 3-4 sentence summary:
1. What this project does
2. What technologies it uses
3. Who would use it

Keep it simple, clear, and exciting!
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )

    return response.choices[0].message.content