from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

table_assoc = Table(
    Column('course_id', Integer, ForeignKey('course.id')),
    Column('student_id', Integer, ForeignKey('student.id'))
)


class Course:
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    students = relationship("Student", secondary=table_assoc)

    def __init__(self, title, description, students):
        self.title = title
        self.description = description
        self.students = students
