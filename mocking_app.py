# Title Mocking string converter app
# Author: Ryan Toff
# Original Created Date: 10/5/2019
# Description: App to convert an input string into camelcasing
# --so that it is output similar to the Spongebob mocking meme


########### CONVERT temp.py TO FLASK APP ###########
# Import flask modules
from flask import Flask, render_template, redirect, request, redirect

# Create Flask APP
app = Flask(__name__)

# Create main page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converted_phrase')
def converted_phrase():
    # Take in the string submitted from index.html
    original_string = request.args.get('original_string')

    # Create a list to hold the characters
    char_list = []

    # Split the string into a list of separate characters
    for char in original_string:
        char_list.append(char)

    # Create variable to iterate over while loop and a list for the converted chars
    i = 0
    converted_char_list = []

    # Convert character case based on even/odd
    while i <= (len(char_list) - 1):
        if (i == 0) or (i % 2 == 0):
            converted_char_list.append(char_list[i].lower())
        else:
            converted_char_list.append(char_list[i].upper())
        i+=1

    # Create variable to hold the converted string
    converted_string = ""
    for char in converted_char_list:
        converted_string += char
    return render_template('converted_phrase.html',original_string=original_string,converted_string=converted_string)

if __name__ == '__main__':
    app.run(debug=True)
