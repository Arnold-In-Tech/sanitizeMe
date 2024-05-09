import os
from config import db, app
from models import Administrator, Donor, Charity, Story
from faker import Faker
import bcrypt


fake = Faker()

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
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            username='admin',
            _password_hash=bcrypt.generate_password_hash('password').decode('utf-8')
        )
        db.session.add(admin)
        db.session.commit()

    def seed_charity():
        print("Creating charity instances...")
        # Assuming you have only one administrator, get its ID
        admin = db. session.query(Administrator).first()
        admin_id = admin.id if admin else None

        for _ in range(10):  
            charity = Charity(
                title=fake.company(),
                charity_description=fake.text(),
                organizer_name=fake.name(),
                location=fake.city(),
                period=fake.date_between(start_date='-1y', end_date='today'),
                status=fake.random_element(elements=('Active', 'Inactive', 'Closed')),
                administrator_id=admin_id, # ID of the single administrator
            )
            db.session.add(charity)
        db.session.commit()

    def seed_donor():
        print("Creating donor instances...")
        for _ in range(30):
            donor = Donor(
                firstname=fake.first_name(),
                lastname=fake.last_name(),
                username=fake.user_name(),
                _password_hash=bcrypt.generate_password_hash('password').decode('utf-8'), 
                anonymous=fake.boolean(), 
                amount=fake.random_int(min=100, max=10000)  
            )
            db.session.add(donor)
        db.session.commit()

    def seed_story():
        print("Creating story instances...")

        charity = db.session.query(Charity).first()
        if charity:
            charity_id = charity.id
        else:
            print("No charities found. Please add at least one charity before seeding stories.")
            exit(1)
        for _ in range(10):
            story = Story(
                beneficiary_name=fake.name(),
                beneficiary_story=fake.text(),
                charity_id=charity_id
            )
            db.session.add(story)
        db.session.commit()

    seed_admin()
    seed_charity()
    seed_donor()
    seed_story()

    print('Complete!')

