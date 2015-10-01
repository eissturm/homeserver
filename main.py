#!/usr/bin/python
from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/butt')
def butt():
    return 'Butts!'

@app.route('/admin/')
def admin():
    return render_template('admin.html')

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template('login.html')
    
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0',port=8080)