BEGIN;

ALTER TABLE people
    ADD COLUMN sex                       VARCHAR(10),
    ADD COLUMN twitter_url               VARCHAR,
    ADD COLUMN work_email                VARCHAR,
    ADD COLUMN personal_emails           JSONB DEFAULT '[]'::JSONB,
    ADD COLUMN industry                  VARCHAR,
    ADD COLUMN job_title                 VARCHAR,
    ADD COLUMN location_country          VARCHAR,
    ADD COLUMN inferred_years_experience INT,
    ADD COLUMN summary                   TEXT,
    ADD COLUMN interests                 JSONB DEFAULT '[]'::JSONB,
    ADD COLUMN linkedin_connections      INT,
    ADD COLUMN pdl_id                    VARCHAR,
    ADD COLUMN harmonic_id               VARCHAR;

COMMIT;