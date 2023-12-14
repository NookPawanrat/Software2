#Assignment 13
#Setting up a backend service with an interface

#1
from flask import Flask, jsonify
app = Flask(__name__)

def prime_number(number):
    if number <=1 :
       return False
    if number % 2 != 0:
        return False
    return True

@app.route('/prime_number/<int:number>',methods = ['GET'])
def check_number(number):
    isprime = prime_number(number)
    response = {
        "Number" : number,
        "isPrime" : isprime
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)



#2
from flask import Flask, jsonify
import mysql.connector

def get_code(code):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='Nook',
        password='nook1996',
        autocommit=True
    )

    cursor = connection.cursor()
    sql = f"SELECT ICAO, name ,location FROM airport WHERE ident='{code}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.close()
    return result


app = Flask(__name__)

@app.route('/airport/<icao>', methods=['GET'])
def airport_info(icao):
    airport_data = get_code(icao)
    if airport_data:
        airport_info = {
            "ICAO": airport_data[0][0],
            "Name": airport_data[0][1],
            "Location": airport_data[0][2]
        }
        return jsonify(airport_info)
    else:
        return jsonify({"error": f"No airport found for ICAO code {icao}"}), 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

