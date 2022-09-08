import csv

html_output = ''
names = []

""" with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    # print(csv_data)
    # print(list(csv_data))

    # skip first two rows
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        # print(line)
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}") """

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # skip first two rows
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        # print(line)
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")


for name in names:
    print(name)

html_output += f'<p>There are currently {len(names)} public contributors. Thank you!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)
