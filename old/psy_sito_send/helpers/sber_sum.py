import requests


def sber_sum(title):
    endpoint = 'https://api.aicloud.sbercloud.ru/public/v2/summarizator/predict'
    response = requests.post(
        endpoint,
        json={
            "instances": [{
                "text": title,
            }]
        }
    )

    response_json = response.json()
    return response_json['prediction_best']['bertscore']

