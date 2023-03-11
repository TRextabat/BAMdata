#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd

bedgraph = pd.read_csv('coverage.bedgraph', sep='\t', header=None, names=['chrom', 'start', 'end', 'coverage'])

threshold = 5

found = bedgraph['coverage'] >= threshold

# where the foundings change from False to True (the start of a peak)
peak_starts = np.where(found & ~found.shift(1, fill_value=False))[0]

# where the foundings change from True to False (the end of a peak)
peak_ends = np.where(~found &  found.shift(1, fill_value=False))[0]

# Combine the start and end indices into a DataFrame of peak regions

peaks = pd.DataFrame({'chrom': bedgraph.loc[peak_starts, 'chrom'].values, 
                      'start': bedgraph.loc[peak_starts, 'start'].values,
                      'end': bedgraph.loc[peak_ends, 'end'].values})
print(peaks)

print(f'Found {len(peaks)} peaks with coverage >= {threshold}.')

