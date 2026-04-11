### building url dynamically
### variable rule
### Jinja - 2 template Engine

### Jinja2 Template Engine : 
'''

{{ }}   -> expression to print output in html
{%...%}  -> conditions,for loops
{#...#}  -> this is for comments

'''

from flask import Flask,render_template,request,redirect,url_for
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

# @app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'HELLO {name}!'
#     return render_template('submit.html')

## variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score > 50:
        res = "PASSED"
    else:
        res ="FAILED"
        
    return render_template('result.html',result=res)

## for loop
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score >= 50:
        res = "PASSED"
    else:
        res ="FAILED"
        
    exp = {'Score' : score,"res" : res}
    
    return render_template('result1.html',result=exp)

### if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result2.html',result=score)

@app.route('/success/<int:score>')
def fail(score):
        
    return render_template('result.html',result=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form.get('c'))
        data_science=float(request.form['datascience'])
        
        total_score = (science + maths + c + data_science)/4
        return redirect(url_for('successres',score=total_score))
    else:    
        return render_template('getresult.html')
if __name__ == "__main__": 
    app.run(debug = True)

