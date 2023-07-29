import os
from flask import Flask
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_DATABASE')
    )
    cursor = connection.cursor()
    cursor.execute('SELECT NOW()')
    result = cursor.fetchone()
    connection.close()
    return f"Success Connection! Current time: {result[0]}"

if __name__ == '__main__':
    app.run(debug=True, host=os.getenv('FLASK_HOST', '0.0.0.0'), port=int(os.getenv('FLASK_PORT', 5000)))
