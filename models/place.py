#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, Integer, Float
from models.base_model import ForeignKey, relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer(), nullable=False, default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0)
    price_by_night = Column(Integer(), nullable=False, default=0)
    latitude = Column(Float())
    longitude = Column(Float())
    # amenity_ids = []
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")
    reviews = relationship("Review", back_populates="place")

    # @property
    # def reviews(self):
    #     """return the list of review instance linked"""
    #     from models import storage
    #     from models.review import Review
    #     reviews = []
    #     all = storage.all(Review)
    #     for key, value in all.items():
    #         if self.id == value.place_id:
    #             reviews.append(value)
    #     return reviews
