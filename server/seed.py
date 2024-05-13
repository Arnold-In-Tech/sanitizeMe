import os
from config import db, app, bcrypt
from models import Administrator, Donor, Charity, Story
from faker import Faker
import random
from datetime import datetime

fake = Faker()
Faker.seed(42)

with app.app_context():

    print('Deleting existing data...')
    Story.query.delete()
    db.session.commit()

    Charity.query.delete()
    db.session.commit()

    Donor.query.delete()
    db.session.commit()

    Administrator.query.delete()
    db.session.commit()

    def seed_admin():
        print("Creating admin instances...")
        admin = Administrator(
            firstname=fake.unique.first_name(),
            lastname=fake.unique.last_name(),
            username='admin',
            _password_hash=bcrypt.generate_password_hash('password').decode('utf-8')
        )
        db.session.add(admin)
        db.session.commit()

    def seed_charity():
        print("Creating charity instances...")
        # Assuming you have only one administrator, get its ID
        admin = db.session.query(Administrator).first()
        admin_id = admin.id if admin else None

        donors = db.session.query(Donor).all()

        for _ in range(10):

            index = random.randint(0,len(donors)-1)
            don_id = donors[index].id if donors else None

            charity = Charity(
                title=fake.company(),
                charity_description=fake.text(),
                organizer_name=fake.name(),
                location=fake.city(),
                period= str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")), 
                status=fake.random_element(elements=('Active', 'Inactive', 'Closed')),
                total_amount=fake.pyint(5000,500000),
                administrator_id=admin_id, # ID of the single administrator
                donor_id = don_id
            )
            db.session.add(charity)
        db.session.commit()

    def seed_donor():
        print("Creating donor instances...")
        for _ in range(30):
            donor = Donor(
                firstname=fake.unique.first_name(),
                lastname=fake.unique.last_name(),
                username=fake.user_name(),
                _password_hash=bcrypt.generate_password_hash('password').decode('utf-8'), 
                anonymous=fake.boolean(), 
                amount=fake.random_int(min=100, max=10000)  
            )
            db.session.add(donor)
        db.session.commit()

    def seed_story():
        print("Creating story instances...")
        charities = db.session.query(Charity).all()
        for _ in range(50):
            index = random.randint(0,len(charities)-1)
            char_id = charities[index].id if charities else None

            story = Story(
                beneficiary_name=fake.name(),
                beneficiary_story=fake.text(),
                charity_id=char_id
            )
            db.session.add(story)
        db.session.commit()

    seed_admin()
    seed_donor()
    seed_charity()
    seed_story()

    print('Complete!')