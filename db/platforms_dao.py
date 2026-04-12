import pandas as pd
from db.connection import get_connection

def load_platforms():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM platforms", conn)
    conn.close()
    return df
