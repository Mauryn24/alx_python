#!/usr/bin/python3

"""
    Copy the previous task to a new script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text
        variable (replace underscore _ symbols with a space )
        /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
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

"""Define a route for the "/c/<text>" URL and set strict_slashes to False"""
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """replace underscores (_) with spaces in the text variable"""
    text = text.replace("_", " ")
    """Return "C " followed by the value of the text variable"""
    return 'C {}'.format(text)

"""Define a route for the "/python/<text>" URL and set strict_slashes to False"""
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text='is cool'):
    """replace underscores (_) with spaces in the text variable"""
    text = text.replace("_", " ")
    """Return "Python " followed by the value of the text variable"""
    return 'Python {}'.format(text)

if __name__ == '__main__':
    """Start the application and make it listen on IP address 0.0.0.0 and port 5000"""
    app.run(host='0.0.0.0', port=5000)