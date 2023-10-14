from bs4 import BeautifulSoup
import fake_useragent
import requests
import time

url = 'https://neurosciencenews.com/neuroscience-terms/mental-health/page/'
arr = []
arr_img = []
# for i in range(1, 2):
for i in range(1, 164):
    print(i)
    next_url = f'{url}{i}/'
    # print(next_url)
    ua = fake_useragent.UserAgent()
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=next_url, headers=fake_ua)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    article_arr = soup.find_all('article')

    # div2 = div.find_all('div', class_='mask')
    # # print(div2)
    #
    for txt in article_arr:
        # print(txt)
        link = txt.find("a", class_="mask-img")
        # print(link.get("href"))
        img = txt.find("img")

        # print(img)
        img_arr = []
        try:
            img_arr = img.get("srcset").split(',')
        except:
            pass

        try:
            img_arr.append(img.get("src"))
        except:
            pass

        # print(img_arr)
        # src = img.get("src")
        # gg = srcset.split(',')
        # print(gg)
        img_link = ''
        for ff in img_arr:
            # print(ff)
            # img_link = ff.strip()
            if '585w' in ff:
                img_link = ff.strip().split(' ')[0]
            if '770w' in ff:
                img_link = ff.strip().split(' ')[0]
            if 'ic.jpg' in ff:
                img_link = ff.strip()
            if '1200w' in ff:
                img_link = ff.strip().split(' ')[0]
            if '1155w' in ff:
                img_link = ff.strip().split(' ')[0]
            if '1170w' in ff:
                img_link = ff.strip().split(' ')[0]

        # print(img_link)
    #     if link:
    #         # print(link.get("href"))
    #         arr.append(link.get("href"))
        link_link = ''
        try:
            link_link = link.get("href")
        except:
            pass

        out = f'{img_link}***{link_link}'
        if len(out.split('***')[0]) > 0 and len(out.split('***')[1]) > 0:
            # print(out, flush=True)
            arr_img.append(out)
    #
    # arr_set = list(set(arr))
    arr_img_set = list(set(arr_img))



for i in arr_img_set:
    print(i, flush=True)

