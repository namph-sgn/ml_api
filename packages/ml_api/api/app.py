from flask import Flask

from api.config import get_logger
from api.controller import prediction_app


_logger = get_logger(logger_name=__name__)

def create_app(*, config_object)->Flask:
    """Create a flask app instance"""
    flask_app = Flask('ml_api')
    flask_app.config.from_object(config_object)

    # Import blueprints
    flask_app.register_blueprint(prediction_app)
    _logger.debug('Application Instance Created')

    return flask_app