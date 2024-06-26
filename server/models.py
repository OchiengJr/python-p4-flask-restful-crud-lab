from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Example: Limited to 100 characters and not nullable
    image = db.Column(db.String)  # Example: Path to image file
    price = db.Column(db.Float, default=0.0)  # Example: Default price set to 0.0
    is_in_stock = db.Column(db.Boolean, default=True)  # Example: Default is True
    
    def __init__(self, name, image=None, price=0.0, is_in_stock=True):
        self.name = name
        self.image = image
        self.price = price
        self.is_in_stock = is_in_stock

    def __repr__(self):
        return f'<Plant {self.name} | In Stock: {self.is_in_stock}>'
    
    # Optional: Define serialize_rules to customize serialization
    # serialize_rules = ('-some_related_object',)
    
    # Optional: Add validation logic for fields
    # Example: Ensure name is unique or validate price range

    # Optional: Add indexes or constraints
    # Example: Indexing name for faster queries

# Example usage:
if __name__ == '__main__':
    # Create tables based on models
    with app.app_context():
        db.create_all()
