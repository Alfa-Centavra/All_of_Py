import os
import requests
import pandas as pd
import matplotlib.pyplot as plt


def fast_analit():
    cookies = {
        '__utma': '111200662.1807441124.1700584732.1700584732.1700584732.1',
        '__utmc': '111200662',
        '__utmz': '111200662.1700584732.1.1.utmcsr=yandex.ru|utmccn=(referral)|utmcmd=referral|utmcct=/',
        '__utmt': '1',
        '__utmb': '111200662.1.10.1700584732',
        '__gads': 'ID=eeea82e0ea97a3fd:T=1700584735:RT=1700584735:S=ALNI_MbtbEBvYrzbM9M5WiRLkJU2F9KaeQ',
        '__gpi': 'UID=00000cd6979fddfc:T=1700584735:RT=1700584735:S=ALNI_MZ2srRh-Mzx3oBlEfcI4yIHoLCZ1A',
    }

    headers = {
        'authority': 'countrymeters.info',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru,en;q=0.9',
        'cache-control': 'max-age=0',
        'referer': 'https://yandex.ru/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/116.0.5845.660 YaBrowser/23.9.5.660 Yowser/2.5 Safari/537.36',
    }

    response = requests.get('https://countrymeters.info/ru/World', cookies=cookies, headers=headers)

    tables = pd.read_html(response.text)
    table = tables[0].values
    column_name_1 = table[1][1]
    column_entry_1 = table[1][0].replace(" ", "")
    column_name_2 = table[2][1]
    column_entry_2 = table[2][0].replace(" ", "")
    labels = column_name_1, column_name_2
    population = int(column_entry_1), int(column_entry_2)
    data = {column_name_1: [column_entry_1], column_name_2: [column_entry_2]}
    df = pd.DataFrame(data)
    df2 = pd.DataFrame(tables[0])
    df.to_csv('man_wman_stats.csv', index=False, sep=';')
    df2.to_csv('full_stat.csv', index=False, sep=';', header=False)
    os.startfile(r'full_stat.csv')

    fig1, ax1 = plt.subplots()
    total = sum(population)
    pie_colors = ['#66b3ff', '#ff9999']
    plt.title('Количество мужчин/женщин на земле', fontsize=15)
    ax1.pie(population, labels=labels, colors=pie_colors, autopct=lambda p: '{:.0f}'.format(p * total / 100))
    plt.show()


if __name__ == '__main__':
    fast_analit()
