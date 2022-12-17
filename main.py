import requests
from bs4 import BeautifulSoup
import pandas
import csv

# file = open("stoloto.csv", "w")
# file.truncate()
# file.close()

count = 0  # "счетчик для заголовка"

#891, 1460
for num in range(1467, 1469):

    url = f'https://www.stoloto.ru/ruslotto/archive/{num}'
    r = requests.get(url)
    status=r.status_code

    # if status != 200:
    #     raise ValueError ("Oops!  Server don`t ask.  Try again...")

    soup = BeautifulSoup(r.text, "html.parser")

    res = soup.find(class_='data')

    new_str = [num]

    for number in res.find_all('span'):
        new_str.append(int(number.text))
    count +=1
    with open('stoloto.csv', 'a', newline='') as file:
        fieldnames = ["Number", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                      '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32',
                      '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48',
                      '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64',
                      '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80',
                      '81', '82', '83', '84', '85', '86', '87', '88', '89', '90']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',', quoting=csv.QUOTE_ALL)

        if count < 2:
            writer.writeheader()
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerow(new_str)

    print(new_str)
