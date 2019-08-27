import requests
from lxml import html
from tqdm import tqdm

response = []
failed_search = []
header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
up = '▲'
down = '▼'


def string_cleaner(my_stg, remove):
    # this function could be imported as a module that i made, it is here just to make easier if someone wants just
    # this script

    for symbol in remove:
        symbol = str(symbol)

        if symbol in my_stg:
            my_stg = my_stg.replace(symbol, '')
        else:
            pass

    return my_stg


def my_url(stock):  # pass the stock name to the NASDAQ realtime site
    url = f'https://www.nasdaq.com/symbol/{stock}/real-time'

    return url


def up_or_down(var):  # identifies if the stock has gone up or down
    if 'green' in str(var).lower():
        return up
    else:
        return down


def formatter(c_info, spaces=None):  # c_info is the abbreviation of Company_information that is given
    c_str = ''                       # spaces is the number of spaces between columns in the final print
    if spaces is None:
        spaces = [55, 15, 20, 3, 0]  # default values for columns spacing
    for (j, k) in zip(c_info, spaces):
        c_str += str(j)+' '*(k-len(j))
    return c_str


while True:

    input_str = 'Which stocks would you like to search? (e.g., TSLA, AAPL, FB):\n'
    stocks = str(input(input_str)).upper().replace(',', ' ')
    stocks = stocks.split()
    stocks = list(dict.fromkeys(stocks))

    print('\n\n\n')
    for i in tqdm(stocks):
        try:
            page = requests.get(my_url(i), headers=header)
            my_html = html.fromstring(page.content)
            company_name = str(my_html.xpath('//*[@id="qwidget_pageheader"]/h1/text()')[0])
            company_name_replaces = ['Common Stock', 'Real Time Stock Quotes', 'Class A']
            company_name = string_cleaner(company_name, company_name_replaces)
            price = my_html.xpath('//*[@id="qwidget_lastsale"]/text()')[0]
            variation = my_html.xpath('//*[@id="qwidget_netchange"]/text()')[0]
            variation_direction = my_html.xpath('//*[@id="qwidget_netchange"]')[0].items()
            response.append([company_name[0:45], i[0:9], price, up_or_down(variation_direction), variation + ' %'])
        except:
            failed_search.append(i)

    if response:

        list_header = ['Company name', 'Symbol', 'Stock Price', 'Today fluctuation', '']
        print('\n' * 3 + formatter(list_header) + '\n(Max, 50 characters) \n')

        for i in response:
            print(formatter(i))

    if failed_search:

        print(f"\nCouldn't find these companies: {str(failed_search)}\n")

    goagain = str(input('\n\nWould you like to make another search? (y or n): \n'))
    if goagain is not 'y':
        break

