from __future__ import annotations

from typing import Type

from flask import Flask, jsonify, request
from flask.views import MethodView
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from models import Adverts, Session
from schema import CreateAdverts, UpdateAdverts

app = Flask("app")


class HttpError(Exception):
    def __init__(self, status_code: int, error_message: dict | list | str):
        self.status_code = status_code
        self.error_message = error_message


class AdvertsView(MethodView):
    def get(self, advert_id: int):
        with Session() as session:
            advert = get_advert(session, advert_id)
            return jsonify(
                {
                    "id": advert.id,
                    "title_advert": advert.title_advert,
                    "description": advert.description,
                    "user": advert.user,
                    "create_date": advert.create_date.isoformat(),
                }
            )

    def post(self):
        json_data = validate(CreateAdverts, request.json)
        with Session() as session:
            advert = Adverts(**json_data)
            session.add(advert)
            try:
                session.commit()
            except IntegrityError:
                raise HttpError(409, "advert already exists")
            return jsonify({"status": "success", "id": advert.id})

    def patch(self, advert_id: int):
        json_data = validate(UpdateAdverts, request.json)
        with Session() as session:
            advert = get_advert(session, advert_id)
            for field, value in json_data.items():
                setattr(advert, field, value)
            session.add(advert)
            session.commit()
            return jsonify({"status": "success", "id": advert.id})

    def delete(self, advert_id):
        with Session() as session:
            advert = get_advert(session, advert_id)
            session.delete(advert)
            session.commit()
            return jsonify({"status": "success", "id": advert.id})


@app.errorhandler(HttpError)
def error_handler(er: HttpError):
    http_reponse = jsonify({"status": "error", "description": er.error_message})
    http_reponse.status_code = er.status_code
    return http_reponse


def validate(schema: Type[CreateAdverts] | Type[UpdateAdverts], json_data: dict):
    try:
        model = schema(**json_data)
        validate_data = model.model_dump(exclude_none=True)
    except ValidationError as er:
        raise HttpError("400", er.errors())
    return validate_data


def get_advert(session: Session, advert_id: int):
    advent = session.get(Adverts, advert_id)
    if advent is None:
        raise HttpError(404, "advent not found")
    return advent


adverts_view = AdvertsView.as_view("adverts")
app.add_url_rule(
    "/adverts/<int:advert_id>",
    view_func=adverts_view,
    methods=["GET", "PATCH", "DELETE"],
)
app.add_url_rule("/adverts/", view_func=adverts_view, methods=["POST"])
if __name__ == "__main__":
    app.run()
