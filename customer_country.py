#import customer.csv file
#creat new file w customer name and country they are from
# show total number of customers read from file




import csv

readcust= open('customers.csv','r')
customers = open('customers_country.csv','w')


csv_file = csv.reader(readcust)  #could also do ,delimater=',')

next(csv_file)   #this skips a row

count=0
customers.write("Name, Country\n")

for rec in csv_file:
    customers.write(f"{rec[1]},{rec[2]},{rec[4]}\n")
    count+=1
 #waits for user enters enter key (can see 1 record at a time)
 

customers.close()
print(f"the total number of customers is: {count}")