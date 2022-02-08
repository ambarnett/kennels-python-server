EMPLOYEES = [
    {
        "id": 1,
        "name": "Bob"
    },
    {
        "id": 2,
        "name": "Jack"
    }
]


def get_all_employees():
    """returns all employees

    Returns:
        list: all employees
    """
    return EMPLOYEES


def get_single_employee(id):
    """returns a single employee found by their id

    Args:
        id (int): the unique id of an employee

    Returns:
        object: employee
    """
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
