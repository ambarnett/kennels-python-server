CUSTOMERS = [
    {
        "id": 1,
        "name": "Sally"
    },
    {
        "id": 2,
        "name": "Joe"
    }
]

def get_all_customers():
    """returns all customers

    Returns:
        list: customers
    """
    return CUSTOMERS

def get_single_customer(id):
    """returns single customer based 

    Args:
        id ([type]): [description]

    Returns:
        [type]: [description]
    """
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    
    return requested_customer
