from flask_restx import fields

from webapp import api


card_model = api.model("card_model", {
    "id": fields.Integer,
    "max_credit": fields.Integer,
    "avl_credit": fields.Integer,
    "payable_bal": fields.Integer
})

card_request = api.model("card_request", {
    "max_credit": fields.Integer
})

# update_card_request = api.model("update_card_request", {
#     "max_credit": fields.Integer
# })

