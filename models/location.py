class Location():
    def __init__(self, id, name, address, animal_id, employee_id):
        self.id = id
        self.name = name
        self.address = address
        self.animal_id = animal_id
        self.employee_id = employee_id
        self.animal = None
        self.employee = None