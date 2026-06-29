# Setup Guide (VS Code)

1. Install [Python 3.10+](https://www.python.org/downloads/)
2. Install [VS Code](https://code.visualstudio.com/)
3. Install extensions:
   - **Python** (Microsoft)
   - **Pylance**
   - **Black Formatter**
   - **GitLens** (optional)
4. Open the repo folder in VS Code: `code .`
5. Select the venv interpreter: `Ctrl+Shift+P` → "Python: Select Interpreter" → choose `./venv`
6. Set format-on-save (optional) in `settings.json`:
```json
{
  "editor.formatOnSave": true,
  "python.formatting.provider": "black"
}
```
7. Run any file with the ▶️ button or `python path/to/file.py` in the integrated terminal.
