from flask import Flask

'''
Flask() :

It creates an instance of the Flask class, which will be your WSGI (Web Server Gateway Interface) application.
'''

### wsgi application
app = Flask(__name__) 

## a decorator for my route of the homepage:
@app.route("/")
def welcome():
    return "welcome to these flask course.This should be an amazing course."

@app.route("/index")
def index():
    return "welcome to the index page"


if __name__ == "__main__": ## this is an entry point for my py file and my program wi;; execute form this function
    app.run(debug = True)
    ## debug = True which allows you to make live changes in the website
    
## this is how we design a skeleton for a website using flask framework

