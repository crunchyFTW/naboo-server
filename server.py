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


# todo : is the root id 1 always static or do i need to get the new root each time ? maybe using first line of table of nodes to determine root node ?

setup_app()
