import requests


razer_key = '14671e53fd9f14cea97a04a05d9da83e5dfc76c07a750b19c8c120cc'


# Replace 'your_api_key' with your actual TextRazor API key
API_KEY = razer_key
API_URL = 'https://api.textrazor.com'

def get_tags_from_textrazor(text):
    headers = {
        'x-textrazor-key': API_KEY,
    }
    data = {
        'text': text,
        'extractors': 'entities',  # Extracts keywords and entities from text
    }

    response = requests.post(API_URL, headers=headers, data=data)

    if response.status_code == 200:
        result = response.json()
        tags = []
        # Extract tags based on entities
        for entity in result.get("response", {}).get("entities", []):
            tags.append(entity.get("entityId"))  # entityId is the keyword or tag
        return ",".join(tags[:5])
    else:
        print("Error:", response.status_code, response.text)
        return []












