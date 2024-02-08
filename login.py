
import pymysql
import hashlib

##exmple
############## hash -256
password ="1234"
hashed_password = hashlib.sha256(password.encode()).hexdigest()
print(hashed_password)
#############

SECRET_KEY = '@@##sfasfd321'  # Replace with a strong and unique secret key
TOKEN_EXPIRATION_SECONDS = 3600  # Set the expiration time for the token (e.g., 1 hour)




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
            sql = "SELECT * FROM user WHERE username=%s"
            cursor.execute(sql, (username , ))

            user_data = cursor.fetchone()
            
            print(user_data)
            #if user exist return 1
            if user_data:
                return 1
            else:
                print("Invalid username or password")
                return 0

    except pymysql.Error as e:
        print(f"Database error: {e}")

    finally:
        connection.close()







