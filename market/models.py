from market import db, app
from market import bcrypt

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return f'Item {self.name}'

with app.app_context():
    # db.drop_all()
    db.create_all()
    
    # u1 = User("navid", "12345678", "123@1213.com")
    # with app.app_context():
    #     db.session.add(u1)
    #     db.session.commit()
    
    # i1 = Item('Iphone 10', 800,  "13146513165", "good quality")
    # with app.app_context():
    #     db.session.add(i1)
    #     db.session.commit()
    
    # i2 = Item('Laptop', 1000,  "231485522165", "good Laptop")
    # with app.app_context():
    #     db.session.add(i2)
    #     db.session.commit()
    
    # update an item
    # i2 = Item.query.get(2)
    # i2.owner = User.query.filter_by(username="navid").first().id
    # db.session.add(i2)
    # db.session.commit()
    
    # for getting item owner 
    # i = Item.query.filter_by(name="laptop").first()
    # i.owned_user ===> <user 1>