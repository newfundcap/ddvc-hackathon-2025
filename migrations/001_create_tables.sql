BEGIN;
CREATE TABLE company
(
    id                         SERIAL PRIMARY KEY,
    name                       VARCHAR NOT NULL,
    country                    VARCHAR NOT NULL,
    sector                     VARCHAR NOT NULL,
    team                       JSONB   NOT NULL,
    contact                    VARCHAR NOT NULL,
    funding_stage              VARCHAR NOT NULL,
    creation_date              DATE    NOT NULL,
    investors                  JSONB   NOT NULL,
    revenue                    FLOAT   NOT NULL,
    revenue_growth             FLOAT   NOT NULL,
    total_amount_raised        FLOAT   NOT NULL,
    description                TEXT    NOT NULL,
    website                    VARCHAR NOT NULL,
    linkedin                   VARCHAR NOT NULL,
    harmonic_id                VARCHAR NOT NULL,
    pdl_id                     VARCHAR NOT NULL,
    full_time_employees        INTEGER NOT NULL,
    full_time_employees_growth FLOAT   NOT NULL,
    created_at                 TIMESTAMP DEFAULT NOW(),
    updated_at                 TIMESTAMP DEFAULT NOW()
);
-- Other table definitions
COMMIT;
