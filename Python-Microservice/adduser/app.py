from flask import Flask, request, render_template, redirect
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

@app.route('/postuser', methods=["POST"])
def post_user():
    response = request.get_json()
    firstname = response.get('firstname')
    lastname = response.get('lastname')
    email = response.get('email')

    cur = conn.cursor()
    sql = "INSERT INTO memo(firstname, lastname, email) VALUES (%s, %s, %s)"
    data = (firstname, lastname, email)
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    return redirect('http://10.60.7.36:5001/getuser')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)
