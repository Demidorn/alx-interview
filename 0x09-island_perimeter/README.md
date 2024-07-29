# Island Perimeter

## Concepts Needed:
1. 2D Arrays (Matrices):
  * Accessing and iterating over elements in a 2D array.
  * Understanding how to navigate through adjacent cells (horizontally and <br> vertically).
2. Conditional Logic:
  * Applying conditions to determine whether a cell contributes to the perimeter<br> of the island.
3. Counting Techniques:
  * Developing a method to count the edges that contribute to the island’s <br>perimeter.
4. Problem-Solving Strategies:
  * Breaking down the problem into smaller tasks, such as identifying land cells<br> and calculating their contribution to the perimeter.
5. Python Programming:
  * Nested loops for iterating over grid cells.
  * Conditional statements to check the status of adjacent cells.
### Resources:
- **Python Official Documentation:**
  * [Nested Lists:](https://intranet.alxswe.com/rltoken/8SPalOgoGDWQChVbct0p1g) Understanding how to work with lists within lists in Python.
- **GeeksforGeeks Articles:**
  * [Python Multi-dimensional Arrays:](https://intranet.alxswe.com/rltoken/IYcYmeVlCfF-F7Szn1fzfQ) A guide to working with 2D arrays in Python effectively.
- **TutorialsPoint:**
  * [Python Lists:](https://intranet.alxswe.com/rltoken/TZ8UtQaRxN5cFf8c1TB-rw) Explains how to create, access, and manipulate lists in Python,<br>which is essential for working with a grid.
- **YouTube Tutorials:**
  * [Python 2D arrays and lists](https://intranet.alxswe.com/rltoken/H7SwlI_XYDpwYonNYKXQfg)

- [Mock Technical Interviews](https://intranet.alxswe.com/rltoken/9ZYjQgC9HvOLZiHxmgd89Q)

### General Requirements
> - Allowed editors: *vi, vim, emacs*
> - All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 <br> (version 3.4.3)
> - All your files should end with a new line
> - The first line of all your files should be exactly ```#!/usr/bin/python3```
> A ```README.md``` file, at the root of the folder of the project, is mandatory
> - Your code should use the ```PEP 8``` style (version 1.7)
> - You are not allowed to import any module
> - All modules and functions must be documented
> - All your files must be executable

## Tasks
Create a function ```def island_perimeter(grid):``` that returns the<br> perimeter of the island described in ```grid:```
- ```grid``` is a list of list of integers:
    * 0 represents water
    * 1 represents land
    * Each cell is square, with a side length of 1
    * Cells are connected horizontally/vertically (not diagonally).
    * ```grid``` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water <br>surrounding the island).

## Example
``` #!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
```

