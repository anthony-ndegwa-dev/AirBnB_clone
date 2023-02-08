#!/usr/bin/python3
"""User creation class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Attributes for user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
