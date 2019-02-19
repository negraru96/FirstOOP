from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    student_info = (
        {'name' : 'Jim', 'age' : 35},
        {'name' : 'Tim', 'age' : 30},
        {'name' : 'Lim', 'age' : 25},
        {'name' : 'Kim', 'age' : 30},
    );
    return render_template("index.html", random_numbers = [3,1,5,7,4], students = student_info)
if __name__=="__main__"
    app.run(debug=True)
