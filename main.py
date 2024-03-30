from flask import Flask, render_template, request
from dbmanager import DBManager
from log import Log

app = Flask(__name__)
dbm = DBManager()

# Prototype: render form, final: render index
@app.route('/', methods=['POST'])
def form():
    return render_template('form.html')


@app.route('/submitted', methods=['GET', 'POST'])
def process_form():
    new_log = Log(
        time=request.form['log-time'],
        location=request.form['location'],
        activity=request.form['activity'],
        observed=request.form['observed'],
        caught=request.form['caught']
    )

    dbm.add(new_log.get_log())

    return render_template(
        'form-output.html'
    )

if __name__ == "__main__":
    app.run(debug=True)