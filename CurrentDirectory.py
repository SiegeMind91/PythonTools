os.chdir('C:\\Users\\poke\\Desktop\\') #Change the current directory
os.getcwd() #return the current directory

#Create a new file at the current directory
with open('someFile.txt', 'w+') as f:
        f.write('This should be at C:\\Users\\poke\\Desktop\\someFile.txt now.')