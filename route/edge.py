from flask import current_app as app, jsonify

from service.edge import EdgeService


@app.route('/get_edges', methods=['GET'])
def get_edges():
    try:
        edge_service = EdgeService()
        result = edge_service.get_edges()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': e}), 500
    finally:
        edge_service.clean()

