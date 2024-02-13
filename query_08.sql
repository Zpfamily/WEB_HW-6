SELECT l.name AS lector, su.name AS subject, ROUND(AVG(grade),2) as average_garde
FROM marks m 
LEFT JOIN subjects su ON m.subjects_id_fn  = su.id 
LEFT JOIN lectors l ON su.lector_id = l.id 
WHERE l.id = 1
GROUP BY su.id
