from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# How it works page
@app.route('/how-it-works')
def how_it_works():
    return render_template('how_it_works.html')

# Encode page
@app.route('/encode')
def encode():
    return render_template('encode.html')

# Decode page
@app.route('/decode')
def decode():
    return render_template('decode.html')

if __name__ == '__main__':
    app.run(debug=True)
