#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# coverage.bedgraph created with bedtools.
bedgraph = pd.read_csv('coverage.bedgraph', sep='\t', header=None, names=['chrom', 'start', 'end', 'coverage'],low_memory=False)
threshold = 5
window_size = 50
c_df = bedgraph[bedgraph['coverage'] >= threshold]

smoothed_counts = np.convolve(bedgraph['coverage'], np.ones(window_size) / window_size, mode='same')

fig, ax = plt.subplots()

# Plot the smoothed peak positions
ax.plot(c_df['start'], c_df['coverage'], color='b')

# Set the axis labels
ax.set_xlabel('Position')
ax.set_ylabel('Coverage')
plt.show()

