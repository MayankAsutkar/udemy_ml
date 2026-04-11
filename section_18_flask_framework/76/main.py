### integrating html files in the webframework

from flask import Flask,render_template
## render_template is responsible for redirecting to the html page

### wsgi application
app = Flask(__name__) 

## a decorator for my route of the homepage:
@app.route("/")
def welcome():
    return "<html><H1>welcome to the flask frame work</H1></html>"

@app.route("/index")
def index():
    return render_template('index.html') # to run these we need to create a templates folder in same directory and include the html page in the folder

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__": ## this is an entry point for my py file and my program wi;; execute form this function
    app.run(debug = True)

