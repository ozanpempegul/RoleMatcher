# RoleMatcher

-------------------------------

## Python Virtual Environment

To create a new Python virtual environment, run:

```bash
python -m venv venv
```

Activate the environment with:

- On Windows:
    ```bash
    venv\Scripts\activate
    ```
- On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

-------------------------------

## Managing Dependencies

To create a `requirements.txt` file with your current environment's packages, run:

```bash
pip freeze > requirements.txt
```

To install dependencies from `requirements.txt`, run:

```bash
pip install -r requirements.txt
```

-------------------------------

## Create .env file

Create a `.env` file in the project root. Do not commit it; `.env` is already in `.gitignore`.

### SQLite (default)

Set `USE_SQLITE=True` and add your OpenAI settings. PostgreSQL variables are not required.

```
USE_SQLITE=True

OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-5-mini
```

By default the database is stored at:

```
%LOCALAPPDATA%\RoleMatcher\RoleMatcher.db
```

To use a different SQLite file, add `SQLITE_DB_PATH` to `.env`:

```
USE_SQLITE=True
SQLITE_DB_PATH=C:\Users\you\data\RoleMatcher.db

OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-5-mini
```

### PostgreSQL (optional)

Set `USE_SQLITE=False`, then provide PostgreSQL credentials:

```
USE_SQLITE=False

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=your_database_user
POSTGRES_PASSWORD=your_database_password
POSTGRES_DB=your_database_name

OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-5-mini
```

Replace each placeholder with your actual values.

## Database Migrations

To initialize Alembic in your project, run:

```bash
alembic init alembic
```

To create a new migration version, run:

```bash
alembic revision --autogenerate -m "your message here"
```

To apply migrations and upgrade the database, run:

```bash
alembic upgrade head
```

To downgrade the database to a previous migration, run:

```bash
alembic downgrade <revision>
```
Replace `<revision>` with the target revision identifier (e.g., `-1` for one step back).

-------------------------------

Compile the .qrc to a Python module:

- PySide6:
```bash
pyside6-rcc resources.qrc -o resources_rc.py
```

-------------------------------

## Packaging (PyInstaller / Inno Setup)

When building a standalone installer, include the read-only `prompts/` folder in the app bundle. The app loads prompt templates from that folder at runtime and will fail if it is missing from the packaged build.

Runtime data is stored outside the bundle:

| Data | Location |
|------|----------|
| Logs | `logs/` next to the running app (exe folder when installed) |
| Summaries | `summaries/` next to the running app |
| Tailored resumes / cover letters | `tailored_resumes/` next to the running app |
| SQLite database | `%LOCALAPPDATA%\RoleMatcher\RoleMatcher.db` |

When running from source, logs, summaries, and tailored resumes are created relative to the current working directory instead.

**Important:** Bundle `prompts/` with PyInstaller (for example via `--add-data "prompts;prompts"`) and include the same folder in your Inno Setup installer next to the executable or inside the PyInstaller bundle.