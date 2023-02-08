#!/usr/bin/python3
"""
Module defines amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenities user can choose from to offer at its place"""
    name = ""
