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
   

if __name__=="__main__":
    app.run(debug=True)