"""student-profiles database interface."""
# std lib
from pathlib import Path
from pprint import pprint
import sqlite3
import sys
from typing import List, Text, Tuple

# custom
# from backend.students import Student
from students import Student
# from students import Student

# print("databases.py:", __path__)
pprint(sys.path)
db = "backend/data/student-profiles.db"
print("DB exists?:", Path(db).exists())
print("Abs path:", Path(".").resolve())


class StudentProfiles():
    def __init__(self) -> None:
        self.connection = sqlite3.connect(db)
        #self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self._create_names_table()


    def __exit__(self) -> None:
        self.cursor.close()
        self.connection.close()
        print("student-profiles DB closed.")

    
    def _create_names_table(self) -> None:
        self.connection.execute("""create table if not exists names (first text, last text, unique(first, last))""")


    def add_student(self, student: Student) -> None:
        """Add a student to the student-profiles database."""

        first = student.first_name
        last = student.last_name
        self.cursor.execute("""insert or ignore into names values(?, ?)""", (first, last))
        self.connection.commit()


    def all(self) -> List[Tuple[Text]]:
        """Get all records in student-profiles database."""
        records = self.cursor.execute("""select * from names""")
        return records.fetchall()


    def first_name_lookup(self, name: Text) -> List[Text]:
        """Gets student record."""

        record = self.cursor.execute("select * from names where first=?", (name,))
        return record.fetchall()


    def lookup(self, student: Student) -> List[Text]:
        """Gets student record."""

        record = self.cursor.execute(\
            "select * from names where first=? and last=?",\
            (student.first_name, student.last_name,))
        return record.fetchall()


    def create_record(self, student: Student) -> None:
        """Create a new student record."""

        first = student.first_name
        last = student.last_name
        # self.cursor.execute("""insert into names (?, ?) where not exists(select * from names where first=? and last=?)""", (first, last, first, last))

if __name__ == "__main__":
    
    print("Adding student records to DB.")
    profiles = StudentProfiles()
    alice = Student("alice", "zebra")
    bob = Student("bob", "yankee")
    carol = Student("carol", "x-ray")
    profiles.add_student(alice)
    profiles.add_student(bob)
    profiles.add_student(carol)
    print(profiles.all())
    
    # display record count
