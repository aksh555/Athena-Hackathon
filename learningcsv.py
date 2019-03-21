import csv

with open('stud.csv', mode='w') as csv_file:
    fieldnames = ['name', 'dept', 'age']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'name': 'John Smith', 'dept': 'Accounting', 'age': 20})
    writer.writerow({'name': 'Erica Meyers', 'dept': 'IT', 'age': 10})

with open('stud.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print "Column names are", ", ".join(row)
            line_count += 1 
        print "\t",row["name"], "in the" ,row["dept"] ,"department, is", row["age"]
        line_count += 1
    
