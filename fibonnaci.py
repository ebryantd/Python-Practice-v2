import math

fiblist = list()
i = 0
while i <= 19:
    if i >= 2:
        fiblist.append(fiblist[i-2]+fiblist[i-1])
    else:
        fiblist.append(i)

    print(fiblist[i])
    i += 1
