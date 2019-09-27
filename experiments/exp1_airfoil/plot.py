import matplotlib.pyplot as plt
import csv


x = []
y = []

with open('./Rectangle Test/case=18_score=0.2912771810581133.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.plot(x,y)
plt.show()

# ./Rectangle Test/case=13_score=0.26402968205194827.csvcase=18_score=0.2912771810581133.csv
# rect-optim002.txt
