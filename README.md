<div align="center">

# 🐍 Python Learning Journey

**A structured, beginner-to-advanced Python learning repository — notes, exercises, and real projects, all in one place.**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![PRs](https://img.shields.io/badge/PRs-Welcome-orange?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/Prakhar1Ojha/Python-Learning-Journey?style=flat-square)

</div>

---

## 📑 Table of Contents

- [About](#-about)
- [Repository Structure](#-repository-structure)
- [Learning Roadmap](#-learning-roadmap)
- [Progress Tracker](#-progress-tracker)
- [Setup Instructions](#-setup-instructions)
- [Folder Guide](#-folder-guide)
- [Learning Resources](#-learning-resources)
- [Best Practices](#-best-practices--coding-standards)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 📖 About

This is my personal Python learning lab — a living repository I'll keep building on for years. It holds my notes, topic-by-topic exercises, and small-to-large real projects as I go from fundamentals to frameworks, automation, data, and beyond.

It's organized like an open-source educational project so that:
- I can track my own progress over time
- Anyone learning Python can reuse the structure, notes, or exercises
- Each topic folder is self-contained with its own README, examples, and practice problems

## 🗂 Repository Structure

```text
Python-Learning-Journey/
├── README.md                  # You are here
├── ROADMAP.md                 # Full learning path, beginner → advanced
├── RESOURCES.md                # Books, courses, channels, docs
├── CHEATSHEET.md               # Quick-reference Python syntax & commands
├── NOTES.md                    # Running personal notes / gotchas
├── FAQ.md                      # Common questions & error fixes
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
│
├── docs/                       # Setup guides, style guide, learning plan
├── exercises/                  # beginner / intermediate / advanced drills
├── projects/                   # Real mini & full projects
├── notes/                      # Topic deep-dive notes
├── snippets/                   # Reusable code snippets
├── interview/                  # Interview prep & common questions
├── dsa-python/                 # Data structures & algorithms in Python
│
├── oop/  modules/  file-handling/  exception-handling/
├── decorators/  generators/  iterators/
├── multithreading/  multiprocessing/  async/
├── database/  web-scraping/  testing/  scripts/
├── flask/  django/  fastapi/
├── data-analysis/  machine-learning/
│
└── .github/                    # Issue templates, PR template, CI workflows
```

Every topic folder follows the same pattern: a `README.md` explaining the concept, an `examples/` set of runnable `.py` files, and a few practice exercises.

## 🛣 Learning Roadmap

See [ROADMAP.md](./ROADMAP.md) for the full beginner → advanced path (basics → OOP → file/exception handling → functional tools → concurrency → web frameworks → data/ML → interviews).

## ✅ Progress Tracker

| Stage | Topics | Status |
|---|---|---|
| Foundations | Variables, Data Types, Operators, Strings, Loops | 🟡 In Progress |
| Core Structures | Lists, Tuples, Sets, Dicts, Functions, Modules | ⬜ Not Started |
| Intermediate | OOP, File/Exception Handling, Iterators, Generators, Decorators | ⬜ Not Started |
| Functional & Utility | Lambda/Map/Filter/Reduce, Regex, Collections, Datetime, JSON/CSV | ⬜ Not Started |
| Systems | OS/Pathlib, Typing, Logging, Threading, Multiprocessing, Asyncio | ⬜ Not Started |
| Web & APIs | Networking, REST APIs, Web Scraping, Automation | ⬜ Not Started |
| Frameworks | Flask, Django, FastAPI | ⬜ Not Started |
| Data & ML | NumPy, Pandas, Matplotlib, ML Basics | ⬜ Not Started |
| Career | Testing, Deployment, Interview Prep | ⬜ Not Started |

Update this table as topics are completed — swap ⬜ → 🟡 → ✅.

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/Prakhar1Ojha/Python-Learning-Journey.git
cd Python-Learning-Journey

# Create a virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

See [docs/setup.md](./docs/setup.md) for VS Code setup, and [docs/installation.md](./docs/installation.md) for a deeper install/venv guide.

### Useful Commands

**Git**
```bash
git status
git add .
git commit -m "feat: add decorators notes"
git push origin main
```

**Python / pip / venv**
```bash
python file.py            # Run a file
pip install <package>     # Install a package
pip freeze > requirements.txt
deactivate                 # Exit venv
```

## 📂 Folder Guide

| Folder | Purpose |
|---|---|
| `exercises/` | Graded practice problems (beginner → advanced) |
| `projects/` | Standalone runnable mini and full projects |
| `notes/` | Deep-dive written notes per topic |
| `snippets/` | Copy-paste-ready reusable code |
| `interview/` | Common interview questions & answers |
| `dsa-python/` | Data structures & algorithms implementations |
| `oop/`, `decorators/`, `generators/`, `iterators/` | Core language concept folders |
| `multithreading/`, `multiprocessing/`, `async/` | Concurrency & parallelism |
| `flask/`, `django/`, `fastapi/` | Web framework learning |
| `data-analysis/`, `machine-learning/` | NumPy/Pandas/Matplotlib & ML basics |

Each of these folders contains its own `README.md` — start there.

## 📚 Learning Resources

Full list in [RESOURCES.md](./RESOURCES.md) — books, YouTube channels, docs, and practice sites.

## 🧹 Best Practices & Coding Standards

- Follow **PEP8**
- Use **type hints** on function signatures
- Write **docstrings** for every public function/class
- Prefer clear names over comments; comment only the *why*, not the *what*
- One concept per script inside `examples/` folders
- Keep functions small and testable

## 🤝 Contributing

This is primarily a personal learning log, but suggestions, corrections, and PRs are welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md).

## 📄 License

Licensed under the [MIT License](./LICENSE).

## 📬 Contact

**Prakhar Ojha**
GitHub: [@Prakhar1Ojha](https://github.com/Prakhar1Ojha)

---

### 🎯 Future Goals
- Complete all roadmap stages with working examples
- Build 10+ real projects (web, automation, data, ML)
- Add automated tests + CI for every project
- Publish select notes as blog posts
