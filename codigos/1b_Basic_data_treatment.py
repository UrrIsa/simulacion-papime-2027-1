# 1b : Basic data treatment
#-----------------------------

# If you have'nt installed numpy yet, you can do it with :
# pip install numpy


import numpy as np
import pandas as pd

# 1. Categories (in R, these are factors) [https://pandas.pydata.org/docs/user_guide/categorical.html]

# Convert data to category
data = [4, 5, 5, 4, 4, 3, 5, 5, 5, 4, 5, 4, 3, 3]
data = [4, 5, 5, 4, 4, 3, 5, "Ann", 5, 4, 5, 4, 3, 3] # python allows heterogeneous arrays
data = "Ann"
print(type(data)) # data is string (<class 'str'>), takes the last assgiment

# Convert numeric data to category
data_num = [4, 5, 5, 4, 4, 3, 5, 5, 5, 4, 5, 4, 3, 3]
cdata = pd.Categorical(data_num) # pd.Categorical converts the columns into categories
print(cdata)

# Now with alfanumeric data
week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "wednesday", "tuesday", "thursday", "wednesday"]

week = pd.Series(week) # converts week into a Series [https://pandas.pydata.org/docs/reference/api/pandas.Series.html] a unidimensional array that allows data analysis
print(week.dtype) # prints the data type of week (class in R)
print(week.value_counts()) # prints 'week' according to their frequency (from highest to lowest)

# If you want to sort it alphabetically use '.sort_index()' :
# print(week.value_counts().sort_index())

week_ordered = pd. Categorical(
    week,
    categories = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"],
    ordered=False
) # 'categories=' is the equivalent of 'levels='

print(pd.Series(week_ordered).value_counts().reindex(
    ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
)) # Because 'value_counts()' doesn't automatically respect the order od the categories, the order was forced using 'reindex()' by explicity specifying the order we want


#To generate factor levels (without adding data): np.repeat(labels,n)
#Example np.repeat(labels, n = number of replications)
label = ["India", "USA", "Russia"]
v = pd.Categorical(np.repeat(label,4)) # repeat each label four times
print(v)

# Generation of dataframes
df = pd.DataFrame({
    "Student_id" : range (1,11),
    "Class" : ["Algebra"] * 3 + ["Calculus"] * 3 + ["Probability"] * 4
}) 
# We use 'range(1,11)' because the range doesn't include the upper bound
# The equivalence of 'rep("Algebra", 3)' in python is '["Alegbra"] * 3', the multiplication is written explicity.
print(df)


# 2. Combine dataframes
# using pd.concat / np.column_stack / np.vstack for arrays
# pd.concat(axis=1) / (axis=0) for dataframes

# 2.1 We use column_stack() to manipulate columns 

# range(1,n) creates the sequence of number [1,2,..., n]
# with np.resize(array,m) takes that sequence and either enlarge it or crop it to exactly m
# we can describe the columns of an array using '[ , ]'
m = np.column_stack([ np.resize(range(1,4), 9) , range(1,10) ])
print(m)
m = np.column_stack([ ["Ann"] * 9 , range(1,10) ])
print(m)
m = np.column_stack([ [1] * 7, range(1,8) ])
print(m)

m = np.column_stack([ m, range(8,15) ]) # add another column from 8 to 14
print(m) 
m_ordered = m[:,[0,2,1]] # we use advanced indexing of NumPy, ':' means "take all rows" and [0,2,1] indicates the new order (first the column 1, then column2 and finally column 1)
print(m_ordered)


# 2.2 We use vstack() to manipulate rows

ma = np.vstack([ [1] * 3, [1,2,3] ]) # in this case [ , ] indicates the rows
print(ma)

ma_extended = np.column_stack([ [0] * 2 , ma ]) # a column of zeros is added to ma
print(ma_extended)


# There are other ways to achieve the result, but, for example if you want to use your own function to repeat an array (without using 'np.resize') check out Appendix 1 




# APPENDIXES




