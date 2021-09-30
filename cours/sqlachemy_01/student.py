from sqlalchemy import Column, String, Integer, Table, ForeignKey

class Student:
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name ):
        self.name = name