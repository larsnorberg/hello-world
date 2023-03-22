DROP TABLE IF EXISTS person_ex;
CREATE TABLE person_ex (handle VARCHAR(50) PRIMARY KEY NOT NULL, gramps_id TEXT, gender TEXT, given_name TEXT, surname TEXT, title TEXT, change INTEGER, private INTEGER);
CREATE INDEX person_gramps_id ON person_ex(gramps_id);
