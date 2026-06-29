# ❓ FAQ & Common Error Fixes

### `ModuleNotFoundError: No module named 'x'`
You forgot to activate your venv or install the dependency.
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### `IndentationError`
Python is whitespace-sensitive — mixing tabs and spaces breaks it. Set your editor to use spaces only (4 per indent level).

### `git push` rejected
```bash
git pull origin main --rebase
git push origin main
```

### venv not activating on Windows (PowerShell)
Run PowerShell as admin and allow scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### `pip` installs to wrong Python version
Use `python -m pip install <package>` to guarantee it installs to the active interpreter.

### Circular import errors
Usually means two modules import each other. Restructure so shared code lives in a third module both import from.

---

Add new Q&A pairs here as you hit issues — this file is meant to grow with the repo.
