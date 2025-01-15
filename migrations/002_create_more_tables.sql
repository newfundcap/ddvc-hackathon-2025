BEGIN;
CREATE TABLE education
(
    id          SERIAL PRIMARY KEY,
    people_id   INTEGER REFERENCES people (id),
    school_name VARCHAR,
    school_type VARCHAR,
    degrees     TEXT[],
    start_date  DATE,
    end_date    DATE,
    majors      TEXT[],
    summary     TEXT,
    created_at  TIMESTAMP DEFAULT NOW(),
    updated_at  TIMESTAMP DEFAULT NOW()
);

CREATE TABLE experience
(
    id           SERIAL PRIMARY KEY,
    people_id    INTEGER REFERENCES people (id),
    company_name VARCHAR,
    industry     VARCHAR,
    start_date   DATE,
    end_date     DATE,
    title        TEXT,
    summary      TEXT,
    created_at   TIMESTAMP DEFAULT NOW(),
    updated_at   TIMESTAMP DEFAULT NOW()
);

ALTER TABLE company
    ALTER COLUMN creation_date DROP NOT NULL;


COMMIT;