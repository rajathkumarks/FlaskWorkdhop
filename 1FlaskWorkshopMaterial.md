# 1. Flask Framework with Python

[TOC]

## 1.1 Setting up the Environment

### 1.1.1 Objectives

<span style="color:black">It's good practice to have a different python environment for different development setup. Here we're learning about how to setup an virtual environment for Flask Framework for our web application development. </span> 

<span style="color:black">By the end of this section, you should be able to:</span>

- Install <span style="color:red">`virtualenv`</span> , <span style="color:red">`virtualwrapper`</span> and create virtual environments
- Use Flask to setup a simple server and respond with text

### 1.1.2 Getting set up in a virtual environment

<span style="color:black">As you start working on more Python projects, you may find that managing dependencies becomes problematic. For example, you may start a project that uses version 3.5.x of some library, and later on you may start a new project and realize that version 3.7.x of the module is updated. But this new version breaks things in your old project, so you need to either deal with a broken old project, or a new project with an old version of the library.</span>

<span style="color:black">It would be better if we could separate out distinct environments for each Python project we worked on. That way, we wouldn't have to worry about dependencies in one project potentially interfering with other projects.</span>

<span style="color:black">Thankfully, there's a way to set this up without much trouble in Python. The tool we'll be using is called  <span style="color:red">`virtualenv`</span> and<span style="color:red">`virtualwrapper`</span> . Before we get started with any significant Python development, let's set up <span style="color:red">`virtualenv`</span> and<span style="color:red">`virtualwrapper`</span>so we can create separate environments for each project we'll be working on.</span>

#### 1.1.2.1 Installing <span style="color:red">`virtualenv`</span> and <span style="color:red">`virtualwrapper`</span>

```bash
pip3 install virtualenv
```

![](.\images\virtualenv.PNG)

```bash
pip3 install virtualenvwrapper-win
```

![](.\images\virtualwrapper.PNG)

#### 1.1.2.2 Creating Virtual Environment

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

## 1.2 Introduction to Flask Framework

> **<span style="color:black">Pirates use Flask, the Navy uses Django</span>**

### 1.2.1 What is Flask ?

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

### 1.2.2 Flask Exercises

<span style="color:black">For thsi assignemtn you will be creating a very small flask appkication,. Your application should:</span>

- have a route for `/welcome` , which responds with the string "Welcome to Flask from Intell Eyes".
- have a route for `/welcome/home`, which responds with the string "Welcome Home"

**Bonus Exercise**

- have a route for `/welcome/<yourname>`, which responds with string "Welcome `<yourname>`"

# 2. Templating with Jinja2

## 2.1 What is a Template ?

<span style="color:black">Very commonly, we want to send data from our server back to our client. In the olden days, servers often just held a collection of files; the client would request, say, an HTML file, and the server would send it over. Because these files were static and unchanged by the server, such sites are often referred to as *static sites*.</span> 

<span style="color:black">In more modern web development, instead of sending static data all the time, we often want to send *dynamic* data, which may depend on which user is signed in, whether a user's account has expired, and so on. To do this we will be using the templating engine built into Flask, which is called **Jinja2**.</span>

### 2.1.1 Objectives:

<span style="color:black">By the end of this section, you should be able to:</span>

- Use Flask to respond by rendering HTML instead plain text
- Use Jinja2 as a server side templating engine
- Pass values to a server side template with Flask and evaluate them with Jinja

### 2.1.2 Jinja2

<span style="color:black">Since Jinja2 comes with Flask we do not need to <span style="color:red">`pip install`</span> anything and we can get started right away. To evaluate data from our server in our templates we use the <span style="color:red">`{% %}`</span> notation and to print data we use <span style="color:red">`{{ }}`.</span>(Not clear on the difference between evaluating and printing data in a template ? Don't worry, we'll see an example soon)</span>

<span style="color:black">Let's start by first having Flask render HTML. To do so we must include <span style="color:red">`render_template`</span> when importing from flask. Let's make an <span style="color:red">`flask`</span>. Let's make an <span style="color:red">`main.py`</span> and include the following:</span>

```python
# from the flask library import a class named Flask
from flask import Flask, render_template # we are now importing just more than Flask!

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/second')
def second():
    return "WELCOME TO THE SECOND PAGE!"

if __name__ == '__main__':
	app.run()
```

<span style="color:black">So what's happening above ? Instead of just rendering plain text, we are rendering a template called  <span style="color:red">`index.html`</span>. Now in order to make sure that Flask can find our templates, we need to create a folder called <span style="color:red">`templates`</span> and inside let's create our <span style="color:red">`index.html`</span> file.</span>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Intell Eyes</title>
</head>
<body>
   <h1>Hello World</h1>
   <h2>Flask Framework</h2>
</body>
</html>
```

<span style="color:black">Make sure you've made a correct directory structure, as shown below </span>

![](.\images\flasktemplatestructure.PNG)

```directory Structure
root 
  |- main.py
  |- templates
  |	 	|- index.html
  |	 	|
```

<span style="color:black">When you run the above application it's just rendering the static Webpage as we created in a template directory as index.html, But as jinja says it has to work with the dynamic content . so here is the second example to understand the power of Jinja2</span>

**Python Main.py**

```python
# from the flask library import a class named Flask
from flask import Flask, render_template # we are now importing just more than Flask!

app = Flask(__name__)

@app.route('/')
def welcome():
    names_of_instructors = ["Rajath", "Amarnath", "Sudarshan"]
    random_name = "Rajath"
    return render_template('index.html', names=names_of_instructors, name=random_name)

@app.route('/second')
def second():
    return "WELCOME TO THE SECOND PAGE!"

if __name__ == '__main__':
	app.run()
```

**index.html** in templates directory which has some logic here,

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Intell Eyes</title>
</head>
<body>
    {% for instructor_name in names %}
        <p>{{ instructor_name }}</p>
    {% endfor %}

    {% if name == 'Rajath' %}
        <p>Hello {{ name }}!</p>
    {% endif %}
</body>
</html>
```

<span style="color:black">Well when we see <span style="color:red">`main.py`,`index.html`</span> now it looks different than the other one let's see what we've done here, we're passing some variables into the template. These variables are called <span style="color:red">`names`</span>and <span style="color:red">`name`</span> and their values are the <span style="color:red">`names_of_instructors `</span> variable (<span style="color:red">`["Rajath", "Amarnath", "Sudarshan"]`</span>) and <span style="color:red">`random_name `</span>variable <span style="color:red">`("Rajath") `</span>.Very commonly these keys and values will be named as the same, but we are using different names to show the difference in the example.</span>

<span style="color:black">We can iterate over lists using<span style="color:red"> `for` </span>with Jinja and use conditional logic with <span style="color:red">`if` </span>statements! This means we can render the same HTML page and produce different views for different users. Our pages are now much more dynamic! Think about some applications for something like this: templating allows you to listing all of your friends on a social network, displaying information only if you are an admin, show a logout button if you are logged in, and more, all with just a small number of templates living on the server.</span>

<span style="color:black">Note also that that only Python code inside of <span style="color:red">`{{ }}` </span>gets printed to the page. You'll often see <span style="color:red">`for` </span>loops and <span style="color:red">`if` </span>statements defined inside of <span style="color:red">`{% %}`</span>, since we want to evaluate that code, but it's only when we're inside the <span style="color:red">`if`</span> or <span style="color:red">`for `</span>blocks that we want to display something on the page (using <span style="color:red">`{{ }}`</span>).</span>

## 2.2 Template Inheritance

<span style="color:black">One of the more powerful features of Jinja is the ability to use template inheritance, which means that one template can inherit from another. Let's see an example! First, let's create a file called <span style="color:red">`base.html`</span></span>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Intell Eyes</title>
</head>
<body>
   {% block content %}
   {% endblock %}
</body>
</html>
```

<span style="color:black">In another template (in the same directory), create a file called <span style="color:red">`title.html`</span></span>

```html
{% extends "base.html" %}
{% block content %}
<h1>This page has everything our base.html has!</h1>
{% endblock %}
```

<span style="color:black">We can inherit from other templates using <span style="color:red">`extends`</span> keyword. This tremendously reduces our code duplication especially for things like headers and footers. To see this inheritance in action, add another route to your <span style="color:red">`main.py`</span></span>

```python
# from the flask library import a class named Flask
from flask import Flask, render_template # we are now importing just more than Flask!

app = Flask(__name__)

@app.route('/')
def welcome():
    names_of_instructors = ["Rajath", "Amarnath", "Sudarshan"]
    random_name = "Rajath"
    return render_template('index.html', names=names_of_instructors, name=random_name)

@app.route('/second')
def second():
    return "WELCOME TO THE SECOND PAGE!"

@app.route('/title')
def title():
    return render_template('title.html')

if __name__ == '__main__':
	app.run()
```

## 2.3 URL Helpers

<span style="color:black">Another great helper that Jinja has is the <span style="color:red">`url_for`</span> helper which eliminates the need for hard coding a URL. This is very helpful when you have dynamically created URLs or don't always know the exact path. Let's imagine we are working in our <span style="color:red">`index.html`</span> file and we would like an anchor tag to link to the route<span style="color:red"> `/second`</span>. We also know that in our <span style="color:red">`app.py` </span>the function that is used to send a response to our server is called <span style="color:red">`second`</span>. This is what we can place as the value for our <span style="color:red">`url_for()`</span>!</span>

```html
{% extends "base.html" %}
{% block content %}
    {% for name in names %}
        {{name}}
    {% endfor %}

    {% if name == 'Rajath' %}
        <p>Hello Rajath!</p>
    {% endif %}

    Tired of this page? Head over to <a href="{{url_for('second')}}">the second page!</a>
{% endblock %}
```

## 2.4 Getting data from the query string

<span style="color:black">When a user submits a form via a GET request, that form data can be captured from the query string. Flask makes this process a bit easier with a method called <span style="color:red">`request`</span>. Let's see it in action. To begin, start with a simple form in a page called <span style="color:red">`first-form.html`</span>:</span>

```html
{% extends "base.html" %}
{% block content %}
    <form action="/data">
        <input type="text" name="first">
        <input type="text" name="last">
        <input type="submit" value="Submit Form">
    </form>
{% endblock %}
```

<span style="color:black">To capture this data we can use <span style="color:red">`request`</span> which we need to import from <span style="color:red">`flask`</span> and access the <span style="color:red">`args` </span>property inside request.</span>

```python
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
```

#### 2.4.1 Flask Exercises

**Flask Templating**

<span style="color:black">Create a new Flask application with the following:</span>

**Part 1**

- A `base.html` template for others to inherit from
- A route for `/person/<name>/<age>` which renders a template that displays the name and age entered for the URL. That template should inherit from `base.html`

**Part 2**

Refactor your calculator application from before!

- have a route for `/calculate` which renders a template called `calc.html`
- in `calc.html`, build a form which has two inputs (one with a name of `num1` and another with the name of `num2`for numbers and a select field with the name of `calculation` with options for "add", "subract", "multiply" and "divide".
- When the form is submitted it should make a request to a route called `/math`
- In your python file, accept the values from the form and depending on what the request contains, respond with the sum, difference, product or quotient.

# 3. CRUD with Flask

<span style="color:black">**C**reate, **R**ead, **U**pdate and **D**elete</span>

## 3.1 Key Definitions

<span style="color:black">Now that we have a solid understanding of the basics of Flasks, it's time to build some more powerful web applications. Before we do so, let's quickly review some key concepts relating to the internet.</span>

<span style="color:black">**HTTP** - **H**yper **T**ext **T**ransfer **P**rotocol, The protocol that clients and servers use to communicate.</span>

<span style="color:black">**Idempotent** - An operation is idempotent if calling it multiple times yields the same result. </span>

<span style="color:black">**CRUD** - Shorthand for **C**reate, **R**ead, **U**pdate, and **D**elete. We often talk about implementing CRUD on a resource when building web applications.</span>

<span style="color:black">**Resource** - A `noun` that we operate on. An application can have many resources, but each resource will have its own set of routes and CRUD operations. For example, `users` and `tweets` are two examples of resources for Twitter.</span>

### 3.1.2 Objectives

<span style="color:black">By the end of this chapter, you should be able to:</span>

- Explain what REST is and describe RESTful routing
- Include flask modus for overriding the default HTTP method
- Build a CRUD app in Flask
- Include a stylesheet in a Flask application

