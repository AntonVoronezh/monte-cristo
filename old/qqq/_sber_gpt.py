# https://russiannlp.github.io/rugpt-demo/
import requests
import fake_useragent
word = '''ты великий психолог, напиши текст на 300 знаков на основе этого - 

• Снимки МРТ показывают, как мозг выглядит, когда человек теряет самоконтроль.
• Исследование нейробиолога подтверждает предыдущие исследования о самоконтроле.
• Исследование Хеджкока показывает, что истощение самоконтроля происходит в мозге.
• Исследование использует изображения фМРТ для сканирования людей при выполнении задач по самоконтролю.
• Исследование показывает, что передняя поясная кора мозга срабатывает с одинаковой интенсивностью.
• Дорсолатеральная префронтальная кора мозга срабатывает с меньшей интенсивностью после предварительного напряжения самоконтроля.
• Потеря активности в DLPFC может быть следствием потери самоконтроля.
• Исследование может помочь разработать более эффективные методы лечения для людей с пагубными привычками.

'''

ua = fake_useragent.UserAgent()
headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json',
    'Server': 'istio-envoy',
    'Accept-encoding': 'gzip, deflate, br',
    'User-Agent': ua.random,
    'Content-Type': 'application/json',
    'Origin': 'https://russiannlp.github.io',
    'Referer': 'https://russiannlp.github.io/',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
    }

response = requests.post("https://api.aicloud.sbercloud.ru/public/v1/public_inference/gpt3/predict",
                         json={"text": word}, headers=headers)

# print('Status code:', response.status_code)
answer = response.json()
# print(answer['predictions'])
f = answer['predictions'].split('\n\n')
print(f[0])
print('----')
print(f[1])
print('----')
print(f[2])


