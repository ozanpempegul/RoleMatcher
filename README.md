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

## Create .env file
To store your database credentials securely, create a `.env` file in your project's root directory. Add your database information in the following format:

```
DB_HOST=your_database_host
DB_PORT=your_database_port
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name

USE_SQLITE=True
SQLITE_DB_PATH=./job_alerts.db

API_KEY = "YOUR_HASDATA_API_KEY"
base_url = "https://api.hasdata.com/scrape/indeed/listing"
```

Replace each value with your actual database and api details. This file should not be committed to version control; add `.env` to your `.gitignore` file.

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