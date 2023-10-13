from flask_app.config.mysqlconnection import connectToMySQL
import re
#Validacion de expreciones regulares.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(selft,db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.password = db_data['password']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
    @classmethod
    def save(cls,data):
        query ="INSERT INTO users(first_name , last_name , email , password) VALUES (%(first_name)s , %(last_name)s , %(email)s , %(password)s);"
        return connectToMySQL('db_recetas').query_db(query, data)

    @classmethod
    def get_by_email(cls,user_id):
        query ="select * from users where id = %(id)s;"
        data={'id': user_id}
        result = connectToMySQL('db_recetas').query_db(query,data)
        return cl(result[0]) if result else None
    @classmethod
    def get_by_email(cls,data):
        query ="select * from users where email = %(email)s;"
        result = connectToMySQL('db_recetas').query_db(query,data)
        if not result :
            flash('email no encontrado')
            return False
        return cls(result[0]) 
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # prueba si un campo coincide con el patrón
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid    