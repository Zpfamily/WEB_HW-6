    SELECT l.name AS lector, s.name AS subject
FROM marks m 
LEFT JOIN subjects s ON m.subjects_id_fn  = s.id 
LEFT JOIN lectors l ON s.lector_id = l.id 
WHERE l.id = 1
GROUP BY s.id
