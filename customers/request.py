import json
import sqlite3
from models import Customer
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
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor =conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.email,
            a.address
        FROM customer a
          """)
        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['email'], row['address'])
            customers.append(customer.__dict__)
        return json.dumps(customers)

def get_single_customer(id):
  with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.email,
            a.address
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        customer = Customer(data['id'], data['name'], data['email'],
                            data['address'])

        return json.dumps(customer.__dict__)

def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)

    
def create_customer(customer):
  max_id = CUSTOMERS[-1]["id"]
  new_id = max_id + 1
  customer["id"] = new_id
  CUSTOMERS.append(customer)
  return customer

def delete_customer(id):
  customer_index = -1
  for index, customer in enumerate(CUSTOMERS):
      if customer["id"] == id:
        customer_index = index
  if customer_index >= 0:
    CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
  for index, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
        CUSTOMERS[index] = new_customer
        break 