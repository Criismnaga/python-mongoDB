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
        "name": "jiboia",
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

def get_plant_by_id(plant_id):
    if not ObjectId.is_valid(plant_id):
        return print("Plant does not exist")
    
    plant = collection.find_one(({"_id": ObjectId(plant_id)})) #ObjectId transforma a string em um identificador do mongo 

    if plant is None:
        return  print("No matching plant was found. Ensure the provided data is correct and try again")  
    else:
         return print(plant) 
    
def get_difficult_plants():
    plants = collection.find({"difficulty_level":{"$gt":2}}) #operador especial, greanter than equal
    print("List of plants difficult to cultivate:")
    for plant in plants:
        print(plant)

def delete_plant_by_id(plant_id): 
    delete_result = collection.delete_one({"_id": ObjectId(plant_id)})

    if delete_result.deleted_count > 0:
        print("Plant successfuly deleted.")
    else:
        print("No plant plants was modified, check the information e try again.")

def update_plant(plant_id, atribute_to_change ):
    filter = {"_id": ObjectId(plant_id)}
    new_data = {"$set": atribute_to_change} # set é o operador para atualizar atributos/campos especificos. 

    edited_plant = collection.update_one(filter,new_data)

    if edited_plant.modified_count>0:
        print("Plant successfuly updated.")
    else:
        print("No matching plant was found. Ensure the provided data is correct and try again")

#insert_plant(more_plants_2)
get_all_plants()
#get_difficult_plants()
#delete_plant_by_id("683dffb6a12912452a942404")
update_plant("683dffb6a12912452a942405", {"watering": 2, "difficulty_level": 3})
get_plant_by_id("683dffb6a12912452a942405")
