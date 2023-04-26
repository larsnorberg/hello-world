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

-- Analys av reference 1
SELECT obj_class, ref_class, COUNT() from reference
GROUP BY obj_class, ref_class
-- ORDER BY ref_class, obj_class

-- compare relation from event to place direct or via reference table
-- ingen skillnad upptäckt 2023-04-25
-- dock skiljer sig place.title från det som finns i picklad place.blob_data, för vissa rader
SELECT event.description, place.title, pp.title FROM reference AS ref
JOIN event on ref.obj_handle = event.handle
LEFT JOIN place ON ref.ref_handle = place.handle
LEFT JOIN place AS pp on event.place = pp.handle
WHERE ref.obj_class = 'Event' AND ref.ref_class = 'Place'

-- Analys av reference, event som saknar object
SELECT * from event
LEFT JOIN reference on event.handle = reference.ref_handle
WHERE obj_class IS NULL
