#IMPORT + FUCT
import os
from art import logo
print(logo)
bids = {}
def enter_bid(bidder,amount):
    bids[bidder] = amount
 
#BIDDING LOOP
end_auction = False
while not end_auction:
    name = input("What is your name?\n")
    money = int(input("How much do you want to bid?\n£"))
    enter_bid(bidder=name,amount=money)
    add_bid = input("Are there other users who want to bid? Type Yes or No").lower()
    if add_bid == "no":
        end_auction = True
    else:
        os.system('cls||clear')

#RESULTS LOOP
top_bid = 0
winner = ""
for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > top_bid: 
      top_bid = bid_amount
      winner = bidder

print(f"The winner is {winner} with a bid of £{top_bid}")