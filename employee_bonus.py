#read employeepay csv
#

import csv

infile = open("EmployeePay.csv",'r')

csv_file = csv.reader(infile) 

next(csv_file)

for rec in csv_file:
    sal = float(rec[3])
    bonus = sal*float(rec[4])
    totalpay = sal+bonus
    print(f"Name: {rec[1]} {rec[2]}\n")
    print(f"Salary:    ${sal:10,.2f}\n")
    print(f"Bonus:     ${bonus}\n")
    print(f"Total Pay: ${totalpay:10,.2f}\n")
    input()


infile.close()

