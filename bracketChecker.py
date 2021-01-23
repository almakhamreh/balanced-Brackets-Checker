# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 11:09:46 2021

@author: Ahmad Almakhamreh
"""



class Stack:
   def __init__(self):
      self.__mystack = []

   def push(self,item):
      self.__mystack.append(item)

   def pop(self):
      return self.__mystack.pop()

   def isEmpty(self):
      return self.__mystack == []

def isBalanced(myString):
   s = Stack()
   i = 0
   symbol_pairs = {
       '(': ')',
       '[': ']',
       '{': '}',
   }

   openers = symbol_pairs.keys()
   while i < len(myString):
        symbol = myString[i]

        if symbol in openers:
            s.push(symbol)
        else:  # The symbol is a closer

            # If the Stack is already empty, the symbols are not balanced
            if s.isEmpty():
                return "Unbalanced"

            # If there are still items in the Stack, check for a mis-match.
            else:
                top_item = s.pop()
                if symbol != symbol_pairs[top_item]:
                    return "Unbalanced"

        i += 1

   if s.isEmpty():
        return "Balanced"
   else:
      return "Unbalanced"  # Stack is not empty so symbols were not balanced


def main():

   print("This program checks if a symbol string is balanced or not (True if balanced, False otherwise.)")
   print("EX: {([])} is a balanced string because the number of open symbols equals the closed symbols, and the open symbols have to come first.")
   print("the accepted symbols are {}, (), [] ")

   # print(isBalanced("((())){}{}()"))
   myString = input("enter a the symbols: ")

   print(isBalanced(myString))


if __name__ == "__main__" : main()