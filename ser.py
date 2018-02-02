from flask import  request, Flask, render_template

myapp = Flask(__name__, template_folder='templates')

@myapp.route("/")
def celtofaren():
    return render_template('try.html')

@myapp.route("/ctof")
def celtof():
    str1  = request.args.get('string1')
    str2  = request.args.get('string2')
    if str1==str2:
        return "strings are same"
    else:
        return "strings are not same"
