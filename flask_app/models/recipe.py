from flask_app.config.mysqlconnection import connectToMySQL

class Recipe: 
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.instruction = db_data['instruction']
        self.date_made = db_data['date_made']
        self.ubder_30 = db_data['under_30']
        self.users_id = db_data['users_id']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, description, instruction, date_made, under_30, users_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(date_made)s, %(under_30)s, %(users_id)s);"
        return connectToMySQL('db_recetas').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('db_recetas').query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL('db_recetas').query_db(query, data)
        if len(result) < 1:
            return None
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instruction=%(instruction)s, date_made=%(date_made)s, under_30=%(under_30)s, users_id=%(users_id)s WHERE id=%(id)s;"
        return connectToMySQL('db_recetas').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('db_recetas').query_db(query, data)