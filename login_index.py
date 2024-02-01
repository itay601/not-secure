from flask import Flask , render_template, request, flash, redirect, url_for, make_response,Response
from werkzeug.security import generate_password_hash, check_password_hash

from login import  login_user
from req_db import *

app = Flask(__name__)



#need system_screen only with token in headers (not working)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')   

    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        token = login_user(username, password)

        if token:
            print(f"Login successful. Token: {token}")

            # Render the template
            rendered_template = render_template('system_screen.html')

            # Create a response object and set the Authorization header
            response = Response(rendered_template)
            response.headers['Authorization'] = f'Bearer {token}'
            return response
           #print(f"Login successful. Token: {token}")
           #return render_template('system_screen.html')   
     
    return render_template('login.html')



    

@app.route('/register.html', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    elif request.method == 'POST':
        id = request.form['id']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        register_new_user(id , username , email , password)
        return render_template('login.html')
        
        
        return render_template('system_screen.html')
    return render_template('register.html')




@app.route('/system_screen.html', methods=['GET','POST'])
def system_screen():
    if request.method == 'GET':
        f= generate_token()
        if validate_token==None:
            return render_template('login.html')  
        
    elif request.method == 'POST':
        name  =request.Form['clientName']
        email =request.Form['clientEmail']
        phone =request.Form['clientPhone']
        
        insert_client(name,email,phone)
        return render_template('system_screen.html')
      
    return render_template('system_screen.html')




@app.route('/change_password.html', methods=['GET','POST'])
def change_password():
    if request.method == 'GET':
        return render_template('change_password.html')

    elif request.method == 'POST':
        username =request.Form['username']
        password_old =request.Form['currentPassword']
        password_new =request.Form['newPassword']
        change_password(username,password_old,password_new)
        return render_template('login.html') 
    return render_template('change_password.html')

   




@app.route('/forgot_password.html', methods=['GET','POST'])
def forgot_password():
    if request.method == 'GET':
        return render_template('forgot_password.html')
    elif request.method == 'POST':
        mail =request.Form['email']
        reset_password_and_send_email(mail)
        return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
    
  






