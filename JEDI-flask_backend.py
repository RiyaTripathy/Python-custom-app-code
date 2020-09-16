from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms import TextField
from flask import send_file
from flask_material import Material 

import create_user as action


app = Flask(__name__)
Material(app)

@app.route('/', methods=['GET', 'POST'])
def sign_up():
    error = ""
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        firstname = request.form['first_name']
        lastname= request.form['last_name']
        email = request.form['email']
        login = request.form['login']
        phno = request.form['mobile_phone']
        region = request.form['chosen_attr']
        # Validate form data
        if len(firstname) == 0 or len(lastname) == 0:
            error = "Please supply values to all fields"
        
        else:
            
           print("got em all")
           print(firstname,lastname,email,login,phno,region)
           action.process_request(firstname,lastname,email,login,phno,region)
           #print(message)
        

    # Render the sign-up page
    return render_template('sign-up.html', message=error)



app.run(host='127.0.0.2', port=5001,debug=True)