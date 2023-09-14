#read the contests of clients.txt
#use for value that will 

def main():
    infile=open("clients.txt","r")

    clientNo=1

    for i in infile:
        i=i.rstrip('\n')
        print(f"{clientNo}. {i}")
        clientNo+=1
    
    infile.close()


main()
