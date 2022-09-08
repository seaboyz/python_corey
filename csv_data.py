import csv
from fileinput import filename

""" with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv','w') as new_file:
        csv_writer = csv.writer(new_file,delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line) """
    
""" with open('new_names.csv', 'r') as csv_file:
    # csv_reader = csv.reader(csv_file)
    csv_reader = csv.reader(csv_file,delimiter='\t')

    for line in csv_reader:
        print(line)
         """

with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv','w') as new_file:
        filednames = ['first_name','last_name','email']
        csv_writer = csv.DictWriter(new_file,fieldnames=filednames,delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)

    