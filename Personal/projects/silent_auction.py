import os
dict={}
#function for next entrys and checking if there are no entries
def entry():
    entry=input("If there are more entries yes/no: ")
    if(entry=='yes'):
        os.system('cls')
        bid()
    #cosidering winner if there are no more entries
    elif(entry=='no'):
        max_bid=max(dict.values())
        for i in dict:
            if(dict[i]==max_bid):
                print(f"Winner is {i} of a bid {dict[i]}.")
                break # used because if there are two people having same maximum bid, the person who auctioned first will wins
    else:
        print("Enter valid option i.e yes/no")
        bid()
# function for atleast one entry
def bid():
    name=input("Enter your name: ")
    bid=input("Enter bid: ")
    dict[name]=bid
    entry()
bid()

