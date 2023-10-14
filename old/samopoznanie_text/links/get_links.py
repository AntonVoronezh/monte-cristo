from bs4 import BeautifulSoup

f = open('soup.txt', 'r', encoding="utf8")
soup_f = f.read()
f.close()


soup = BeautifulSoup(soup_f, 'lxml')
h3 = soup.find_all('h3')
print(len(h3))
# print(h3)
for txt in h3:
    link = txt.find("a")
    if link:
        print(f'https://samopoznanie.ru{link.get("href")}')

