from flask import Flask
from flask_cors import CORS

from db.sql.initialize import setup_db


app = Flask(__name__)
CORS(app)


def setup_app():
    setup_db()
    with app.app_context():
        import route.naboo
        import route.edge
    app.run(port=5555, debug=True)


setup_app()
