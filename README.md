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
yoyo apply --database=postgresql://ddvc:password@localhost:5432/ddvc_sourcing
```

#### Test Startups from Different Funding Stages in Health and Fintech
Pre-Seed & Seed Stage

Company Name:Attane Health   - Founders: Elise Bates , David Klick, Emily Brown 

Company Name:Secured Health  - Founders: Sean Crenshaw

Company Name:Included Health - - Founders:Lawrence „Rusty“ Hofmann, Owen Tripp

Company Name:healthOme - - Founders:David Stertzer, Darren Rowe

Company Name:Akute Health - - Founders:Shared Agarwal

Company Name:Humanaut Health - - Founders:Paul Paginate, Tony Cheng, Jim Donnelly

Company Name:Being Health - - Founders:Allie Sharma

Company Name:Always Health - - Founders:Peter Wang, Ian Börk

Company Name:Hi.Health - - Founders:Sebastian Gruber

Company Name:Swap Health - Founders:Aaron Doades

Company Name:moment.ai - - Founders:Megan Gray, Matthew Tarascio 

Company Name:Hang Health - - Founders:Chris Holbrook

Company Name:Definition Health - - Founders:Rosie Scott, Sandeep Chauhan


Series A+ 

Company Name:9fin - - Founders:Steven Hunter 

Company Name:Finally - - Founders:Felix Rodriguez, Edwin Mejia, Glennys Rodriguez 

Company Name:Growfin - - Founders:Raja Jayaraman, Aravind Gopalan

Company Name:Float - - Founders:Griffin Keglevich, Rob Khazzam, Ruslan Nikolaev

Company Name:Finmid - - Founders:Alexander Talkanitsa, Max Scheitel

Company Name:Neural Payments - - Founders:Mick Oppy 

Company Name:Anyfin - - Founders:Mikael Hussain , Filip Polhem

Company Name:Fintecture - - Founders:Faysal Oudmine, Javier Llorden

Company Name:FundThrough - - Founders:Deepak Ramachandran, Steven Uster 

Company Name:Fincom - - Founders:Gideon Drori 

### Run the server
```
fastapi dev app.py
```

Docs will be available at http://127.0.0.1:8000

## Documentation

The following project on startup sourcing receives inputs about opportunities from various sources, such as pitch decks,
urls, data providers, and more, and outputs a filtered and ranked list of the startups in descending order, based on how
they match with particular funds of a company. 