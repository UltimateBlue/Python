import os
bidders = []
anotherBidder = True

os.system('cls' if os.name=='nt' else 'clear')
while anotherBidder:
    fname = input("What's your name: ")
    bd = input("What's your bid? $")
    while not bd.isdecimal():
        print("Invalid value!!!\n try again...")
        bd = input("What's your bid? $")
    bid = int(bd)
    others = input("Is there another bidder? (Y/N)").lower()
    if others == 'n':
        anotherBidder = False
    os.system('cls' if os.name=='nt' else 'clear')
    bidders.append({fname: bid})
    # bidders[i]['fname'] = fname
    # bidders[i]['bid'] = bid
winner = []
maxBid = 0
for entry in bidders:
    val = list(entry.values())[0]
    if  val > maxBid:
        maxBid = val
        winner = []
        winner.append(list(entry.keys())[0])
    elif val == maxBid:
        winner.append(list(entry.keys())[0])
    else:
        continue

if len(winner) > 1:
    print("winners are: ")
    for w in winner:
        print(w + ', ')
    print(f'with ${maxBid} bid')
else:
    print(f'winner is: {winner[0]} with ${maxBid} bid')
    print()

