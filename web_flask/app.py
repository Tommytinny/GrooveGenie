#!/usr/bin/python3
from web_flask.fields import RegistrationForm, LoginForm 
from flask import Flask, render_template, url_for, flash, redirect, jsonify, render_template, request
from models import storage
from models.user import User
from web_flask.recommend import recommend_songs, search_songs


app = Flask(__name__)

app.config['SECRET_KEY'] = '8fa8c82749304b1cd7b9e5bd1b2b4e41'


"""@app.route("/login", methods=['GET'], strict_slashes=False)
def login():
    data = request.get_json()
    hashed_password = check_password_hash(data['password'], method='sha256')
    data["password"] = hashed_password
    instance = User(**data)
    instance.save()
    return jsonify({"message": "User registered successfully!"})
"""

@app.route('/recommend', methods=['GET'])
def recommend():
    song_name = request.args.get('song_name')
    recommendations = recommend_songs(song_name)
    
    
    return render_template('home.html', title='GrooveGenie', recommendations=recommendations)
    #return jsonify({"recommended_songs": recommendations.tolist()})

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    filtered_songs = search_songs(query)
    return jsonify(filtered_songs)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!i')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='GrooveGenie')

@app.route("/", methods=['GET', 'POST'])
def page():
    return render_template('index.html', title='GrooveGenie')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
     flash('Login Unsuccessful. Please check username  and password', 'red')
    return render_template('login.html', title='Login', form=form)

@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='GrooveGenie')

@app.route("/", methods=['GET', 'POST'])
def page():
    return render_template('index.html', title='GrooveGenie')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
