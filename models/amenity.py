#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    # Establishes a relationship between amenities and places
    place_amenities = relationship("Place", secondary=place_amenity,
                                   viewonly=False)
