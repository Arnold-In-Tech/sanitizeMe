#!/usr/bin/env python3
from dotenv import load_dotenv
load_dotenv()

from flask import request, session, make_response, send_from_directory
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask import jsonify

from config import app, db, api
from models import Administrator, Donor, Charity, Story



class Home(Resource):
    def get(self):
        return send_from_directory(app.static_folder, "index.html")


@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, "index.html")


# Only the donor will be allowed to sign-up
class Signup(Resource):
    def post(self):
        json = request.get_json()

        firstname = json.get('firstname')
        lastname = json.get('lastname')
        username = json.get('username')
        password = json.get('password')
        anonymous = json.get('anonymous')
        amount = json.get('anonymous')

        new_user = Donor(
            firstname = firstname,
            lastname = lastname,
            username = username,
            anonymous = anonymous,
            amount = amount
            )
        new_user.password_hash = password
        try:
            db.session.add(new_user)
            db.session.commit()
            session['donor_id'] = new_user.id
            return new_user.to_dict(), 201
        except IntegrityError:
            return {'error': '422 Unprocessable Entity'}, 422


class CheckSession(Resource):
   def get(self):
        if session.get('administrator_id'):
            administrator = Administrator.query.filter(Administrator.id == session['administrator_id']).first()
            return administrator.to_dict(), 200
        elif session.get('donor_id'):
            donor = Donor.query.filter(Donor.id == session['donor_id']).first()
            return donor.to_dict(), 200
        else:
            return {'error': 'Unauthorized'}, 401


class Login(Resource):
    def post(self):

        username = request.get_json()['username']
        password = request.get_json()['password']
        # The fronted login should ask to select user_role (Admin/Donor)
        user_role = request.get_json()['user_role']

        if user_role.lower() == 'administrator':
            administrator = Administrator.query.filter(Administrator.username == username).first()
            if administrator:
                if administrator.authenticate(password):
                    session['administrator_id'] = administrator.id
                    return administrator.to_dict(), 200
            else:
                return {'error': 'Unauthorized: invalid username or password'}, 401

        elif user_role.lower() == 'donor':
            donor = Donor.query.filter(Donor.username == username).first()
            if donor:
                if donor.authenticate(password):
                    session['donor_id'] = donor.id
                    return donor.to_dict(), 200
            else:
                return {'error': 'Unauthorized: invalid username or password'}, 401


class Logout(Resource):
    def delete(self):
        if session['donor_id']:
            session['donor_id'] = None
            return {}, 204
        elif session['administrator_id']:
            session['administrator_id'] = None
            return {}, 204

        return {'error': 'Unauthorized: user is not logged in'}, 401


# List all charities
## GET /charities
class Charities(Resource):
    def get(self):
        charities = [charity.to_dict() for charity in Charity.query.all()]
        response = make_response(
            charities,
            200,
            {"Content-Type": "application/json"},
            )
        return response


# Create new charity
## POST /createCharities
class CreateCharities(Resource):
    def post(self):
        try:
            data = request.get_json()
            new_charity = Charity(
                title=data.get('title'),
                charity_description=data.get('charity_description'),
                organizer_name=data.get('organizer_name'),
                location=data.get('location'),
                administrator_id=data.get('administrator_id'),
                donor_id=data.get('donor_id'),
                status = data.get('status')
            )
            db.session.add(new_charity)
            db.session.commit()
            return new_charity.to_dict(), 201
        except IntegrityError:
            return {'error': 'Unprocessable Entity'}, 422


# Delete charity
## DELETE /charities/<int:id>
class CharityById(Resource):
    def get(self, id):
        charity = Charity.query.filter(Charity.id == id).first()
        if charity:
            response = make_response(
                [charity.to_dict()],
                200,
                {"Content-Type": "application/json"},
            )
            return response
        else:
            response = make_response(
                jsonify({"error": "Charities not found"}),
                404,
                {"Content-Type": "application/json"},
            )
            return response

    def delete(self, id):
        record = Charity.query.filter_by(id=id).first()
        if record:
            db.session.delete(record)
            db.session.commit()
            return {}, 204
        else:
            response = make_response(
                jsonify({"error": "Charity not found"}),
                404,
                {"Content-Type": "application/json"},
            )
            return response



# List of beneficiary stories for a specific charity
## GET /charityStories/<int:id>
class Charity_stories(Resource):
    def get(self, id):
        stories = Story.query.filter(Story.charity_id == id).all()
        if stories:
            response = make_response(
                [story.to_dict() for story in stories],
                200,
                {"Content-Type": "application/json"},
            )
            return response
        else:
            response = make_response(
                jsonify({"error": "Stories not found"}),
                404,
                {"Content-Type": "application/json"},
            )
            return response


# List of charities associated to a specific donor (myCharities)
## GET /myCharities/<int:id>
class Donor_charities(Resource):
    def get(self, id):
        charities = Charity.query.filter(Charity.donor_id == id).all()
        if charities:
            response = make_response(
                [charity.to_dict() for charity in charities],
                200,
                {"Content-Type": "application/json"},
            )
            return response
        else:
            response = make_response(
                jsonify({"error": "Charities not found"}),
                404,
                {"Content-Type": "application/json"},
            )
            return response


api.add_resource(Home, '/', endpoint='home' )
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(Charities, '/charities', endpoint = 'charities')
api.add_resource(CreateCharities, '/createCharities',  endpoint='createCharities')
api.add_resource(CharityById, '/charities/<int:id>',  endpoint='charityById')
api.add_resource(Charity_stories, '/charityStories/<int:id>', endpoint='Charity_stories')
api.add_resource(Donor_charities, '/myCharities/<int:id>', endpoint='Donor_charities')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
