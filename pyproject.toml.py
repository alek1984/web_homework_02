[tool.poetry]
name = "personal_assistant"
version = "1.0.0"
description = "Персональний помічник"
authors = ["Ваше ім'я <email@example.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.10"
django = "^4.2"
djangorestframework = "^3.14"
fastapi = "^0.110.0"
uvicorn = "^0.27"
sqlalchemy = "^2.0"
alembic = "^1.12"
psycopg2-binary = "^2.9"
motor = "^3.3"
pymongo = "^4.6"
pydantic = "^2.5"
python-dotenv = "^1.0"

[tool.poetry.dev-dependencies]
pytest = "^8.0"
pytest-cov = "^4.1"

