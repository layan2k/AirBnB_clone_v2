#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    setattr(self, key, type(self))
                elif key == 'created_at' or key == 'updated_at':
                    """ Converts datetime string to datetime format """
                    setattr(self, key, datetime.strptime(value,
                                                         "%Y-%m-%dT%H:%M:%S.%f"
                                                         ))
                else:
                    setattr(self, key, value)
            if 'id' not in kwargs.keys():
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs.keys():
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs.keys():
                self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        # String representation doesn't include '__class__'
        dictionary = self.to_dict()
        dictionary.pop('__class__')
        return '[{}] ({}) {}'.format(cls, self.id, dictionary)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.unow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        # print(dictionary)
        dictionary['__class__'] = str(type(self).__name__)
        # dictionary.update({'__class__':(str(type(self)).split('.')[-1].split('\'')[0]})
        # print(dictionary)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """ Deletes instance from storage """
        from models import storage
        storage.delete(self)
