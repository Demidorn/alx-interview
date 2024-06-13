# Minimum Operations

## Concepts Needed:
> - Concepts Needed:<br>
>> Familiarity with dynamic programming can help in breaking <br>down the problem into simplersubproblems and building up the solution.
> - Prime Factorization:<br>
>> Understanding how to perform prime factorization is crucial since<br> the problem can be reducedto finding the sum of the <br> prime factors of the target number ```n```.
> - Code Optimization:<br>
>> Knowing how to approach problems from an optimization perspective <br> can be useful in findingthe most efficient solution.
> - Greedy Algorithms:<br>
>> The problem can also be approached with greedy algorithms,<br> choosing the best option ateach step.
> - Basic Python Programming:<br>
>> Proficiency in Python, including loops, conditionals, and functions,<br> is necessary to implementthe solution.<br>
- [Mock Technical Interview](/rltoken/HX0vuVl1V-9T4vvh8NDCyw)

### General requirement
> - Allowed editors: **vi, vim, emacs**
> - All your files will be interpreted/compiled on **Ubuntu 20.04 LTS** usingb__python3__ (version 3.4.3)
> - All your files should end with a new line
> - The first line of all your files should be exactly
```#!/usr/bin/python3```
> - A ```README.md```file, at the root of the folder of the project, <br> is mandatory
> - Your code should be documented
> - Your code should use the *PEP 8* style (version 1.7.x)
> - All your files must be executable

## TASK
> In a text file, there is a single character ```H```. Your text editor <br>can execute only two operations in this file: CopyAll and Paste <br>. Given a number ```n```, write a method that calculates the <br> fewest number of operationsneeded to result in exactly ```n``` ```H```<br> characters in the file.
> - Prototype: ```def minOperations(n)```
> - Returns an integer
> - If ```n``` is impossible to achieve, return ```0```
#### Example:<br>
n = 9<br>
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH<br>
Number of operations: 6
