from deep_translator.constants import BASE_URLS, GOOGLE_LANGUAGES_TO_CODES
from deep_translator.exceptions import NotValidPayload
from deep_translator.parent import BaseTranslator
import requests

url = BASE_URLS['WORLDLINGO']

params = {#wl_srclang=en&wl_trglang=de
    "wl_srclang": "en",
    "wl_trglang": "de",
    "wl_password": "merciWitcher3",
    "wl_data": "cute"
}
#
# params = {
# "wl_data": "japanese",
#     "wl_srclang": "ja",
# "wl_trglang": "en",
# "wl_trgenc": "shift_jis"
# }

response = requests.get(url,
                        params=params)

print(response.url)
print(response.text)
