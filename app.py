from flask import Flask, render_template  # 1. ADDED RENDER_TEMPLATE HERE

app = Flask(__name__)

@app.route('/')
def home():
    # 2. THIS TELLS FLASK TO LOOK FOR index.html IN THE templates FOLDER
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
