#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Merge Peaks with d=100
import pandas as pd

peaks_df = pd.read_csv('peaks.txt', sep='\t', header=None,skiprows=1, names=['chrom', 'start', 'end', 'coverage'],low_memory=False)

# initialize an empty list to store merged peaks
merged_peaks = []

# initialize variables to store information about the current peak
current_chrom = None
current_start = None
current_end = None
current_coverage = None
for index, row in peaks_df.iterrows():
    chrom = row['chrom']
    start = row['start']
    end = row['end']
    coverage = row['coverage']
    
    start = int(start)
    end = int(end)
    coverage = float(coverage)
    
    distance = 100
    # check if this is the first peak or if the current peak overlaps with the previous peak
    if current_chrom is None or chrom != current_chrom or start > current_end + distance:
        
        # if this is a new peak, add the previous peak to the list of merged peaks (if there is one)
        if current_chrom is not None:
            merged_peaks.append((current_chrom, current_start, current_end, current_coverage))
        
        # start a new peak
        current_chrom = chrom
        current_start = start
        current_end = end
        current_coverage = coverage
        
    else:
        # update the end position and coverage of the current peak
        current_end = max(current_end, end)
        current_coverage = max(current_coverage, coverage)

# add the last peak to the list of merged peaks
if current_chrom is not None:
    merged_peaks.append((current_chrom, current_start, current_end, current_coverage))

merged_df = pd.DataFrame(merged_peaks, columns=['chrom', 'start', 'end', 'coverage'])

# write the merged peaks to a new file
#merged_df.to_csv('merged2_peaks.txt', sep='\t', index=False, header=False)


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

#data = pd.read_csv("merged2_peaks.txt", sep="\t", header=None, skiprows = 1,names=["chrom", "start", "end", "coverage"],low_memory="False")

# extract coverages from data
coverages = merged_df["coverage"]

# count the number of peaks with the same coverage
coverage_counts = {}
for coverage in coverages:
    if coverage in coverage_counts:
        coverage_counts[coverage] += 1
    else:
        coverage_counts[coverage] = 1

for coverage, count in coverage_counts.items():
    print(f"Number of peaks with coverage {coverage}: {count}")
#plt.show()  

