DROP TABLE IF EXISTS project_two.practice_summary;


CREATE TABLE project_two.practice_summary AS
SELECT
    difficulty_level,
    COUNT(*) AS total_practices,
    SUM(duration_minutes) AS total_practice_time,
    ROUND(AVG(duration_minutes), 2) AS average_practice_time
FROM project_two.michelle
GROUP BY difficulty_level
ORDER BY total_practice_time DESC;
