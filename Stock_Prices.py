import requests
from lxml import html

response = []
failed_search = []
header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
up = '▲'
down = '▼'


def my_url(stock):  # pass the stock name to the NASDAQ realtime site
    url = f'https://www.nasdaq.com/symbol/{stock}/real-time'

    return url


def up_or_down(var):  # identifies if the stock has gone up or down
    if 'green' in str(var).lower():
        return up
    else:
        return down


def formatter(c_info):  # abbreviation of Company_information that comes in the response list.
    c_str = f'{c_info[0]}' + ' ' * (70 - len(c_info[0])) + f'{c_info[1]}' + ' '*(15 - len(c_info[1])) + f'{c_info[2]}'\
               + ' ' * (20 - len(c_info[2])) + f'{c_info[3]}' + ' ' * (3 - len(c_info[3])) + f'{c_info[4]} %'
    return c_str


stocks = str(input('Which stocks would you like to search? (e.g., TSLA, AAPL, FB):\n')).upper().replace(',', ' ').split()

for i in stocks:
    try:
        page = requests.get(my_url(i), headers=header)
        my_html = html.fromstring(page.content)
        company_name = str(my_html.xpath('//*[@id="qwidget_pageheader"]/h1/text()')[0]).replace("Common Stock", '') \
            .replace('Real Time Stock Quotes', '')
        price = my_html.xpath('//*[@id="qwidget_lastsale"]/text()')[0]
        variation = my_html.xpath('//*[@id="qwidget_netchange"]/text()')[0]
        variation_direction = my_html.xpath('//*[@id="qwidget_netchange"]')[0].items()
        response.append([company_name[0:50], i[0:9], price, up_or_down(variation_direction), variation])
    except:
        failed_search.append(i)

if len(response) > 0:
    list_header = ['Company name', 'Symbol', 'Stock Price', 'Today fluctuation', '']
    print('\n' * 5 + formatter(list_header).replace('%', '') + '\n(Max, 50 characters) \n')

    for i in response:
        print(formatter(i))

if failed_search:
    print(f"\n\n\nCouldn't find these companies: {str(failed_search)}")
