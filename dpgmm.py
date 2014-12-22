'''
Code to calculate clusters using a Dirichlet Process
Gaussian mixture model. 

Requires scikit-learn:
  http://scikit-learn.org/stable/
'''

import numpy
from sklearn import mixture

FILENAME = "mcdonalds-normalized-data.tsv"
OUTPUT_FILENAME = "classified_result.txt"

with open(FILENAME) as f:
    ncols = len(f.readline().split("\t"))

# Note: you'll have to remove the last "name" column in the file (or
# some other such thing), so that all the columns are numeric.
x = numpy.loadtxt(open(FILENAME, "rb"), delimiter = "\t", skiprows = 1, usecols=range(1, ncols))
label = numpy.loadtxt(open(FILENAME, "rb"), delimiter = "\t", skiprows = 1, usecols={0}, dtype='object')

dpgmm = mixture.DPGMM(n_components = 5, n_iter = 1000, alpha = 1)
dpgmm.fit(x)
clusters = dpgmm.predict(x)

# My own function
print label
print clusters

group_num = 0
for num in clusters:
	if num > group_num:
		group_num = num

# group number is the biggest index plus 1
group_num += 1;

group = {}

for tmp in range(0, group_num):
	group[tmp] = set()

print group

for idx, classified_group in enumerate(clusters):
	group[classified_group].add(label[idx])

output = open(OUTPUT_FILENAME, 'w');


real_idx = 0
for i in range(0, group_num):
	if len(group[i]) > 0:
		output.write(str(real_idx)+"st group:\n")
		real_idx += 1
		for j in range(0, len(group[i])):
			output.write(str(group[i].pop()) + ", ")
		output.write("\n\n")

output.close()








