import os
import pymongo

MONGODB_URI = os.environ.get('MONGOHQ_URL', "")
client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()

def store_results(request_args, request_json, result_json, collection_name):
    collection = db[collection_name]
    result_dict = {"request_args":request_args,
                   "request_json":request_json,
                   "result_data":result_json,
                   "mongo_debug":{"MONGODB_URI":MONGODB_URI,
                                  "collection_object":str(collection),
                                  "previous_collection_count":collection.count(),
                                  }
                   }
    collection.insert(result_dict)
    result_dict['_id'] = str(result_dict['_id'])
    return result_dict

