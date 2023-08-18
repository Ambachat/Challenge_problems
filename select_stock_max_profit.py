#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 20:10:03 2023

@author: ambarish

An investor saved some money and wants to invest in stock. They want to buy at most one share per company from 
a number of stocks. Total invested cannot exceed the saving.  
He has the future values of those stocks after one year. 
We need to write a python code to determine max profit that can be earned after a year. 
Input for python function is the saving amount, current value list and future values list.
Example is
Saving=250
Current_values=[175, 133,109,210,97]
Future_values=[200,125,128,228,133]
Total profit is (133-97)+(128-109)=55
"""
#################################### New ####################################

def max_profit(saving, current_values, future_values):

  """
  This function takes three arguments: saving, current_values, and future_values.
  saving is the amount of money that is available to invest.
  current_values is a list of the current values of the stocks.
  future_values is a list of the future values of the stocks.

  The function returns the maximum profit that can be earned after a year by investing in stocks.
  """

  # Create a list of the profits that can be made by investing in each stock.
  profits = []
  for i in range(len(current_values)):
    profits.append(future_values[i] - current_values[i])

  # Create a list of the indices of the stocks that have the highest profits.
  best_stocks = []
  best_stocks = sorted(range(len(profits)), key=lambda i: profits[i], reverse=True)

  # Calculate the maximum profit that can be earned.
  max_profit = 0
  for i in range(len(best_stocks)):
    if saving >= current_values[best_stocks[i]]:
      max_profit += profits[best_stocks[i]]
      saving -= current_values[best_stocks[i]]

  return max_profit


saving = 300
current_values = [175, 133, 109, 210, 97]
#current_values =[200, 125, 128, 228, 133]
future_values = [130, 125, 128, 228, 132]
result = max_profit(saving, current_values, future_values)
print("Maximum profit:", result)
#max_profit(300,current_values,future_values)

################################################################

