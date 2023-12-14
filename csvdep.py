import csv
with open('deapartment.csv',newline='')as csvfile:
 data=csv.DictReader(csvfile)
 print("ID Department Name")
 print("_______________________")
 for row in data:
  print(row['department_id'], row['department_name'])
