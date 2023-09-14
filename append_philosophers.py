#this program writes 3 lines of data to a file

def main():
    #open a file named philosohers.txt
    outfile=open('philosophers.txt','a')

    outfile.write("Caeden Becker\n")
#append your name to this file
   
    outfile.close()



main()