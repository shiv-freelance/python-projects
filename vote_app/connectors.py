import psycopg2


# database connection
def get_sql_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="super123",
            host="localhost",
            port="5432",
        )
        print("connection with db established!")
    except Exception as exception:
        print(f"Got error while connecting db {exception}")

    return conn


