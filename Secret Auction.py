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
    money = input("How much do you want to bid?\n£")
    enter_bid(bidder=name,amount=money)
    add_bid = input("Are there other users who want to bid? Type Yes or No").lower()
    if add_bid == "no":
        end_auction = True
    else:
        os.system('cls||clear')

#RESULTS LOOP
top_bid = ""
for bid in bids:
    if bid > top_bid:
        top_bid = bid

print(f"The winner is {top_bid} with a bid of £{bids[top_bid]}")