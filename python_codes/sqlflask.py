from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route('/')
def index():
    with app.app_context():
        users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    ## select * from users where id=
    if not user:
        return jsonify({'message': 'User does not exists'}) ,404
    user_data = {
        'id' : user.id,
        'name' : user.name,
        'email' : user.email
    }
    
    return jsonify(user_data), 200

@app.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User does not exists'}) ,404
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': ' user is successfully deleted'}) , 200

@app.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user= User.query.get(user_id)
    if not user:
        return "USER NOT FOUND" , 404
    name = request.form['name']
    email= request.form['email']
    
    user.name = name
    user.email = email

    db.session.commit()

    return jsonify({'message':'User updated successfully', 'success':200})



@app.route('/add' ,methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    user = User(name , email)
    db.session.add(user)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# below is the terminal command
# curl -X PUT -d "name=Updated Name" -d "email=updATED@gmail.com" http://localhost:5000/update/1

# curl -X DELETE http://localhost:5000/delete/89

# curl -X POST -d "name=John WICK CHAPTER 4 &email=jHVWEGWEGV@exm.com" http://localhost:5000/add

#  curl localhost:5000/users/3