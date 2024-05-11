from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db, bcrypt

class Administrator(db.Model, SerializerMixin):
    __tablename__ = 'administrators'
    serialize_rules = ('-charities.administrator',)

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, unique=True, nullable=False)
    lastname = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    charities = db.relationship('Charity', back_populates="administrator")	
    
    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f'Administrator {self.username}, Firstname {self.firstname}, Lastname {self.lastname}, ID: {self.id}'


class Donor(db.Model, SerializerMixin):
    __tablename__ = 'donors'
    serialize_rules = ('-charities.donor',)

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, unique=True, nullable=False)
    lastname = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    anonymous = db.Column(db.Boolean, default=False, nullable=False)
    amount = db.Column(db.Integer, default=0)

    charities = db.relationship('Charity', back_populates="donor")	

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f'Donor {self.username}, Firstname {self.firstname}, Lastname {self.lastname}, ID: {self.id}, Amount: {self.amount}'


class Charity(db.Model, SerializerMixin):
    __tablename__ = 'charities'
    serialize_rules = ('-administrator.charities', '-donor.charities', '-stories.charity',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    charity_description =  db.Column(db.String, nullable=False)
    organizer_name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    period =  db.Column(db.String, nullable=False)
    administrator_id = db.Column(db.Integer, db.ForeignKey('administrators.id'))  
    donor_id = db.Column(db.Integer, db.ForeignKey('donors.id'))  
    status = db.Column(db.String, nullable=False)
    total_amount = db.Column(db.Integer, default=0)

    administrator = db.relationship('Administrator', back_populates="charities")
    donor = db.relationship('Donor', back_populates="charities")
    stories = db.relationship("Story", back_populates="charity")


class Story(db.Model, SerializerMixin):
    __tablename__ = "stories"

    serialize_rules = ('-charities.story',)
    # serialize_only = ('id', 'beneficiary_name', 'beneficiary_story', 'charity.title',)
    # serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    beneficiary_name = db.Column(db.String)
    beneficiary_story = db.Column(db.String)
    charity_id = db.Column(db.Integer, db.ForeignKey("charities.id"))

    charity = db.relationship("Charity", back_populates="stories")

    def __repr__(self):
        return f"<Story ({self.id}) of {self.charity} by  {self.beneficiary_name}: {self.beneficiary_story}>"