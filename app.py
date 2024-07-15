# from flask import Flask, request, render_template, redirect, url_for, flash, session
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# import os
# import google.generativeai as genai
# from functools import wraps
# from dotenv import load_dotenv

# load_dotenv()  # Load environment variables from .env file

# # Configure the Gemini API
# genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
# model = genai.GenerativeModel('gemini-pro')

# app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)

#     def set_password(self, password):
#         self.password = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password, password)

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'user_id' not in session:
#             return redirect(url_for('signin'))
#         return f(*args, **kwargs)
#     return decorated_function

# @app.route('/home')
# @login_required
# def home():
#     return render_template('home.html')

# @app.route('/aboutus')
# @login_required
# def aboutus():
#     return render_template('aboutus.html')

# @app.route('/signin', methods=['GET', 'POST'])
# def signin():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()
#         if user and user.check_password(password):
#             session['user_id'] = user.id
#             return redirect(url_for('index'))
#         else:
#             flash('Invalid username or password')
#     return render_template('signin.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         confirm_password = request.form['confirm_password']

#         if password != confirm_password:
#             flash('Passwords do not match!')
#             return redirect(url_for('signup'))

#         user = User(username=username, email=email)
#         user.set_password(password)
#         db.session.add(user)
#         db.session.commit()
#         flash('Account created successfully. Please log in.')
#         return redirect(url_for('signin'))
#     return render_template('signup.html')

# @app.route('/terms')
# @login_required
# def terms():
#     return render_template('terms.html')

# @app.route('/')
# @login_required
# def index():
#     return render_template('index.html', result=None)

# @app.route('/generate', methods=['POST'])
# @login_required
# def generate_content():
#     text = request.form.get('text')
#     if not text:
#         return render_template('index.html', result='No text provided', generated_output=None)

#     prompt = f" Correct the following sentence: {text}. Provide a concise one-liner with the corrected version."
#     try:
#         response = model.generate_content(prompt)
#         generated_output = response.text.strip()
#         return render_template('index.html', result=None, generated_output=generated_output, input_text=text)
#     except Exception as e:
#         return render_template('index.html', result=f'An error occurred: {str(e)}', generated_output=None, input_text=text)

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)

