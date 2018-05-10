won = 0
draw = 0
lost = 0
total = 0

# a, b -> my rolls
# c, d -> opponent's rolls
for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            for d in range(1, 7):

                # 
                if c<d:
                    c = 7
                else:
                    d = 7
                
                if a+b < c+d:
                    won += 1
                elif a+b == c+d:
                    draw += 1
                else:
                    lost += 1
                
                total += 1

# output:
# 1206 won, 45 draw, 45 lost
# 1296 games total
# 0.9306 + 0.0347 + 0.0347 = 1.0
print("{0} won, {1} draw, {2} lost".format(won, draw, lost))
print("{0} games total".format(total))
print("{0:.4f} + {1:.4f} + {2:.4f} = {3}".format(won / total, draw / total, lost / total, (won / total) + (draw / total) + (lost / total)))
