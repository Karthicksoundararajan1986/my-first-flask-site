from flask import Flask, render_template # Must include render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') # This links to your HTML file
