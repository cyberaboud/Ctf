from flask import Flask, render_template, request, send_file
from subprocess import PIPE, Popen


app = Flask(__name__)


def exec(q):
    p = Popen(q, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    if stdout:
        return "ok"
    return stderr.decode()

@app.get("/")
def index():
    return render_template('index.html', output="")

@app.post("/")
def query():
    q = request.form['q']
    q = q[:16]
    result = exec(q)
    return render_template('index.html', output=result)

@app.get("/code")
def code():
    return send_file(__file__)