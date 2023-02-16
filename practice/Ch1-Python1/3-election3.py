

print("*** Election ***")
voters = int(input("Enter a number of voter(s) : "))
num = list(map(int,input().split()))[:voters]

check = 0

for j in num:
    if (j<1)  :
        check += 1
    elif (j>20):
        check += 1
    
if check == voters:
    print("*** No Candidate Wins ***")
        
        
x = []
y = []
for i in num:
    if i not in x:
        x.append(i)
    elif i not in y:
        y.append(i)
   
print(x)     
print(*y)
