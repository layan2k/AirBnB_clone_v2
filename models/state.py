#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    # Establishes a relationship between Cities and States
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """ Returns a dictionary of all cities with a state_id
            matching this instance's id
        """
        from models.__init__ import storage
        from models.city import City
        # Create empty list
        c_dict = []

        # Fill with all cities whose state_id match this instance's id
        for key, value in storage.all(City).items():
            if value.to_dict()['state_id'] == self.id:
                c_dict.append(value)

        c_dict.sort(key=lambda x: x.name)

        return c_dict
