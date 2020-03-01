# Algorithms

## Backtracking

"Backtracking is a general algorithm for finding all solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate as soon as it determines that the candidate cannot possibly be completed to a valid solution." - Wikipedia

### Knight's Tour

A knight's tour is a sequence of moves of a knight on an N*N chessboard such that the knight visits every square only once.

### Rat in the Maze

In this problem, there is a given maze of size N x N. The source and the destination location is top-left cell and bottom right cell respectively. The objective is the find the path from the source to the destination if one exists.

### N Queen Problem

N Queen is the problem of placing N chess queens on an N×N chessboard such that no two queens attack each other.

### Subset Sum Problem

Given a set of integers and an integer s, is there a non-empty subset whose sum is s?

### Graph Coloring

'm Coloring Problem'. Given an undirected graph and a number m, determine if the graph can be colored with at most m colors such that no two adjacent vertices of the graph are colored with same color.

### Hamiltonian Cycle

A Hamiltonian path is a path in an undirected or directed graph that visits each vertex exactly once. A Hamiltonian cycle (or Hamiltonian circuit) is a Hamiltonian path that is a cycle. Problem is to determine whether a and cycle exists in a graph using its adjacency matrix.

### Sodoku

Sudoku is a logic-based, combinatorial number-placement puzzle. The objective is to fill a N×N grid with digits so that each column, each row, and each of the N N^(1/2)×N^(1/2) subgrids that compose the grid contain all of the digits from 1 to N.
This solver can solve any N*N board (e.g 9x9, 16x16 etc..)

Sodoku GUI designed using Tkinter for a 9x9 board. Can play game and also visualise the backtracking algorithm in progress.

## Dynamic Programming

### Fibonacci

Finding the nth fibonacci number in the sequence. The Fibonacci sequence is the sum of the two preceding numbers, starting from 0 and 1.

### Ugly Numbers

Ugly numbers are numbers whose only prime factors are 2, 3 or 5. Using dynmaic programming to find the nth ugly number.

### Catalan Numbers

The Catalan numbers form a sequence of natural numbers that occur in various counting problems, often involving recursively-defined objects. 

Writing a program to find the nth Catalan Number.

## Numerical Analysis

### Bisection Method

The bisection method is a root-finding method that applies to any continuous functions for which one knows two values with opposite signs. Related to Intermediate Value Theorem. If there is a root of f(x) on the interval [a, b] then f(a) and f(b) must have a difference sign i.e. f(a)f(b) < 0

Implementation of this method in python to the root of f(x) on an interval if it exists.

### Newton's Method

Newton's method, also known as the Newton–Raphson method, in Python. Named after Isaac Newton and Joseph Raphson, is a root-finding algorithm which produces successively better approximations to the roots (or zeroes) of a real-valued function.

### Secant Method

The secant method root-finding algorithm in Python. The method uses a succession of roots of secant lines to better approximate a root of a function f.

### Gaussian Elimination

Gaussian elimination, also known as row reduction, is an algorithm in linear algebra for solving a system of linear equations. Program illustrates how to solve a system using this method in python.

