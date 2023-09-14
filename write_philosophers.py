#this program writes 3 lines of data to a file

def main():
    #open a file named philosohers.txt
    outfile=open("philosophers.txt",'w')

    #write the nemae of 3 philosphers in file

    outfile.write("John Locke"+'\n')
    outfile.write("David Hume"+'\n')
    outfile.write("Edmund Burke"+'\n')

    outfile.close()



main()
