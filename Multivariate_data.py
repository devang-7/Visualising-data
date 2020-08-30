
#How to select dataframe subsets from multivariate data
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 100) # Show all columns when looking at dataframe
# Download NHANES 2015-2016 data
df = pd.read_csv("nhanes_2015_2016.csv")

# Keep only body measures columns, so only columns with "BMX" in the name
# get columns names
col_names = df.columns
# One way to get the column names we want to keep is simply by copying from the above output and storing in a list
keep = ['BMXWT', 'BMXHT', 'BMXBMI', 'BMXLEG', 'BMXARML', 'BMXARMC',
       'BMXWAIST']
# Another way to get only column names that include 'BMX' is with list comprehension
# [keep x for x in list if condition met]
[column for column in col_names if 'BMX' in column]
keep = [column for column in col_names if 'BMX' in column]
# use [] notation to keep columns
df_BMX = df[keep]