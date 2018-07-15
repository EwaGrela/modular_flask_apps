from flask import Blueprint, jsonify, g, request
import json
import sqlite3


DATABASE = "/home/ewa/modular_flask_app/modular_flask_apps/main_app/database/database.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

blueprint = Blueprint("api", __name__)
@blueprint.route('/')
def main_api():
    return 'api works'

@blueprint.route('/all_cities', methods= ["GET", "POST"])
def all_cities():
    if request.method =="GET":
        return get_cities()
    else:
        return post_city()


def get_cities():
    db = get_db()
    lim = request.args.get("limit")

    if lim is not None:
        results = db.execute("SELECT * FROM city limit :lim", {"lim": lim}).fetchall()
    else:
        results = db.execute("SELECT * FROM city").fetchall()
    results = [res['city'] for res in results]
    return jsonify(results)


def add_city():
    db = get_db
    return "to be added later"

@blueprint.route("/all_actors", methods = ["GET", "POST"])
def all_actors():
    if request.method =="GET":
        return get_actors()
    else:
        return post_actor()

def get_actors():
    db = get_db()
    results = db.execute("SELECT * from actor order by last_name").fetchall()
    results = [res["last_name"] for res in results]
    return jsonify(results)

def post_actor():
    return "to be added later"

# more endpoint will be added later, as I expand the application
