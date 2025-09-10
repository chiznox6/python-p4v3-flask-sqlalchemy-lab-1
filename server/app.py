# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)


# ----------------------------
# View: Get earthquake by ID
# ----------------------------
@app.route('/earthquakes/<int:id>')
def get_earthquake(id):
    quake = Earthquake.query.filter_by(id=id).first()
    if quake:
        return jsonify(
            id=quake.id,
            location=quake.location,
            magnitude=quake.magnitude,
            year=quake.year
        ), 200
    else:
        return jsonify({'message': f'Earthquake {id} not found.'}), 404


# ---------------------------------------------
# View: Get earthquakes by minimum magnitude
# ---------------------------------------------
@app.route('/earthquakes/magnitude/<float:magnitude>')
def get_quakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    quakes_data = [
        {'id': q.id, 'location': q.location, 'magnitude': q.magnitude, 'year': q.year}
        for q in quakes
    ]
    return jsonify(count=len(quakes_data), quakes=quakes_data), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
