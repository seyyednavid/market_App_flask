from market import db
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    
    def __init__(self, name, price,barcode, description):
        self.name = name
        self.price = price
        self.barcode = barcode
        self.description = description
        
    # return in object form => Ttem.query.all() like [Item iphone, Item Laptop]
    def __repr__(self):
        return f'Item {self.name}' 