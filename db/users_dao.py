import pandas as pd
from db.connection import get_connection

def load_users():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM users", conn)
    conn.close()
    return df
