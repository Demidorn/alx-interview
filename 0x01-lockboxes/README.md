# Lockboxes
- Algorithm, Python

## Concepts Needed:
- Lists and List Manipulation:<br>
Understanding how to work with lists, including accessing elements,<br> iterating over lists, andmodifying lists dynamically.
- Graph Theory Basics:<br>
Although not explicitly required, knowledge of graph theory (especially <br>concepts related totraversal algorithms like Depth-First Search or Breadth-First Search)<br> can be very helpful insolving this problem, as the boxes and keys can be <br>thought of as nodes and edges in a graph.
- Algorithmic Complexity:<br>
Understanding the time and space complexity of your solution is important,<br> as it can help inwriting more efficient algorithms.
- Recursion:<br>
Some solutions might require a recursive approach to traverse through the boxes and keys.
- Queue and Stack:<bbr>
Knowing how to use queues and stacks is crucial if implementing a breadth-first<br> search (BFS)or depth-first search (DFS) algorithm to traverse through<br> the keys and boxes.
- Set Operations:<br>
Understanding how to use sets for keeping track of visited boxes and available<br>keys canoptimize the search process.

- [Mock Technical Interview](/rltoken/TJ0FJhWeEGolIqMpwBn7Pg)

### General requirements
> - Allowed editors: **vi, vim, emacs**
> - All your files will be interpreted/compiled on **Ubuntu 20.04 LTS** <br >using
*python3 (version 3.4.3)*
> - All your files should end with a new line
> - The first line of all your files should be exactly ```#!/usr/bin/python3```
> - A **README.md** file, at the root of the folder of the project, is mandatory
> - Your code should be documented
> - Your code should use the __PEP 8__ style (version 1.7.x)
> - All your files must be executable

## TASK
> You have ```n``` number of locked boxes in front of you. Each box is numbered <br>sequentially from **0** to **n - 1** and each box may contain keys to the<br> other boxes.<br>
> Write a method that determines if all the boxes can be opened.
> - Prototype: ```def canUnlockAll(boxes)```
> - __boxes__ is a list of lists
> - A key with the same number as a box opens that box
> - You can assume all keys will be positive integers
>> - There can be keys that do not have boxes
> - The first box ***boxes[0]*** is unlocked
> - Return *True* if all boxes can be opened, else return *False*