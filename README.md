# Assignment 6

## Description
Using classes and enums to determine mortgage payment options for clients.

## Author
Dongok yang

## Assignment
Assignment 6: Defining and using classes.
Created Enum: Enums are created to utilize the interest rates and payment frequency. Using enum helps users easily to understand and maintain code.

Created Class: A mortgage class includes functions such as setting the value of the loan amount, interest rate, amortization period, and payment frequency. and also It calculated desired amount of payments.  By making Class, the file is easier to understand and maintain.

Created Unit Test Class: A Mortgage tests class is made to verify that every functions made in mortgage class does desired tasks and verify it doesn't show error. doing this improve reliability of the codes and helps user to test each function seperately. 

Updated Client Program: The main.py program is made to get data from pixell_river_mortgages.txt and prints calculated payments, mortgage amount, rate, amortization of that data. It also shows error when data has invalid data or the file is missing. major function used in this file is seperated to mortgage.py and the values this file uses such as mortage rate, and amortization is seperated in pixell_lookup.py. By seperating major functions, this program improves readability of codes and help user to easily manage and maintain codes. 

Exceptions handling: When data from pixell_river_mortgages.txt have invalid loan amount, interest rates, amortization, main.py file shows error message. and also when the file is missing, it shows exception.