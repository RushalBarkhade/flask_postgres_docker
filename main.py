from flask import Flask,request,jsonify
import json
from init_db import get_db_connection

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"

@app.route('/create',methods=["POST"])
def add_user():
    try:
        conn = get_db_connection()
        json_data=json.loads(request.data)
        name = json_data['name']
        address = json_data['address']
        salary = json_data['salary']
        age = json_data['age']
        SQL = "INSERT INTO company(name, address, salary,age) " \
                "VALUES(%s, %s, %s,%s)"
        data = (name,address,salary,age)
        cursor = conn.cursor()
        cursor.execute(SQL,data)
        conn.commit()
        resp = jsonify("User added successfully!")
        resp.status_code = 200
        return resp
    except Exception as exception:
        print(exception)
        return jsonify(str(exception))
    finally:
        conn.close()
        pass

@app.route("/get_users",methods=["GET"])
def get_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM company;")
        books = cursor.fetchall()
        resp = jsonify(json.dumps(books))
        resp.status_code = 200
        return resp
        
    except Exception as exception:
        print(exception)
        return jsonify(str(exception))
    finally:
        conn.close()
        pass

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)