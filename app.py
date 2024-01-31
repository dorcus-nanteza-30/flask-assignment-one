from flask import Flask, render_template


app= Flask(__name__)

@app.route('/')
def home():
    return '<h2> WELCOME TO OUR APP</h2>'

@ app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thankyou') 
def thankyou():
    return render_template('thankyou.html')

@app.route('/form')
def form():
    return render_template('form.html')

