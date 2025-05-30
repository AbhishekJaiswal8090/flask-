#building url dynamically
#variable rule
#jinja 2 template engine

'''
{{}} expressions to print o/p in html page
{%..%} conditions or loops
{#..#} this is for comments

'''
from flask import Flask, render_template, request

app =Flask(__name__)

##different request methods uses in flask

@app.route("/")
def welcome_page():
    return "<b>WELCOME </b>"

##GET METHODS
@app.route("/index")
def index():
    return render_template('index.html',method=['GET'])

@app.route("/about")
def about():
    return render_template("about.html")

#POST METHOD
@app.route('/form', methods=['GET', 'POST'])
def get_req():
    if request.method == 'POST':
        name = request.form.get('name', '')
        return f"Hello {name}"
    return render_template('form.html')
#variable rule
#@app.route('/success/<score>') 
#def success(score):
    #return 'The marks you got is '+str(score)

@app.route('/success/<int:score>') 
def success(score):
    res=''
    if score >=50:
        res='PASS'
    else:
        res='FAIL'    
    return render_template('result.html',results=res)


@app.route('/successres/<int:score>') 
def successres(score):
    res = 'PASS' if score >= 50 else 'FAIL'
    exp = {'score': score, 'res': res}
    return render_template('result1.html', result=exp)

@app.route('/successif/<int:score>') 
def successif(score):
    res=''
   
    return render_template('result2.html',results=score)

if __name__=="__main__":
    app.run(debug=True)