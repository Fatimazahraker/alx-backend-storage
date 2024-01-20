-- No table for a meeting
-- SQL script that creates a view need_meeting

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80 
AND (students.last_meeting IS NULL OR students.last_meeting < DATE_ADD(NOW(), INTERVAL -1 MONTH));
