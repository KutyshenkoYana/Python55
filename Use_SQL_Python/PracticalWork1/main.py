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


def show_doctors_specializations(session):
    query = """
    SELECT D.SURNAME, S.NAME
    FROM DoctorsSpecializations DS
        JOIN DOCTORS D ON DS.DOCTOR_ID = D.ID
        JOIN SPECIALIZATION S ON DS.SPECIALIZATION_ID = S.ID
    """
    query = text(query)

    result = session.execute(query)
    print("doctors surname")

    for row in result:
        print(row)


# show_doctors_specializations(session)


def show_doctors_salary(session):
    query = """
    SELECT D.SURNAME, D.SALARY + D.PREMIUM
    FROM DOCTORS D JOIN VACATIONS V ON D.ID = DOCTOR_ID
    WHERE V.ENDDATE > CURRENT_DATE AND V.START_DATE < CURRENT_DATE
    """

    query = text(query)

    result = session.execute(query)
    print("Doctors surname and salary")

    for row in result:
        print(row)


# show_doctors_salary(session)


def _show_name_departmens(session):
    query = """
    SELECT NAME
    FROM DEPARTMENTS
    """

    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)


def show_wards(session):
    _show_name_departmens(session)
    department_name = input("Enter department name: ")

    query = f"""
    SELECT *
    FROM WARDS W JOIN DEPARTMENTS D ON D.ID = W.DEPARTMENT_ID
    WHERE D.NAME = '{department_name}'
    """

    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)


# show_wards(session)


def show_donation(session):
    month_number = input("Enter month (number): ")
    year_number = input("Enter year: ")

    query = f"""
    SELECT *
    FROM DONATIONS D
        JOIN DEPARTMENT DEP ON D.DEPARTMENT_ID = DEP.ID
        JOIN SPONSORS S ON D.SPONSOR_ID = S.ID
    WHERE EXTRACT(MONTH FROM DONATION_DATE) = '{month_number}'
        AND EXTRACT(YEAR FROM DONATION_DATE) = '{year_number}'
    """

    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)


show_donation(session)
