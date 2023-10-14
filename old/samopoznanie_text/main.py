# from text_parser.helpers.set_folders import set_folders
# from text_parser.helpers.save_all_links_by_sub_theme import save_all_links_by_sub_theme
# from text_parser.helpers.get_all_texts_by_links import get_all_texts_by_links
# from text_parser.helpers.translate_all_text import translate_all_text
from old.samopoznanie_text.helpers.get_all_texts_by_links import get_all_texts_by_links

# links = ['https://samopoznanie.ru/articles/smysl_zhizni70005/']

with open("links/links.txt") as file:
    links = [row.strip() for row in file]

get_all_texts_by_links(links)
