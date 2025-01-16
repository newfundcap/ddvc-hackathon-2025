BEGIN;
ALTER TABLE ranker_company
    ADD COLUMN category      TEXT,
    ADD COLUMN justification TEXT,
    ADD COLUMN warnings      TEXT
;

ALTER TABLE ranker ALTER COLUMN description TYPE TEXT;


COMMIT;