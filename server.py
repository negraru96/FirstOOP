from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def create():
    print(request.form)
    print('Name', request.form['Name'])
    print('Email', request.form['Email'])
    print('City', request.form['City'])
    print('Activity', request.form['Activity'])
    print('Other', request.form['Other'])
    return render_template("created.html")

@app.route('/danger')
def danger():
    return redirect('/')
    alert("A user tried to visit /danger. We have redirected the user to /");

if __name__=="__main__":
    app.run(debug=True)
