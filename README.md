# General

This is just a place where I store my modules and scripts as a backup, feel free to use then.

---
CODE SAMPLES:
---

__List_cleaner:__
  ```c
  import list_cleaner

  remove = ['/', ',', ')', ':', '\n']
  name_list = ['joao/', 'ana,', 'pedro:', 'hope)', 'ema\n']

  name_list = list_cleaner.lc(name_list, remove)

  print(name_list)
  ```
The output would be
  ```c
  ['joao', 'ana', 'pedro', 'hope', 'ema']
  ```
---
  
  __Stock_prices (WebScrapper):__
  
  Open in cmd the .py file
  ```
  py stock_prices.py
  ```
  Select the option you want, if you chose to do a new search type in the abbreviation of the companies you want to search (they can be separated using spaces, commas or both)
  ````
  What would you like to do?
1. Make a new search
2. Use saved stock list in a new search
Response: 1

Which stocks would you like to search? (e.g., TSLA, AAPL, FB)
Response:tsla, aapl, fb, googl, ndaq



100%|████████████████████████████████████████████████████████████████████████████████████| 5/5 [00:04<00:00,  1.05it/s]



Company name                                           Symbol         Stock Price         Today fluctuation
(Max, 50 characters)

Tesla, Inc.                                            TSLA           $246.70             ▲  11.16 %
Apple Inc.                                             AAPL           $223.72             ▲  7.02 %
Facebook, Inc.                                         FB             $188.49             ▲  2.32 %
Alphabet Inc.                                          GOOGL          $1220.98            ▲  15.28 %
Nasdaq, Inc.                                           NDAQ           $98.18              ▲  0.03 %

Would you like to save this search? (y or n)
Response: y

How would you like to name the save?:
Response: standart

Would you like to make another search? (y or n)
Response:n
  ````
if you decide to save the search you can run the script again and select the saved file and re-do the search like this:
````
What would you like to do?
1. Make a new search
2. Use saved stock list in a new search
Response: 2

Saved searches:
standart: TSLA, AAPL, FB, NDAQ, GOOGL

Please type a save to load: standart



100%|████████████████████████████████████████████████████████████████████████████████████| 5/5 [00:04<00:00,  1.01it/s]



Company name                                           Symbol         Stock Price         Today fluctuation
(Max, 50 characters)

Tesla, Inc.                                            TSLA           $246.70             ▲  11.16 %
Apple Inc.                                             AAPL           $223.72             ▲  7.02 %
Facebook, Inc.                                         FB             $188.49             ▲  2.32 %
Nasdaq, Inc.                                           NDAQ           $98.18              ▲  0.03 %
Alphabet Inc.                                          GOOGL          $1220.98            ▲  15.28 %
````

---
