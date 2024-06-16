from flask import Flask

from webapp.config import Config
from webapp.extensions import db, api
from webapp.main import ns_cards, ns_events


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init db
    db.init_app(app)

    from webapp.models import Card, Event
    with app.app_context():
        db.create_all()

    api.init_app(app)
    api.add_namespace(ns_cards)
    api.add_namespace(ns_events)

    return app
