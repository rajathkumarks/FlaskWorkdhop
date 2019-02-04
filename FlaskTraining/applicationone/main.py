# from the flask library import a class named Flask
from flask import Flask, render_template,request # we are now importing just more than Flask!

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/second')
def second():
    return "WELCOME TO THE SECOND PAGE!"

@app.route('/title')
def title():
    return render_template('title.html')

@app.route('/show-form')
def show_form():
    return render_template('first-form.html')

@app.route('/data')
def print_name():
	first = request.args.get('first')
	last = request.args.get('second')
	return first

if __name__ == '__main__':
	app.run()