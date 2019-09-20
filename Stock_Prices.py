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
    url = f'https://old.nasdaq.com/symbol/{stock_name}/real-time'

    return url


def up_or_down(html_string):  # identifies if the stock has gone up or down
    if 'green' in str(html_string).lower():
        return up
    else:
        return down


def formatter(c_info, spaces=None):
    """
    This function format the information in evenly spaced columns,
    c_info is the abbreviation of Company_information array that is given,
    spaces is the number of spaces between columns in the final print
    """
    c_str = ''
    if spaces is None:
        spaces = [55, 15, 20, 3, 0]   # default value for spaces
    for (j, k) in zip(c_info, spaces):
        c_str += str(j) + ' ' * (k - len(j))
    return c_str


def saver(save_name):
    stock_list = [x for x in stocks if x not in failed_search]
    try:
        with open('stock_saves.json', 'r+') as json_file:
            data = json.load(json_file)
            json_file.seek(0)
            data[save_name] = stock_list
            json.dump(data, json_file, indent=4)
    except FileNotFoundError:
        with open('stock_saves.json', 'w') as json_file:
            data = {save_name: stock_list}
            json.dump(data, json_file, indent=4)
    except json.decoder.JSONDecodeError:
        print('The file that saves searches is corrupted, please delete "stock_saves.json" and try again')


while True:
    stocks = []
    option = input('What would you like to do?\n1. Make a new search\n2. Use saved stock list in a new search\n' +
                   'Response: ').strip()

    while option is not '1' and option is not '2':
        option = input("\nThis isn't a valid number, please input a valid number '1' or '2':")

    if option is '1':
        input_str = '\nWhich stocks would you like to search? (e.g., TSLA, AAPL, FB)\nResponse:'
        stocks = str(input(input_str)).upper().replace(',', ' ')
        stocks = stocks.split()
        stocks = list(dict.fromkeys(stocks))  # remove repeated names

    if option is '2':
        try:
            with open('stock_saves.json', 'r') as json_file:  # load from save file
                data = json.load(json_file)

                if data.keys():
                    print('\nSaved searches')
                    for key in data:
                        values = string_cleaner(str(data[key]), ["'", '[', ']'])
                        print(f'{key}: {values}')

                    select_save = input('\nPlease type a save to load \nResponse: ')
                    if select_save not in data.keys():
                        print('Save file does not exist')
                        continue
                    else:
                        stocks = data[select_save]

        except FileNotFoundError:
            print('\nThere is no saves\n')
            continue

    if not stocks:
        print('No search terms' + '\n' * 3)
        continue

    print('\n' * 3)
    for stock in tqdm(stocks):
        try:
            page = requests.get(my_url(stock))
            my_html = html.fromstring(page.content)
            company_name = str(my_html.xpath('//*[@id="qwidget_pageheader"]/h1/text()')[0])
            company_name_replaces = ['Common Stock', 'Real Time Stock Quotes', 'Class A']
            company_name = string_cleaner(company_name, company_name_replaces)  # sanitize the company name
            price = my_html.xpath('//*[@id="qwidget_lastsale"]/text()')[0]
            variation = my_html.xpath('//*[@id="qwidget_netchange"]/text()')[0]
            variation_direction = my_html.xpath('//*[@id="qwidget_netchange"]')[0].items()
            response.append([company_name[0:45], stock[0:9], price, up_or_down(variation_direction), variation + ' %'])
        except IndexError:
            failed_search.append(stock)

    if response:
        list_header = ['Company name', 'Symbol', 'Stock Price', 'Today fluctuation', '']
        print('\n' * 3 + formatter(list_header) + '\n(Max, 50 characters) \n')

        for i in response:
            print(formatter(i))

    if failed_search:
        print(f"\nCouldn't find these companies: {str(failed_search)}")

    save = input('\nWould you like to save this search? (y or n) \nResponse: ')
    if save is 'y':
        save_as = str(input('\nHow would you like to name the save?: \nResponse: '))
        saver(save_as)

    repeat = str(input('\nWould you like to make another search? (y or n) \nResponse:'))
    if repeat is not 'y':
        break

    failed_search.clear()
    response.clear()
    print('\n' * 50)
