from peewee import *
from datetime import datetime
from config import config

# Database Connection
db = PostgresqlDatabase(
    config.db_name,
    user=config.db_user,
    password=config.db_password,
    host=config.db_host,
    port=config.db_port,
)

# Models
class BaseModel(Model):
    class Meta:
        database = db

class Company(BaseModel):
    id = AutoField()
    name = CharField()
    country = CharField()
    sector = CharField()
    team = TextField()  # JSON data
    contact = CharField()
    funding_stage = CharField()
    creation_date = DateField()
    investors = TextField()  # JSON data
    revenue = FloatField()
    revenue_growth = FloatField()
    total_amount_raised = FloatField()
    description = TextField()
    website = CharField()
    linkedin = CharField()
    harmonic_id = CharField()
    pdl_id = CharField()
    full_time_employees = IntegerField()
    full_time_employees_growth = FloatField()
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

class People(BaseModel):
    id = AutoField()
    first_name = CharField()
    last_name = CharField()
    education = CharField()
    past_companies = TextField()  # JSON data
    linkedin = CharField()
    github = CharField()
    previous_founded_companies_count = IntegerField()
    role = CharField()

class CompanyPeople(BaseModel):
    id = AutoField()
    company = ForeignKeyField(Company, backref='company')
    people = ForeignKeyField(People, backref='people')

class Filter(BaseModel):
    id = AutoField()
    name = CharField()
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

class FilterCompany(BaseModel):
    id = AutoField()
    filter = ForeignKeyField(Filter, backref='companies')
    company = ForeignKeyField(Company, backref='filters')

class Ranker(BaseModel):
    id = AutoField()
    name = CharField()
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

class RankerCompany(BaseModel):
    id = AutoField()
    company = ForeignKeyField(Company, backref='rankers')
    ranker = ForeignKeyField(Ranker, backref='companies')
    score = FloatField()
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)


