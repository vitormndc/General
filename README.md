############# General

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
  
  __Stock_prices:__
  
  Open in cmd the .py file
  ```
  py stock_prices.py
  ```
  Type in the abbreviation of the companies you want to search (they can be separated using spaces, commas or both)
  ````
  Which stocks would you like to search? (e.g., TSLA, AAPL, FB):
  tsla, aapl, fb, ano, asa
  ````
  the output should look like this
  ````
  Company name                                      Symbol         Stock Price         Today fluctuation 
  (Max, 50 characters) 

  Tesla, Inc.                                       TSLA           $214.05             ▲  2.65 %
  Apple Inc.                                        AAPL           $206.77             ▲  4.126 %
  Facebook, Inc. Class A                            FB             $180.49             ▲  2.74 %
  ASA  Gold and Precious Metals Limited             ASA            $13.23              ▼  0.08 %



  Couldn't find these companies: ['ANO']
  ````
---
