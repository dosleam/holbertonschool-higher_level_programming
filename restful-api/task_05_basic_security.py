#!/bin/usr/python3

"""
Ce script est une application Flask qui utilise l'authentification
basique et les tokens JWT (JSON Web Tokens)
pour sécuriser des endpoint.
Il gère aussi différents types d'erreurs J
comme les tokens expirés ou invalides.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['JWT_SECRET_KEY'] = 'your_secret_key'

jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password1"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("passwordadmin"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Vérifie les identifiants d'un utilisateu
    avec une authentification basique.

    Args:
        username (str): Le nom d'utilisateur.
        password (str): Le mot de passe non haché fourni par l'utilisateur.

    Returns:
        bool: True si l'utilisateur existe
        et que le mot de passe est correct, sinon False.
    """
    user = users.get(username)
    if not user:
        return False
    return check_password_hash(user['password'], password)


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Route protégée par une authentification basiqu
    Accessible uniquement aux utilisateurs authentifiés.

    Returns:
        Response: Message de confirmation si l'accès est autorisé.
    """
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint pour la connexion des utilisateurs.
    Si les identifiants sont corrects,
    un token JWT est généré et retourné.

    Returns:
        Response: Un token JWT ou un message d'erreur
        si les identifiants sont incorrects.
    """
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password required"}), 400

    username = data['username']
    password = data['password']
    user = users.get(username)

    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity={"username": username, "role": user['role']}
    )
    return jsonify(access_token=access_token)


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Route protégée par un token JW
    L'utilisateur doit fournir un token valide pour y accéder.

    Returns:
        Response: Message de confirmation si l'accès est autorisé.
    """
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Route réservée aux administrateurs. Vérifie le rôle de l'utilisateur
    à partir du token JWT.

    Returns:
        Response: Message de confirmation si l'accès est autoris
        ou un message d'erreur si l'utilisateur n'est pas admin.
    """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"})


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Gère les erreurs lorsque l'utilisateur tente d'accéd
    une route protégée sans fournir de token JWT.

    Returns:
        Response: Message d'erreur indiquant
        que le token est manquant ou invalide.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Gère les erreurs lorsque l'utilisateur fournit un token JWT invalide

    Returns:
        Response: Message d'erreur indiquant que le token est invalide.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Gère les erreurs lorsque l'utilisateur fournit un token JWT expiré.

    Returns:
        Response: Message d'erreur indiquant que le token a expiré.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Gère les erreurs lorsque l'utilisateur fournit un token JWT révoqué.

    Returns:
        Response: Message d'erreur indiquant que le token a été révoqué.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Gère les erreurs lorsque l'utilisateur doit fournir un token JW
    "frais" pour certaines actions sensibles.

    Returns:
        Response: Message d'erreur indiquant qu'un token frais est requis.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
