-- list place_title IS NULL
SELECT place_title 
FROM persons_event WHERE place_title IS NULL

-- update place_title IS NULL
UPDATE persons_event 
SET place_title = '' 
WHERE place_title IS NULL

-- update persons_person.birth_year
UPDATE persons_person 
SET birth_year = (SELECT substr(persons_event.date,1,4) FROM persons_event
WHERE persons_person.handle = persons_event.obj_handle AND persons_event.event_code = 12)

-- delete event data from one source
DELETE FROM persons_event
WHERE source_app = 8 -- 8: Malmön2

-- PersonFamily.sql
SELECT person.given_name FROM reference
JOIN family ON reference.ref_handle = family.handle
JOIN person on reference.obj_handle = person.handle
WHERE family.gramps_id = 'F0001'