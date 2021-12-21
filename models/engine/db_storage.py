#!/usr/bin/python3
""" Database storage engine """
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """ Storage class """

    __engine = None
    __session = None

    def __init__(self):
        """ Init """
        # Create engine using environmental variables
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(
                                                getenv('HBNB_MYSQL_USER'),
                                                getenv('HBNB_MYSQL_PWD'),
                                                getenv('HBNB_MYSQL_HOST'),
                                                getenv('HBNB_MYSQL_DB'),
                                                pool_pre_pring=True
                                      ))

        # Drop all tables if in test environment
        if getenv('HBNB_ENV') == 'test':
            from models.base_model import Base
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary of all objects in database
            Will return a dictionary of all objects of one class if specified
        """
        self.cls = cls
        dictionary = {}

        # Get a list of all objects, or a list of all objects of one class
        if cls is None:
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review
            from models.place import Place
            objects = self.__session.query(State).all()
            objects = objects + self.__session.query(City).all()
            objects = objects + self.__session.query(Place).all()
            objects = objects + self.__session.query(User).all()
            objects = objects + self.__session.query(Review).all()
        else:
            objects = self.__session.query(cls).all()

        # Build dictionary from list. Key format is <Class name>.<object id>
        for obj in objects:
            key = obj.to_dict()['__class__'] + "." + obj.to_dict()['id']
            dictionary[key] = obj

        return dictionary

    def new(self, obj):
        """ Add object to current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from current database session if obj is not None """
        if obj is not None:
            self.__session.query(type(obj).__name__).\
                filter(type(obj).__name__.id == obj.id).\
                delete(synchronize_session=False)

    def reload(self):
        """ Creates session and all tables in database """
        from models.base_model import Base, BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place

        # Create all tables in the database
        Base.metadata.create_all(self.__engine)

        # Create current session
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
