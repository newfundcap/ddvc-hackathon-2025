from peewee import *
from datetime import datetime
from config import config
from playhouse.postgres_ext import BinaryJSONField, PostgresqlExtDatabase, ArrayField

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
    class Meta:
        db_table = 'company'

    id = AutoField()
    name = CharField(null=False)
    country = CharField()
    sector = CharField()
    logo_url = CharField()
    contact = CharField()
    funding_stage = CharField()
    creation_date = DateField()
    investors = BinaryJSONField()
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
    class Meta:
        db_table = 'people'

    id = AutoField()
    first_name = CharField()
    last_name = CharField()
    linkedin = CharField()
    github = CharField()
    previous_founded_companies_count = IntegerField()
    role = CharField()
    sex = CharField()
    twitter_url = CharField()
    work_email = CharField() 
    personal_emails = BinaryJSONField()
    industry = CharField()
    job_title = CharField()
    location_country = CharField()
    inferred_years_experience = IntegerField()
    summary = TextField() 
    interests = BinaryJSONField()
    pdl_id = CharField()
    harmonic_id = CharField()
    linkedin_connections = IntegerField()



class CompanyPeople(BaseModel):
    class Meta:
        db_table = 'company_people'

    id = AutoField()
    company = ForeignKeyField(Company, backref='employees')
    people = ForeignKeyField(People, backref='companies')



class Filter(BaseModel):
    class Meta:
        db_table = 'filter'

    id = AutoField()
    name = CharField()
    settings = BinaryJSONField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)


class FilterCompany(BaseModel):
    class Meta:
        db_table = 'filter_company'

    id = AutoField()
    filter = ForeignKeyField(Filter, backref='companies')
    company = ForeignKeyField(Company, backref='filters')


class Ranker(BaseModel):
    class Meta:
        db_table = 'ranker'

    id = AutoField()
    name = CharField()
    description = TextField() # summary of diff types of rankers, e.g. investment thesis or investor preferences
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)


class RankerCompany(BaseModel):
    class Meta:
        db_table = 'ranker_company'

    id = AutoField()
    company = ForeignKeyField(Company, backref='rankers')
    ranker = ForeignKeyField(Ranker, backref='companies')
    score = FloatField()
    category = CharField()
    justification = CharField()
    warnings = CharField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)


class Education(BaseModel):
    class Meta:
        db_table = 'education'

    id = AutoField()
    people = ForeignKeyField(Company, backref='education')
    school_name = CharField()
    school_type = CharField()
    degrees = ArrayField(CharField)
    start_date = DateField()
    end_date = DateField()
    majors = ArrayField(CharField)
    summary = TextField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)


class Experience(BaseModel):
    class Meta:
        db_table = 'experience'

    id = AutoField()
    people = ForeignKeyField(Company, backref='experience')
    company_name = CharField()
    industry = CharField()
    start_date = DateField()
    end_date = DateField()
    title = CharField()
    summary = TextField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
