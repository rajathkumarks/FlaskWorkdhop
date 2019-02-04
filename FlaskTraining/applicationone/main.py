# from the flask library import a class named Flask
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

# listen for a route to `/` - this is known as the root route
@app.route('/')
def home():
	return "Hello World!"

@app.route('/welcome')
def welcome():
	return "Welcome to Intell Eyes A Company by Countinfinite Technologies Pvt Ltd"

if __name__ == '__main__':
	app.run()