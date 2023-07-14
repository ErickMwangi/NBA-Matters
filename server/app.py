#!/usr/bin/env python3

from flask import Flask,jsonify,make_response,request
from flask_migrate import Migrate
from flask_restful import Api,Resource
from flask_cors import CORS
from models import db, Team, Player

app = Flask(
    __name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build'
)

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NBA2K23.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate=Migrate(app,db)
db.init_app(app)
api=Api(app)

class Index(Resource):
    def get(self):
        response_dict = {
            'welcome':"welcome to NBA2k23 players"
        }
        response=make_response(
            jsonify(response_dict),
            200
        )
        return response
api.add_resource(Index,"/")  

class Teams(Resource):
    def get(self):
        teams = Team.query.all()
        response_dict_list = [team.to_dict() for team in teams]
        response = make_response(jsonify(response_dict_list), 200)
        return response
    
    def post(self):
        data = request.get_json()
        new_team = Team(
            name=data.get('name'),
            title=data.get('title'),
            location=data.get('location')
        )
        db.session.add(new_team)
        db.session.commit()
        return make_response(jsonify(new_team.to_dict()), 201)

api.add_resource(Teams,"/teams")

class TeamById(Resource):
    def delete(self,id):
        tea = Team.query.filter_by(id=id).first()
        db.session.delete(tea)
        db.session.commit()
        response = make_response(jsonify({"message":"deleted successfully"}), 200)
        return response
api.add_resource(TeamById,"/team/<int:id>")    

class Players(Resource):
    def get(self):
        players = Player.query.all()
        response_dict_list = [player.to_dict() for player in players]
        response = make_response(jsonify(response_dict_list),200)
        return response
    
    def post(self):
        data = request.get_json()
        new_player = Player(
            name=data.get('name'),
            image=data.get('image'),
            team=data.get('team'),
            ranking=data.get('ranking')
        )
        db.session.add(new_player)
        db.session.commit()
        return make_response(jsonify(new_player.to_dict()), 201)


api.add_resource(Players,"/players")



if __name__ == '__main__':
    app.run(port=5555)
