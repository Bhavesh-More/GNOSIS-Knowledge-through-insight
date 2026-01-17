from flask import Blueprint, jsonify

history_bp = Blueprint("history", __name__)

@history_bp.route("/history", methods=["GET"])
def history():
    return jsonify({
        "history": [],
        "message": "History service placeholder"
    }), 200
