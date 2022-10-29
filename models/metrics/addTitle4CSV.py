# importing python package
import pandas as pd

# read contents of csv file
file = pd.read_csv("sys_metrics.csv")
# print("\nOriginal file:")
# print(file)

# adding header
headerList = ['client_id', 'round_number','hierachy', 'num_samples','set','bytes_written','client computations','bytes_read']

# converting data frame to csv
file.to_csv("sys_metrics.csv", header=headerList, index=False)

# display modified csv file
""" file2 = pd.read_csv("gfg2.csv")
print('\nModified file:')
print(file2) """
