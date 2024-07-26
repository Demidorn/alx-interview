# Log Parsing

## Concepts Needed:
  1. File I/O in Python:
    * Understand how to read from __sys.stdin__ line by line.
    * [Python Input and Output](https://intranet.alxswe.com/rltoken/f7U2MDsBT_rd9AfUUaqVnQ)
  2. Signal Handling in Python:
    * Handling keyboard interruption (CTRL + C) using signal handling in Python.
    * [Python Signal Handling](https://intranet.alxswe.com/rltoken/1nDqPJe80rSD-NMulzjJBw)
  3. Data Processing:
    * Parsing strings to extract specific data points.
    * Aggregating data to compute summaries.
  4. Regular Expressions:
    * Using regular expressions to validate the format of each line.
    * [Python Regular Expressions](https://intranet.alxswe.com/rltoken/ZsD-YLisfaHFeMT_sZxX1Q)
  5. Dictionaries in Python:
    * Using dictionaries to count occurrences of status codes and accumulate file sizes.
    * [Python Dictionaries](https://intranet.alxswe.com/rltoken/JM-RpavKkb8yanxWEnNYJw)
  6. Exception Handling:
    * Handling possible exceptions that may arise during file reading and data processing.
    * [Python Exceptions](https://intranet.alxswe.com/rltoken/OA2PlryrYA2gyCCKIsdgUw)

  - [Mock Technical Interview](https://intranet.alxswe.com/rltoken/VlOaXKkbecRYdnTLaLU1lg)

### Requirements
> - Allowed editors: *vi, vim, emacs*
> - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using ```python3``` (version 3.4.3)
> - All your files should end with a new line
> - The first line of all your files should be exactly ```#!/usr/bin/python3```
> - A ```README.md``` file, at the root of the folder of the project, is mandatory
> - Your code should use the ```PEP 8``` style (version 1.7.x)
> - All your files must be executable
> - The length of your files will be tested using ```wc```
## Task<br>
Write a script that reads stdin line by line and computes metrics:<br>
  * Input format: ```<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <br> <file size>``` (if the format is not this one, the line must be skipped)<br>
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the <br> beginning:
    - Total file size: ```File size: <total size>```
    - where ```<total size>``` is the sum of all previous ```<file size> ```(see input format above)
    - Number of lines by status code:
      * possible status code: ```200, 301, 400, 401, 403, 404, 405``` and ```500```
      * if a status code doesn’t appear or is not an integer, don’t print anything for this status <br>code
      * format: ```<status code>: <number>```
      * status codes should be printed in ascending order

### Example
``` 
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
```

