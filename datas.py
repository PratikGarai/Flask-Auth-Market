items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500, 'description':"An ordinary phone with a lot of extraordinary features"},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900, 'description':"An ordinary laptop with a lot of extraordinary features"},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150, 'description':"An ordinary keyboard with a lot of extraordinary features"}
]

from market import Item, db

def generate_Items():
    for it in items :
        item = Item(name=it['name'], barcode=it['barcode'], price=it['price'], description=it['description'])
        db.session.add(item)
        db.session.commit()

    print(Item.query.all())