from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def create():
    print(request.form)
    print('OQuantity', request.form['OQuantity'])
    print('MQuantity', request.form['MQuantity'])
    print('SQuantity', request.form['SQuantity'])
    print('IQuantity', request.form['IQuantity'])
    print('FName', request.form['FName'])
    print('LName', request.form['LName'])
    print('Email', request.form['Email'])
    print('Address', request.form['Address'])
    print('City', request.form['City'])
    print('State', request.form['State'])
    print('Zip', request.form['Zip'])
    return render_template("created.html")

if __name__=="__main__":
    app.run(debug=True)
