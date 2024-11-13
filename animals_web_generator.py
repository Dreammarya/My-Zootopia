import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animal_data(animals_data):
    for animal in animals_data:
        # Retrieve values safely, using get to handle missing fields
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        locations = animal.get("locations", [])
        animal_type = animal.get("characteristics", {}).get("type")

        # Print each field only if it exists
        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if locations:
            print(f"Location: {locations[0]}")  # Print the first location if it exists
        if animal_type:
            print(f"Type: {animal_type}")
        print()  # Blank line between animals for readability


# Load data from the JSON file and print the output
animals_data = load_data('animals_data.json')
print_animal_data(animals_data)