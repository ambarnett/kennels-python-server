LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "64 Washington Heights"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "101 Penn Ave"
    }
]


def get_all_locations():
    """returns all locations

    Returns:
        list: all locations
    """
    return LOCATIONS


def get_single_location(id):
    """returns a single location found by it's id

    Args:
        id (int): the unique identifier of the object in the list

    Returns:
        object: location
    """
    requested_location = None
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location
