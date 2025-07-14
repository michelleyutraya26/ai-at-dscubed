CREATE SCHEMA IF NOT EXISTS project_two;

CREATE TABLE IF NOT EXISTS project_two.michelle (
    session_id SERIAL PRIMARY KEY,
    practice_date DATE NOT NULL,
    duration_minutes INT CHECK (duration_minutes > 0),
    piece_played VARCHAR(100),
    difficulty_level VARCHAR(10) CHECK (difficulty_level IN ('Easy', 'Medium', 'Hard')),
    notes TEXT
);
