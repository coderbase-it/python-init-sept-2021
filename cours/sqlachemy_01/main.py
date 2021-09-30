from sqlalchemy import create_engine, Integer, ForeignKey, MetaData, Table, Column, String
engine = create_engine('sqlite:///base.db')
meta = MetaData()

students = Table( 'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)

meta.create_all(engine)


# creation de student
new_student = students.insert().values(name="Pierre")
print(new_student)
print(new_student.compile().params)
connection = engine.connect()
connection.execute(new_student)


# et récupération des students

query = students.select()

resultat = connection.execute(query)

for element in resultat:
    print(element)