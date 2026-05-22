'''
Explore the 'Flask' module and create a web server using Flask and Python..
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World this is me Nahid!</p>"

app.run()