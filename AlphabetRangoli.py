def print_rangoli(size):
    alpha = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    for i in range(size-1, -size, -1):
        x = abs(i)
        line = alpha[size:x:-1]+alpha[x:size]
        #print(line)
        print ("--"*x+ '-'.join(line)+"--"*x)        
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)