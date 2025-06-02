from pymongo import MongoClient
from bson import ObjectId #binary JSON

client = MongoClient("mongodb://root:senha123@localhost:27017/")
db=client["plant_db"]
collection = db["plant"]

#print("DB and collection successfuly created")

document = {
    "name": "monstera",
    "watering": 3,
    "difficulty_level": 1,
}
#insere um
#collection.insert_one(document)

more_plants = [
    {
        "name": "zamiocuca",
        "watering": 1,
        "difficulty_level": 1,
    },
    {
        "name": "maranta turtle",
        "watering": 2,
        "difficulty_level": 3,
        "description": "Very sensitive to water and sunlight be careful"
    },
]
#insere várias
#collection.insert_many(more_plants)

more_plants_2 = [
    {
        "name": "juboia",
        "watering": 1,
        "difficulty_level": 1,
    },
    {
        "name": "cacto",
        "watering": 1,
        "difficulty_level":2,
        "description": "Very sensitive to water and sunlight be careful",
        "weather": "hot and dry"
    },
]

def insert_plant(plant_json):
    new_plant = plant_json
    insert_result = collection.insert_many(new_plant)

    inserted_plants = collection.find({"_id":{"$in": insert_result.inserted_ids}})

    print("List of inserted plants:")
    for plant in inserted_plants:
        print(plant)

def get_all_plants():
    plants = collection.find()
    print("List of all plants:")
    for plant in plants:
        print(plant)

def get_difficult_plants():
    plants = collection.find({"difficulty_level":{"$gt":2}}) #operador especial, greanter than equal
    print("List of plants difficult to cultivate:")
    for plant in plants:
        print(plant)

def delete_plant_by_id(plant_id): 
    detele_duplicated = collection.delete_one({"_id": ObjectId(plant_id)})

    if detele_duplicated.deleted_count > 0:
        print("Plant successfuly deleted.")
    else:
        print("There wasn't any plant with _id.")


#insert_plant(more_plants_2)
get_all_plants()
get_difficult_plants()
#delete_plant_by_id("683dffb6a12912452a942404")


