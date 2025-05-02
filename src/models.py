from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()


user_planet_association =db.Table(
    'user_planet',
    db.Column('user_id', Integer, db.ForeignKey(
        'users.id'), primary_key=True),

    db.Column('planet_id', Integer, db.ForeignKey(
        'planets.id'), primary_key=True),
              
)

user_warrior_association =db.Table(
    'user_warrior',
    db.Column('user_id', Integer, db.ForeignKey(
        'users.id'), primary_key=True),

    db.Column('warrior_id', Integer, db.ForeignKey(
        'warriors.id'), primary_key=True),
              
)

user_spaceship_association =db.Table(
    'user_spaceship',
    db.Column('user_id', Integer, db.ForeignKey(
        'users.id'), primary_key=True),

    db.Column('spaceship_id', Integer, db.ForeignKey(
        'spaceships.id'), primary_key=True),
              
)




class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    last_name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    planets: Mapped[List['Planet']]=relationship(
        secondary=user_planet_association,
        back_populates='users'
    )

    warriors: Mapped[List['Warrior']]=relationship(
        secondary=user_warrior_association,
        back_populates='users'
    )

    spaceships: Mapped[List['Spaceship']]=relationship(
        secondary=user_spaceship_association,
        back_populates='users'
    )

    
class Planet(db.Model):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    size: Mapped[str] = mapped_column(nullable=False)

    users: Mapped[List['User']]=relationship(
        secondary=user_planet_association,
        back_populates='planets'
    )
   

class Warrior(db.Model):
    __tablename__ = "warriors"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    last_name: Mapped[str] = mapped_column(String(250), nullable=False)
    race: Mapped[str] = mapped_column(String(250), nullable=False)

    users: Mapped[List['User']]=relationship(
        secondary=user_warrior_association,
        back_populates='warriors'
    )
   

class Spaceship(db.Model):
    __tablename__ = "spaceships"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    color: Mapped[str] = mapped_column(String(250), nullable=False)
    size: Mapped[str] = mapped_column(nullable=False)

    users: Mapped[List['User']]=relationship(
        secondary=user_spaceship_association,
        back_populates='spaceships'
    )
    



