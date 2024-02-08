from flask import Flask , render_template, request, flash, redirect, url_for, make_response,Response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

from login import  login_user
from req_db import *
from send_pass_to_email import reset_password_and_send_email



app = Flask(__name__)


app.config['JWT_SECRET_KEY'] = '7$*&?>fhd3433@#4227'  # Change this to a secure random key in production
jwt = JWTManager(app)




#need system_screen only with token in headers (not working)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')   

    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_exist = login_user(username, password)

        if user_exist:
            access_token = create_access_token(identity=username)
            # Render the template
            return render_template('system_screen.html')  
    return render_template('login.html')



    

@app.route('/register.html', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        id_ = request.form['id']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        register_new_user(id_ , username , email , password)
        return render_template('login.html')
        
        
        return render_template('system_screen.html')
    return render_template('register.html')




@app.route('/system_screen.html', methods=['GET','POST'])
@jwt_required()
def system_screen():
    if request.method == 'GET':
        current_user = get_jwt_identity()
        print(current_user)
        if current_user==None:
            return render_template('login.html')  
        
    elif request.method == 'POST':
        name  =request.form['clientName']
        email =request.form['clientEmail']
        phone =request.form['clientPhone']
        
        insert_client(name,email,phone)
        return render_template('system_screen.html')
      
    return render_template('system_screen.html')




@app.route('/change_password.html', methods=['GET','POST'])
def change_password_():
    if request.method == 'GET':
        return render_template('change_password.html')

    elif request.method == 'POST':
        username     = request.form['username']
        password_old = request.form['currentPassword']
        password_new = request.form['newPassword']
        change_password(username, password_old, password_new)
        return render_template('login.html') 
    return render_template('change_password.html')

   




@app.route('/forgot_password.html', methods=['GET','POST'])
def forgot_password():
    if request.method == 'GET':
        return render_template('forgot_password.html')
    elif request.method == 'POST':
        mail =request.form['email']
        reset_password_and_send_email(mail)
        return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
    
  






