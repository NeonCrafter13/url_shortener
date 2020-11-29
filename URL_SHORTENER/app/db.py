import pymongo
mongocontainer = "mongo-container"
myclient = pymongo.MongoClient(f"mongodb://{mongocontainer}:27017/")

mydb = myclient["urls"]

urls = mydb["urls"]

urls.create_index("token")

def create_short(token: str, url:str):
    myquery = {"token": token}
    mydoc = urls.find(myquery)

    for _ in mydoc:
        return "Token already in use"

    mydict = {"token": token, "url": url}

    x = urls.insert_one(mydict)
    return True

def get_url(token: str) -> str:
    myquery = {"token" : token}
    mydoc = urls.find(myquery)

    for i in mydoc:
        return i["url"]
    return False