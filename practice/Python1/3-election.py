print("*** Election ***")
voters = int(input("Enter a number of voter(s) : "))
lst = list(map(int,input().split()))

def mode(array):
    most = max(list(map(array.count, array)))
    return list(set(filter(lambda x: array.count(x) == most, array)))

winner = mode(lst)

if winner[0] >= 1  and winner[0] <= 20:
    print(winner[0])
else:
    print("*** No Candidate Wins ***")
'''
for j in num:
    if (j<0)  :
        print('*** No Candidate Wins ***')
        break
    elif (j>20):
        print('*** No Candidate Wins ***')
        
x = []
y = []
for i in num:
    if i not in x:
        x.append(i)
    elif i not in y:
        y.append(i)
        
print(*y)
'''
