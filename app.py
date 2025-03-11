from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['DEBUG'] = True  # Enabling debug mode via config

# Configuration for SQLite Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# SQLAlchemy instance initialization
db = SQLAlchemy(app)

# Define the Profile model
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # Custom string representation of the Profile object
    def __repr__(self):
        return f"Profile(id={self.id}, Name: {self.first_name} {self.last_name}, Age: {self.age})"

# Create the database and tables (with app context)
# Assuming you're in Python Shell or a script

# Step 1: Import the Flask app and database instance
# from app import app, db, Profile  # app.py should be the name of your script

# Step 2: Push the application context
# with app.app_context():
#     db.create_all()

    # # Now you can safely add records to the database
    # new_profile = Profile(first_name='John', last_name='Doe', age=30)
    # db.session.add(new_profile)  # Add the object to the session
    # db.session.commit()  # Commit the changes to the database
    # print("Profile added successfully!")


# Run the Flask application
if __name__ == '__main__':
    app.run()
