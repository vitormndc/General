# General

Thsi is just a place where i store my modules and scripts as a backup, feel free to use then.


CODE SAMPLE:

  List_cleaner:
  ```c
  import list_cleaner

  remove = ['/', ',', '>', '<', ':', ';', ')', '(', '\n', '\\']
  name_list = ['joao/', 'ana,', 'pedro:', 'hope)', 'ema\n']

  name_list = list_cleaner.lc(name_list, remove)

  print(name_list)
  ```
  The output would be
  ```c
  ['joao', 'ana', 'pedro', 'hope', 'ema']
  ```

