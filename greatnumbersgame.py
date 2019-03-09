from flask import Flask, render_template, session, request, redirect, flash
import random

app = Flask(__name__)
app.secret_key = "greatnumgame"

# def setSession():
#     session['num'] = random.randint(1,100)

# @app.route("/")
# def index():
#     if session['num'] == None:
#         setSession()
#     else:
#         pass
#     print (session["num"])
#     return render_template("index.html")
#
# @app.route("/guess", methods=["POST"])
# def checkNumber():
#     error = None
#     success - None
#     guess = request.form['guess']
#     if request.method == "POST":
#         if guess.isdigit():
#             numguess = int(guess)
#             if numguess == session['num']:
#                 flash("Correct", "success")
#                 return redirect("/")
#             elif numguess > session['num']
#                 flash("Too high", "error")
#             else:
#                 flash("Too low", "error")
#         else:
#             flash("Not a valid guess", "error")
#     elif isinstance(guess, str):
#         flash("Not a valid guess", "error")
#
#         return redirect("/")
#
# @app.route("/reset", methods=["GET", "POST"])
# def reset():
#     setSession()
#     return redirect("/")

@app.route('/')
def index():
    if 'message' not in session:
        session["message"]=""
    if 'number' not in session:
        session['number']=random.randrange(1,101)
    return render_template("index.html", message=session['message'] )

@app.route('/guess', methods=['POST'])
def guess():

    guess=int(request.form['number'])
    if guess== session['number']:
        session['message']= "you win!"
    if guess > session['number']:
        session['message']= 'Too high guess lower'
    elif guess< session['number']:
        session['message']= 'Too low guess higher'
    return redirect('/')
    
@app.route('/reset')
def reset():
    session['number']
    session.pop("number")
    session.pop("message")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
