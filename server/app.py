from flask import Flask
from config.base import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register routes
    from api.analyze import analyze_bp
    from api.history import history_bp
    from api.profile import profile_bp

    app.register_blueprint(analyze_bp, url_prefix="/api")
    app.register_blueprint(history_bp, url_prefix="/api")
    app.register_blueprint(profile_bp, url_prefix="/api")

    @app.route("/health", methods=["GET"])
    def health_check():
        return {"status": "ok"}, 200

    return app

app = create_app()
