from csv import writer,DictWriter

with open("5_file0.csv", 'w', newline = "") as f:
    # csv_writer = writer(f)
    # print(csv_writer)
    # csv_writer.writerow(['Name','age'])
    # csv_writer.writerow(["Bhaumik",24])

    # csv_writer.writerows([['Hemil',21], ['Arth',16]])

    csv_file = DictWriter(f, fieldnames = ["name", "age"])

    csv_file.writeheader()
    csv_file.writerow({"name": "Bhaumik", "age": 24})

    csv_file.writerows([
        {'name': 'Hemil', 'age': 21},
        {'name': 'Arth', 'age': 16}
    ])
