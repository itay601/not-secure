import pymysql.cursors
import random
import string
from argon2 import PasswordHasher


###########################################################################
#chack common passwords  /// ilustrate large library of common passwords
passwords111= {"passwords":{"12345678910" , "Password" ,"P@ssw0rd",
                          "Pass@123" , "Aa@123456","1q2w3e4r5t"}}

def common_passwords(password,passwords111):
    for x in passwords111["passwords"]:
        if x == password:
            print("chahnge password")
        
    return "not common password"    




#common_passwords("assword",passwords111)
##########################################################################
import hashlib
import random
import string

def verify_sha1_hash(password, hashed_password):
   
    # Hash the provided password using SHA1
    hashed_input_password = hashlib.sha1(password.encode()).hexdigest()
    
    # Compare the hashed input password with the provided hashed password
    return hashed_input_password == hashed_password

# Example usage:
stored_hashed_password = "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"  # Example hashed password (corresponding to "password")
password_attempt = "password"  # Example password attempt

if verify_sha1_hash(password_attempt, stored_hashed_password):
    print("Password is correct!")
else:
    print("Password is incorrect.")
    
def hash1_password(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest()
    print(sha1_hash)
    return sha1_hash

#####################################################################



#itay
ph = PasswordHasher()
name = ph.hash("itay")
print(name)






def connect_to_db():
    host = "127.0.0.1"
    user = "root"
    password = "my-secret-pw"
    dbname = "USERS"

    # Connect to the database
    db_connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=dbname,
        port=3456,
        cursorclass=pymysql.cursors.DictCursor,
    )

    return db_connection


def validate_password(username, pWord):
    # Connect to the database
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            # Check if the username and password match a user in the database
            sql = "SELECT password FROM user WHERE username=%s"
            cursor.execute(sql, (username,))
            pass_hash = cursor.fetchone()
            ph = PasswordHasher()

            # On success return 1
            if ph.verify(pass_hash["password"], pWord):
                return 1
            else:
                print("Invalid username or password")
                return 0

    except pymysql.Error as e:
        print(f"Database error: {e}")

    finally:
        if connection:
            connection.close()





def change_password(username, pWord):
    # Connect to the database
    ph = PasswordHasher()
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            # Check if the username and password match a user in the database
            sql = "UPDATE user SET password =%s WHERE username =%s"
            pHash = ph.hash(pWord)
            if ph.verify(pHash, pWord):
                cursor.execute(
                    sql,
                    (
                        pHash,
                        username,
                    ),
                )
                connection.commit()
                print("commited update")
                return 1
            else:
                raise pymysql.Error

    except pymysql.Error as e:
        print(f"Database error: {e}")
        return 0

    finally:
        if connection:
            connection.close()


def register_new_user(username, email, pWord):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            ph = PasswordHasher()
            passHash = ph.hash(pWord)
            sql = "INSERT INTO user (username, email, password) VALUES (%s, %s, %s)"
            values = (username, email, passHash)
            cursor.execute(sql, values)
        # Commit the changes to the database
        connection.commit()
        print("User registered successfully!")

    except pymysql.Error as e:
        print(f"Error: {e}")

    finally:
        connection.close()


def register_new_client(username, email, phoneNum):
    try:
        connection = connect_to_db()
        with connection.cursor() as cursor:
            sql = "INSERT INTO clients (name, email, phone) VALUES (%s, %s, %s)"
            values = (username, email, phoneNum)
            cursor.execute(sql, values)
        # Commit the changes to the database
        connection.commit()
        print("Client registered successfully!")

    except pymysql.Error as e:
        print(f"Error: {e}")

    finally:
        if connection:
            connection.close()


"""
Experimental from here down


"""


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def show_user_db():
    # Connect to the database
    try:
        connection = connect_to_db()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM user;"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row)

    except:
        print("something failed")

    finally:
        if connection:
            connection.close()


###working and checked
def show_client_db():
    # Connect to the database
    try:
        connection = connect_to_db()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM clients;"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row)

    except:
        print("something failed")

    finally:
        if connection:
            connection.close()
