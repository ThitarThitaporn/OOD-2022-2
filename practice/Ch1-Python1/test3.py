vote = int(input("Enter a number of voter(s) : "))
num = int(input()).split()[:vote]
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
# number of elements
n = int(input("Enter number of elements : "))
  
# Below line read inputs from user using map() function 
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
  
print("\nList is - ", a)
'''