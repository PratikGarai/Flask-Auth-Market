from market import db
from market import bcrypt
from market import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1500)
    items = db.relationship('Item', backref='user', lazy=True)

    def __repr__(self):
        return self.username

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain):
        self.password_hash = bcrypt.generate_password_hash(plain).decode('utf-8')

    def check_password(self, passc):
        return bcrypt.check_password_hash(self.password_hash, passc)


class Item(db.Model) :
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return self.name