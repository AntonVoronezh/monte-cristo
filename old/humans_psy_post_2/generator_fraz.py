from random import choice

arr = [
    'верни смешной рассказ на русском языке от лица POL о TEMA с нелогичным окончанием от второго лица длиной PREDL предложения по SLOV слов в виде json с результатом в поле description'
]

# arr = [
#     'смешной рассказ на русском языке от лица POL о TEMA с нелогичным окончанием от второго лица длиной PREDL предложения по SLOV слов'
# ]

for r in arr:
    pol = ['женщины', 'мужчины']
    tema = ['саморазвитии', 'психологии', 'фобиях', 'психологических тестах']

    for p in pol:
        pp = str(p)
        r1 = r.replace("POL", pp)

        for t in tema:
            tt = str(t)
            r2 = r1.replace("TEMA", tt)

            for pr in range(3,5):
                prpr = str(pr)
                r3 = r2.replace("PREDL", prpr)

                for sl in range(15, 16):
                    slsl = str(sl)
                    r4 = r3.replace("SLOV", slsl)

                    print(r4)
                    # print(choice(range(1, 100000)))
                    # print(f'"{choice(range(1, 100000))}" : {r4},')