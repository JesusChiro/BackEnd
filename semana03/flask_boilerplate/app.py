from flask import Flask, request
from db import db
from flask_migrate import Migrate
from ma import ma
from routes.countrys_router import countrys_router

app = Flask(__name__)
Migrate = Migrate(app, db)


app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/jobs"

ma.init_app(app)
db.init_app(app)

app.register_blueprint(countrys_router, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
