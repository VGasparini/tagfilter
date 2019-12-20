import os
from flask import Flask, render_template, request, redirect

# Flask main file. It generate html page and read input data


class App():
    def __init__(self, tweets, tags):
        self.app = Flask(__name__)
        self.tags = tags

        @self.app.route("/", methods=['GET', 'POST'])
        def index():

            if request.method == 'POST':

                tags.add(request.form['tag_input'])

                return redirect(request.url)

            return render_template("index.html", tweets=tweets, tags=tags)

    def run(self):
        self.app.run(debug=True)
