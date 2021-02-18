"""
File that implements the routes of the API (webservice).
"""

from flask import request, jsonify, abort
from personalfinances import app, db, bcrypt
# from personalfinances.models import
