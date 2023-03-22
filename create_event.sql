DROP TABLE IF EXISTS event_ex;
CREATE TABLE event_ex (handle VARCHAR(50) PRIMARY KEY NOT NULL, gramps_id TEXT, date TEXT, description TEXT, place_handle VARCHAR(50), change INTEGER, private INTEGER);
CREATE INDEX event_gramps_id ON event_ex(gramps_id);
