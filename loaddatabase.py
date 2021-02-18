"""
File that initializes the database by inserting a few lines that can be used for testing.
"""

import os
from personalfinances import db, bcrypt

try:
    os.remove('personalfinances/site.db')
    print('previous DB file removed')
except:
    print('no previous file found')

db.create_all()
