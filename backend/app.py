from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Backend!"

@app.route('/db')
def db_check():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="dummydb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Database Connected!'")
        result = cursor.fetchone()
        return str(result[0])
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
