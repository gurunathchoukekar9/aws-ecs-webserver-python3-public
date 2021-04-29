# db/postgre_db.py

import psycopg2
import json


class MyPostgreDb:
    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port

    def list_postgre_db_tables(self):
        conn = None
        try:
            print("Inside list_postgre_db_tables table")
            conn = psycopg2.connect(database=self.db_name, user=self.db_user, password=self.db_password,
                                    host=self.db_host, port=self.db_port)
            print(conn)
            db_cursor = conn.cursor()

            sql_list_table = """
            SELECT table_schema, table_name
            FROM information_schema.tables
            WHERE(table_schema = 'public');"""

            db_cursor.execute(sql_list_table)
            list_tables = db_cursor.fetchall()

            print(f"list_tables length={len(list_tables)}")
            print("table name are :")
            for t_name_table in list_tables:
                print(t_name_table)

            db_cursor.close()

            print("database connection was successful")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def create_my_custom_table(self):
        conn = None
        try:
            print("Inside create_my_custom_table method")
            conn = psycopg2.connect(database=self.db_name, user=self.db_user, password=self.db_password,
                                    host=self.db_host, port=self.db_port)
            print(conn)
            db_cursor = conn.cursor()

            sql_create_table = """
            CREATE TABLE IF NOT EXISTS app_custom_data (
                id serial NOT NULL PRIMARY KEY,
                inserted_at TIMESTAMP NOT NULL DEFAULT NOW(),
                data json NOT NULL DEFAULT '{}'::jsonb
            );"""

            db_cursor.execute(sql_create_table)
            db_cursor.close()
            conn.commit()
            print("Create table completed successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def insert_custom_data(self, data):
        conn = None
        id = None
        try:
            print("Inside insert_custom_data method")
            data_json = json.dumps(data)
            conn = psycopg2.connect(database=self.db_name, user=self.db_user, password=self.db_password,
                                    host=self.db_host, port=self.db_port)
            cur = conn.cursor()
            sql = """INSERT INTO app_custom_data(data)
                VALUES(%s) RETURNING id;"""
            cur.execute(sql, (data_json,))

            id = cur.fetchone()[0]
            conn.commit()
            cur.close()
            print(f"Added {data} in db successfully. Primary key id is {id}")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return id

    def list_custom_data(self):
        conn = None
        custom_data_list = []
        try:
            print("Inside list_custom_data method")
            conn = psycopg2.connect(database=self.db_name, user=self.db_user, password=self.db_password,
                                    host=self.db_host, port=self.db_port)
            print(conn)
            db_cursor = conn.cursor()

            sql_list_records = "SELECT id,inserted_at,data FROM app_custom_data;"

            db_cursor.execute(sql_list_records)
            list_records = db_cursor.fetchall()

            print(f"list_records length={len(list_records)}")
            print(f"printing records from table:")

            for record in list_records:                
                custom_data = {
                    'id': record[0],
                    'inserted_at': record[1],
                    'data': record[2]
                }
                custom_data_list.append(custom_data)
            print(custom_data_list)

            db_cursor.close()

            print("list_custom_data method completed successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return custom_data_list
