import psycopg2 as ps
import pandas as pd

def select(in_put):

    conn = ps.connect(
                        host="10.64.10.85",
                        database="IZ_DB",
                        user="maciek",
                        port="5432",
                        password="Test1234!!!!")

    sql = in_put
    dat = pd.read_sql_query(sql, conn)
    conn = None
    return dat