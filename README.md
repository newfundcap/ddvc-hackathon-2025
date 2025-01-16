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
##### Company Overview

---

###### Pre-Seed & Seed Stage

- **Company Name:** Attane Health  
  **Founders:** Elise Bates, David Klick, Emily Brown
  **Website:** https://attane-health.com/

- **Company Name:** Secured Health  
  **Founders:** Sean Crenshaw
**Website:** http://securedhealth.co/
  
- **Company Name:** Included Health  
  **Founders:** Lawrence “Rusty” Hofmann, Owen Tripp
**Website:** https://includedhealth.com/
  
- **Company Name:** healthOme  
  **Founders:** David Stertzer, Darren Rowe
**Website:** https://healthome.com/
  
- **Company Name:** Akute Health  
  **Founders:** Shared Agarwal
  **Website:** http://akutehealth.com/
  
 --> Should be ranked low, if the search is made for Brain Health Startups, as this is EHR startup

- **Company Name:** Humanaut Health  
  **Founders:** Paul Paginate, Tony Cheng, Jim Donnelly
  **Website:** http://humanauthealth.com/


- **Company Name:** Being Health  
  **Founders:** Allie Sharma
**Website:** https://beinghealth.co/
  
- **Company Name:** Always Health  
  **Founders:** Peter Wang, Ian Börk
**Website:** https://alwayshealth.io/
  
- **Company Name:** Hi.Health  
  **Founders:** Sebastian Gruber
**Website:** http://hi.health/
  
- **Company Name:** Swap Health  
  **Founders:** Aaron Doades
**Website:** https://swaphealth.com/
  
- **Company Name:** moment.ai  
  **Founders:** Megan Gray, Matthew Tarascio
**Website:** https://www.moment.ai/
  
- **Company Name:** Hanu Health  
  **Founders:** Chris Holbrook
**Website:** https://hanuhealth.com/
  
- **Company Name:** Definition Health  
  **Founders:** Rosie Scott, Sandeep Chauhan
**Website:** https://www.definitionhealth.co.uk/
  
---

###### Series A+

- **Company Name:** 9fin  
  **Founders:** Steven Hunter
**Website:** https://9fin.com/
  
- **Company Name:** Finally  
  **Founders:** Felix Rodriguez, Edwin Mejia, Glennys Rodriguez
  **Website:** https://finally.com/
  
 --> Should be filtered out, due to Debt Stage Funding Stage

- **Company Name:** Growfin  
  **Founders:** Raja Jayaraman, Aravind Gopalan
  **Website:** https://growfin.ai/

- **Company Name:** Float  
  **Founders:** Griffin Keglevich, Rob Khazzam, Ruslan Nikolaev
**Website:** https://floatfinancial.com/
  
- **Company Name:** Finmid  
  **Founders:** Alexander Talkanitsa, Max Scheitel
**Website:** https://finmid.com/
  
- **Company Name:** Neural Payments  
  **Founders:** Mick Oppy
**Website:** https://neuralpayments.com/
  
- **Company Name:** Anyfin  
  **Founders:** Mikael Hussain, Filip Polhem
**Website:** https://anyfin.com/
  
- **Company Name:** Fintecture  
  **Founders:** Faysal Oudmine, Javier Llorden
**Website:** http://fintecture.com/
  
- **Company Name:** FundThrough  
  **Founders:** Deepak Ramachandran, Steven Uster
**Website:** https://fundthrough.com/
  
- **Company Name:** Fincom  
  **Founders:** Gideon Drori
**Website:** https://fincom.co/
  

### Run the server
```
fastapi dev app.py
```

Docs will be available at http://127.0.0.1:8000

## Documentation

The following project on startup sourcing receives inputs about opportunities from various sources, such as pitch decks,
urls, data providers, and more, and outputs a filtered and ranked list of the startups in descending order, based on how
they match with particular funds of a company.