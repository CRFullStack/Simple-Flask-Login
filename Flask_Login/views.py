"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, url_for, request
from Flask_Login import app

# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def loginMain():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'admin' or request.form['pwd'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('welcome'))
    return render_template('loginPage.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'admin' or request.form['pwd'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('welcome'))
    return render_template('loginPage.html', error=error)

@app.route('/welcome')
def welcome():
    """Renders the index page."""
    return render_template(
        'index.html',
        title='Contact',
        year=datetime.now().year,
        message='Your site.'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )




if __name__=='__main__':
    app.run(debug=True)
