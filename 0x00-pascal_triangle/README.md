# 0x00. Pascal's Triangle
## Must Know
To successfully complete this project, you should revise the following Python concepts:

1. Lists and List Comprehensions:<br>
Understand how to create, access, modify, and iterate over lists.<br>
Utilize list comprehensions for more concise and readable code,<br> especially for generating rows of Pascal’s Triangle.<br>
2. Functions:
Know how to define and call functions.<br>
Pass parameters and return values, particularly how to return<br> a list of lists representing Pascal’s Triangle.<br>
3. Loops:<br>
Use for and while loops to iterate through sequences.<br>
Nested loops may be necessary for generating each row and <br>calculating the values of Pascal’s Triangle.<br>
4. Conditional Statements:<br>
Apply if, elif, and else conditions to implement logic based on <br>the position within Pascal’s Triangle (e.g., the edges of the triangle <br>always being 1).<br>
5. Recursion (Optional):<br>
While not strictly necessary, understanding recursion can provide<br> an alternative approach to generating Pascal’s Triangle.<br>
Recognize base cases and recursive cases for a function that <br>generates the triangle’s rows.<br>
6. Arithmetic Operations:<br>
Perform addition, a fundamental operation for calculating each <br>element of Pascal’s Triangle as the sum of the two elements directly above it.<br>
7. Indexing and Slicing:<br>
Access elements and slices of lists, crucial for identifying and<br> summing the correct elements when constructing each row of the triangle.<br>
8. Memory Management:<br>
Be mindful of how lists are stored and copied, especially when creating <br>new rows based on the values of the previous row.<br>
9. Error and Exception Handling (Optional):<br>
Use try-except blocks as needed to handle potential errors, such as<br> invalid input types or values.<br>
10. Efficiency and Optimization:<br>
Consider the time and space complexity of different approaches to generating <br>Pascal’s Triangle.<br>
Evaluate and apply optimizations to improve the performance of the solution.<br>
By revisiting these concepts, you will be well-prepared to tackle the challenges of implementing Pascal’s Triangle in Python, applying both your<br> mathematical understanding and programming skills to develop <br>an efficient and effective solution.<br>

### Tasks
> - 0. Pascal's Triangle
> Create a function def pascal_triangle(n): 
>> - that returns a list of lists of integers representing the <br>Pascal’s triangle of n:
>> - Returns an empty list if n <= 0
>> You can assume n will be always an integer