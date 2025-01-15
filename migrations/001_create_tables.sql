BEGIN;
CREATE TABLE company
(
    id                         SERIAL PRIMARY KEY,
    name                       VARCHAR NOT NULL,
    country                    VARCHAR,
    sector                     VARCHAR,
    team                       JSONB  ,
    contact                    VARCHAR,
    funding_stage              VARCHAR,
    creation_date              DATE    NOT NULL,
    investors                  JSONB ,
    revenue                    FLOAT ,
    revenue_growth             FLOAT ,
    total_amount_raised        FLOAT ,
    description                TEXT  ,
    website                    VARCHAR,
    linkedin                   VARCHAR,
    harmonic_id                VARCHAR,
    pdl_id                     VARCHAR,
    full_time_employees        INTEGER,
    full_time_employees_growth FLOAT ,
    created_at                 TIMESTAMP DEFAULT NOW(),
    updated_at                 TIMESTAMP DEFAULT NOW()
);

CREATE TABLE people
(
    id                               SERIAL PRIMARY KEY,
    first_name                       VARCHAR NOT NULL,
    last_name                        VARCHAR NOT NULL,
    education                        VARCHAR ,
    past_companies                   JSONB   ,
    linkedin                         VARCHAR ,
    github                           VARCHAR ,
    previous_founded_companies_count INTEGER ,
    role                             VARCHAR
);

CREATE TABLE company_people
(
    id         SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES company (id),
    people_id  INTEGER REFERENCES people (id)
);

CREATE TABLE filter
(
    id         SERIAL PRIMARY KEY,
    name       VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP
);

CREATE TABLE filter_company
(
    id         SERIAL PRIMARY KEY,
    filter_id  INTEGER REFERENCES filter (id),
    company_id INTEGER REFERENCES company (id)
);

CREATE TABLE ranker
(
    id         SERIAL PRIMARY KEY,
    name       VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP
);

CREATE TABLE ranker_company
(
    id         SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES company (id),
    ranker_id  INTEGER REFERENCES ranker (id),
    score      FLOAT NOT NULL default 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP
);
COMMIT;