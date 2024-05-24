from flask import Flask, render_template, Response
from gets import get_saying
import os

app = Flask(__name__)

@app.route("/")
def serve():
    s = get_saying("./text")
    return render_template('landing.html', name="The Generator", saying=s)

@app.route("/resources")
def serve_resources():
    return render_template('resources.html', name="The Generator", title="Resources", description="Resources about AI in society, Markov chains, and similar toolsets.")

@app.route("/css/<content>")
def serve_css(content):
    f = open(os.getcwd() + "/css/" + content)
    read_content = f.read()
    f.close()
    return Response(read_content, mimetype='text/css')

@app.route("/js/<content>")
def serve_js(content):
    f = open(os.getcwd() + "/js/" + content)
    read_content = f.read()
    f.close()
    return Response(read_content, mimetype='text/js')

@app.route("/images/<content>")
def serve_image(content):
    f = open(os.getcwd() + "/images/" + content, 'rb')
    read_content = f.read()
    f.close()
    return Response(read_content, mimetype='img/png')
