print("Welcome to blind auction: \n")
bids={}
biddingFinished = False

def findHigherBidder(biddingRecord):
    highestBid = 0
    winner =""
    for bidder in biddingRecord:
        bidAmount = biddingRecord[bidder]
        if bidAmount >highestBid:
            highestBid = bidAmount
            winner =bidder
    print(f"{winner} is the highest bidder")
    
    
while not biddingFinished:
    name = input("What is your name: ")
    bid = int(input("Enter the bid amount: $"))
    bids[name] = bid
    decision = input("Type 'y' if any user wants to bid and 'n' to end: ")
    if decision =="n":
        biddingFinished = True
        findHigherBidder(bids)




    