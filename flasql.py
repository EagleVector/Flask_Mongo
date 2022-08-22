from flask import Flask ,request,jsonify
import  mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host = "localhost" , user = 'root' , passwd = "Eagle_Vector1996@")
cursor = mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.tasktable (name varchar(30) , number int)")

@app.route('/insert',methods = ['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into taskdb.tasktable  values(%s,%s)",(name ,number))
        mydb.commit()
        return jsonify(str('succesfully inserted'))

@app.route('/update', methods = ['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        cursor.execute("UPDATE taskdb.tasktable SET number = number + 500 WHERE name = %s",(get_name,))
        mydb.commit()
        return jsonify(str("Updated Successfully"))

@app.route('/delete', methods = ['POST'])
def delete():
    if request.method == 'POST':
        del_number = request.json['del_number']
        cursor.execute("DELETE FROM taskdb.tasktable WHERE number = %s",(del_number,))
        mydb.commit()
        return jsonify(str("Deleted Successfully"))

@app.route("/fetch",methods = ['POST','GET'])
def fetch_data():
    cursor.execute("select * from taskdb.tasktable")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))

if __name__ == '__main__':
    app.run()
