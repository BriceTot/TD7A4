# app.py

# Import the Flask module
from flask import Flask

# Import the PyMongo module to interact with MongoDB
from pymongo import MongoClient

# Create a Flask application instance
app = Flask(__name__)

# Connect to the MongoDB container
# We use the hostname "mongodb" to connect to the MongoDB container
# as it will be automatically resolved to the IP address of the container
# within the Docker network
client = MongoClient("mongodb://mongodb:27017/")

# Get a reference to the test_database
db = client.test_database

# Get a reference to the test_collection
collection = db.test_collection

# Define the route for the index page
@app.route("/")
def index():
    #insert a document in the collection
    collection.insert_one({'this is a new insert' : 18})

    # Fetch a single document from the test_collection
    data = collection.find_one()

    #read a file
    file1 = open("volumeBenefits.txt","r")
    text = file1.read()

    #create the text to show to the user
    final_text=str(data)+"\n\n"+text
    
    # Return the fetched data as a string
    return final_text

# Start the Flask application if this file is being executed as the main script
if __name__ == "__main__":
    # Start the Flask application, listening on all available interfaces
    app.run(host="0.0.0.0")
