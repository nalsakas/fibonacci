# Fibonacci number generator

## Problem Statement
For a given number n {0,1,2,3,...}, determine corresponding Fibonacci number. Use depth first and breadth first algorthms. 

## Solutuion
Implementation uses bfs and dfs alorithms with minimal space complexity.
Algorithms only keeps track of the last two Fibonacci numbers i and j.
For dfs algorithm, previous values are store in stack frame but doesn't needed.
For bfs algorithm, previous values are overwritten in for loop.
Algorithms only return last Fibonacci number (j) for a given number (n).

fib(1) = 0
fib(2) = 1
fib(3) = 1
fib(4) = 2
fib(5) = 3
fib(6) = 5 
...