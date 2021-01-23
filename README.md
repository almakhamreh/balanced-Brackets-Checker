# balancedBrackets
Simple python program to check weather a string has balanced brackets

This program checks balanced brackets using a stack in python.

Algorithm:

    1. traverse the string

    2. when you encounter an opening bracket i.e.  (, {, \[ push it into the stack

    3. when you encounter a closing bracket, check to see if the top item on the stack is its matching opener. if they are a pair continue, return false (unbalanced) otherwise

    4. if you finished traversing the string & the stack is empty, return true (Balanced)

    5. if the stack is not empty after traversing the string return false (unbalanced)
