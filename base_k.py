
import psycopg2 as db
import os
from dotenv import load_dotenv

load_dotenv()


class Database:
    @staticmethod
    def connect(query: str, type: str):
        database = db.connect(
            database=os.getenv("DB_NAME"),
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

        cursor = database.cursor()
        cursor.execute(query)

        data_type = ["insert", "delete", "update", "create"]
        if type in data_type:
            database.commit()

            if type == "insert":
                return "inserted"

            elif type == "delete":
                return "deleted"

            else:
                return "updated"

        elif type == "select":
            return cursor.fetchall()

        else:
            return "*** Aniqlanmagan query ***"