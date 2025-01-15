import json

from peewee import *
from datetime import datetime
from config import config
from playhouse.pool import PooledPostgresqlExtDatabase
from playhouse.postgres_ext import BinaryJSONField, PostgresqlExtDatabase

# Database Connection
db = PostgresqlExtDatabase(
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
    name = CharField(null=False)
    country = CharField()
    sector = CharField()
    contact = CharField()
    funding_stage = CharField()
    creation_date = DateField()
    investors = BinaryJSONField(default='[]')
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
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

class People(BaseModel):
    id = AutoField()
    first_name = CharField()
    last_name = CharField()
    education = CharField()
    past_companies = BinaryJSONField(default='{}')
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
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

class FilterCompany(BaseModel):
    id = AutoField()
    filter = ForeignKeyField(Filter, backref='companies')
    company = ForeignKeyField(Company, backref='filters')

class Ranker(BaseModel):
    id = AutoField()
    name = CharField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

class RankerCompany(BaseModel):
    id = AutoField()
    company = ForeignKeyField(Company, backref='rankers')
    ranker = ForeignKeyField(Ranker, backref='companies')
    score = FloatField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)


