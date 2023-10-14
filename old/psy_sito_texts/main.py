import time
from old.psy_sito_texts.helpers.ya import get_yandex_text_by_link
from old.psy_sito_texts.helpers.save_yandex_text import save_yandex_text


# links = ['https://neurosciencenews.com/social-media-cosmetic-surgery-23976/']

with open("links.txt") as file:
    links = [row.strip() for row in file]

for link in links:
    text = get_yandex_text_by_link(link)
    save_yandex_text(text)
    print(link)
    time.sleep(1)
