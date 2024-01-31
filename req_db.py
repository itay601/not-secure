import pymysql.cursors
import random
import string



def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password








###work and checked###
def show_user_db():
    host = '127.0.0.1' 
    user = 'root'
    password = 'my-secret-pw' 
    dbname = 'USERS'

    # Connect to the database
    connection = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    database=dbname,
                                    port=3456,
                                    cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user;"

            cursor.execute(sql)

            result = cursor.fetchall()
            for row in result:
                print(row)
    except:
        print("something failed")

    finally:
        connection.close()

#show_user_db()

###working and checked
def show_client_db():
    host = '127.0.0.1' # there is no place like home (127.0.0.1 == localhost)
    user = 'root'
    password = 'my-secret-pw'  # Replace with your password
    dbname = 'USERS'

    # Connect to the database
    connection = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    database=dbname,
                                    port=3456,
                                    cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM clients;"

            cursor.execute(sql)

            result = cursor.fetchall()
            for row in result:
                print(row)
    except:
        print("something failed")

    finally:
        connection.close()




###work and checked###
def register_new_user(id_, username, email, password):
    host = '127.0.0.1'
    user = 'root'
    password = 'my-secret-pw'
    dbname = 'USERS'

    try:
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=dbname,
                                     port=3456,
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            sql = "INSERT INTO user (id, username, email, password) VALUES (%s, %s, %s, %s)"
            values = (id_, username, email, password)

            cursor.execute(sql, values)

        # Commit the changes to the database
        connection.commit()

        print("User registered successfully!")

    except pymysql.Error as e:
        print(f"Error: {e}")

    finally:
        if connection:
            connection.close()



"""
def login_user():
    host = '127.0.0.1' # there is no place like home (127.0.0.1 == localhost)
    user = 'root'
    password = 'my-secret-pw'  # Replace with your password
    dbname = 'USERS'

    # Connect to the database
    connection = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    database=dbname,
                                    port=3456,
                                    cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user"

            cursor.execute(sql)

            result = cursor.fetchall()
            for row in result:
                print(row)
    except:
        print("something failed")

    finally:
        connection.close()
"""

#####working 
def change_password(username,password_old,password_new):
    host = '127.0.0.1' # there is no place like home (127.0.0.1 == localhost)
    user = 'root'
    password = 'my-secret-pw'  # Replace with your password
    dbname = 'USERS'

    # Connect to the database
    connection = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    database=dbname,
                                    port=3456,
                                    cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Check if the user exists
            sql_select_user = "SELECT * FROM user WHERE username=%s AND password=%s"
            cursor.execute(sql_select_user, (username,password_old))
            user_data = cursor.fetchone()

            if user_data:
                
                # Update the user's password in the database
                sql_update_password = "UPDATE user SET password=%s WHERE username=%s"
                cursor.execute(sql_update_password, (password_new, username))
                connection.commit()
    except:
        print("something failed")

    finally:
        connection.close()        



####working
def insert_client(name,email,phone):
    host = '127.0.0.1'
    user = 'root'
    password = 'my-secret-pw'
    dbname = 'USERS'

    try:
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=dbname,
                                     port=3456,
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            sql = "INSERT INTO clients (name, email, phone) VALUES (%s,%s,%s)"
            values = (name, email, phone)

            cursor.execute(sql, values)

        # Commit the changes to the database
        connection.commit()

        print("client inserted successfully!")

    except pymysql.Error as e:
        print(f"Error: {e}")

    finally:
        if connection:
            connection.close()


insert_client("name","email@gmail.com", "550654354")        
show_client_db()




"""
import pymysql
import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your_secret_key'  # Replace with a strong and unique secret key
TOKEN_EXPIRATION_SECONDS = 3600  # Set the expiration time for the token (e.g., 1 hour)

def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(seconds=TOKEN_EXPIRATION_SECONDS)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def login_user(username, password):
    host = '127.0.0.1'
    user = 'root'
    password = 'my-secret-pw'
    dbname = 'USERS'

    # Connect to the database
    connection = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                database=dbname,
                                port=3456,
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Check if the username and password match a user in the database
            sql = "SELECT * FROM user WHERE username=%s AND password=%s"
            cursor.execute(sql, (username, password))

            user_data = cursor.fetchone()

            if user_data:
                # If user is found, generate and return a token
                user_id = user_data['id']
                token = generate_token(user_id)
                return token
            else:
                print("Invalid username or password")

    except pymysql.Error as e:
        print(f"Database error: {e}")

    finally:
        connection.close()

# Example usage:
username_input = input("Enter username: ")
password_input = input("Enter password: ")

token = login_user(username_input, password_input)

if token:
    print(f"Login successful. Token: {token}")



"""




#generate password chenge password in db and send emial with th password


"""


import pymysql
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def generate_random_password(length=12):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def send_email(receiver_email, subject, body):
    sender_email = 'your_email@gmail.com'  # Replace with your email address
    sender_password = 'your_email_password'  # Replace with your email password
    smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL(smtp_server, 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

def reset_password_and_send_email(username):
    host = '127.0.0.1'
    user = 'root'
    password = 'my-secret-pw'
    dbname = 'USERS'

    # Connect to the database
    connection = pymysql.connect(host=host,
                                user=user,
                                password=password,
                                database=dbname,
                                port=3456,
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Check if the user exists
            sql_select_user = "SELECT * FROM user WHERE username=%s"
            cursor.execute(sql_select_user, (username,))
            user_data = cursor.fetchone()

            if user_data:
                # Generate a new random password
                new_password = generate_random_password()

                # Update the user's password in the database
                sql_update_password = "UPDATE user SET password=%s WHERE username=%s"
                cursor.execute(sql_update_password, (new_password, username))

                # Send the new password to the user's email
                receiver_email = user_data['email']
                email_subject = "Password Reset"
                email_body = f"Your new password is: {new_password}"
                send_email(receiver_email, email_subject, email_body)
                
                print("Password reset successfully. Check your email for the new password.")
            else:
                print("User not found.")

    except pymysql.Error as e:
        print(f"Database error: {e}")

    finally:
        connection.close()

# Example usage:
username_input = input("Enter username: ")
reset_password_and_send_email(username_input)"""





def rend_password_and_send_to_email(email):
    host = '127.0.0.1' # there is no place like home (127.0.0.1 == localhost)
    user = 'root'
    password = 'my-secret-pw'  # Replace with your password
    dbname = 'USERS'

    # Connect to the database
    connection = pymysql.connect(host=host,
                                    user=user,
                                    password=password,
                                    database=dbname,
                                    port=3456,
                                    cursorclass=pymysql.cursors.DictCursor)
    
    #Generate a random password of length 12
    random_password = generate_random_password()
    print(random_password) 

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user"

            cursor.execute(sql)

            result = cursor.fetchall()
            for row in result:
                print(row)
    except:
        print("something failed")

    finally:
        connection.close()              
        
        
        