import requests
import pandas as pd


def parce_and_dataframe():
    cookies = {
        'A1': 'd=AQABBDiAW2UCEAJPywPxSbX-c_UytjS8oysFEgEBAQHRXGVlZZ6fzyMA_eMAAA&S=AQAAAiF64SKpyS2uiQd1ls1MUZc',
        'A3': 'd=AQABBDiAW2UCEAJPywPxSbX-c_UytjS8oysFEgEBAQHRXGVlZZ6fzyMA_eMAAA&S=AQAAAiF64SKpyS2uiQd1ls1MUZc',
        'A1S': 'd=AQABBDiAW2UCEAJPywPxSbX-c_UytjS8oysFEgEBAQHRXGVlZZ6fzyMA_eMAAA&S=AQAAAiF64SKpyS2uiQd1ls1MUZc',
        'cmp': 't=1700495414&j=0&u=1---',
        'gpp': 'DBAA',
        'gpp_sid': '-1',
        'gam_id': 'y-ZrU.j9RE2uII913pM5dohLIpR7ON2pgb~A',
        'axids': 'gam=y-ZrU.j9RE2uII913pM5dohLIpR7ON2pgb~A&dv360=eS1LZHhuZU1CRTJ1Rmdfb0VleS5uVEtpaEZ1RFUxc2dSSn5B',
        'PRF': 't%3DBTC-USD',
        'tbla_id': 'e6976b0a-c9a1-49ec-a2f1-abad97b5fc9f-tuctc5505ba',
        'maex': '%7B%22v2%22%3A%7B%7D%7D',
        '__gpi': 'UID=00000ccec2e7298f:T=1700495456:RT=1700495456:S=ALNI_MZ1b9Lx-uOmyyB6gj9Jw0hWlI3bEA',
    }

    headers = {
        'authority': 'finance.yahoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/'
                  'apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'A1=d=AQABBDiAW2UCEAJPywPxSbX-c_UytjS8oysFEgEBAQHRXGVlZZ6fzyMA_eMAAA&S=
        # AQAAAiF64SKpyS2uiQd1ls1MUZc; A3=d=AQABBDiAW2UCEAJPywPxSbX-c_UytjS8oysFEgEBAQHRXGV
        # lZZ6fzyMA_eMAAA&S=AQAAAiF64SKpyS2uiQd1ls1MUZc; A1S=d=AQABBDiAW2UCEAJPywPxSbX-c_Uy
        # tjS8oysFEgEBAQHRXGVlZZ6fzyMA_eMAAA&S=AQAAAiF64SKpyS2uiQd1ls1MUZc; cmp=t=170049541
        # 4&j=0&u=1---; gpp=DBAA; gpp_sid=-1; gam_id=y-ZrU.j9RE2uII913pM5dohLIpR7ON2pgb~A;
        # axids=gam=y-ZrU.j9RE2uII913pM5dohLIpR7ON2pgb~A&dv360=eS1LZHhuZU1CRTJ1Rmdfb0VleS5u
        # VEtpaEZ1RFUxc2dSSn5B; PRF=t%3DBTC-USD; tbla_id=e6976b0a-c9a1-49ec-a2f1-abad97b5fc
        # 9f-tuctc5505ba; maex=%7B%22v2%22%3A%7B%7D%7D; __gpi=UID=00000ccec2e7298f:T=170049
        # 5456:RT=1700495456:S=ALNI_MZ1b9Lx-uOmyyB6gj9Jw0hWlI3bEA',
        'referer': 'https://yandex.ru/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/116.0.5845.660 YaBrowser/23.9.5.660 Yowser/2.5 Safari/537.36',
    }

    params = {
        'period1': '1410912000',
        'period2': '1700438400',
        'interval': '1mo',
        'filter': 'history',
        'frequency': '1mo',
        'includeAdjustedClose': 'true',
    }

    response = requests.get('https://finance.yahoo.com/quote/BTC-USD/history',
                            params=params, cookies=cookies, headers=headers)
    tables = pd.read_html(response.text)
    table = tables[0][:100]
    df = pd.DataFrame(table)
    df.rename(columns={'Close*': 'Close'}, inplace=True)
    df.to_excel('full_btc_price&volume_lst100mnth.xlsx', index=False)
    df = df.drop(['Open', 'High', 'Low', 'Adj Close**'], axis=1)
    df.to_csv('btc_price&volume_lst100mnth.csv', index=False, sep=';')


if __name__ == '__main__':
    parce_and_dataframe()
