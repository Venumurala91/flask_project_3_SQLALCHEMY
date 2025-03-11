from flask import Flask,request,jsonify
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


from app import db, Profile

@app.route('/userget', methods=['GET'])
def get_users():
    # Retrieve data from the request (if necessary)
    data = request.get_json()


    if not data or not 'first_name' in data or not 'last_name' in data or not 'age' in data:
        return jsonify({"error": "Missing details"}), 400

    
    profiles = Profile.query.all()

    # Convert profile data to a list of dictionaries
    profiles_list = [{"id": profile.id, "first_name": profile.first_name, "last_name": profile.last_name, "age": profile.age} for profile in profiles]

    return jsonify(profiles_list)  



# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
