from flask import Flask, render_template
from helper import *

app = Flask(__name__)

# static pages served here including bare minimum jinja pages
@app.route('/')
def home():
    pass

# ...

# login required pages served here

# ...

# implement any other logic

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)