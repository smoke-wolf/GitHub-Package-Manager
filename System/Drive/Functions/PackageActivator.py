import os

cwd = os.getcwd()

spacer = '===================================================='

print('=================Available_Packages=================')
print('''Local : 1
GitHub : 2''')
inp = int(input('Enter value to continue: '))
if inp == 2:

    with open(f'{cwd}/System/Cache/System/GitHub/int.py', 'r') as r, open(f'{cwd}/System/Cache/System/GitHub/int2.py', 'w') as o:
        for line in r:
            if line.strip():
                o.write(line)

    f = open(f'{cwd}/System/Cache/System/GitHub/int2.py', "r")


    lines = f.readlines()
    count = 0
    for line in lines:
        count += 1

    count1 = 0
    for line in lines:
        count1 += 1
        print("{} | {}".format(count1, line.strip()))
        print(spacer)
        if count1 == count:
            valuee = input('Enter a value to continue: ')
            value = lines[int(valuee)-1]
            listOfWords = value.split('+', 1)
            if len(listOfWords) > 0:
                value = listOfWords[1]

            value = value.split('-', 1)[0]

            try:
                os.system(f'{value}')

            except:
                print('Package Error')
elif inp == 1:
    f = open(f'{cwd}/System/Cache/System/Local/Int2.py', 'r')

    with open(f'{cwd}/System/Cache/System/Local/Int.py', 'r') as r, open(f'{cwd}/System/Cache/System/Local/Int2.py', 'w') as o:
        for line in r:
            if line.strip():
                o.write(line)
    f = open(f'{cwd}/System/Cache/System/Local/Int2.py', "r")

    lines = f.readlines()
    count = 0
    for line in lines:
        count += 1

    count1 = 0
    for line in lines:
        count1 += 1
        print("{} | {}".format(count1, line.strip()))
        print(spacer)
        if count1 == count:
            valuee = input('Enter a value to continue: ')
            value = lines[int(valuee)-1]
            listOfWords = value.split('+', 1)
            if len(listOfWords) > 0:
                value = listOfWords[1]

            value1 = value.split('-', 1)[0]

            try:
                os.system(f'{value1}')
            except:
                print('os error')

            listOfWords = value.split('-', 1)
            if len(listOfWords) > 0:
                value = listOfWords[1]

            value = value.split('*', 1)[0]

            try:
                os.system(f'{value}')
            except:
                print('Package Error')

