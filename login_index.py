from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    
        print('Username1:', username)
        print('Password:', password)
        #check and works!!! 
        if username == "s":
            return render_template('system_screen.html')
        #now we need here to do input validation 
        # for login file     




    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
    
  


