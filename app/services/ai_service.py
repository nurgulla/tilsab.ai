import requests
from flask import current_app

class AIServiceError(Exception):
    pass

class AIService:
    def get_business_context(self):
        return current_app.config.get('BUSINESS_CONTEXT', 'Sen bir asistansin.')

    def yanit_uret(self, mesaj, gecmis=None):
        api_key = current_app.config.get('GROQ_API_KEY')
        if not api_key:
            return "Demo modu: Yapay zeka yaniti (API anahtari bulunamadi)."
            
        if gecmis is None:
            gecmis = []
            
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        messages = [{"role": "system", "content": self.get_business_context()}]
        for m in gecmis:
            messages.append(m)
            
        messages.append({"role": "user", "content": mesaj})
        
        payload = {
            "model": "openai/gpt-oss-120b",
            "messages": messages
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data['choices'][0]['message']['content']
        except Exception as e:
            raise AIServiceError(f"Yapay zeka servisi hatasi: {str(e)}")

ai_service = AIService()
