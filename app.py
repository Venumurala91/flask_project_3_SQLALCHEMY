from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['DEBUG'] = True  # Enabling debug mode via config

# Configuration for SQLite Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy()


db.init_app(app)

# Define the Profile model
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # Custom string representation of the Profile object
    def __repr__(self):
        return f"Profile(id={self.id}, Name: {self.first_name} {self.last_name}, Age: {self.age})"


@app.route('/userget', methods=['GET'])
def get_users():
    # Retrieve data from the database
    profiles = Profile.query.all()

    # Convert profile data to a list of dictionaries 
    profiles_list = [{"id": profile.id, "first_name": profile.first_name, "last_name": profile.last_name, "age": profile.age} for profile in profiles]

    print(profiles_list)
    return jsonify(profiles_list)  

@app.route('/adduser',methods=['POST'])
def add_user():

    data=request.get_json()
    first_name=data.get('first_name')
    last_name=data.get('last_name')
    age=data.get('age')

    if  not first_name or not last_name or not age:
        return jsonify({"error":"Missing profile details"}), 400
    

    try:
        profile=Profile(first_name=first_name,last_name=last_name,age=age)

        db.session.add(profile)
        db.session.commit()

        return jsonify({"message":"user created successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  

    

# Run the Flask application

if __name__ == '__main__':
    app.run(debug=True)




