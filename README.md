EEE120-Group-10-Final-
Final project for EEE120: Digital circuit and Python system to check exam eligibility
# EEE120 Final Project – Eligibility System

## Description
This project implements a digital logic system to determine student eligibility.

The system checks:
- Attendance (A)
- Assignments (B)
- Fees (C)
- Academic Warning (W)

## Logic
Eligible = (A AND B AND C) AND (NOT W)

## Python Extension
The Python version adds:
- Conditionally Eligible (if 2 out of 3 conditions are met)

## Demo
The system is demonstrated using:
- Digital circuit (CircuitVerse)
- Python simulation

## Circuit Link
https://circuitverse.org/users/426416/projects/final-group-10

## Example
Input: A=1, B=1, C=1, W=0  
Output: Eligible

## Boolean Expression
Eligible = A AND B AND C AND (NOT D)

## How to Run
1. Open main.py
2. Run the program
3. Change values of A, B, C, D to test different cases

## Example
Input:
A = True
B = True
C = True
D = False

Output:
Eligible = True
Conditional = False
Not Eligible = False

## Conclusion
This project demonstrates how digital logic design can be implemented both in hardware (CircuitVerse) and software (Python), producing identical results.

## Circuit Design
[Circuit](CircuitDesign.png)

## Python Output
[Python](Python_output.png)
[Python Code](Pythoncode.png)

## Truth Table
[Truth Table](TruthTable.jpg)
