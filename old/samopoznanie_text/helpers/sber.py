import requests

endpoint = 'https://api.aicloud.sbercloud.ru/public/v2/summarizator/predict'


def get_sber_summary(text):
    response = requests.post(
        endpoint,
        json={
            "instances": [{
                "text_for_msg": text,
                "num_beams": 5,
                "num_return_sequences": 3,
                "length_penalty": 0.5}]
        }
    )

    response_json = response.json()
    return response_json['prediction_best']['bertscore']
