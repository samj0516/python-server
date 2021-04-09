EMPLOYEES = [
    {
      "id": 1,
      "name": "Carly Simon",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Brad Pitt",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Penelope Featherbottom",
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Willie Wonka",
      "locationId": 2
    },
    {
      "name": "Bethany Winkelvoss",
      "locationId": 2,
      "id": 5
    },
    {
      "name": "Minnie Mouse",
      "locationId": 4,
      "id": 6
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee