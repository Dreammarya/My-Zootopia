import json


def load_data(file_path):
    with open(file_path, "r") as fileobj:
        data = json.loads(fileobj.read())
    return data


def print_animal_data(animals_data):
    for animal in animals_data:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        locations = animal.get("locations", [])
        animal_type = animal.get("characteristics", {}).get("type")

        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if locations:
            print(f"Location: {locations[0]}")
        if animal_type:
            print(f"Type: {animal_type}")
        print()

animals_data = load_data("animals_data.json")
print_animal_data(animals_data)
