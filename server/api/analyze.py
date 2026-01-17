from flask import Blueprint, request, jsonify

analyze_bp = Blueprint("analyze", __name__)

@analyze_bp.route("/analyze", methods=["POST"])
def analyze():
    """
    Chat-style analyze endpoint.
    Accepts text or files.
    """
    payload = {
        "text": request.form.get("text"),
        "files": [f.filename for f in request.files.values()]
    }

    # AI CALL WILL COME HERE LATER
    # result = ai_service.analyze(payload)

    return jsonify({
        "status": "received",
        "message": "Analysis request accepted",
        "payload": payload
    }), 200
