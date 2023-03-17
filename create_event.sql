DROP TABLE IF EXISTS event_ex;
CREATE TABLE event_ex (handle VARCHAR(50) PRIMARY KEY NOT NULL, gramps_id TEXT, date_str TEXT, description TEXT, place_handle VARCHAR(50), change_str TEXT, private INTEGER)
DROP INDEX IF EXISTS event_gramps_id;
CREATE INDEX event_gramps_id ON event_ex(gramps_id);
INSERT INTO event_ex (handle, gramps_id) values ('abcd', 'E0001')