import sqlite3
from student import Student

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE students (
            first text,
            last text,
            sn integer
            )""")

def insert_stud(stud):
    with conn:
        c.execute("INSERT INTO students VALUES (:first, :last, :sn)", {'first': stud.first, 'last': stud.last, 'sn': stud.sn})


def get_studs_by_name(lastname):
    c.execute("SELECT * FROM students WHERE last=:last", {'last': lastname})
    return c.fetchall()

def remove_stud(stud):
    with conn:
        c.execute("DELETE from students WHERE first = :first AND last = :last",
                  {'first': stud.first, 'last': stud.last})

stud_1 = Student('Erwin', 'Milan', 2014101852)
stud_2 = Student('Jose', 'Rizal', 2014123456)

insert_stud(stud_1)
insert_stud(stud_2)

emps = get_studs_by_name('Milan')
print(emps)

conn.close()