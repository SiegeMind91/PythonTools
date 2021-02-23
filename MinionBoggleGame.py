def minion_game(string):
    vowels = 'AEIOU'

    kevScore = 0
    stuScore = 0
    #This is one method
    #for i in range(len(string)):
    #    if string[i] in vowels:
    #        kevScore += (len(string)-i)
    #    else:
    #        stuScore += (len(string)-i)
    
    #This is the other
    slen = len(string)
    tsub = int(slen * (slen + 1) / 2)        
    kevScore = sum(slen - i for i in range(slen) if string[i] in vowels)   
    stuScore = tsub - kevScore      
            
    if kevScore > stuScore:
        print("Kevin", kevScore)
    elif kevScore < stuScore:
        print("Stuart", stuScore)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)