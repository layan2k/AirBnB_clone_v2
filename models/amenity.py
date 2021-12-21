#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


# class Amenity(BaseModel, Base):
#     """
#     this is a amenity class
#     """
#     __tablename__ = "amenities"

#     name = Column(String(128), nullable=False)
#     place_amenities = relationship("Place", secondary="place_amenity",
#                                    viewonly=False)
class Amenity(BaseModel, Base):
    """gives the amenities available for a place"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
