# Title Mocking string converter app
# Author: Ryan Toff
# Original Created Date: 10/5/2019
# Description: App to convert an input string into camelcasing
# --so that it is output similar to the Spongebob mocking meme

# Import flask modules
from flask import Flask, render_template, redirect, request, flash, session, url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

# Create Flask APP
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class SassForm(FlaskForm):
    original_string = TextAreaField("Enter a phrase, I'll sass you all day.", validators=[DataRequired()])
    submit = SubmitField('Sass Me')

# Create main page
@app.route('/', methods=['GET', 'POST'])
def index():

    form = SassForm()

    if form.validate_on_submit():
        # Take in the string submitted from index.html
        session['original_string'] = form.original_string.data

        # Create a list to hold the characters
        char_list = []

        # Split the string into a list of separate characters
        for char in session['original_string']:
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

        # Flash the converted string to the user
        flash(converted_string)

        return redirect(url_for('index'))

    return render_template('index.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
