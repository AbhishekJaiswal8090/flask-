from flask import Flask
'''
It creates an instance of the flask
which will be your wsgi (web server gateway interface) application


'''
#BASIC SETUP

#WSGI APPlication
app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this flash course Hello brother This should be amazing course"

@app.route("/web")
def web():
    return "Welcome to th web page"

@app.route("/html")
def return_html():
    return "<HTML><H1>ABHISHEK JAISWAL</H1></HTML>"
if __name__=="__main__":
    app.run(debug=True)