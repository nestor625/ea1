import logging
from flask import Flask
from flask_appbuilder import AppBuilder
from flask_appbuilder.models.sqla import Model
from flask_appbuilder.models.sqla.base import SQLA
from sqlalchemy.engine import Engine
from sqlalchemy import event
from .indexview import FABView

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
# Flask-AppBuilder 5 keeps application and security models on
# flask_appbuilder.models.sqla.Model.metadata. Bind that metadata so
# db.create_all() creates those tables. Flask-SQLAlchemy 3 also requires
# an application context for the session and for create_all().
db = SQLA(app, metadata=Model.metadata)
with app.app_context():
    appbuilder = AppBuilder(app, db.session, base_template='mybase.html', indexview=FABView)


"""
Only include this for SQLLite constraints
"""
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


from app import views, data

with app.app_context():
    db.create_all()
#data.fill_gender()
#data.fill_data()

