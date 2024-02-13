SELECT gr.name as [group], 
       s.name as student, 
       SUBSTR(s.name, INSTR(s.name, ' ') + 1) AS last_name
FROM students s
LEFT JOIN groups gr ON s.group_id = gr.id 
WHERE group_id = 1
ORDER BY last_name;
