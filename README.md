# 🔍 Codebase Storyteller

> **Understand any GitHub repository instantly — powered by AI**

Codebase Storyteller is an AI-powered web tool that analyzes any public GitHub repository and gives you a complete picture in seconds — structure, tech stack, health score, and a plain-English summary.

Built for the **Open Source Hackathon 2026** 🏆

---

## 🚀 Live Demo

> Paste any GitHub URL → Click Analyze → Get instant insights!

---

## ✨ Features

| Feature | Description |
|---|---|
| 🗂️ **Repo Structure** | See all top-level folders and files instantly |
| 🔍 **Tech Stack Detection** | Automatically detects Python, JS, Docker, React, and 10+ more |
| 🤖 **AI Summary** | Plain-English explanation of what the project does |
| 📊 **Code Health Score** | Rates README, tests, docs, and license out of 100 |
| 🔥 **Roast Mode** | AI gives a savage-but-funny critique of the codebase |
| 📋 **Copy Report** | One-click shareable report |
| ⚡ **GSAP Animations** | Smooth, professional UI animations |

---

## 🛠️ Tech Stack

- **Backend** — Python, Flask
- **AI** — Groq API (LLaMA 3.3 70B)
- **Frontend** — HTML, CSS, JavaScript, GSAP
- **Libraries** — GitPython, Groq SDK

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Akanksha950/codebase-storyteller
cd codebase-storyteller
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get a free Groq API key
👉 https://console.groq.com → Sign up → Create API Key

### 5. Set your API key
```bash
# Windows
$env:GROQ_API_KEY="your_key_here"

# Mac/Linux
export GROQ_API_KEY="your_key_here"
```

### 6. Run the app
```bash
python app.py
```

### 7. Open in browser
http://127.0.0.1:5000


---

## 🎯 How It Works

User enters GitHub URL
↓
Flask receives the request
↓
GitPython clones the repository
↓
Analyzer reads folders & files
↓
Tech stack detected from file signatures
↓
Groq AI generates plain-English summary
↓
Health score calculated (README, tests, docs, license
↓
Results displayed with smooth animations

---

## 📁 Project Structure

codebase-storyteller/
│
├── app.py                  # Flask app — main entry point
├── requirements.txt        # Python dependencies
├── README.md               # You are here!
│
├── analyzer/
│   ├── init.py
│   ├── repo_parser.py      # Clones repo, reads structure
│   ├── tech_detector.py    # Detects tech stack
│   ├── storyteller.py      # AI summary via Groq
│   ├── code_health.py      # Health score calculator
│   └── roaster.py          # AI roast mode 🔥
│
├── templates/
│   └── index.html          # Frontend UI
│
└── static/
└── style.css           # Additional styles

---

## 🌍 Real World Problem Solved

Millions of developers waste hours trying to understand unfamiliar codebases. Whether you're:
- 🎓 A **student** trying to contribute to open source
- 👔 A **developer** onboarding to a new project
- 🏢 A **team** evaluating third-party code

**Codebase Storyteller** gives you instant clarity — no more digging through hundreds of files manually.

---

## 🙋 Author

Made with ❤️ by **Akanksha Kumari**
Open Source Hackathon 2026

---

## 📄 License

MIT License — free to use and modify!