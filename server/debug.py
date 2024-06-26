#!/usr/bin/env python3

from app import app, db
from models import Plant
import ipdb  # Import ipdb for debugging

if __name__ == '__main__':
    # Initialize the application context
    with app.app_context():
        # Ensure the database is initialized and up-to-date
        db.init_app(app)
        # Optionally, migrate the database to the latest version
        # migrate = Migrate(app, db)
        
        # Insert a breakpoint for debugging
        ipdb.set_trace()
        
        # Example: Querying and interacting with the database
        # Example usage:
        plants = Plant.query.all()
        print("All plants in the database:")
        for plant in plants:
            print(f"{plant.id}: {plant.name}")
