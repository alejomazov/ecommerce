import mysql.connector
import bcrypt
import json


class BaseDatos:

    def __init__(self,config_file):
        try:
            with open(config_file, 'r') as f:
                db_config = json.load(f)

            self.conector = mysql.connector.connect(**db_config)
            self.cursor = self.conector.cursor()
            print("conectado exitosamente")
        except Exception as e:
            print(f'Algo fallo en la conexion {e}')

    def password_hashed(self, password):
        salt = bcrypt.gensalt()
        password_hashed = bcrypt.hashpw(password, salt)
        return password_hashed
            
    def sign_up(self, **kwargs):
        try:
            # Generar dinámicamente las columnas y los placeholders
            columns = ', '.join(kwargs.keys())  # Columnas (nombres)
            placeholders = ', '.join(['%s'] * len(kwargs))  # Placeholders para los valores
            values = tuple(kwargs.values()) # Valores reales como tupla
            # Construir la consulta SQL de forma segura
            sql_query = f"INSERT INTO users ({columns}) VALUES ({placeholders})"
            # Ejecutar la consulta con valores seguros
            self.cursor.execute(sql_query, values)
            self.conector.commit()

            print("Datos insertados correctamente.")
            
        except Exception as e:  # Capturar el error específico
            print(f"No se pudo ingresar los datos: {e}")

    def login(self, email, password):
        try:
             # Construir la consulta SQL de forma segura
            sql_query = f"SELECT password FROM users WHERE email = %s"
            # Ejecutar la consulta 
            self.cursor.execute(sql_query, (email,))
            hashed =self.cursor.fetchone()
            password_hashed = hashed[0]

            if bcrypt.checkpw(password, password_hashed.encode(encoding='utf-8')):
               print("Pasword is correct!")
            else:
               print ("Password is incorrect!")
            
        except Exception as e:  # Capturar el error específico
            print(f"Algo fallo al iniciar sesión:  {e}")

