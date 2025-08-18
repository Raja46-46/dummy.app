from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def hello():
    return "Backend Connected ✅"

@app.route("/db")
def db_connect():
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="dummydb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM test;")
    result = cursor.fetchone()
    return f"DB Message: {result[0]}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
