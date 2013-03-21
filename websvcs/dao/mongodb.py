from tornado.options import options, logging
import tornado.web
from tornado.web import RequestHandler, HTTPError

from pymongo import Connection
import json
from bson import objectid

class MongoDbHandler(RequestHandler):
    def get(self, identity):
        logging.info("MongoDbHandler.get(%s)" % identity)

        ids = identity.split("/")
        if len(ids) == 1:
            args = self.request.arguments
            query = {}

            normalize_fn = lambda x: x.lower()

            for key in args.keys():
                iargs = args[key]
                if len(iargs) == 1:
                    query[key] = normalize_fn(args[key][0])
                else:
                    query[key] = {"$in": map(normalize_fn, args[key])}

            collection = open_collection(ids[0])
            json_items = []

            for idx, item in enumerate(collection.find(query)):
                json_item = jsonable_item(item)
                json_item["uri"] = self.request.uri + "/" + json_item["id"]
                json_items.append(json_item)

            json_items.append({
                "First Name": "Hector",
                "Last Name": "Rovira",
                "Birth Date": "03/14/13",
                "status": "incomplete"
            })

            self.write({ "items": json_items })
            self.set_status(200)
            return

        if len(ids) == 2:
            collection = open_collection(ids[0])
            item = collection.find_one({"_id": objectid.ObjectId(ids[1]) })
            if not item is None:
                json_item = jsonable_item(item)
                json_item["uri"] = self.request.uri
                self.write(json_item)
                self.set_status(200)
                return

        self.set_status(404)

    def post(self, identity):
        logging.info("MongoDbHandler.post(%s)" % identity)

        ids = identity.split("/")
        if len(ids) <= 0: raise HTTPError(401)

        stored_item = json.loads(self.request.body)
        # Figure out issue where label is getting set as an array
        labels = stored_item["label"]
        if not labels is None and type(labels) is list: stored_item["label"] = labels[0]

        collection = open_collection(ids[0])
        insert_id = str(collection.insert(stored_item))

        self.write({ "id": insert_id, "uri": self.request.uri + "/" + insert_id })
        self.set_status(200)

    def put(self, identity):
        logging.info("MongoDbHandler.put(%s)" % identity)

        ids = identity.split("/")
        if len(ids) <= 0: raise HTTPError(401)

        stored_item = json.loads(self.request.body)

        # Figure out issue where label is getting set as an array
        labels = stored_item["label"]
        if not labels is None and type(labels) is list: stored_item["label"] = labels[0]

        update_id = ids[1]
        collection = open_collection(ids[0])
        collection.update({ "_id": objectid.ObjectId(update_id) }, stored_item )

        self.write({ "id": update_id, "uri": self.request.uri + "/" + update_id })
        self.set_status(200)

def jsonable_item(item):
    json_item = {}
    for k in item.iterkeys():
        if k == "_id":
            json_item["id"] = str(item["_id"])
        elif "[]" in k:
            json_item[k.replace("[]", "")] = item[k]
        else:
            json_item[k] = item[k]
    return json_item

def open_collection(collection_name):
    connection = Connection(options.mongo_uri)
    db = connection["proforma"]
    return db[collection_name]