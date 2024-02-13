    SELECT s.name AS subject, s.name as student, ROUND(AVG(grade),2) as average_garde
    FROM marks g
    LEFT JOIN students s ON s.id = g.students_id_fn 
    LEFT JOIN subjects d ON g.subjects_id_fn = d.id 
    WHERE g.subjects_id_fn = 2
    GROUP BY s.id
    ORDER BY average_garde DESC
    LIMIT 1