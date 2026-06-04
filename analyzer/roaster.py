import os
from groq import Groq

def roast_repo(repo_url, folders, files, tech_stack, health_score):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    prompt = f"""
You are a savage but funny code reviewer who roasts GitHub repositories like a comedy roast.

Repository: {repo_url}
Tech Stack: {', '.join(tech_stack)}
Folders: {', '.join(folders)}
Files: {', '.join(files)}
Health Score: {health_score}/100

Write 3-4 short, funny, savage roast lines about this repository.
Be like a comedian — funny, sharp, but not mean.
Use emojis. Keep each line punchy.
Examples of tone:
- "This repo has no tests. Living life on the edge! 💀"
- "README has 2 lines. Even a fortune cookie gives more info. 🍪"
Make it hilarious but relevant to what you see in the repo.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )

    return response.choices[0].message.content