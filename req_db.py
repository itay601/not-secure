import pymysql.cursors
import random
import string



##exmple
############## hash -256
import hashlib
password ="1234"
hashed_password = hashlib.sha256(password.encode()).hexdigest()
print(hashed_password)
#############



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








