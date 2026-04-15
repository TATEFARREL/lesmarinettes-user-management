FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN uv pip install --system --no-cache-dir -r pyproject.toml

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
