lst = list(map(int, input("Enter Your List : ").split()))
#print(lst)
#print(len(lst)-2)

if len(lst) >= 3 :
    result = []
    for i in range(0, len(lst)-2):
        for j in range(i+1, len(lst)-1):
            for k in range(j+1,len(lst)):
                if lst[i]+lst[j]+lst[k] == 0 :
                    result.append([lst[i],lst[j],lst[k]]) 
                    
    
    new_res = []
    for ele in result :
        if ele not in new_res:
            new_res.append(ele)
            
    result = new_res
    print(result)

else:
    print("Array Input Length Must More Than 2")
                    