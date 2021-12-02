import os
from main import create_app
from api.utils.database import db
from api.config.config import ProductionConfig, TestingConfig, DevelopmentConfig

if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app = create_app(config=app_config)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()