from flask_restx import Namespace

ns_cards = Namespace("v1/cards")
ns_events = Namespace("v1/events")

from webapp.main import event_routes
from webapp.main import card_routes
