# Title Mocking string converter app
# Author: Ryan Toff
# Original Created Date: 10/5/2019
# Description: App to convert an input string into camelcasing
# --so that it is output similar to the Spongebob mocking meme


########### CONVERT temp.py TO FLASK APP ###########
# Import flask modules
from flask import Flask, render_template, redirect

# Create Flask APP
app = Flask(__name__)

# Create main page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
