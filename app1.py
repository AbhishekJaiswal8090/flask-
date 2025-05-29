from flask import Flask, render_template, template_rendered

app=Flask(__name__)

@app.route("/")
def welcome_page():
    return "<b>WELCOME </b>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)