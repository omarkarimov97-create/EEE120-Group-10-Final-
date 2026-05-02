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


## Example
Input: A=1, B=1, C=1, W=0  
Output: Eligible
