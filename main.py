from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.


bid_dictionary = {}
more_bids = 'yes'
winning_bid = 0

while more_bids != 'no':
  print(logo)
  name = input("What is your name?")
  bid  = int(input("What is your bid?"))
  bid_dictionary[name] = bid
  more_bids = input("Enter 'yes' for more bids, 'no' if there are no more bids.")
  clear()

for key in bid_dictionary:
  if winning_bid < bid_dictionary[key]:
    winner = key
    winning_bid = bid_dictionary[key]
print(logo)
if more_bids == 'no':
    print(f"The auction winner is {winner} and the winning bid is {winning_bid}")



