from old.samopoznanie_text.helpers.get_one_text_by_llink import get_text_by_link


def get_all_texts_by_links(links):
    for link in links:
        get_text_by_link(link)

