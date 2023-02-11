#!/usr/bin/python3
"""
Defines review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Reviews from users about a place"""
    place_id = ""
    user_id = ""
    text = ""
