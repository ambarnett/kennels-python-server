ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
    }
]


def get_all_animals():
    """returns all animals 

    Returns:
        list: all animals
    """
    return ANIMALS


# Function with a single parameter
def get_single_animal(id):
    """returns a single animal that is found by its id

    Args:
        id (int): the id of the animal

    Returns:
        object: animal
    """
    # Variable to hold the found animal, if it exisits
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops I used in JavaScript
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal
