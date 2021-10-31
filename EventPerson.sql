-- EventPerson.sql
SELECT event.gramps_id,person.gramps_id,person.given_name,person.surname 
FROM event
JOIN reference ON event.handle = reference.ref_handle
JOIN person ON reference.obj_handle = person.handle
WHERE person.gramps_id = 'I0005'