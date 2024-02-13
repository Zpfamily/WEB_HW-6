SELECT s.name as student, su.name AS subject, gr.name AS [group], grade
FROM marks m
LEFT JOIN students s ON s.id = m.students_id_fn 
LEFT JOIN subjects su ON m.subjects_id_fn = su.id 
LEFT JOIN groups gr ON s.group_id = gr.id 
WHERE su.id = 1 AND gr.id = 1
ORDER BY grade DESC