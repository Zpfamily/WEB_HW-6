SELECT su.name AS subject, s.name as student, l.name AS lector
FROM marks m
LEFT JOIN students s ON s.id = m.students_id_fn 
LEFT JOIN subjects su ON m.subjects_id_fn = su.id 
LEFT JOIN lectors l ON su.lector_id = l.id 
WHERE s.id = 3 AND l.id = 1
GROUP BY subject
ORDER BY subject