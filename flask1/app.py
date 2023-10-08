#app.py
# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#List of tasks
tasks = []

@app.route('/')
def index ():
    return render_template('./index.html',tasks =tasks)

@app.route('/add_task', methods = ['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)