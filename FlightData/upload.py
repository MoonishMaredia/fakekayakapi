import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Create a new client and connect to the server
uri = "mongodb+srv://moonishm:wq5cPVT8zcpy361m@fakekayakcluster.jdydf.mongodb.net/?retryWrites=true&w=majority&appName=FakeKayakCluster"
# client = MongoClient(uri)
# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

def upload_json_array_to_mongodb(file_path, db_name, collection_name, chunk_size=5000, mongo_uri=uri):

    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=60000)
    db = client[db_name]
    collection = db[collection_name]

    with open(file_path, 'r') as file:
        json_array = json.load(file)

    if isinstance(json_array, list):
        # Split the data into chunks
        print(len(json_array))
        for i in range(0, len(json_array), chunk_size):
            chunk = json_array[i:i+chunk_size]
            try:
                collection.insert_many(chunk)
                print(f"Inserted {len(chunk)} documents into {collection_name}.")
            except Exception as e:
                print(f"Error inserting documents: {e}")
    else:
        print("The file does not contain a valid JSON array.")

    client.close()

# Example usage
file_path = 'output.txt'  # Replace with the path to your text file containing the JSON array
db_name = 'fakekayak'
collection_name = 'flights'

upload_json_array_to_mongodb(file_path, db_name, collection_name)
