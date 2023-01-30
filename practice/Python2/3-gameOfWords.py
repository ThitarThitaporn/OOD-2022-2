class Torkham:
    def __init__(self):
        self.words = []
        
    def restart(self):
        self.words = []
        return "game restarted"
    
    def play(self,word):
        n = len(self.words)
        if n == 0:
            self.words.append(word)
            return f'\'{word}\' -> {self.words}'
        elif word[0].lower() == self.words[-1][-2].lower() and word[1].lower() == self.words[-1][-1].lower():
            self.words.append(word)
            return f'\'{word}\' -> {self.words}'
        else:
            return f'\'{word}\' -> game over'
    
torkham = Torkham()
print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')
while len(S) > 0:
    if S[0][0] == 'P' and len(S[0]) > 2:
        print(torkham.play(S[0][2:]))
        S = S[1:]
    elif S[0][0] == 'R':
        print(torkham.restart())
        S = S[1:]
    elif S[0][0] == 'X':
        exit()
    else :
        print(f'\'{S[0]}\' is Invalid Input !!!')
        exit()
    