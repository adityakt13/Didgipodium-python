inventory = []
inventory.append({
    'S.No': 1,
    'Item Name':'Electric Bulb',
    'Item Id' : 16521,
    'Cost Per Item': 60.00,
    'Tax %' : 5   
})
inventory.append({
    'S.No': 2,
    'Item Name':'Ups - System',
    'Item Id' : 26521,
    'Cost Per Item': 5000.00,
    'Tax %' : 10
})
inventory.append({
    'S.No': 3,
    'Item Name':'Electric Fan',
    'Item Id' : 26522,
    'Cost Per Item': 1000.00,
    'Tax %' : 8
})
inventory.append({
    'S.No': 4,
    'Item Name':'Electric Charger',
    'Item Id' : 26523,
    'Cost Per Item': 500.00,
    'Tax %' : 10
})
inventory.append({
    'S.No': 5,
    'Item Name':'Electric Motor',
    'Item Id' : 26524,
    'Cost Per Item': 2000.00,
    'Tax %' : 15
})
print(inventory)
def bill (order):
    total_bill = 0
    for entry in order:
        id = entry[0]
        qty = entry[1]
        total_bill += calculate (id, qty)
    return total_bill

def calculate (id,qty):
    for record in inventory:
        if record ['Item Id'] == id:
            amt = record ['Cost Per Item' ] * qty
            tax = amt * record ['Tax %']/ 100
            return amt + tax
    return 0

# taking input 
n = int(input('>>>'))
orders = [list(map(int,input ('>').split()) for i in range (n))]
print(orders)

total = bill (orders)
print(f"Amount = {total}")
inventory.extend