import requests
from bs4 import BeautifulSoup

endpoint = 'https://api.aicloud.sbercloud.ru/public/v2/summarizator/predict'
text = '''
Живите дольше и процветайте, делая противоположное тому, что вы слышали: Может быть, сначала прочтите это 
'''

# text_for_msg = 'Self-Actualization In Psychology: Theory, Examples & Characteristics '


response = requests.post(
    endpoint,
    json={
        "instances": [{
            "text": text,
# "top_k": 50, "top_p": 0.05,
#             "num_beams": 5,
#             "num_return_sequences": 5,
#             "length_penalty": 0.5,
            # "temperature": 0.1,
# "genstrategy": "sampling"
        }]
    }
)

response_json = response.json()
# print(response_json)
print(len(text))
print(len(response_json['prediction_best']['bertscore']))
print(response_json['prediction_best']['bertscore'].replace('.', '\n'))


#
# split = text_for_msg.replace('\n', '').split('.')
# # print(split)
#
# for line in split:
#     print(len(line))
#     if len(line) < 200:
#         response = requests.post(
#             endpoint,
#             json={
#                 "instances": [{
#                     "text_for_msg": line,
#         # "top_k": 50, "top_p": 0.25,
#         #             "num_beams": 5,
#         #             "num_return_sequences": 15,
#                     "length_penalty": 0.9,
#                     # "no_repeat_ngram_size": 1
#                 }]
#             }
#         )
#
#         response_json = response.json()
#         # print(response_json)
#         # print(len(response_json['prediction_best']['bertscore']))
#         if response_json['prediction_best']['bertscore']:
#             print(response_json['prediction_best']['bertscore'].replace('.', '\n'))