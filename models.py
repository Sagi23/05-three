from datetime import date
import os
from sqlalchemy import Column, DateTime, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from env.config import database_setup


database_path_local = f'postgresql://{database_setup["user_name"]}:{database_setup["password"]}@{database_setup["url"]}/{database_setup["database_name"]}'

database_path = os.environ.get('DATABASE_URL', "postgres://{}:{}@{}/{}".format(database_setup["user_name"], database_setup["password"], database_setup["url"], database_setup["database_name"]))


db = SQLAlchemy()

def setup_db(app, database_path=database_path):
  """binds a flask application and a SQLAlchemy service"""
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  ctx = app.app_context()
  ctx.push()
  db.init_app(app)
  db.create_all()


def db_drop_and_create_all():
    """drops the database tables and starts fresh
    can be used to initialize a clean database
    """
    db.drop_all()
    db.create_all()
    db_init_records()


def db_init_records():
    """this will initialize the database with some test records."""

    new_actor = (Actor(
        name = "Brad Pitt",
        gender = "Male",
        age = 25
        ))

    new_movie = (Movie(
        title = "Fight Club",
        release_date = date.today()
        ))

    new_actor.insert()
    new_movie.insert()
    db.session.commit()



class Actor(db.Model):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            }


class Movie(db.Model):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(DateTime)

    def __init__(self, title , release_date):
        self.title  = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            "id": self.id,
            "title ": self.title,
            "release_date": self.release_date,
            }