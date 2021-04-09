LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive"
    },
    {
      "name": "The Devil's Kennel",
      "address": "666 Deddog way",
      "id": 3
    },
    {
      "id": 4,
      "name": "Dog Daze",
      "address": "321 eatMyShorts ave"
    },
    {
      "name": "Murfreesboro",
      "address": "678 Main St.",
      "id": 5
    }
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    
    requested_location = None
    
    for location in LOCATIONS:
        
        if location["id"] == id:
            requested_location = location
    
    return requested_location

