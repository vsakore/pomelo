from flask_restx import Resource

from webapp.main import ns_events


@ns_events.route("/events")
class AllEvents(Resource):

    def get(self):
        pass

    def post(self):
        pass


@ns_events.route("/events/<int:event_id>")
class OneEvent(Resource):
    def get(self):
        pass

    def post(self):
        pass
