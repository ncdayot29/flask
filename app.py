from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    feedback = request.form['feedback']
    # For now, we'll just pass data to the thank-you page
    return render_template('thankyou.html', name=name, feedback=feedback)

if __name__ == '__main__':
    app.run()
