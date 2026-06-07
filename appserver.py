
import os
from config import config


os.chdir(config["appPath"])

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = "<html><div>Hello World</div></html>"

# Define a route for the root URL ("/")
@app.route("/", methods=["GET"])
def index():
    return data

# Define a route for a specific resource ("/api/resource")
@app.route("/api/resource", methods=["GET"])
def get_resource():
    return jsonify({"resource": "This is a sample resource"})

# Define a route for creating a new resource ("/api/resource", methods=["POST"])
@app.route("/api/resource", methods=["POST"])
def create_resource():
    data = request.get_json()
    return jsonify({"message": "Resource created successfully", "data": data})

# Define a route for updating an existing resource ("/api/resource/<id>", methods=["PUT"])
@app.route("/api/resource/<int:id>", methods=["PUT"])
def update_resource(id):
    data = request.get_json()
    return jsonify({"message": "Resource updated successfully", "data": data})

# Define a route for deleting a resource ("/api/resource/<id>", methods=["DELETE"])
@app.route("/api/resource/<int:id>", methods=["DELETE"])
def delete_resource(id):
    return jsonify({"message": "Resource deleted successfully"})


if __name__ == "__main__":
    port = config["thisAppPort"]
    app.run(debug=True, port=port)
    print("Server started on port", port)





	





