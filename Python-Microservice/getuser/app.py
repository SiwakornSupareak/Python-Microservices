from flask import Flask, request, render_template, redirect, jsonify
import os
#pip install mysql-connector-python
import mysql.connector as mysql

app = Flask(__name__)

# Configure MySQL connection
conn = mysql.connect(
    host="localhost",
    user="root",
    password="Buffon.bf@27",
    port=3306,
    database="my_memo"
)

app = Flask(__name__)

@app.route('/getuser/v1/<idmemo>', methods=["GET"])
def get_user_by_id(idmemo):
    cur = conn.reconnect()
    cur = conn.cursor()

    sql = "SELECT idmemo, firstname, lastname, email "
    sql += "FROM memo WHERE idmemo=%s ORDER BY firstname"
    data = (idmemo,)
    cur.execute(sql, data)
    records = cur.fetchall()
    cur.close()
    return jsonify(records)

@app.route('/getuser', methods=["GET"])
def get_all_users():
    cur = conn.reconnect()
    cur = conn.cursor()

    sql = "SELECT idmemo, firstname, lastname, email FROM memo ORDER BY firstname"
    cur.execute(sql)
    records = cur.fetchall()
    cur.close()
    return jsonify(records)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)