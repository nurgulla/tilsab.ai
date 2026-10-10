from flask import Flask, jsonify
from flask_cors import CORS
from app.database import init_db
from app.routes import main_bp, api_bp

def create_app(config_name='default'):
    app = Flask(__name__)
    
    from config import config_dict
    app.config.from_object(config_dict[config_name])
    
    CORS(app)
    
    with app.app_context():
        init_db(app)
        
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    @app.route('/health')
    def health():
        return jsonify({'durum': 'aktif', 'mesaj': 'Sunucu saglikli calisiyor.'}), 200
        
    return app
