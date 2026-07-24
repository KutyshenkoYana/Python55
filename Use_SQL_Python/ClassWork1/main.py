import os

import dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

dotenv.load_dotenv()  # read env

# отримуемо дани з .env
host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
db = os.getenv("DB")

# шлях до бази данних
db_uri = f"postgresql+psycopg2://{user}:{password}@{host}/{db}"

# створення пидключення (engine)
engine = create_engine(db_uri)

# створення сесии (session) на основи пидключення (engine)
Session = sessionmaker(bind=engine)  # клас з можливистю пидключення до бази данних
session = Session()  # конкретна сесия

# отримання таблиць з бази данних
# metadata = MetaData()
# metadata.reflect(bind=engine)
#
# tables = metadata.tables
# print(list(tables.keys()))


# запуск sql запиту , конкретний доктор
doctor_name = input("Enter doctor name: ")

query = f"""
    SELECT *
    FROM DOCTORS
    WHERE NAME = '{doctor_name}'
"""

# пидправити текст
query = text(query)


# запуск
result = session.execute(query)

# виведення результату рядкив
for row in result:
    print(row)
