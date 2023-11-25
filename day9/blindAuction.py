from replit import clear
from blindAuctionArt import logo

print(logo)

bidder = {}


def highest_bidder(bidding_record):
    winner = max(bidding_record, key=bidding_record.get)
    highest_bid = bidding_record[winner]

    print(f"The winner is {winner} with a bid of ${highest_bid}")


bidding = True
while bidding:
    name = input("What is your name? ")
    price = float(input("What is your bid? "))  # Convert input to float
    bidder[name] = price

    bid_again = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if bid_again == "no":
        bidding = False
        clear()
    elif bid_again == "yes":
        clear()

highest_bidder(bidder)
