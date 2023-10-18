import pandas as pd


def save_xlsx(arr):
    df = pd.DataFrame(arr,
                      columns=['дата выхода', 'время выхода', 'название', 'комментарий', 'статистика', 'ссылка',
                               'админ', 'кол подписчиков', 'просм на пост', 'вовлеченность ER', 'стоим подписч',
                               'упоминания',
                               'репосты', 'всего ссылок', 'плохих ссылок', 'стоимость рекламы'])

    # print(df)
    df.to_excel("out.xlsx")
