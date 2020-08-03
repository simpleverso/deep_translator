from deep_translator.constants import BASE_URLS, GOOGLE_LANGUAGES_TO_CODES
from deep_translator.exceptions import NotValidPayload
from deep_translator.parent import BaseTranslator
import requests

url = BASE_URLS['FRENGLY']

params = {
   "email": 'nidhaloff@gmail.com',
   "password": 'merciWitcher3',
   "text": 'Bonjour Monsieur',
   "src": 'fr',
   "dest": 'en'
}

response = requests.post(url,
                        json=params, verify=False)

print(response.url)
print(response.text)
