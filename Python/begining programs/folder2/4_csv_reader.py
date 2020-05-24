from csv import reader, DictReader

with open('4_file0.csv', 'r') as csv_file:
    # This will hardly used in programm (just to create the list of that file)
    file1 = reader(csv_file)

    # for row in file1:
    #     print(row)

    # This can be used to create dictionary (better to get the access of perticular column)
    file2 = DictReader(csv_file)

    for row in file2:
        print(row)