# Making Change
Algorithm  Python

## Concepts Needed:
1. Greedy Algorithms:
  - Understanding how greedy algorithms work and why they are suitable for<br> the coin change problem.<br>
  - Recognizing the limitations of greedy algorithms and scenarios where<br> they might not provide the optimal solution.
2. Dynamic Programming:
  - Basic principles of dynamic programming as a method to solve <br>optimization problems.
  - The concept of overlapping subproblems and optimal substructure in the <br> context of the coin change problem.
3. lgorithmic Complexity:
  - Analyzing the time and space complexity of algorithms.
- Striving for solutions with lower complexity to meet runtime constraints.
4. Problem-Solving Strategies:
  - Breaking down the problem into smaller, manageable sub-problems.
  - Iterative vs recursive approaches to dynamic programming.
5. Python Programming:
  - Manipulating lists and using list comprehensions.
  - Implementing functions with efficient looping and conditional statements.

### Resources:
- Python Official Documentation:
  * [More Control Flow Tools (for loops, if statements)](https://intranet.alxswe.com/rltoken/oVyaCk8erLwLPj96P-qlCw)
- GeeksforGeeks Articles:
  * [Coin Change | DP-7](https://intranet.alxswe.com/rltoken/iQPaO5JhI-BtuZdm6HIVCQ)
  * [Greedy Algorithm to find Minimum number of Coins](https://intranet.alxswe.com/rltoken/FsBN0oeRp0FpyU8sMd4UiA)
- YouTube Tutorials:
  *b[Dynamic Programming - Coin Change Problem](https://intranet.alxswe.com/rltoken/qFEdwwtAVyJr9NLHDZDsUQ) for a visual and step-by-step<br> explanation of the dynamic programming approach.

- [Mock Technical Interview](https://intranet.alxswe.com/rltoken/ktLaKIVRkq_-byFO-_-aGg)


### General
> - Allowed editors: *vi, vim, emacs*
> - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using ```python3``` (version 3.4.3)
> - All your files should end with a new line
> - The first line of all your files should be exactly ```#!/usr/bin/python3```
> - A ```README.md``` file, at the root of the folder of the project, is mandatory
> - Your code should use the ```PEP 8``` style (version 1.7.x)
> - All your files must be executable


## Change comes from within
Given a pile of coins of different values, determine the fewest number of coins needed<br>to meet a given amount total.
  * Prototype: ```def makeChange(coins, total)```
  * Return: fewest number of coins needed to meet ```total```
    - If _total_ is 0 or less, return __0__
    - If _total_ cannot be met by any number of coins you have, return __-1__
- ```coins``` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than __0__
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

# Test File
``` #!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))
```

