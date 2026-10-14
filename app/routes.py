from flask import Blueprint, request, jsonify, render_template
from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError

main_bp = Blueprint('main', __name__)
api_bp = Blueprint('api', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@api_bp.route('/sohbet', methods=['POST'])
def sohbet():
    data = request.get_json()
    if not data or 'mesaj' not in data:
        return jsonify({'basari': False, 'hata': 'Eksik veri, mesaj gerekli.'}), 400
        
    mesaj = data['mesaj']
    gecmis = data.get('gecmis', [])
    
    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)
        return jsonify({'basari': True, 'cevap': cevap}), 200
    except AIServiceError as e:
        return jsonify({'basari': False, 'hata': 'Yapay zeka su an yanit veremiyor.'}), 503

@api_bp.route('/leads', methods=['POST'])
def api_lead_ekle():
    data = request.get_json()
    if not data or 'isim' not in data or 'email' not in data:
        return jsonify({'basari': False, 'hata': 'Isim ve e-posta alanlari zorunludur.'}), 400
        
    try:
        lead_ekle(data['isim'], data['email'], data.get('telefon', ''), data.get('amac', ''))
        return jsonify({'basari': True, 'mesaj': 'Kayit basariyla eklendi.'}), 201
    except Exception as e:
        return jsonify({'basari': False, 'hata': str(e)}), 500

@api_bp.route('/leads', methods=['GET'])
def api_tum_leadler():
    try:
        leads = tum_leadler()
        return jsonify({'basari': True, 'leads': leads}), 200
    except Exception as e:
        return jsonify({'basari': False, 'hata': str(e)}), 500
