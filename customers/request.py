CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct",
      "email": "dogluvr420@cmail.com"
    },
    {
      "id": 2,
      "name": "Samantha Campbell",
      "address": "205 Lutie Street",
      "email": "camsam420@cmail.com"
    },
    {
      "id": 3,
      "name": "Jenny Craig",
      "address": "203 Lutie Street",
      "email": "jennycraig@fourtwenty.com"
    },
    {
      "id": 4,
      "name": "Simone Waverly",
      "address": "666 Lucifer Way",
      "email": "satanluvr66@fourtwenty.com"
    },
    {
      "email": "sandwich@bagel.com",
      "name": "Bagel Sandwich",
      "address": "637 bagel way",
      "id": 5
    },
    {
      "email": "blong@mymail.com",
      "name": "Brenda Long",
      "address": "222 idontknkow way",
      "id": 6
    },
    {
      "email": "depressedPoet@cmail.com",
      "name": "Sylvia Plath",
      "address": "444 Bell Jar Blvd",
      "id": 7
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer