import sys
import numpy as np
# import pandas
import math
import matplotlib
import matplotlib.pyplot as plt
import glob

#data_path = "~/Documents/CS 229/fMRI_TC/ICA_time_course"
#file_name = "NCANDA_S00033.txt"

folder_path = '~/Documents/CS 229/fMRI_TC'
pattern_match = '/*.txt'

craddock = glob.glob(folder_path + 'craddock100_time_course' + pattern_match)
ICA = glob.glob(folder_path + 'ICA_time_course' + pattern_match)

num_bins = 269

def print_in_lines(arr, n):
	size = len(arr)
	for i in range(int(math.ceil(float(size) / n))):

		if (n * i) + n <= size:
			print(str(n*i) + " - " + str((n * i) + n - 1) + ":" + str(arr[(n*i) : (n*i) + n]))
		else:
			print(str(n*i) + " - " + str(size - 1) + ":" + str(arr[(n*i):]))

def main():
	# Data introduction
    f = np.loadtxt(data_path + file_name)
    print("\nThe normalized data is organized as (time, region): \n")
    print(np.shape(f))
    print("\n")

    time_dur = len(f)
    regions = len(f[1])

    # Intial data processing

    print("Here are the min max readings of each brain region: \n")

    min_max = []
    lin_dif = []
    fold_change = []
    for j in range(regions): 
    	if j%2 == 1:
    		plt.hist(f[:, j], num_bins)
    	min_max.append([np.min(f[:, j]), np.max(f[:, j])])
    	lin_dif.append(np.max(f[:, j]) - np.min(f[:, j]))
    	# fold_change.append((np.max(f[:, j]) - np.min(f[:, j])) * 2 / (math.abs(np.max(f[:, j])) + math.abs(np.max(f[: , j]))))
    	plt.show()
    print(min_max)

    print("\nHere are the linear differences: \n")
    print_in_lines(lin_dif, 5)

    # print("\nHere are the fold changes normalized to average of min and max values")
    # print_in_lines(fold_change, 5)

if __name__ == "__main__":
    main()


