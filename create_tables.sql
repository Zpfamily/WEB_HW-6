-- Table: Groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Table: Lectors
DROP TABLE IF EXISTS lectors;
CREATE TABLE lectors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Table: Subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    lector_id INTEGER, 
    FOREIGN KEY (lector_id) REFERENCES lectors (id)
);   

-- Table: Students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
);

-- Table: Marks
DROP TABLE IF EXISTS marks;
CREATE TABLE marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade INTEGER,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    subjects_id_fn INTEGER,
    students_id_fn INTEGER,
    FOREIGN KEY (subjects_id_fn) REFERENCES subjects (id),
    FOREIGN KEY (students_id_fn) REFERENCES students (id)
);
