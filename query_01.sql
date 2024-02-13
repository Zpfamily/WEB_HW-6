    SELECT s.name as student, ROUND(AVG(grade),2) as average_grade
    FROM marks m
    LEFT JOIN students s ON s.id = m.students_id_fn 
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5
    
