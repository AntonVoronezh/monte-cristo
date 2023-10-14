import requests
from bs4 import BeautifulSoup

endpoint = 'https://api.aicloud.sbercloud.ru/public/v2/rewriter/predict'
text = '''
 Расстройства возбуждения, включая сексуальную сонливость, лунатизм и ночные кошмары, не имеют устоявшихся рекомендаций по лечению.
 Исследование Дженнифер Мундт показывает эффективность когнитивно-поведенческой терапии, гипноза, гигиены сна и запланированных пробуждений при расстройствах возбуждения.
 Парасомнии могут быть опасны и приводить к травмам, пациенты часто не помнят своих действий во время таких эпизодов.
 В ходе исследования Мундт обнаружил, что наиболее эффективными методами лечения являются когнитивно-поведенческая терапия, гипноз, гигиена сна и запланированные пробуждения.
 Распространенность парасомний составляет 6,9% при хождении во сне, 10% при кошмарах во сне, 18,5% при пробуждениях в состоянии спутанности сознания, 7,1% при сексуальной бессоннице и 4,5% при приеме пищи, связанной со сном.
 Поведенческие и психологические методы лечения парасомний NREM нуждаются в рандомизированных контролируемых исследованиях для определения их эффективности.

'''

# text_for_msg = 'Что же происходит, почему, казалось бы, очевидные плюсы и доводы в пользу улучшения качества жизни воспринимаются в штыки?'
response = requests.post(
    endpoint,
    json={
        "instances": [{
            "text_for_msg": text,
            "num_return_sequences": 15,
            "range_mode": "classifier"
        }]
    }
)

response_json = response.json()
# print(response_json)
print(len(text))
print(len(response_json['prediction_best']['classifier']))
# print(response_json['prediction_best']['bertscore'].replace('.', '\n'))
print(response_json['prediction_best']['classifier'].replace('.', '\n'))

#
# split = text_for_msg.replace('\n', '').split('.')
# print(split)

# for line in split:
#     response = requests.post(
#         endpoint,
#         json={
#             "instances": [{
#                 "text_for_msg": line,
#     # "top_k": 50, "top_p": 0.25,
#                 "num_beams": 5,
#                 "num_return_sequences": 5,
#                 "length_penalty": 0.5,
#                 "no_repeat_ngram_size": 1
#             }]
#         }
#     )
#
#     response_json = response.json()
#     # print(response_json)
#     # print(len(response_json['prediction_best']['bertscore']))
#     print(response_json['prediction_best']['bertscore'].replace('.', '\n'))

response2 = requests.post(
    endpoint,
    json={
        "instances": [{
            "text_for_msg": text,
            "num_return_sequences": 15,
            "range_mode": "bertscore"
        }]
    }
)

response_json2 = response2.json()
# print(response_json)
# print(len(text_for_msg))
print(len(response_json2['prediction_best']['bertscore']))
print(response_json2['prediction_best']['bertscore'].replace('.', '\n'))
