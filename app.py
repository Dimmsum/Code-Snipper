#Imports the flask package
from flask import Flask, render_template,url_for
from sqlalchemy import SQLAlchemy


#creating an instance of the flask class from the flask package
app = Flask(__name__)
#database instance
db = SQLAlchemy(app)
#connecting the app file to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config[SECRET_KEY] = 'password'

@app.route('/') # "/" is the default route 
def home(): #function that will be executed when the default route is accessed
    return render_template('Home.html') #Returns the html file when the route is accessed

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/register')
def register():
    return render_template('Register.html')

if __name__ == '__main__':
    app.run(debug=True) #runs the flask

