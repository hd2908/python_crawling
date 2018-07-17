import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.fitt.kr/index.fitt')
html = res.text
soup = BeautifulSoup(res.content, 'html.parser')
my_ranks_num = soup.select(
    '.index-rank-number'
)
my_ranks = soup.select(
    '.text-hover.gymLink > span'
)
for rank in my_ranks:
    print(" ".join(rank.text.split()))


# print(title.get_text())