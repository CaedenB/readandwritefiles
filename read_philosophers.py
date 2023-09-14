#this reads and displays the contents of philosophers txt file

def main():
    infile=open("philosophers.txt",'r')
    #read file contents
   # file_contents=infile.read()
    line1=infile.readline().rstrip('\n')
    line2=infile.readline().rstrip('\n')
    line3=infile.readline().rstrip('\n')

#print the data
    print(line1)
    print(line2)
    print(line3)

    infile.close()


main()