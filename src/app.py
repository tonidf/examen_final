from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_manager, login_required, logout_user, current_user
from validators import LoginForm, RegisterForm, ContactForm
from models.ModelsUser import ModelUser
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

db = MySQL(app)

login_manager = LoginManager(app)

@login_manager.user_loader
def get_by_id(id):
    return ModelUser.get_by_id(db, id)


@app.route('/', methods=['POST', 'GET'])
def register():
    try:
        form = RegisterForm()

        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            email = request.form.get('email')
            ModelUser.register(db, password, email, username )

            logged_user = ModelUser.login(db, password, username)

            if logged_user:
                if logged_user.password:
                    print('Autenticado')
                    login_user(logged_user)
                    return redirect(url_for('login'))
                else:
                    print('Contraseña incorrecta')
                    return redirect(url_for('register'))
            else:
                print('hola')
                return redirect(url_for('register'))
        else:
            # if current_user.is_authenticated:
            #     return redirect(url_for('login'))
            return render_template('register.html', form=form)
        
    except Exception as e:
        raise Exception(e)
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        form = LoginForm()

        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            logged_user = ModelUser.login(db, password, username )

            if logged_user:
                if logged_user.password:
                    print('Autenticado')
                    login_user(logged_user)
                    ##Falta return
                else:
                    print('Contraseña incorrecta')
                    return redirect(url_for('login.html'))
            else:
                print('Usuario no encontrado')
        else:
            # if current_user.is_authenticated:
            #     return "adios"
            return render_template('login.html', form=form)
        
    except Exception as e:
        raise Exception(e)
    
# @app.route('/contacts')
# def contacts():
#     form = ContactForm

#     return render_template('contacts.html')

if __name__ == '__main__':
    app.config.from_object(config['Development'])
    app.run()