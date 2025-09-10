from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# ----------------------------
# Earthquake model
# ----------------------------
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    serialize_rules = ('-id',)  # Optional, adjust serialization rules

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=False)
    magnitude = db.Column(db.Float, nullable=False)
    year = db.Column(db.Integer, nullable=False)
