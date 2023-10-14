import pandas as pd

def save_xlsx(name, current_link, row_split, desc, participants, views_per_post, er_per_post, p_pdp, mentions_count, reposts_count):
    tg_link = row_split.replace('@','')

    df = pd.DataFrame([
        ['', '', name, '', current_link, f'http://t.me{tg_link}', desc, participants, views_per_post, er_per_post, p_pdp, mentions_count, reposts_count ]
    ],
     columns=['дата выхода', 'время выхода', 'название', 'комментарий', 'статистика', 'ссылка',
                               'админ', 'кол подписчиков', 'просм на пост',  'вовлеченность ER', 'стоим подписч', 'упоминания', 'репосты'])

    # print(df)
    df.to_excel("out.xlsx")