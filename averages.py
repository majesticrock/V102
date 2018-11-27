import numpy as np

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def average(pathToFile, delimiter=";"):
    content = csv_read(pathToFile, delimiter)
    n = len(content)
    #Set this to the line where your values start
    #remember that arrays start at 0 not at 1
    first_index = 1
    #Set this to the column where your values are
    col = 0
    avg = 0
    evg_err = 0

    for i in range(first_index, n):
        avg += float(content[i][col])
    
    avg /= n

    for i in range(first_index, n):
        avg_err = (float(content[i][col]) - avg)**2

    avg_err = np.sqrt(avg_err)
    avg_err /= np.sqrt(n * (n-1))

    return [avg, avg_err]

files = ["magnet0-5.csv", "magnet1-0.csv", "magnet1-5.csv", "magnet2-0.csv", "magnet2-5.csv", "magnet3-0.csv", "magnet3-5.csv", "magnet4-0.csv", "magnet4-5.csv", "magnet5-0.csv"]

averages = []

for f in files:
    averages.append(average("csv/" + f))

header = "$I$ / A; \\multicolumn{2}{c}{$\overline{T}$ / s}"
strom = 0.5


with open("csv/mittelwerte-magnet.csv", "w") as f:
    f.write(header)
    for x in averages:
        f.write(f"\n{strom:.1f};{x[0]:.2f};{x[1]:.2f}")
        strom += 0.5