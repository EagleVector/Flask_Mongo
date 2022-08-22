#Fetching data from mysql or any database


from flask import Flask, request, jsonify
import mysql.connector as conn
app = Flask(__name__)

@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get("mail")
    return "This is my first api for {} {} {}".format(get_name, mobile_number, mail_id)

@app.route("/get_data")
def get_data_from_sql():
    db = request.args.get('db')
    tn = request.args.get('tn')
    try:
        connection = conn.connect(host='localhost', user = 'root', passwd = 'Eagle_Vector1996@', database =db)
        cur = connection.cursor(dictionary=True)
        cur.execute(f'SELECT * FROM {tn}')
        data = cur.fetchall()
        connection.commit()
        connection.close()

    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)


if __name__ == '__main__':
    app.run(port = 5002)