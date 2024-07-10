# Star Wars API
Algorithm, API, JavaScript

The “0. Star Wars Characters” project requires you to interact with an external API to <br>fetch and display information about Star Wars characters based on the movie ID <br>provided as an argument. To successfully complete this project, you need to be familiar<br> with several key concepts related to web programming, API interaction, and <br>asynchronous programming in JavaScript.<br>

### Concepts Needed:<br>
1. HTTP Requests in JavaScript:<br>
    * Understanding how to make HTTP requests to external services using the ```request``` module or alternatives like ```fetch``` in Node.js.
    * [A Complete Guide to Making HTTP Requests in Node.js](https://intranet.alxswe.com/rltoken/iRse23lnV4gAsD9JJTJMMQ)
2. Working with APIs:<br>
    * Understanding the basics of RESTful APIs and how to interact with them.
    * Parsing JSON data returned by APIs.
    * [Working with APIs in JavaScript](https://intranet.alxswe.com/rltoken/KyGS_uB68mLaP5irrH8JVA)
3. Asynchronous Programming:<br>
    * Managing asynchronous operations with callbacks, promises, and <br>async/await syntax.
    * Handling API response data asynchronously.
    * [Asynchronous Programming in JavaScript](https://intranet.alxswe.com/rltoken/tdKMGJrRstCkXSReNfRFpQ)
4. Command Line Arguments in Node.js:<br>
     Using the ```process.argv``` array to access command-line arguments passed <br> to a Node.js script.
    * [How to Parse Command Line Arguments in Node.js](https://intranet.alxswe.com/rltoken/oWBOWJZLF_D9GfOydPz6Kg)
5. Array Manipulation and Iteration:<br>
    * Iterating over arrays and manipulating data structures to format and display <br> character names.
    * [JavaScript Array Methods](https://intranet.alxswe.com/rltoken/8zdG036OYYvVco_AZTExoA)

- [Mock Technical Interview](https://intranet.alxswe.com/rltoken/du6hlPQm6qi4A7eEursNhQ)

## General Requirements
> - Allowed editors: ```vi, vim, emacs```
> - All your files will be interpreted on Ubuntu 20.04 LTS using ```node``` (version 10.14.x)
> - All your files should end with a new line
> - The first line of all your files should be exactly ```#!/usr/bin/node```
> - A ```README.md``` file, at the root of the folder of the project, is mandatory
> - Your code should be ```semistandard``` compliant. [Rules of Standard](https://intranet.alxswe.com/rltoken/9P3gH5mVdJCEKL87E-IMaA) + [semicolons on top](https://intranet.alxswe.com/rltoken/WjMvQfBMKBdsNUuHyg55Dw). Also as reference: [AirBnB style](https://intranet.alxswe.com/rltoken/Xp81RT-Sfi7uE_kNCSXunw)
> - All your files must be executable
> - The length of your files will be tested using ```wc```
> - You are not allowed to use ```var```


### More info
- Install Node 10
``` {
    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs
}```

- Install semi-standard
[Documentation](https://intranet.alxswe.com/rltoken/WjMvQfBMKBdsNUuHyg55Dw)
```$ sudo npm install semistandard --global```

- Install ```request``` module and use it
[Install request module and use it](https://intranet.alxswe.com/rltoken/BWz2gc45S-nZaxEY6GA6Zw)
``` {
    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules
}```

### Tasks
Star Wars Characters <br>
In your Repository ```alx-interview```, create a directory ```0x06-starwars_api``` <br> and in file ```0-starwars_characters.js``` write your code as instructed below.<br>
Write a script that prints all  characters of a Star Wars movie: 
 - The first positional argument passed is the Movie <br>ID - example: *3* = “Return of the Jedi”<br> 
 - Display one character name per<br> line **in the same order as the “characters” <br>list in the /films/ endpoint**
 - You must use the [Star wars API](https://intranet.alxswe.com/rltoken/gh_NaSUk9QlXHVoACFU-tg) 
 - You must use the ```request``` module |


#### Example output
```./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna```


**Author**
* Ikilai Doreen - [Demidorn](https://github.com/Demidorn)