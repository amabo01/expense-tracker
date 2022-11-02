# -*- coding: utf-8 -*-
"""expensetracker.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CHAXmBAATLeo6bXpcR0X2DvPmLaK5H-L
"""

import numpy as np
import pandas as pd
class expenseTracker():
  def __init__(self, income):
    self.income = income
  def addExpense():
    income = input("Add income for this month: ")
    food = input("Add food expense for this month: ")
    ent = input("Add entertainment expense for this month: ")
    util = input("Add utility expense for this month: ")
    transport = input("Add transport expense for this month: ")
    misc = int(income) - int(food) - int(util) - int(ent) - int(transport)
    #return food, ent, util, transport, misc
    expenses = [['income', int(income)], ['food', int(food)], ['entertainment', int(ent)], ['utility', int(util)], ['transport', int(transport)], ['miscallaneous', int(misc)]]
    df = pd.DataFrame(expenses, columns=['Expense', 'Amount'])
    print(df)
  addExpense()