import sqlite3
from datetime import datetime
import faker
from random import randint, choice, sample
from itertools import cycle
from tabulate import tabulate

NUMBER_STUDENTS = randint(30, 50)
NUMBER_GROUPS = 3
NUMBER_LECTORS = randint(3, 5)
NUMBER_SUBJECTS = randint(5, 8)
NUMBER_MARKS = 100
NUMBER_MARKS_PER_STUDENT = 20

def create_db():
    # Read the SQL script file to create tables
    with open('create_tables.sql', 'r') as f:
        sql = f.read()

    # Connect to the database (if it doesn't exist, it will be created)
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        # Execute the SQL script to create tables in the database
        cur.executescript(sql)

def generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_LECTORS, NUMBER_SUBJECTS, NUMBER_MARKS):
    fake_data = faker.Faker()
    fake_students = [fake_data.name() for _ in range(NUMBER_STUDENTS)]
    fake_groups = [fake_data.name() for _ in range(NUMBER_GROUPS)]
    fake_lectors = [fake_data.name() for _ in range(NUMBER_LECTORS)]
    fake_subjects = [fake_data.name() for _ in range(NUMBER_SUBJECTS)]
    print(list(fake_subjects))
    print(len(fake_subjects))
    
    fake_marks = [fake_data.random_number(digits=2) for _ in range(NUMBER_MARKS)]  # Adjust digits as needed
    return fake_students, fake_groups, fake_lectors, fake_subjects, fake_marks

def prepare_data(students, groups, lectors, subjects, marks):
    # Prepare data for groups, lectors, and subjects
    for_groups = [(group,) for group in groups]
    for_lectors = [(lector,) for lector in lectors]
    
    # Generate lector IDs
    lector_ids = list(range(1, len(lectors) + 1))
 
    # Prepare data for subjects with correct lector IDs
    # for_subjects = [(subject, choice(lector_ids)) for subject in subjects]
    for_subjects = [(subject, lector_id) for subject,  lector_id in zip(subjects, cycle(lector_ids))]
    
    # Generate group IDs
    group_ids = list(range(1, len(groups) + 1))

    # Prepare data for students with correct group IDs
    for_students = [(student, group_id) for student, group_id in zip(students, cycle(group_ids))]
    
    
    # for_marks = []
    # for student_id, student in enumerate(students, start=1):
    #     # Вибрати випадкову підвибірку оцінок для студента
    #     student_marks = sample(marks, min(NUMBER_MARKS_PER_STUDENT, len(marks)))
    #     for subject_id in range(1, len(subjects) + 1):
    #         # Додати оцінки до загального списку для кожного предмету
    #         for mark in student_marks:
    #             for_marks.append((mark, subject_id, student_id))
    
    
    
    
    # Prepare data for marks with each student in each subject
    max_subject_id = len(subjects)  # Maximum subject ID
    print(max_subject_id)
    for_marks = []
    students_per_subject = len(students)  # Number of students per subject
    for subject_id in range(1, max_subject_id + 1):
        marks_for_subject = [(choice(marks), subject_id, student_id) for student_id in range(1, students_per_subject + 1)]
        for_marks.extend(marks_for_subject)
    
    return for_groups, for_lectors, for_students, for_subjects, for_marks



#, groups, lectors, subjects, marks
def insert_data_to_db(students, groups, lectors, subjects, marks) -> None:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        
        # Insert data into students table
        sql_to_students = """INSERT INTO students(name, group_id) VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)
        
        # Insert data into groups table
        sql_to_groups = """INSERT INTO groups(name) VALUES (?)"""
        cur.executemany(sql_to_groups, groups)
        
        # Insert data into lectors table
        sql_to_lectors = """INSERT INTO lectors(name) VALUES (?)"""
        cur.executemany(sql_to_lectors, lectors)
        
        # Insert data into subjects table
        sql_to_subjects = """INSERT INTO subjects(name, lector_id) VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)
        
        # Insert data into marks table
        sql_to_marks = """INSERT INTO marks(grade, subjects_id_fn, students_id_fn) VALUES (?, ?, ?)"""
        cur.executemany(sql_to_marks, marks)

def execute_query(sql: str) -> None:
    with sqlite3.connect('tables.db') as con:
        cur = con.cursor()
        
        with open(sql, 'r') as file:
            sql_query = file.read()
        cur.execute(sql_query)
        # Отримання назв стовбців
        columns = [description[0] for description in cur.description]
        # Отримання результатів запиту
        results = cur.fetchall()
        # Виведення результатів у вигляді таблиці
        print(tabulate(results, headers=columns, tablefmt="grid"))
        
        
def main():
    create_db() 
    students, groups, lectors, subjects, marks = generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_LECTORS, NUMBER_SUBJECTS, NUMBER_MARKS)
    # Prepare data in tuples format
    for_groups, for_lectors, for_students, for_subjects, for_marks = prepare_data(students, groups, lectors, subjects, marks)
    # Now you can insert this data into your database using SQL queries
    insert_data_to_db(for_students, for_groups, for_lectors, for_subjects, for_marks)
    count = 1
    print(f"Знайти 5 студентів із найбільшим середнім балом з усіх предметів. Query {count}:")
    print(execute_query("query_01.sql"))
    count += 1
    print(f"Знайти студента із найвищим середнім балом з певного предмета. Query {count}:")
    print(execute_query("query_02.sql"))
    count += 1
    print(f"Знайти середній бал у групах з певного предмета. Query {count}:")
    print(execute_query("query_03.sql"))
    count += 1
    print(f"Знайти середній бал на потоці (по всій таблиці оцінок). Query {count}:")
    print(execute_query("query_04.sql"))
    count += 1
    print(f"Знайти які курси читає певний викладач. Query {count}:")
    print(execute_query("query_05.sql"))
    count += 1
    print(f"Знайти список студентів у певній групі. Query {count}:")
    print(execute_query("query_06.sql"))
    count += 1
    print(f"Знайти оцінки студентів у окремій групі з певного предмета. Query {count}:")
    print(execute_query("query_07.sql"))
    count += 1
    print(f"Знайти середній бал, який ставить певний викладач зі своїх предметів. Query {count}:")
    print(execute_query("query_08.sql"))
    count += 1
    print(f"Знайти список курсів, які відвідує студент. Query {count}:")
    print(execute_query("query_09.sql"))
    count += 1
    print(f"Список курсів, які певному студенту читає певний викладач. Query {count}:")
    print(execute_query("query_10.sql"))
    

if __name__ == "__main__":
    main()
 
    
    