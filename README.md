# Graph Coloring
This is a Python 3.5 application designed to solve the planar graph coloring problem.

The graph coloring problem is simple: how do you color a planar graph with the least ammount of colors, such as that 2 adjacent vertices don't have the same color?

This application implements 4 solutions:
- Simple backtracking;
- Backtracking with forward checking;
- Backtracking with forward checking and least remaining values;
- Backtracking with forward checking, least remaining values and degree verification for decision taking in draw situations.

Usage: "python main.py input_file output_file [performance_file]".

The first 2 arguments are obligatory: the input file and the output file of the solution.  
The third parameter is optional: you can pass a performance file if you want to test the performance of the different solutions implemented. Note that, if this parameter is not given, these tests will not be run.
