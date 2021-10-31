-- PersonFamily.sql
SELECT person.given_name FROM reference
JOIN family ON reference.ref_handle = family.handle
JOIN person on reference.obj_handle = person.handle
WHERE family.gramps_id = 'F0001'