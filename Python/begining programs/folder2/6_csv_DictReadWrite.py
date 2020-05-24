from csv import DictReader, DictWriter

with open('6_file0.csv','r') as a:
    with open('6_file1.csv', 'w', newline='') as b:
        read_file = DictReader(a)
        write_file = DictWriter(b, fieldnames = ['fn', 'ln', 'age'])
        write_file.writeheader()
        for row in read_file:
            firstname, lastname, age = row.get('first_name'),row.get(' last_name'),row.get(' age')
            write_file.writerow(
                {'fn': firstname, 'ln': lastname, 'age': age}
            )