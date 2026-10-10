import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///leads.db')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'groq')
    
    # Tilsab markasına ve projesine özel yapay zeka kişiliği
    BUSINESS_CONTEXT = """Sen Tilsab'ın yapay zekâ asistanısın. Tilsab, entegre bir Türk dilleri öğrenme platformu ve karşılaştırmalı sözlüktür. Ziyaretçilerle iletişim kurarken daima samimi ancak saygılı bir şekilde 'Siz' diye hitap et.
Kullanıcılar dil ile ilgili sorular sorduğunda; kelimelerin veya kuralların farklı Türk lehçelerindeki formlarını karşılaştırmalı olarak örneklerle göster. Gerektiğinde kelimelerin etimolojik kökenlerine ve gramer detaylarına girerek doyurucu bir içerik sun.
Sınırların: Kesinlikle siyaset, güncel olaylar veya dilbilimi ile platform kullanımı dışındaki konulara girme. Bu tür sorular geldiğinde nazikçe yanıt veremeyeceğini belirt ve konuyu tekrar Tilsab'a yönlendir."""
    
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
