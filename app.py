# from flask import Flask, request, render_template, flash
# # # from . import create_app
# # # app = create_app()
# # from .models import User

# # app = Flask(__name__)

# # @app.route('/')
# # def helloworld():
# #     return render_template("index1234.html")

# # #database = {'soham01@gmail.com': '111', 'roshni02@gmail.com': '222', 'sourashis03@gmail.com': '333'}

# # @app.route('/blog', methods=['POST', 'GET'])
# # def login():
# #     email = request.form['email']
# #     password = request.form['pass']
# #     user = User.query.filter_by(email=email).first()
# #     if user:
# #         if user.password != password:
# #             return render_template('index1234.html', info='Invalid Password')
# #         else:
# #             return render_template('blog.html')
# #     else:
# #         return render_template('index1234.html', info='Invalid User')


# #     # if name1 not in database:
# #     #     return render_template('index1234.html', info='Invalid User')
# #     # else:
# #     #     if database[name1] != pwd:
# #     #         return render_template('index1234.html', info='Invalid Password')
# #     #     else:
# #     #         return render_template('blog.html')

# # if __name__ == '__main__':
# #     app.run()



# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_pymongo import PyMongo
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# app = Flask(__name__)
# app.secret_key = 'asdfghjkl'  # Replace with a secure secret key
# app.config['MONGO_URI'] = 'mongodb+srv://ToDo_nodejs:nodejs@mydatabase.lq765og.mongodb.net/?retryWrites=true'  # Replace with your MongoDB URL
# mongo = PyMongo(app)

# # Initialize Flask-Login
# login_manager = LoginManager()
# login_manager.init_app(app)

# class User(UserMixin):
#     def __init__(self, user_data):
#         self.user_data = user_data
#         self.id = user_data['_id']
#         self.username = user_data['username']
#         self.email = user_data['email']
#         self.password = user_data['password']

# # Function to load user for Flask-Login
# @login_manager.user_loader
# def load_user(user_id):
#     user_data = mongo.db.users.find_one({'_id': user_id})
#     return User(user_data) if user_data else None

# @app.route('/')
# def home():
#     return 'Welcome to the Flask Login System'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         user_data = mongo.db.users.find_one({'email': email})
#         if user_data and check_password_hash(user_data['password'], password):
#             user = User(user_data)
#             login_user(user)
#             flash('Logged in successfully!', category='success')
#             return redirect(url_for('profile'))
#         else:
#             flash('Invalid credentials. Please try again.', category='error')

#     return render_template('login.html')

# @app.route('/profile')
# @login_required
# def profile():
#     return f'Logged in as {current_user.username}'

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('Logged out successfully!', category='success')
#     return redirect(url_for('home'))

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password = request.form.get('password')
#         hashed_password = generate_password_hash(password, method='sha256')

#         user_data = {
#             'username': username,
#             'email': email,
#             'password': hashed_password
#         }

#         user_id = mongo.db.users.insert_one(user_data).inserted_id
#         print(user_id)
#         flash('Registration successful!', category='success')
#         return redirect(url_for('login'))

#     return render_template('signup.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template, flash

app = Flask(__name__)

@app.route('/')
def helloworld():
    return render_template("login.html")

database = {'sohambiswas05@gmail.com': '555', 'roshnimitra02@gmail.com': '222', 'sourashissarkar3@gmail.com': '333'}

@app.route('/home', methods=['POST', 'GET'])
def login():
    name1 = request.form['email']
    pwd = request.form['pass']
    if name1 not in database:
        return render_template('login.html', info='Invalid User')
        flash('Invalid User', category='error')
    
    else:
        if database[name1] != pwd:
            return render_template('login.html', info='Invalid Password')
            flash('Incorrect user', category='error')
            
        else:
            return render_template('home.html', name=name1)
            flash('Logged in successfully!', category='error')
        

if __name__ == '__main__':
    app.run()
