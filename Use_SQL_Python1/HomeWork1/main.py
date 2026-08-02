import os

import dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

dotenv.load_dotenv()

host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
db = os.getenv("DB")

db_uri = f"postgresql+psycopg2://{user}:{password}@{host}/{db}"

engine = create_engine(db_uri)

Session = sessionmaker(bind=engine)
session = Session()

# metadata = MetaData()
# metadata.reflect(bind=engine)
#
# tables = metadata.tables
# print(list(tables.keys()))


# Вивести інформацію про всі навчальні групи
def show_groups(session):
    query = """
    SELECT *
    FROM Groups
    """

    query = text(query)
    result = session.execute(query)

    print("Groups: ")

    for row in result:
        print(row)


# show_groups(session)


# Вивести назви кафедр і груп, які до них відносяться (JOIN)
def show_departments_groups(session):
    query = """
    SELECT D.Name, G.Name
    FROM Departments D
        JOIN Groups G ON D.Id = G.DepartmentId
    """

    query = text(query)
    result = session.execute(query)

    print("Departments and groups:")

    for row in result:
        print(row)


# show_departments_groups(session)


# Вивести назви груп, що належать до конкретного факультету
def show_groups_by_faculty(session):
    faculty_name = input("Enter faculty name: ")

    query = f"""
    SELECT G.Name
    FROM Groups G
        JOIN Departments D ON G.DepartmentId = D.Id
        JOIN Faculties F ON D.FacultyId = F.Id
    WHERE F.Name = '{faculty_name}'
    """

    query = text(query)
    result = session.execute(query)

    print("Groups:v")

    for row in result:
        print(row)


# show_groups_by_faculty(session)
