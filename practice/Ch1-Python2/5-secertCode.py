def bon(w):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    w = w.lower()
    
    code = 0
    i = 0
    while i < len(w):
        j = i + 1
        while j < len(w) and w[i] == w[j]:
            j += 1
            code = 4 * (alphabet.index(w[i]) + 1)
        i = j

        
    return code
            
    
    

secretCode = input("Enter secret code : ")
print(bon(secretCode))