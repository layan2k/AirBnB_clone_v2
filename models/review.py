#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
import models


class Review(BaseModel):
    """ Review classto store review information """
    if models.storage_t == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
