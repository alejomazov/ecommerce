
import src.database.connection as sqldb
from flask import Flask, render_template,request, redirect, url_for


app = Flask(__name__,template_folder='src\\templates',static_folder='src\\static')

db = sqldb.BaseDatos(config_file="src\\utils\\config_db.json")


'''


print ("ingrese sus datos para suscribirse")
email = input ('ingrese un email: ')
password = input ('ingrese un password:').encode(encoding='utf-8')

name = ''
phone = ''

password_hashed = db.password_hashed(password)

user = {'email':email,'password':password_hashed,'name':name, 'phone':phone}

db.sign_up(**user)

print ("ingrese sus datos para logearse")
email = input ('ingrese un email: ')
password = input ('ingrese un password:').encode(encoding='utf-8') 

db.login(email, password)
'''

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/shop.html')
def shop():
    return render_template('shop.html')

@app.route('/shop-single.html')
def shop_single():
    return render_template('shop-single.html')

@app.route('/contact.html', methods = ['GET', 'POST'])
def contact():

    return render_template('contact.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method=='POST':
        email= request.form['email']
        password = request.form['password']
        print (type(email))
        print (password )
        logged = db.login(email, password.encode(encoding='utf-8') )

        if logged == True:
            return redirect(url_for('home'))
        else: 
            return render_template('login.html')
    else:    
        return render_template('login.html')
    

            
if __name__ == "__main__":
    app.run(debug=True)