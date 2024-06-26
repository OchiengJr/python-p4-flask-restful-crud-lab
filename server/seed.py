#!/usr/bin/env python3

from app import app
from models import db, Plant

if __name__ == '__main__':
    with app.app_context():
        try:
            # Delete existing plants
            Plant.query.delete()

            # Create new plant instances
            aloe = Plant(
                name="Aloe",
                image="./images/aloe.jpg",
                price=11.50,
                is_in_stock=True,
            )

            zz_plant = Plant(
                name="ZZ Plant",
                image="./images/zz-plant.jpg",
                price=25.98,
                is_in_stock=False,
            )

            # Add plants to the session
            db.session.add(aloe)
            db.session.add(zz_plant)

            # Commit the changes
            db.session.commit()
        
        except Exception as e:
            print(f"An error occurred: {e}")
            db.session.rollback()  # Rollback changes in case of error
