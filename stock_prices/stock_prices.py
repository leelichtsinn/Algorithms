#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # create variable to store max profit
    # loop through prices list starting from 1 index
    # find profit
    max_profit = 0
    for i in prices[1:]:
        for j in prices[i:]:
            temp_val = prices[i] - prices[i - 1]
            if max_profit < temp_val:
                max_profit = temp_val
            return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
