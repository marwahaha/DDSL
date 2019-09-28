import matplotlib.pyplot as plt
import csv


x = []
y = []

##with open('./Rectangle Test/case=19_score=0.3384301165941705.csv') as f:
##    reader = csv.reader(f, delimiter=',')
##    for row in reader:
##        x.append(float(row[0]))
##        y.append(float(row[1]))


with open('rect-optim003.txt') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y)
plt.show()

# ./Rectangle Test/case=19_score=0.3384301165941705.csv
# rect-optim002.txt
