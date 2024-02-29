from flask import (
    Flask,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    make_response,
    Response,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

from req_db import *
from send_pass_to_email import reset_password_and_send_email 


app = Flask(__name__)


app.config[
    "JWT_SECRET_KEY"
] = "7$*&?>fhd3433@#4227"  # Change this to a secure random key in production
jwt = JWTManager(app)


"""
                                                                
                                                                   
888888888888  ,ad8888ba,    88888888ba,      ,ad8888ba,            
     88      d8"'    `"8b   88      `"8b    d8"'    `"8b           
     88     d8'        `8b  88        `8b  d8'        `8b          
     88     88          88  88         88  88          88     888  
     88     88          88  88         88  88          88     888  
     88     Y8,        ,8P  88         8P  Y8,        ,8P          
     88      Y8a.    .a8P   88      .a8P    Y8a.    .a8P      888  
     88       `"Y8888Y"'    88888888Y"'      `"Y8888Y"'       888  
                                                                   
                                                                                      

    
	"""


login_attempts = {}
# need system_screen only with token in headers (not working)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("login.html")

    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Check if the user has exceeded the login attempts
        if username in login_attempts and login_attempts[username] >= 2:
            return render_template("forgot_password.html",message1="only email for now ,to much login requests!!")

        if validate_password(username, password):
            access_token = create_access_token(identity=username)
            if username in login_attempts:
                del login_attempts[username]
            # Render the template
            return render_template("system_screen.html",success="Loged in!!")
        else:
            login_attempts[username] = login_attempts.get(username, 0) + 1
            return render_template("login.html",changed_pass="try agian")




@app.route("/register.html", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]

        if request.form["user_type"] == "user":
            password = request.form["password1"]
            password2 = request.form["password2"]
            if password == password2:
                register_new_user(username, email, password)
                return render_template("system_screen.html",success="you registered!!")
            else:
                return render_template("register.html",no_same_pass="not the same passwords")

        elif request.form["user_type"] == "client":
            phoneNum = request.form["clientPhone"]
            register_new_client(username, email, phoneNum)
            return redirect("/show.html")


@app.route("/change_password.html", methods=["GET", "POST"])
def Code_password_():
    if request.method == "GET":
        return render_template("change_password.html")

    elif request.method == "POST":
        username = request.form["username"]
        password_old = request.form["currentPassword"]
        password_new = request.form["newPassword1"]

        if validate_password(username, password_old):
            if change_password(username, password_new):
                return render_template("login.html",changed_pass="the password changed")
            else:
                return render_template("change_password.html",message="something happend try again" )        
        else:
            return render_template("change_password.html",message="user or pass wrong try again" )
            




@app.route("/forgot_password.html", methods=["GET", "POST"])
def forgot_password():
    if request.method == "GET":
        return render_template("forgot_password.html")
    if request.method == "POST":
        mail = request.form["email"]
        if reset_password_and_send_email(mail):### in this function we need to insert the code to db 
            return render_template("change_password.html",message="enter code you got from email")
        else: 
            #something happend massage to client
            return render_template("forgot_password.html",message1="something heppand try agian")


@app.route("/system_screen.html", methods=["GET", "POST"])
@jwt_required()
def system_screen():
    if request.method == "GET":
        current_user = get_jwt_identity()
        print(current_user)
        if current_user == None:
            return render_template("login.html",message2="try again!!")


# Skeleton method, needs to be tailored to our needs
@app.route("/show.html", methods=["GET"])
def show():
    if request.method == "GET":
        host = "127.0.0.1"
        user = "root"
        password = "my-secret-pw"
        dbname = "USERS"

        # Connect to the database
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=dbname,
            port=3456,
            cursorclass=pymysql.cursors.DictCursor,
        )

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM clients;"  # Change statement accordingly
                cursor.execute(sql)
                result = cursor.fetchall()
        except:
            print("something failed")

        finally:
            connection.close()
        return render_template(
            "table_display.html", headings=("uName", "email", "pass"), data=result
        )  # (("Jeff","j@mail.com","asd123"),("don","d@mail.com","ads321"))


if __name__ == "__main__":
    app.run(debug=True)
