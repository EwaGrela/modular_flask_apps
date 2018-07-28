from flask import Blueprint, render_template, request, g
import sqlite3

blueprint = Blueprint("site", __name__, template_folder ="templates")

DATABASE = "/home/ewa/modular_flask_app/modular_flask_apps/main_app/database/database.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@blueprint.route("/")
def main_page():
    return render_template("site/index.html")

@blueprint.route("/all_cities", methods= ["GET", "POST"])
def all_cities():
    if request.method=="GET":
        return get_cities()
    else:
        return post_city()

def get_cities():
    db = get_db()
    results = db.execute("SELECT * FROM city").fetchall()
    return render_template("site/cities.html", cities = results)


@blueprint.route("/all_actors", methods =["GET", "POST"])
def all_actors():
    if request.method =="GET":
        return get_actors()
    else:
        return post_actor()
        
def get_actors():
    db = get_db()
    results = db.execute("select * from actor").fetchall()
    return render_template("site/actors.html", actors = results)