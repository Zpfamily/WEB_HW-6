SELECT  s.name as student, su.name AS subject
FROM marks m
LEFT JOIN students s ON s.id = m.students_id_fn 
LEFT JOIN subjects su ON m.subjects_id_fn = su.id 
WHERE s.id = 3
GROUP BY subject
ORDER BY subject