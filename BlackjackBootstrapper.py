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
    hit = 0
    double = 0
    stand = 0
    n = 1000000
    for i in range(n):
        standTurn = p
        hitAndDouble = hitTurn(p)
        dealer = dealerTurn(d)
        if (hitAndDouble == 1000):
            hit -= 1
            double -= 2
        else:
            if (dealer == 1000):
                hit += 1
                double += 2
            else:
                if (dealer > hitAndDouble):
                    hit -= 1
                    double -= 2
                else:
                    hit += 1
                    double += 2
        if (dealer == 1000):
            stand += 1
        else:
            if (dealer > standTurn):
                stand -= 1
            else:
                stand += 1
                
    turns = [hit, double, stand]
    returnVals = ['hit', 'double', 'stand']
    returnString = 'Player Reccomendation: ' + returnVals[turns.index(max(turns))] + '. Values of [hit, double, stand]: ' + str(turns)
    return returnString
playerCount = int(input("What is the total count of the player? ")) #Takes user input
dealerCount = int(input("What is the dealer show card value? "))
print(recommendation(playerCount, dealerCount))
