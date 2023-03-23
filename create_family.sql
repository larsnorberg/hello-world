DROP TABLE IF EXISTS family_ex;
CREATE TABLE family_ex (handle VARCHAR(50) PRIMARY KEY NOT NULL, gramps_id TEXT, father_handle VARCHAR(50), mother_handle VARCHAR(50), family_type TEXT, change INTEGER, private INTEGER);
CREATE INDEX family_gramps_id ON family_ex(gramps_id);
DROP TABLE IF EXISTS family_child_ex
CREATE TABLE family_ex (handle VARCHAR(50) PRIMARY KEY NOT NULL)