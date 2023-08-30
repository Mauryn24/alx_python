#!/usr/bin/python3

"""
    Copy the previous task to a new script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition
"""


from flask import Flask


"""create a web application instance"""
app = Flask(__name__)

"""Define a route for the root URL ("/") and set strict_slashes to False"""
@app.route('/', strict_slashes=False)
def hello():
    """Return the 'Hello HBNB!' message as the response"""
    return 'Hello HBNB!'

"""Define a route for the '/hbnb' URL and set strict_slashes to False"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return the "HBNB" message as the response"""
    return 'HBNB'

if __name__ == '__main__':
    """Start the application and make it listen on IP address 0.0.0.0 and port 5000"""
    app.run(host='0.0.0.0', port=5000)