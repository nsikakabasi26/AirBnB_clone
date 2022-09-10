#!/usr/bin/python3
""" A module that defines city"""
from models.base_model import BaseModel


class City(BaseModel):
    """class to create a city"""
    state_id = ""
    name = ""
