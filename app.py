from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Backend!"

@app.route('/db')
def db_conn():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="dummydb"
        )
        return "DB Connection Success!"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
