from flask import Blueprint, jsonify

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile", methods=["GET"])
def profile():
    return jsonify({
        "topics": [],
        "insights": []
    }), 200
