# Prime Game

## Concepts Needed:
1. Prime Numbers:
  * Understanding what prime numbers are.
  * Efficient algorithms for identifying prime numbers within a range.
2. Sieve of Eratosthenes:
  * An efficient algorithm for finding all prime numbers up to any given limit, which<br> can be particularly useful for this task.
3. Game Theory:
  * Basic principles of competitive games where players take turns and the <br>concept of optimal play.
  * Understanding win conditions and strategies that lead to a win or loss.
4. Dynamic Programming/Memoization:
  * Using previous results to make future calculations faster, potentially necessary <br>for optimizing the solution for multiple rounds of the game.
5. Python Programming:
  * Loops and conditional statements for implementing game logic and algorithms.
  * Arrays and lists for storing the integers and tracking removed numbers.
## Resources:
- Prime Numbers and Sieve of Eratosthenes:
  * [Khan Academy: Prime Numbers:](https://intranet.alxswe.com/rltoken/IUKEfGVroNza8u37x0lEzw) Introduction to prime numbers.
  * [Sieve of Eratosthenes in Python:](https://intranet.alxswe.com/rltoken/sVjdrNQEaErO_qRYsVMTEg) A step-by-step guide to implementing the sieve <br>algorithm in Python.
- Game Theory Basics:
  * [Game Theory Introduction:](https://intranet.alxswe.com/rltoken/lH4z--LnsuXYKh23Ji9Elw) A simple explanation of game theory and<br> strategic decision-making.
- Dynamic Programming:
  * [What Is Dynamic Programming With Python Examples: ](https://intranet.alxswe.com/rltoken/W6T0RxWaFG3GisPxLLNYkQ)An introduction to dynamic programming<br> with Python examples.
- Python Official Documentation:
  * [Python Lists:](https://intranet.alxswe.com/rltoken/JTEGXnSDYDp8yblD9y86eg) Managing lists in Python, useful for tracking the game state.

- [Mock Technical Interview](https://intranet.alxswe.com/rltoken/h176d28650FiZFWhWw9_Sg)

### General Requirements
> - Allowed editors: *vi, vim, emacs*
> - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
> - All your files should end with a new line
> - The first line of all your files should be exactly ```#!/usr/bin/python3```
> - A ```README.md``` file, at the root of the folder of the project, is mandatory
> - Your code should use the PEP 8 style (version 1.7.x)
> - All your files must be executable

## TASK
**Prime Game**<br>
Maria and Ben are playing a game. Given a set of consecutive <br>integers starting from 1 up to and including n, they take turns <br> choosing a prime number from the set and removing that number <br>and its multiples from the set. The player that cannot make <br>a move loses the game.<br>
They play x rounds of the game, where n may be different for <br>each round. Assuming Maria always goes first and both players <br>play optimally, determine who the winner of each game is.
- Prototype: ```def isWinner(x, nums)```
- where ```x``` is the number of rounds and ```nums``` is an array of ```n```
- Return: name of the player that won the most rounds
- If the winner cannot be determined, return ```None```
- You can assume ```n``` and ```x``` will not be larger than 10000
- You cannot import any packages in this task
**Example:**
  - x = 3, nums = [4, 5, 1]<br>
First round: 4
  - Maria picks 2 and removes 2, 4, leaving 1, 3
  - Ben picks 3 and removes 3, leaving 1
  - Ben wins because there are no prime numbers left for Maria to choose<br>
Second round: 5
  - Maria picks 2 and removes 2, 4, leaving 1, 3, 5
  - Ben picks 3 and removes 3, leaving 1, 5
  - Maria picks 5 and removes 5, leaving 1
  - Maria wins because there are no prime numbers left for Ben to choose<br>
Third round: 1
  - Ben wins because there are no prime numbers for Maria to choose<br>
**Result: Ben has the most wins**

### Test file __main_0.py__
``` #!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```


