import random as r
s = r.randint(0,100)
print("Enter Your guesses(2 Players)")
player1 = int(input("Player 1 : "))
player2 = int(input("Player 2 : "))
a = {}
a["p1"] = (abs(player1 - s))
a["p2"] = (abs(player2 - s))

print(a,s)

