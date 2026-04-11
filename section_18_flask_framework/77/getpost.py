### working with http verbs get and post

from flask import Flask,render_template,request
## render_template is responsible for redirecting to the html page

### wsgi application
app = Flask(__name__) 

## a decorator for my route of the homepage:
@app.route("/")
def welcome():
    return "<html><H1>welcome to the flask frame work</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html') 
## by defualt the request is of type get.

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'HELLO {name}!'
    return render_template('form.html')

if __name__ == "__main__": 
    app.run(debug = True)

