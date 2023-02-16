print("*** Election ***")
voters = int(input("Enter a number of voter(s) : "))
num = list(map(int,input().split()))[:voters]

check = 0
vote = []
for j in num:
    if (j<0)  :
        check+=1
    elif (j>20):
        check+=1
    else:
        vote.append(j)

if check == voters:
    print('*** No Candidate Wins ***')

# Count the number of occurrences of each element in the list
counted = {}
for element in vote:
    if element in counted:
        counted[element] += 1
    else:
        counted[element] = 1

# Find the most common element(s)
most_common = max(counted.values())
most_common_elements = [k for k, v in counted.items() if v == most_common]

# Print the most common element(s)
if len(most_common_elements) == 1:
    print(most_common_elements[0])
else:
    for element in most_common_elements:
        print(element,end=' ')
        
    