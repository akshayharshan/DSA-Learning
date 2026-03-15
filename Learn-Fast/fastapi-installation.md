python3 -m venv .venv
# Activate environment:
Windows: .venv\Scripts\activate
macOS/Linux: source .venv/bin/activate 
pip install "fastapi[standard]"

uvicorn app.main:app --reload

./.venv/bin/python -m fastapi dev app/main.py
