from packages.ml_api.api.app import create_app
from packages.ml_api.api.config import DevelopmentConfig, PACKAGE_ROOT
import sys
import os
PACKAGE_ROOT = os.path.join(os.pardir)
sys.path.append(PROJ_ROOT)
MODELS_ROOT = os.path.join(PACKAGE_ROOT, "models")
sys.path.append(MODELS_ROOT)

application = create_app(config_object=DevelopmentConfig)

if __name__ == '__main__':
	application.run()
