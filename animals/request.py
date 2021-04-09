ANIMALS = [
    {
      "id": 1,
      "name": "Doodles",
      "breed": "Poodle",
      "customerId": 1,
      "locationId": 4
    },
    {
      "id": 2,
      "name": "Charlie",
      "breed": "Black and Tan coonhound",
      "locationId": 2,
      "customerId": 2
    },
    {
      "id": 3,
      "name": "LunaBean",
      "breed": "Husky/Lab mix",
      "customerId": 2,
      "locationId": 2
    },
    {
      "id": 4,
      "name": "Evee",
      "breed": "Collie",
      "customerId": 3,
      "locationId": 3
    },
    {
      "id": 6,
      "name": "Molly",
      "breed": "lab/retriever mix",
      "customerId": 2,
      "locationId": 2
    },
    {
      "name": "Rocco",
      "breed": "Chihuahua",
      "locationId": 2,
      "customerId": 1,
      "id": 7
    },
    {
      "id": 8,
      "name": "Lucy",
      "breed": "Golden doodle",
      "locationId": 3,
      "customerId": 7
    }
]

def get_all_animals():
    return ANIMALS

# Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal