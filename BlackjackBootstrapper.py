import random
counts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #Array of possible hit values
random.shuffle(counts) #Randomizes order of array
def dealerTurn(n): #Dealear function, standing on 17
    while (n < 17):
        n += counts[random.randint(0, 12)] #Adds a random value from cards
    if (n > 21):
        return 1000
    else:
        return n
def hitTurn(p):
    p += counts[random.randint(0, 12)]
    if (p > 21):
        return 1000
    else:
        return p
def recommendation(p, d):
    hit = 0 #Keep track of wins/losses when hitting
    double = 0 #Keep track of wins/losses when doubling
    stand = 0 #Keep track of wins/losses when standing
    n = 1000000 #Number of simulations to be run
    for i in range(n):
        standTurn = p #Stores standing value
        hitAndDouble = hitTurn(p) #Stores hit and double value
        dealer = dealerTurn(d) #Runs through a dealer turn, standing on a 17
        if (hitAndDouble == 1000): #Checks if hit/double busted
            hit -= 1 #Adds a loss to the counters
            double -= 2
        else:
            if (dealer == 1000): #Checks if dealer busted
                hit += 1 #Adds a win to the counters
                double += 2
            else:
                if (dealer > hitAndDouble):
                    hit -= 1
                    double -= 2
                else:
                    hit += 1
                    double += 2
        if (dealer == 1000): #Checks if dealer busted
            stand += 1 #Adds a win to the counter
        else:
            if (dealer > standTurn): #Compares standing value to dealer value
                stand -= 1 #Adds a loss
            else:
                stand += 1 #Adds a win
                
    turns = [hit, double, stand]
    returnVals = ['hit', 'double', 'stand']
    return returnVals[turns.index(max(turns))], turns
playerCount = int(input("What is the total count of the player?")) #Takes user input
dealerCount = int(input("What is the dealer show card value?"))
recommendation(playerCount, dealerCount)
