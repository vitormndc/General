import requests
import json
from lxml import html
from tqdm import tqdm

response = []
failed_search = []
up = '▲'
down = '▼'


def string_cleaner(my_stg, remove):

    for symbol in remove:
        symbol = str(symbol)

        if symbol in my_stg:
            my_stg = my_stg.replace(symbol, '')
        else:
            pass

    return my_stg


def my_url(stock_name):
    url = f'https://www.nasdaq.com/symbol/{stock_name}/real-time'

    return url


def up_or_down(html_string):  # identifies if the stock has gone up or down
    if 'green' in str(html_string).lower():
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


def saver(save_name):
    stock_list = list(set(stocks) - set(failed_search))
    print(stock_list)
    try:
        with open('stock_saves.json', 'r+') as json_file:
            data = json.load(json_file)
            json_file.seek(0)
            data[save_name] = stock_list
            json.dump(data, json_file, indent=4)
    except:
        with open('stock_saves.json', 'w') as json_file:
            data = {save_name: stock_list}
            json.dump(data, json_file, indent=4)


def opener(save_name):
    pass


while True:
    input_str = 'Which stocks would you like to search? (e.g., TSLA, AAPL, FB):\n'
    stocks = str(input(input_str)).upper().replace(',', ' ')
    stocks = stocks.split()
    stocks = list(dict.fromkeys(stocks))   # remove repeated names

    print('\n\n\n')
    for stock in tqdm(stocks):
        try:
            page = requests.get(my_url(stock))
            my_html = html.fromstring(page.content)
            company_name = str(my_html.xpath('//*[@id="qwidget_pageheader"]/h1/text()')[0])
            company_name_replaces = ['Common Stock', 'Real Time Stock Quotes', 'Class A']
            company_name = string_cleaner(company_name, company_name_replaces)    # sanitize the company name
            price = my_html.xpath('//*[@id="qwidget_lastsale"]/text()')[0]
            variation = my_html.xpath('//*[@id="qwidget_netchange"]/text()')[0]
            variation_direction = my_html.xpath('//*[@id="qwidget_netchange"]')[0].items()
            response.append([company_name[0:45], stock[0:9], price, up_or_down(variation_direction), variation + ' %'])
        except:
            failed_search.append(stock)

    if response:

        list_header = ['Company name', 'Symbol', 'Stock Price', 'Today fluctuation', '']
        print('\n' * 3 + formatter(list_header) + '\n(Max, 50 characters) \n')

        for i in response:
            print(formatter(i))

        response.clear()

    if failed_search:
        print(f"\nCouldn't find these companies: {str(failed_search)}\n")
        failed_search.clear()

    save = str(input('\nWould you like to save this search? (y or n): '))
    if save is 'y':
        save_as = str(input('\nHow would you like to name the save?: '))
        saver(save_as)

    repeat = str(input('\nWould you like to make another search? (y or n): '))
    if repeat is not 'y':
        break

    print('\n'*10)
