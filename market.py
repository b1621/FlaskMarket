from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# URI = Uniform Resource Identifiers
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024),
                            nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'
item1 = Item(name='a', price=20, barcode='123456789123', description='disc')

# with app.app_context():
        # db.create_all()
        # db.session.add(item1)
        # db.session.commit()

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    # items = [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]
    items = Item.query.all()
    return render_template('market.html', items=items)
