from flask import render_template , redirect , session , request , flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    # ver si el nombre de usuario proporcionado existe en la base de datos
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # usuario no está registrado en la base de datos
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # si obtenemos False después de verificar la contraseña
        flash("Invalid Email/Password")
        return redirect('/')
    # si las contraseñas coinciden, configuramos el user_id en sesión
    session['user_id'] = user_in_db.id
    session['username'] = user_in_db.username
    session['email'] = user_in_db.email
    # ¡¡¡Nunca renderices en una post!!!
    return redirect('/recipes')



@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        # redirigimos a la plantilla con el formulario
        return redirect('/')
    # ...hacer otras cosas
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }
    user_id = User.save(data)
    if not user_id:
        flash('User not created')
        return redirect('/')
    flash('User created!')
    return redirect('/')