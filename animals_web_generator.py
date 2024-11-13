import json


def load_data(file_path):
    """Loads the JSON file with animal data."""
    with open(file_path, 'r') as handle:
        return json.load(handle)


def generate_animal_data_string(animals_data):
    """Generates a string with animal data formatted in HTML."""
    output = ''  # Initialize an empty string to store the HTML content.

    for animal in animals_data:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        locations = animal.get("locations", [])
        animal_type = animal.get("characteristics", {}).get("type")

        # Create HTML for each animal inside <li> tags.
        output += '<li class="cards__item">'

        if name:
            output += f"Name: {name}<br/>\n"
        if diet:
            output += f"Diet: {diet}<br/>\n"
        if locations:
            output += f"Location: {locations[0]}<br/>\n"  # Display the first location
        if animal_type:
            output += f"Type: {animal_type}<br/>\n"

        output += '</li>'  # Close the <li> tag

    return output


def update_template_with_animal_data(animals_data, template_path, output_path):
    """Reads the template, replaces the placeholder, and writes the updated content to a new file."""

    # Read the content of the template HTML file
    with open(template_path, 'r') as file:
        template_content = file.read()

    # Generate the HTML for the animal data
    animal_data_string = generate_animal_data_string(animals_data)

    # Replace the placeholder with the generated animal data
    updated_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_data_string)

    # Write the updated content to the new HTML file (animals.html)
    with open(output_path, 'w') as file:
        file.write(updated_html_content)

    print(f"The animal data has been added to {output_path}")


# Load data from the JSON file
animals_data = load_data('animals_data.json')

# Define the template path and the output path for the final HTML file
template_path = 'animals_template.html'
output_path = 'animals.html'

# Update the template with the animal data and write to a new file
update_template_with_animal_data(animals_data, template_path, output_path)
