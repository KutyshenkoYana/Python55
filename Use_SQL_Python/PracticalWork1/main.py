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

    for row in result:
        print(row)


show_doctors_specializations(session)
