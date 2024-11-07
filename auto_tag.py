
# Key = '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'
# data = "'Rajasthan is a state in northwestern India. It covers 342,239 square kilometres (132,139 sq mi) or 10.4 per cent of India's total geographical area. It is the largest Indian state by area and the seventh largest by population. It is on India's northwestern side, where it comprises most of the wide and inhospitable Thar Desert (also known as the Great Indian Desert) and shares a border with the Pakistani provinces of Punjab to the northwest and Sindh to the west, along the Sutlej-Indus River valley. It is bordered by five other Indian states: Punjab to the north; Haryana and Uttar Pradesh to the northeast; Madhya Pradesh to the southeast; and Gujarat to the southwest. Its geographical location is 23°.3' to 30°.12' North latitude and 69°.30' to 78°.17' East longitude, with the Tropic of Cancer passing through its southernmost tip.\nIts major features include the ruins of the Indus Valley civilisation at Kalibangan and Balathal, the Dilwara'"

# import requests

# API_URL = "https://api-inference.huggingface.co/models/efederici/text2tags"
# headers = {"Authorization":"Bearer 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" }

# def get_tags(text):
#     payload = {"inputs": text}
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()
# gen_tags = get_tags(data)[0]['summary_text'].split(',')[:3]
# print(gen_tags)

razer_key = '14671e53fd9f14cea97a04a05d9da83e5dfc76c07a750b19c8c120cc'
import requests

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

# Test with a sample text
text = "India, officially the Republic of India, is a country in South Asia.  It is the seventh-largest country in the world by area and the most populous country. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west; China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia.\nModern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago.\nTheir long occupation, initially in varying forms of isolation as hunter-gatherers, has made the region highly diverse, second only to Africa in human genetic diversity. Settled life emerged on the subcontinent in the western margins of the Indus river basin 9,000 years ago, evolving gradually into the Indus Valley Civilisation of t"
tags = get_tags_from_textrazor(text)
print("Extracted Tags:", tags[:5])


# # Simulate auto-tagging with Gemini Pro
# def auto_tag_article(summary: str) -> str:
#     tags = []
#     if "is" in summary:
#         tags.append("is")
#     if "the" in summary:
#         tags.append("is")
#     if "of" in summary:
#         tags.append("of")
#     return ",".join(tags)






