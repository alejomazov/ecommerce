
import src.database.connection as sqldb

db = sqldb.BaseDatos(config_file="src\\utils\\config_db.json")





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

            
