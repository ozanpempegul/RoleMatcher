# job_alerts

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

## Database Migrations

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