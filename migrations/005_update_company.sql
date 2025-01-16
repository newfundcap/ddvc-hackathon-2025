BEGIN;
ALTER TABLE company ADD COLUMN logo_url varchar;
ALTER TABLE people DROP COLUMN past_companies;

COMMIT;