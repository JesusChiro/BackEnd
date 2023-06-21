from models.countrys_model import CountrysModel
from schemas.countrys_schema import CountrysSchema
from db import db


class CountrysController:
    def __init__(self):
        self.model = CountrysModel
        self.schema = CountrysSchema

    def getAll(self):
        try:
            records = self.model.query.all()
            data_schema = self.schema(many=True)
            return data_schema.dump(records), 200
        except Exception as error:
            return {
                "message": "Error al obtener los registros",
                "error": str(error),
            }, 400

    def create(self, json):
        try:
            data_schema = self.schema()
            record = data_schema.load(json)
            db.session.add(record)
            db.session.commit()
            return data_schema.dump(record), 201
        except Exception as error:
            return {
                "message": "Error al crear el registro",
                "error": str(error),
            }, 400
