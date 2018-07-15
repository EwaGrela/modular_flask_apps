from flask import Flask

app = Flask(__name__)

from main_app.api.routes import blueprint
from main_app.site.routes import blueprint

app.register_blueprint(api.routes.blueprint, url_prefix="/api")
app.register_blueprint(site.routes.blueprint, url_prefix ="/site")

