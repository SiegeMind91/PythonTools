def merge_the_tools(string, k):
    # your code goes here
    S, N = string, int(k) 
    #Complex but cool thing here, 
    #the '*[iter(S)] * N' part is creating N copies of iter(S) 
    #and adding them to a list and then unpacking that list
    for part in zip(*[iter(S)] * N):   
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

    #For better understanding of the above put this in IDLE;
    #for part in zip(*[iter('abcdefghi')]*3):
    #    print(part)


    #Simpler version of the solution
    #S, N = string, int(k)
    #temp = []
    #len_temp = 0
    #for item in S:
    #    len_temp += 1
    #    if item not in temp:
    #        temp.append(item)
    #    if len_temp == K:
    #        print ''.join(temp)
    #        temp = []
    #        len_temp = 0        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)