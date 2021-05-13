from packages.ml_api.api.config import get_logger
from flask import Blueprint, request
from api.config import get_logger


prediction_app = Blueprint('prediction_app', __name__)
_logger = get_logger(logger_name = __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'