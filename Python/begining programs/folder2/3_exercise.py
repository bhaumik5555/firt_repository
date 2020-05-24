with open('3_userdata.txt', 'r') as datafile:
    with open('3_userinfo.txt', 'w') as infofile:
        a = len(datafile.readlines())
        datafile.seek(0)
        for x in range(0,a):
            name, salary = datafile.readline().split(',')
            infofile.write(f'{name}\'s salary is {salary}')