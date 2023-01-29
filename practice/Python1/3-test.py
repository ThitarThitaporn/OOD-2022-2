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