# Komroom

## Step 1

remote this repo

```terminal
git clone
```

## Step 2

make virtual enviroment

```terminal
python -m venv .env
```

## Step 3

Configure .env file

```env
DATABASE_PORT=5432
POSTGRES_PASSWORD=
POSTGRES_USER=postgres
POSTGRES_DB=komroom
POSTGRES_HOST=postgres
POSTGRES_HOSTNAME=127.0.0.1
```

## Step 4

run the envirotment first and then run the server using ``uvicorn``. In here I'm using linux to run the enviroment

```terminal
source env/bin/activate
uvicorn app.main:app --host localhost --port 8000 --reload

```

## Step 5

### Alembic Command

Below are some important Alembic commands you should know:

- init – prepares the project to work with alembic
- upgrade – upgrade the database to a later version
- downgrade – revert to a previous version
- revision – creates a new revision file
