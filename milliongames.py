from random import randint

games = 10000000
won = 0
draw = 0
lost = 0

for c in range(0, games):
    i_got = [randint(1, 6), randint(1, 6)]
    he_got = [randint(1, 6), randint(1, 6)]
    if he_got[0] < he_got[1]:
        he_got[0] = 7
    else:
        he_got[1] = 7
    
    if i_got[0]+i_got[1] > he_got[0]+he_got[1]:
        lost += 1
    elif i_got[0]+i_got[1] == he_got[0]+he_got[1]:
        draw += 1
    else:
        won += 1

# example output:
# 385991 won, 424800 draw, 9189209 lost
# 10000000 games total
# 0.0386 + 0.0425 + 0.9189 = 1.0
print("{0} won, {1} draw, {2} lost".format(won, draw, lost))
print("{0} games total".format(games))
print("{0:.4f} + {1:.4f} + {2:.4f} = {3}".format(won / games, draw / games, lost / games, (won / games) + (draw / games) + (lost / games)))

