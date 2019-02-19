from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')

def hello_world():
    return render_template("index.html", first_name="Michael", last_name="Negraru", list=[1,3,5])

if __name__=="__main__":

    app.run(debug=True)
