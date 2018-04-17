import random as r
s = r.randint(0,100)
print("Enter Your guesses(2 Players)")
p1 = input("Name Player1:")
p2= input("Name Player2:")
player1 = int(input(p1+" : "))
player2 = int(input(p2+" : "))
a = {}
a[p1] = (abs(player1 - s))
a[p2] = (abs(player2 - s))

print(a,s)

l = min(a.values())
for i in a.keys():
    if a[i] == l:
        print("Winner is ",i,"with value",l)
