from json import json_util, ObjectId
import json

def query_data(client, db_name, collection_name, orig_code, dest_code):
    db = client[db_name]
    collection = db[collection_name]

    travel_key = orig_code + "_" + dest_code

    cursor = collection.find({"travel_key": travel_key})

    # Convert cursor to list of dictionaries and modify _id
    result = []
    for doc in cursor:
        # Convert _id to string
        if '_id' in doc:
            doc['_id'] = str(doc['_id'])
        result.append(doc)

    # Use json_util to handle MongoDB-specific types
    return json.loads(json_util.dumps(result))