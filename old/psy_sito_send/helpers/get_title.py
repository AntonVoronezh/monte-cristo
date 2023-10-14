from old.psy_sito_send.helpers.sber_sum import sber_sum


def strip_title(text):
    return text.lstrip().upper()[:1] + text.lstrip().lower()[1:]


def get_title(title):
    title_f = title.replace('.', '')
    title_strip = title_f.strip()
    title_len = len(title_strip)

    if title_len > 100:
        print('Титл больше 100')
        return strip_title(sber_sum(title_strip))
    else:
        return strip_title(title_strip)
