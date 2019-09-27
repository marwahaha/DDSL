import os

remove = []

for root, dirs, files in os.walk('Rectangle Test'):
    for file in files:
        for index in range(len(file)):
            if file[index] == '_':
                filecut = index
                break
        number = file[5:filecut]
        if int(number) > 99:
            remove.append(file)

for name in remove:
    os.remove('./Rectangle Test/'+name)
