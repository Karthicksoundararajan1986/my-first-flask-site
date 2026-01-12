@app.route('/')
def home():
    # If this line still says return "My Python website is running", 
    # it will always stay blank. It MUST use render_template.
    return render_template('index.html')
