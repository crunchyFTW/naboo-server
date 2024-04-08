from flask import current_app as app, jsonify, request
import json

from service.naboo import NabooService


@app.route('/tree_get_all', methods=['GET'])
def get_tree():
    try:
        naboo_service = NabooService()
        result = naboo_service.tree_get_all()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': e}), 500
    finally:
        naboo_service.clean()


@app.route('/naboo_get_by_id', methods=['POST'])
def get_tree_by_id():
    body = json.loads(request.data)
    parent_id_list = body.get("parent_id_list", [])

    try:
        # Check if parent_id_list is a list
        if not isinstance(parent_id_list, list):
            raise ValueError("wrong type of parent id list")
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    try:
        naboo_service = NabooService()
        result = naboo_service.get_tree_by_parent_id(parent_id_list)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': e.args}), 500
    finally:
        naboo_service.clean()


