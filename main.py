import requests
from bs4 import BeautifulSoup
import pandas
import csv

# f = open('stoloto.csv','w')
# f.close()


for num in range(1454,1458):

    url = f'https://www.stoloto.ru/ruslotto/archive/{num}'
    r = requests.get(url)
    print(r.status_code)

    soup = BeautifulSoup(r.text, "html.parser")

    res = soup.find(class_='data')

    new_str = [num]

    for number in res.find_all('span'):
        new_str.append(int(number.text))

    with open('stoloto.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        #writer = csv.writer(f)
        writer.writerow(new_str)

    print(new_str)

