from pymongo import MongoClient


client = MongoClient(
    "mongodb+srv://tcc_dev:123605@cluster0.b7x8w.mongodb.net/tcc_dev?retryWrites=true&w=majority")\
    .get_database()
