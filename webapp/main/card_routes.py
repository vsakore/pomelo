from flask import request
from flask_restx import Resource

from webapp import db
from webapp.main import ns_cards
from webapp.main.api_models import card_request, card_model
from webapp.models import Card


@ns_cards.route("/")
class AllCards(Resource):

    @ns_cards.marshal_list_with(card_model)
    def get(self):
        cards = Card.query.all()
        return cards, 200

    @ns_cards.expect(card_request)
    @ns_cards.marshal_with(card_model)
    def post(self):
        body = request.get_json()
        max_credit = body.get("max_credit", 0)
        avl_credit, payable_bal = max_credit, 0
        card = Card(max_credit=max_credit, avl_credit=avl_credit, payable_bal=payable_bal)

        db.session.add(card)
        db.session.commit()

        return card, 201


@ns_cards.route("/<int:card_id>")
class OneCard(Resource):
    @ns_cards.marshal_with(card_model)
    def get(self, card_id):
        card = Card.query.filter_by(id=card_id).first_or_404("Card does not exist")
        return card, 200

    @ns_cards.expect(card_request)
    @ns_cards.marshal_with(card_model)
    def put(self, card_id):
        body = request.get_json()
        new_max_credit = body.get("max_credit", 0)

        card = Card.query.filter_by(id=card_id).first_or_404("Card does not exist")
        card.max_credit = new_max_credit
        db.session.commit()

        return card, 200

    @ns_cards.marshal_with(card_model)
    def delete(self, card_id):
        card = Card.query.filter_by(id=card_id).first_or_404("Card does not exist")
        db.session.delete(card)
        db.session.commit()

        return {"id": card_id}, 204


@ns_cards.route("/<int:card_id>/summary")
class CardSummary(Resource):
    def get(self):
        pass
