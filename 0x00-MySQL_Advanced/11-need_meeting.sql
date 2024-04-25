-- lists all students with  a score under 80
-- and either have no `last_meeting` date or the `last_meeting` date is more than 7 months ago.
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));
