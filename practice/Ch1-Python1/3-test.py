'''print("*** Election ***")
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
#--------------------------------
'''
import sys

print('*** Election ***')
i = int(input("Enter a number of voter(s) : "))
arr = [int(i) for i in input().split()]

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        if(i<=20):
            curr_frequency = List.count(i)
        
            if(curr_frequency> counter):
                counter = curr_frequency
                num = i
        
        
    if (i<0 or i>20) :
       print('*** No Candidate Wins ***')
       sys.exit()
 
    return num  

print(most_frequent(arr))'''