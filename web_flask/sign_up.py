#!/usr/bin/python3

from flask import Flask, render_template, request, jsonify
from werkzeug.security import generate_password_hash
from models import storage
from models.user import User


app = Flask(__name__)


@app.route("/sign_up", methods=['POST'], strict_slashes=False)
def sign_up():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    data["password"] = hashed_password
    instance = User(**data)
    instance.save()
    return jsonify({"message": "User registered successfully!"})

    