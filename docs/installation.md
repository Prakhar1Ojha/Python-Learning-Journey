# Installation & Virtual Environment Guide

## 1. Check Python version
```bash
python --version
```

## 2. Create a virtual environment
```bash
python -m venv venv
```

## 3. Activate it
```bash
# Windows (cmd)
venv\Scripts\activate.bat

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

## 4. Install dependencies
```bash
pip install -r requirements.txt
```

## 5. Freeze new dependencies
```bash
pip freeze > requirements.txt
```

## 6. Deactivate when done
```bash
deactivate
```

## Why use a venv?
Keeps each project's dependencies isolated so installing a package for one project never breaks another.
