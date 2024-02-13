SELECT  s.name AS subject, gr.name AS [group], ROUND(AVG(grade),2) as average_garde
FROM marks g
LEFT JOIN students s ON s.id = g.students_id_fn 
LEFT JOIN subjects d ON g.subjects_id_fn = d.id 
LEFT JOIN groups gr ON s.group_id = gr.id 
WHERE g.subjects_id_fn = 2
GROUP BY gr.id 
ORDER BY average_garde DESC
