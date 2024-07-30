from flask import Flask
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/')
def index():
    try: 
     conn = get_db_connection()
     cur = conn.cursor()
     cur.execute('SELECT version();')
     db_version = cur.fetchone()
     cur.close()
     conn.close()
     print("Chao mung den voi webserver!")
     print("Ket noi database thanh cong!")
     return f'Database version: {db_version}'
    except:
     return "Chao mung den voi webserver!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
