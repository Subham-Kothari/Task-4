# Name : Subham Kothari
# Date : 08-08-2025
# app.py


from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = {}

# Home route (optional)
@app.route("/")
def home():
    return "User Management API is running!"

# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# Get a single user by ID
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user}), 200
    return jsonify({"error": "User not found"}), 404

# Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user_id = data.get("id")
    name = data.get("name")

    if not user_id or not name:
        return jsonify({"error": "Missing 'id' or 'name'"}), 400

    if user_id in users:
        return jsonify({"error": "User with this ID already exists"}), 409

    users[user_id] = {"name": name}
    return jsonify({"message": "User added", "user": {user_id: users[user_id]}}), 201

# Update an existing user
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    name = data.get("name")

    if not name:
        return jsonify({"error": "Missing 'name' field"}), 400

    users[user_id]["name"] = name
    return jsonify({"message": "User updated", "user": {user_id: users[user_id]}}), 200

# Delete a user
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": {user_id: deleted_user}}), 200

if __name__ == "__main__":
    app.run(debug=True)
