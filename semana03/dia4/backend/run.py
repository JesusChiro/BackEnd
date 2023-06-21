from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
"""Configurando SQLAlchemy"""
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/lista_tareas"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


### Crear mi primera tabla con el ORM ##
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(100), nullable=False)

    def __init__(self, descripcion, estado):
        self.descripcion = descripcion
        self.estado = estado


db.create_all()
print("se creó la tabla en la base de datos")


# --- CREATE TABLE tarea(
#     id int primary key not null auto_incre,
#     descripcion varchar(200),
#     estado varchar(100))

""" Uso de Marshmallow """

ma = Marshmallow(app)


class TareaSchema(ma.Schema):
    class Meta:
        fields = ("id", "descripcion", "estado")


@app.route("/")
def index():
    context = {"status": True, "content": "Servidor activo"}

    return jsonify(context)


@app.route("/tarea", methods=["POST"])
def set_tarea():
    descripcion = request.json["descripcion"]
    estado = request.json["estado"]

    # insert into tarea
    nueva_tarea = Tarea(descripcion, estado)
    db.session.add(nueva_tarea)
    db.session.commit()

    data_schema = TareaSchema()
    context = {"status": True, "content": data_schema.dump(nueva_tarea)}

    return jsonify(context)


@app.route("/tarea")
def get_tarea():
    data = Tarea.query.all()  # select id,descripcion,estado from tarea
    data_schema = TareaSchema(many=True)

    context = {"status": True, "content": data_schema.dump(data)}
    return jsonify(context)


@app.route("/tarea/<id>")
def get_tarea_by_id(id):
    data = Tarea.query.get(id)  # select * from tarea where id=?
    data_schema = TareaSchema()

    context = {"status": True, "content": data_schema.dump(data)}
    return jsonify(context)


@app.route("/tarea/<id>/", methods=["PUT"])
def update_tarea(id):
    descripcion = request.json["descripcion"]
    estado = request.json["estado"]
    tarea = Tarea.query.get(id)
    tarea.descripcion = descripcion
    tarea.estado = estado
    db.session.commit()

    data_schema = TareaSchema()
    context = {"status": True, "content": data_schema.dump(tarea)}
    return jsonify(context)


@app.route("/tarea/<id>/", methods=["delete"])
def delete_tarea(id):
    tarea = Tarea.query.get(id)
    db.session.delete(tarea)
    db.session.commit()

    data_schema = TareaSchema()
    context = {"status": True, "content": data_schema.dump(tarea)}

    return jsonify(context)


if __name__ == "__main__":
    app.run(debug=True)
