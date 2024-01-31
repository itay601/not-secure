from flask import Flask ,Blueprint, render_template, request, flash, redirect, url_for
#from . models import User
from werkzeug.security import generate_password_hash, check_password_hash
#from . import db, mycursor   ##means from __init__.py import db





app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')   

    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print('Username1:', username)
        print('Password:', password) 
        
        #the input validation
        if username =='s':
            return render_template('system_screen.html')

        #now we need here to do input validation 
        # for login file     
     
    return render_template('login.html')





@app.route('/register.html', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        insert_user_register_post(username,email,password)
        return render_template('system_screen.html')
    return render_template('register.html')




@app.route('/system_screen.html', methods=['GET','POST'])
def system_screen():
    if request.method == 'GET':
        return render_template('login.html')
    #elif request.method == 'POST':

    return render_template('system_screen.html')




@app.route('/change_password.html', methods=['GET','POST'])
def change_password():
    if request.method == 'GET':
        return render_template('change_password.html')
    #elif request.method == 'POST':

    return render_template('change_password.html')




@app.route('/forgot_password.html', methods=['GET','POST'])
def forgot_password():
    if request.method == 'GET':
        return render_template('forgot_password.html')
    #elif request.method == 'POST':

    return render_template('forgot_password.html')




@app.route('/login.html', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
    
  






