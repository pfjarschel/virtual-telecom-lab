import numpy as np
import matplotlib.pyplot as plt

filename = "test.txt"

ch1 = []
ch2 =[]
with open(filename, 'r') as file:
    lines = file.readlines()

    for line in lines[1:]:
        line_strings = line.split("\t")
        ch1.append(float(line_strings[1]))
        ch2.append(float(line_strings[2]))
    
    file.close()

ch1 = np.array(ch1)
ch2 = np.array(ch2)

n, bins, patches = plt.hist([ch1, ch2], bins=100)

# i_errs = []
# for i_coord in ch1:



plt.show()