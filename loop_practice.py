demoList = [1,2,3,4,5,6,7,8,9,10]
secList = [10,20,30,40,50,60,70,80,90,100]

for i in range(0, len(demoList)):
    if demoList[i] % 2 == 0:
        continue
    print(demoList[i])
    
"""
qs = ["What is your name?",
      "What is your favorite color?",
      "What is your age?"]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3
 """

#i = 5
"""
for number in demoList:
    if i <= len(demoList):
            print(demoList[i])
            i += 1
    else:
        break
"""
"""
for i, number in enumerate(demoList):
    print(demoList[i])
"""

#for i in range(0, len(demoList)-1):
#    print(demoList[i])
"""
for i in range(0, len(demoList)):
    for j in range(0, len(secList)):
        print(demoList[i]*secList[j])
"""
"""
x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New Year!")
"""
"""
for i in range(0, len(secList)):
    print(secList[i])
    if secList[i]+100 == 150:
        break
"""
