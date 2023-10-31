from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Team(db.Model, SerializerMixin):
    __tablename__ = "teams"
    serialize_rules = ("-team_player", "-team_player.team")
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    title = db.Column(db.String)
    location = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    team_player = db.relationship("Team_player", backref="team")

class Player(db.Model, SerializerMixin):
    __tablename__ = "players"
    serialize_rules = ("-team_player",)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    team = db.Column(db.String)
    image = db.Column(db.String)
    ranking = db.Column(db.String)
    mvp = db.Column(db.String)
    team_player = db.relationship("Team_player", backref="player")

class Team_player(db.Model, SerializerMixin):
    __tablename__ = "team_players"
    serialize_rules = ("-team.team_player", "-player.team_player")
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
