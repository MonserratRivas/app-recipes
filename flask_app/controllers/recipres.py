from flask import render_template , redirect ,session, request, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/recipe')
def recipe():
    return render_template('recipe/index.html')