# Flask Framework with Python

[TOC]

## Setting up the Environment

### Objectives:

<span style="color:black">It's good practice to have a different python environment for different development setup. Here we're learning about how to setup an virtual environment for Flask Framework for our web application development. </span> 

<span style="color:black">By the end of this section, you should be able to:</span>

- Install <span style="color:red">`virtualenv`</span> , <span style="color:red">`virtualwrapper`</span> and create virtual environments
- Use Flask to setup a simple server and respond with text

### Getting set up in a virtual environment

<span style="color:black">As you start working on more Python projects, you may find that managing dependencies becomes problematic. For example, you may start a project that uses version 3.5.x of some library, and later on you may start a new project and realize that version 3.7.x of the module is updated. But this new version breaks things in your old project, so you need to either deal with a broken old project, or a new project with an old version of the library.</span>

<span style="color:black">It would be better if we could separate out distinct environments for each Python project we worked on. That way, we wouldn't have to worry about dependencies in one project potentially interfering with other projects.</span>

<span style="color:black">Thankfully, there's a way to set this up without much trouble in Python. The tool we'll be using is called  <span style="color:red">`virtualenv`</span> and<span style="color:red">`virtualwrapper`</span> . Before we get started with any significant Python development, let's set up <span style="color:red">`virtualenv`</span> and<span style="color:red">`virtualwrapper`</span>so we can create separate environments for each project we'll be working on.</span>

#### Installing <span style="color:red">`virtualenv`</span> and <span style="color:red">`virtualwrapper`</span>

```bash
pip3 install virtualenv
```

![](.\images\virtualenv.PNG)

```bash
pip3 install virtualenvwrapper-win
```

![](.\images\virtualwrapper.PNG)

#### Creating Virtual Environment

<span style="color:black">To create virtual environment, you'll use <span style="color:red">`mkvirtualenv`</span> command </span>

```bash
mkvirtualenv flasktraining
```

<span style="color:black">Here in this case i'm using my virtual environment name as **flasktraining**, you can use your own virtual environment name. </span>

![](.\images\mkvirtualenv.PNG)

<span style="color:black">When it's created , it gets into virtual environment. To get out of your virtual environment use **`deactivate`**</span> 

<span style="color:black">To work in virtual environment you need to type in as follows,</span>

```bash
workon flasktraining
```

![](.\images\workondeactivate.PNG)

```bash
deactivate
```

<span style="color:black">to exit the virtual environment to your base machine.</span>

<span style="color:black">To list the virtualenvironments that we've created in our system,</span> you can use the <span style="color:red">`lsvirtualenv -b`</span> command (<span style="color:red">`-b`</span> stands for "brief").

```bash
lsvirtualenv -b
```

![](.\images\lsvirtualenv.PNG)

<span style="color:black">In my case i've installed with four virtual environments viz., </span>

1. djangoapps
2. embedded
3. flaskapps
4. flasktraining -- <span style="color:blue"> Virtual Environment that created now.</span>

<span style="color:black">Let's install flask python package for the virtual environment that we've created . To install flask package i'm using PyPi (Python Package Index)</span>

```bash
pip3 install flask
```

<span style="color:black">make sure that you're working inside the virtual  environment you've created.</span>

![](.\images\flaskinstall.PNG)

<span style="color:black">Let's check our installation happend we made has done properly, to check go to python interactive shell by typing <span style="color:red">`python`</span> in your command prompt. Then type in <span style="color:red">`import flask`</span>, if you don't see any error then you're installed flask on your virtual environment</span>

![](.\images\flaskcheck.PNG)

## Introduction to Flask Framework

> **<span style="color:black">Pirates use Flask, the Navy uses Django</span>**

### What is Flask ?

<span style="color:black">Flask is a micro-framework in Python. It allows us to easily start a server, and, when combined with other modules, build sophisticated applications. Flask is very easy to get started with so let's jump in!</span> 

<span style="color:black">Now let's create an <span style="color:red">main.py</span> file in the desired location. To begin, we'll just use the below code.</span>

```python
# from the flask library import a class named Flask
from flask import Flask

# create an instance of the Flask class
app = Flask(__name__)

# listen for a route to `/` - this is known as the root route
@app.route('/')
def home():
	return "Hello World!"

if __name__ == '__main__':
	app.run()
```

<span style="color:black">Make sure we saved our file. Next, in the terminal let's run <span style="color:red">`python main.py`</span> and head over to <span style="color:red">`localhost:5000`/`127.0.0.1:5000`</span> in the browser. You should see the text "Hello World" appear on the page!</span>.

![](.\images\flaskruntest.PNG)

<span style="color:black">Now let's try to add another route to our application. When a user goes to <span style="color:red">`localhost:5000\welcome`</span> we should return the text "Welcome to Intell Eyes A Company by Countinfinite Technologies Pvt Ltd." . We will need to include another route as well as a function to run when that route is reached.</span>

```python
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
```

<span style="color:black">Check back your link that you created has a new route by hitting <span style="color:red">`127.0.0.1:5000\welcome`</span> on your favourite browser.</span>

![](.\images\intelleyeswelcome.PNG)

### Flask Exercises

<span style="color:black">For thsi assignemtn you will be creating a very small flask appkication,. Your application should:</span>

- have a route for `/welcome` , which responds with the string "Welcome to Flask from Intell Eyes".
- have a route for `/welcome/home`, which responds with the string "Welcome Home"

**Bonus Exercise**

- have a route for `/welcome/<yourname>`, which responds with string "Welcome `<yourname>`"