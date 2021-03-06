from packages.ml_api.api.config import get_logger
from flask import Blueprint, request, jsonify
from packages.models.regression_model.predict import make_prediction
from packages.ml_api.api.config import get_logger


prediction_app = Blueprint('prediction_app', __name__)
_logger = get_logger(logger_name = __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'

@prediction_app.route('/v1/predict/regression', methods=['POST'])
def predict():
    if request.method == 'POST':
        json_data = request.get_json()
        _logger.info('Input: {}'.format(json_data))

        result = make_prediction(input_data=json_data)
        _logger.info('Outputs: {}'.format(result))

        predictions = result.get('predictions')[0]
        version = result.get('version')

        return jsonify({'predictions': predictions,
        'version': version})