#!/usr/bin/python3

# import our flask class
from flask import Flask

app = Flask(__name__)

# return a simple string
@app.route("/", methods=['GET'])
def citihom():
    return "Hello Citi Group Students!"

# perform some math
@app.route("/math", methods=['GET'])
def math():
    x = 5
    y = 2
    answer = x + y
    return str(answer)

if __name__ == '__main__':
    #run our flash application on all IPs:2224
    app.run(host='0.0.0', port=2224)
