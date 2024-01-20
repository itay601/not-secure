import os 

def input_validate(username,password):
     username =  username.encode('utf8')
     check_unique_username(username)
     check_3_or_more_uniq_characters(password)
 
