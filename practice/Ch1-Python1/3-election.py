print("*** Election ***")
voters = int(input("Enter a number of voter(s) : "))
num = list(map(int,input().split()))[:voters]

check = 0

for j in num:
    if (j<1)  :
        check += 1
    elif (j>20):
        check += 1
    
max=0
win=[]

for i in num:
    if(num.count(i)>=max and i<=20 and i>=0):
        max=num.count(i)
for i in num:
    if(num.count(i)==max and i not in win):
        win.append(i)
if check == voters:
    print("*** No Candidate Wins ***")   
else: 
    win.sort()
    print(*win)