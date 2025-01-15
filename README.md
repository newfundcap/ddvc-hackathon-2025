# ddvc-hackathon-2025

Code for the Data Driven VC Hackathon 2025 in Paris

# STARTUP SOURCING

This project was built as part of the Data-Driven VC Hackathon organized
by [Red River West](https://redriverwest.com) & [Bivwak! by BNP Paribas](https://bivwak.bnpparibas/)

## Installation

### Virtual env

Use `python 3.13.x`

```
python3 -m venv env
source env/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Setup the database

```
psql postgres;
```

```sql
CREATE USER ddvc WITH PASSWORD 'password';
CREATE DATABASE "ddvc_sourcing" WITH OWNER "ddvc";
```

### Create the tables
```
yoyo apply --database=postgresql://localhost:5432/ddvc_sourcing
```


### Run the server
```
fastapi dev app.py
```

Docs will be available at http://127.0.0.1:8000

## Documentation

The following project on startup sourcing receives inputs about opportunities from various sources, such as pitch decks,
urls, data providers, and more, and outputs a filtered and ranked list of the startups in descending order, based on how
they match with particular funds of a company. 