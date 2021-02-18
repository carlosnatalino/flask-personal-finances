"""
Initialization file.
"""

from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from sqlalchemy import event

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'  # change and create your own key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# see more at: https://flask.palletsprojects.com/en/1.1.x/config/#SEND_FILE_MAX_AGE_DEFAULT
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # option to be used during the development phase, prevents caching

app.config['SQLALCHEMY_ECHO'] = True  # option for debugging -- should be set to False for production

# this line is to be used if you are considering uploading large files
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


# this function activates stricter handling foreign keys
def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('pragma foreign_keys=ON')


db = SQLAlchemy(app)
event.listen(db.engine, 'connect', _fk_pragma_on_connect)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from personalfinances import routesapi
