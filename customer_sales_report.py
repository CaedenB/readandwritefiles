#read sales file
#create a new file 
#write customer ID and calcuated total from salesreport.csv
import csv

rsales= open("sales.csv", 'r')
report= open("salesreport.csv", 'w')

readsales=csv.reader(rsales)


next(readsales)
report.write('Customber ID , Total'+'\n')
custid= '250'
total=0

for rec in readsales:
    if custid==rec[0]:
        total+= float(rec[3])+float(rec[4])+float(rec[5])

    else:
        report.write(custid +','+ str(round(total,2))+'\n')
        custid=rec[0]
        total=float(rec[3])+float(rec[4])+float(rec[5])

report.write(custid +','+ str(round(total,2))+'\n')

report.close()