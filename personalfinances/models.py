"""
File that contains the database modeling using SQLAlchemy.
SQLAlchemy implements the object-relational mapping (ORM) concept.
Using this approach, each database table becomes a Python class,
each column/field in the database becomes a property of a class in Python,
and each row in the database becomes an object in Python.

More info: https://flask-sqlalchemy.palletsprojects.com/en/
"""

from datetime import datetime
from personalfinances import db
