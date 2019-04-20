#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# ### The Pandas Series Object

# In[2]:


data = pd.Series([0.25, 0.5, 0.75, 1.0])
data


# In[3]:


data.values


# In[4]:


data.index


# In[5]:


data[1]


# In[6]:


data[1:3]


# From what we’ve seen so far, it may look like the Series object is basically interchangeable with a one-dimensional NumPy array. The essential difference is the presence of the index: while the NumPy array has an implicitly defned integer index used to access the values, the Pandas Series has an explicitly defned index associated with the values.
# This explicit index definition gives the Series object additional capabilities. For example, the index need not be an integer, but can consist of values of any desired type. For example, if we wish, we can use strings as an index:

# In[7]:


data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
data


# In[8]:


data['b']


# We can even use noncontiguous or nonsequential indices:

# In[9]:


data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=[2, 5, 3, 7])
data


# In[10]:


data[5]


# ### Series as specialized dictionary
# In this way, you can think of a Pandas Series a bit like a specialization of a Python dictionary. A dictionary is a structure that maps arbitrary keys to a set of arbitrary values, and a Series is a structure that maps typed keys to a set of typed values. This typing is important: just as the type-specific compiled code behind a NumPy array makes it more efficient than a Python list for certain operations, the type information
# of a Pandas Series makes it much more efficient than Python dictionaries for certain operations.
# We can make the Series-as-dictionary analogy even more clear by constructing a Series object directly from a Python dictionary:

# In[11]:


population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}

population = pd.Series(population_dict)
population


# By default, a Series will be created where the index is drawn from the sorted keys. From here, typical dictionary-style item access can be performed:

# In[12]:


population['California']


# Unlike a dictionary, though, the Series also supports array-style operations such as slicing:

# In[13]:


population['Texas':'Illinois']


# ### Constructing Series objects
# For example, data can be a list or NumPy array, in which case index defaults to an integer sequence:

# In[14]:


pd.Series([2, 4, 6])


# data can be a scalar, which is repeated to fill the specified index:

# In[15]:


pd.Series(5, index=[100, 200, 300])


# data can be a dictionary, in which index defaults to the sorted dictionary keys:
# 

# In[16]:


pd.Series({2:'a', 1:'b', 3:'c'})


# In each case, the index can be explicitly set if a different result is preferred:

# In[17]:


pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])


# Notice that in this case, the Series is populated only with the explicitly identified keys.

# ### The Pandas Index Object
# If a Series is an analog of a one-dimensional array with flexible indices, a DataFrame is an analog of a two-dimensional array with both flexible row indices and flexible column names. Just as you might think of a two-dimensional array as an ordered sequence of aligned one-dimensional columns, you can think of a DataFrame as a
# sequence of aligned Series objects. Here, by “aligned” we mean that they share the same index.

# In[18]:


area_dict = {'California': 423967, 'Texas': 695662, 
             'New York': 141297,'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
area


# In[19]:


states = pd.DataFrame({'population': population,
                        'area': area})
states


# Like the Series object, the DataFrame has an index attribute that gives access to the index labels:

# In[20]:


states.index


# Additionally, the DataFrame has a columns attribute, which is an Index object holding the column labels:

# In[21]:


states.columns


# Thus the DataFrame can be thought of as a generalization of a two-dimensional NumPy array, where both the rows and columns have a generalized index for accessing the data.

# #### DataFrame as specialized dictionary
# Similarly, we can also think of a DataFrame as a specialization of a dictionary. Where a dictionary maps a key to a value, a DataFrame maps a column name to a Series of column data. For example, asking for the 'area' attribute returns the Series object
# containing the areas we saw earlier:

# In[22]:


states['area']


# Notice the potential point of confusion here: in a two-dimensional NumPy array, data[0] will return the first row. For a DataFrame, data['col0'] will return the first column. Because of this, it is probably better to think about DataFrames as generalized dictionaries rather than generalized arrays, though both ways of looking at the situation can be useful. 

# #### Constructing DataFrame objects
# A Pandas DataFrame can be constructed in a variety of ways. Here we’ll give several examples.
# 
# **From a single Series object.** A DataFrame is a collection of Series objects, and a singlecolumn DataFrame can be constructed from a single Series:

# In[23]:


pd.DataFrame(population, columns=['population'])


# **From a list of dicts.** Any list of dictionaries can be made into a DataFrame. We’ll use a simple list comprehension to create some data:

# In[24]:


data = [{'a': i, 'b': 2 * i}
        for i in range(3)]
pd.DataFrame(data)


# Even if some keys in the dictionary are missing, Pandas will fill them in with NaN (i.e., “not a number”) values:

# In[25]:


pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])


# **From a dictionary of Series objects.** As we saw before, a DataFrame can be constructed from a dictionary of Series objects as well:

# In[26]:


pd.DataFrame({'population': population,
              'area': area})


# **From a two-dimensional NumPy array.** Given a two-dimensional array of data, we can create a DataFrame with any specified column and index names. If omitted, an integer index will be used for each:

# In[27]:


pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar'],
             index=['a', 'b', 'c'])


# **From a NumPy structured array.** A Pandas DataFrame operates much like a structured array, and can be created directly from one:

# In[28]:


A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
A


# In[29]:


pd.DataFrame(A)


# ### The Pandas Index Object
# We have seen here that both the Series and DataFrame objects contain an explicit index that lets you reference and modify data. This Index object is an interesting structure in itself, and it can be thought of either as an immutable array or as an ordered set (technically a multiset, as Index objects may contain repeated values).
# Those views have some interesting consequences in the operations available on Index objects. As a simple example, let’s construct an Index from a list of integers:

# In[30]:


ind = pd.Index([2, 3, 5, 7, 11])
ind


# #### Index as immutable array
# The Index object in many ways operates like an array. For example, we can use standard Python indexing notation to retrieve values or slices:

# In[31]:


ind[1]


# In[32]:


ind[::2]


# Index objects also have many of the attributes familiar from NumPy arrays:

# In[33]:


print(ind.size, ind.shape, ind.ndim, ind.dtype)


# One difference between Index objects and NumPy arrays is that indices are immutable—that is, they cannot be modified via the normal means:

# In[34]:


ind[1]=0


# This immutability makes it safer to share indices between multiple DataFrames and arrays, without the potential for side effects from inadvertent index modification.
# #### Index as ordered set
# Pandas objects are designed to facilitate operations such as joins across datasets, which depend on many aspects of set arithmetic. The Index object follows many of he conventions used by Python’s built-in set data structure, so that unions, intersections, differences, and other combinations can be computed in a familiar way:

# In[35]:


indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])


# In[36]:


indA & indB # intersection


# In[37]:


indA | indB # union


# In[38]:


indA ^ indB # symmetric difference


# These operations may also be accessed via object methods—for example, indA.intersection(indB).

# ### Data Indexing and Selection
# #### Data Selection in Series
# ##### Series as dictionary
# Like a dictionary, the Series object provides a mapping from a collection of keys to a collection of values:

# In[39]:


import pandas as pd
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
data


# In[40]:


data['b']


# We can also use dictionary-like Python expressions and methods to examine the keys/indices and values:

# In[41]:


'a' in data


# In[42]:


data.keys()


# In[43]:


list(data.items())


# Series objects can even be modified with a dictionary-like syntax. Just as you can extend a dictionary by assigning to a new key, you can extend a Series by assigning to a new index value:

# In[44]:


data['e'] = 1.25
data


# This easy mutability of the objects is a convenient feature: under the hood, Pandas is making decisions about memory layout and data copying that might need to take place; the user generally does not need to worry about these issues.
# #### Series as one-dimensional array
# A Series builds on this dictionary-like interface and provides array-style item selection via the same basic mechanisms as NumPy arrays—that is, _slices, masking, and fancy indexing_. Examples of these are as follows:

# In[45]:


# slicing by explicit index
data['a':'c']


# In[46]:


# slicing by implicit integer index
data[0:2]


# In[47]:


# masking
data[(data > 0.3) & (data < 0.8)]


# In[48]:


# fancy indexing
data[['a', 'e']]


# #### Indexers: loc, iloc, and ix
# These slicing and indexing conventions can be a source of confusion. For example, if your Series has an explicit integer index, an indexing operation such as data[1] will use the explicit indices, while a slicing operation like data[1:3] will use the implicit Python-style index.

# In[49]:


data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
data


# In[50]:


# explicit index when indexing
data[1]


# In[51]:


# implicit index when slicing
data[1:3]


# Because of this potential confusion in the case of integer indexes, Pandas provides some special indexer attributes that explicitly expose certain indexing schemes. These are not functional methods, but attributes that expose a particular slicing interface tothe data in the Series.
# 
# First, the **loc** attribute allows indexing and slicing that always references the explicit index:

# In[52]:


data.loc[1]


# In[53]:


data.loc[1:3]


# The **iloc** attribute allows indexing and slicing that always references the implicit Python-style index:

# In[54]:


data.iloc[1]


# In[55]:


data.iloc[1:3]


# A third indexing attribute, ix, is a hybrid of the two, and for Series objects is equivalent to standard []-based indexing. The purpose of the ix indexer will become more apparent in the context of DataFrame objects, which we will discuss in a moment.

# **So, this is what you need to remember:**
# 
# **.loc** takes slices based on labels. **.iloc** uses observations’ position. **.ix** uses both labels and positions.
# 
# **.loc** includes last element, when using an interval slice (e.g, [“a”:”c”]). .iloc does not include last element.
# 
# When using a integer based index be clear with what you want and avoid confusion by appropriately selecting **.loc** or **iloc** for the task. Avoid using **.ix**.

# ### Data Selection in DataFrame
# #### DataFrame as a dictionary
# The first analogy we will consider is the DataFrame as a dictionary of related Series objects. Let’s return to our example of areas and populations of states:

# In[56]:


area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})

pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
data


# The individual Series that make up the columns of the DataFrame can be accessed via dictionary-style indexing of the column name:

# In[57]:


#Dictionary sytle
data['area']


# In[58]:


#attribute style
data.area


# In[59]:


data.area is data['area']


# 
# Though this is a useful shorthand, keep in mind that it does not work for all cases! For example, if the column names are not strings, or if the column names conflict with methods of the DataFrame, this attribute-style access is not possible. For example, the DataFrame has a pop() method, so data.pop will point to this rather than the "pop" column:

# In[60]:



data.pop is data['pop']


# In particular, you should avoid the temptation to try column assignment via attribute **_(i.e., use data['pop'] = z rather than data.pop = z)_**.
# 
# Like with the Series objects discussed earlier, this dictionary-style syntax can also be used to modify the object, in this case to add a new column:

# In[61]:


data['density'] = data['pop'] / data['area']
data


# #### DataFrame as two-dimensional array
# As mentioned previously, we can also view the DataFrame as an enhanced two-dimensional array. We can examine the raw underlying data array using the values attribute:

# In[62]:


data.values


# With this picture in mind, we can do many familiar array-like observations on the DataFrame itself. For example, we can transpose the full DataFrame to swap rows and columns:

# In[63]:


data.T


# When it comes to indexing of DataFrame objects, however, it is clear that the dictionary-style indexing of columns precludes our ability to simply treat it as a NumPy array. In particular, passing a single index to an array accesses a row:

# In[64]:


data.values[0]


# and passing a single “index” to a DataFrame accesses a column:

# In[65]:


data['area']


# Thus for array-style indexing, we need another convention. Here Pandas again uses the loc, iloc, and ix indexers mentioned earlier. Using the iloc indexer, we can index the underlying array as if it is a simple NumPy array (using the implicit Python-style index), but the DataFrame index and column labels are maintained in the result:

# In[66]:


data.iloc[:3, :2]


# In[67]:


data.loc[:'Florida', :'pop']


# The ix indexer allows a hybrid of these two approaches:

# In[68]:


data.ix[:3, :'pop']


# Keep in mind that for integer indices, the ix indexer is subject to the same potential sources of confusion as discussed for integer-indexed Series objects.
# 
# Any of the familiar NumPy-style data access patterns can be used within these indexers. For example, in the loc indexer we can combine masking and fancy indexing as in the following:

# In[69]:


data.loc[data.density > 100, ['pop', 'density']]


# #### Additional indexing conventions
# There are a couple extra indexing conventions that might seem at odds with the preceding discussion, but nevertheless can be very useful in practice. First, while _indexing_ refers to columns, _slicing_ refers to rows:

# In[70]:


data['Florida':'Illinois']


# Such slices can also refer to rows by number rather than by index:

# In[71]:


data[1:3]


# In[72]:


data[data.density > 100]


# ### Operating on Data in Pandas
# One of the essential pieces of NumPy is the ability to perform quick element-wiseoperations, both with basic arithmetic (addition, subtraction, multiplication, etc.) and with more sophisticated operations (trigonometric functions, exponential and logarithmic functions, etc.). Pandas inherits much of this functionality from NumPy, and the ufuncs.
# 
# Pandas includes a couple useful twists, however: for unary operations like negation and trigonometric functions, these ufuncs will preserve index and column labels in the output, and for binary operations such as addition and multiplication, Pandas will
# automatically align indices when passing the objects to the ufunc. This means that keeping the context of data and combining data from different sources—both potentially error-prone tasks with raw NumPy arrays—become essentially foolproof ones with Pandas. We will additionally see that there are well-defined operations between one-dimensional Series structures and two-dimensional DataFrame structures.

# #### Ufuncs: Index Preservation
# Because Pandas is designed to work with NumPy, any NumPy ufunc will work on Pandas Series and DataFrame objects. Let’s start by defining a simple Series and DataFrame on which to demonstrate this:

# In[73]:


import pandas as pd
import numpy as np


# In[74]:


rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4))
ser


# In[75]:


df = pd.DataFrame(rng.randint(0, 10, (3, 4)),
                  columns=['A', 'B', 'C', 'D'])
df


# If we apply a NumPy ufunc on either of these objects, the result will be another Pandas object _with the indices preserved:_

# In[76]:


np.exp(ser)


# Or, for a slightly more complex calculation:

# In[77]:


np.sin(df * np.pi / 4)


# ### UFuncs: Index Alignment
# For binary operations on two Series or DataFrame objects, Pandas will align indices in the process of performing the operation. This is very convenient when you are working with incomplete data, as we’ll see in some of the examples that follow.
# #### Index alignment in Series
# As an example, suppose we are combining two different data sources, and find only the top three US states by area and the top three US states by population:

# In[78]:


area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193,
                        'New York': 19651127}, name='population')


# Let’s see what happens when we divide these to compute the population density:

# In[79]:


population / area


# In[80]:


area.index | population.index


# In[81]:


A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
A + B


# If using NaN values is not the desired behavior, we can modify the fill value using appropriate object methods in place of the operators. For example, calling A.add(B) is equivalent to calling A + B, but allows optional explicit specification of the fill value for any elements in A or B that might be missing:

# In[82]:


A.add(B, fill_value=0)


# #### Index alignment in DataFrame
# A similar type of alignment takes place for both columns and indices when you are performing operations on DataFrames:

# In[83]:


A = pd.DataFrame(rng.randint(0, 20, (2, 2)),
                 columns=list('AB'))
A


# In[84]:


B = pd.DataFrame(rng.randint(0, 10, (3, 3)),
                 columns=list('BAC'))
B


# In[85]:


A + B


# In[86]:


fill = A.stack().mean()
A.add(B, fill_value=fill)


# ### Ufuncs: Operations Between DataFrame and Series
# When you are performing operations between a DataFrame and a Series, the index and column alignment is similarly maintained. Operations between a DataFrame and a Series are similar to operations between a two-dimensional and one-dimensional NumPy array. Consider one common operation, where we find the difference of a two-dimensional array and one of its rows:

# In[87]:


A = rng.randint(10, size=(3, 4))
A


# In[88]:


A - A[0]


# In[89]:


df = pd.DataFrame(A, columns=list('QRST'))
df - df.iloc[0]


# In[90]:


df.subtract(df['R'], axis=0)


# In[91]:


halfrow = df.iloc[0, ::2]
halfrow


# In[92]:


df - halfrow


# ### Handling Missing Data
# Here and throughout the book, we’ll refer to missing data in general as null, NaN, or NA values.
# #### None: Pythonic missing data
# The first sentinel value used by Pandas is None, a Python singleton object that is often used for missing data in Python code. Because None is a Python object, it cannot be used in any arbitrary NumPy/Pandas array, but only in arrays with data type 'object' (i.e., arrays of Python objects):

# In[93]:


import numpy as np
import pandas as pd


# In[94]:


vals1 = np.array([1, None, 3, 4])
vals1


# This dtype=object means that the best common type representation NumPy could infer for the contents of the array is that they are Python objects. While this kind of object array is useful for some purposes, any operations on the data will be done at the Python level, with much more overhead than the typically fast operations seen for arrays with native types:

# In[95]:


for dtype in ['object', 'int']:
    print("dtype =", dtype)
    get_ipython().run_line_magic('timeit', 'np.arange(1E6, dtype=dtype).sum()')
    print()


# The use of Python objects in an array also means that if you perform aggregations like sum() or min() across an array with a None value, you will generally get an error:

# In[96]:


vals1.sum()


# #### NaN: Missing numerical data
# The other missing data representation, NaN (acronym for Not a Number), is different; it is a special floating-point value recognized by all systems that use the standard IEEE floating-point representation:

# In[98]:


vals2 = np.array([1, np.nan, 3, 4])
vals2.dtype


# Notice that NumPy chose a native floating-point type for this array: this means that unlike the object array from before, this array supports fast operations pushed into compiled code. You should be aware that NaN is a bit like a data virus—it infects any other object it touches. Regardless of the operation, the result of arithmetic with NaN will be another NaN:

# In[99]:


1 + np.nan


# In[100]:


0 * np.nan


# Note that this means that aggregates over the values are well defined (i.e., they don’t result in an error) but not always useful:

# In[101]:


vals2.sum(), vals2.min(), vals2.max()


# NumPy does provide some special aggregations that will ignore these missing values:

# In[102]:


np.nansum(vals2), np.nanmin(vals2), np.nanmax(vals2)


# Keep in mind that NaN is specifically a floating-point value; there is no equivalent NaN value for integers, strings, or other types.
# #### NaN and None in Pandas
# NaN and None both have their place, and Pandas is built to handle the two of them nearly interchangeably, converting between them where appropriate:

# In[103]:


pd.Series([1, np.nan, 2, None])


# For types that don’t have an available sentinel value, Pandas automatically type-casts when NA values are present. For example, if we set a value in an integer array to np.nan, it will automatically be upcast to a floating-point type to accommodate the NA:

# In[104]:


x = pd.Series(range(2), dtype=int)
x


# In[105]:


x[0] = None
x


# Notice that in addition to casting the integer array to floating point, Pandas automatically converts the None to a NaN value.

# #### Operating on Null Values
# As we have seen, Pandas treats None and NaN as essentially interchangeable for indicating missing or null values. To facilitate this convention, there are several useful methods for detecting, removing, and replacing null values in Pandas data structures. They are:
# 
# isnull()
# 
#     Generate a Boolean mask indicating missing values
#     
# notnull()
# 
#     Opposite of isnull()
#     
# dropna()
# 
#     Return a filtered version of the data
#     
# fillna()
# 
#     Return a copy of the data with missing values filled or imputed
#     
# We will conclude this section with a brief exploration and demonstration of these routines.

# #### Detecting null values
# Pandas data structures have two useful methods for detecting null data: **isnull()** and **notnull()**. Either one will return a Boolean mask over the data. For example:

# In[106]:


data = pd.Series([1, np.nan, 'hello', None])


# In[107]:


data.isnull()


# In[108]:


data[data.notnull()]


# The isnull() and notnull() methods produce similar Boolean results for Data Frames.

# #### Dropping null values
# In addition to the masking used before, there are the convenience methods, dropna() (which removes NA values) and fillna() (which fills in NA values). For a Series, the result is straightforward:

# In[109]:


data.dropna()


# In[110]:


df = pd.DataFrame([[1, np.nan, 2],
              [2, 3, 5],
              [np.nan, 4, 6]])
df


# We cannot drop single values from a DataFrame; we can only drop full rows or full columns. Depending on the application, you might want one or the other, so dropna() gives a number of options for a DataFrame.
# By default, dropna() will drop all rows in which any null value is present:

# In[111]:


df.dropna()


# Alternatively, you can drop NA values along a different axis; axis=1 drops all columns containing a null value:

# In[112]:


df.dropna(axis='columns')


# In[113]:


df.dropna(how ='any')


# In[114]:


df.dropna(how ='all')


# In[115]:


df[3] = np.nan
df


# In[116]:


df.dropna(axis='columns', how='all')


# For finer-grained control, the thresh parameter lets you specify a minimum number of non-null values for the row/column to be kept:

# In[117]:


df.dropna(axis='rows', thresh=3)


# Here the first and last row have been dropped, because they contain only two nonnull values.

# #### Filling null values
# Sometimes rather than dropping NA values, you’d rather replace them with a valid value. This value might be a single number like zero, or it might be some sort of imputation or interpolation from the good values. You could do this in-place using the isnull() method as a mask, but because it is such a common operation Pandas provides the fillna() method, which returns a copy of the array with the null values replaced.

# In[118]:


data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
data


# We can fill NA entries with a single value, such as zero:

# In[119]:


data.fillna(0)


# We can specify a forward-fill to propagate the previous value forward:

# In[120]:


# forward-fill
data.fillna(method='ffill')


# For DataFrames, the options are similar, but we can also specify an axis along which the fills take place:

# In[121]:


df


# In[122]:


df.fillna(method='ffill', axis=1)


# Notice that if a previous value is not available during a forward fill, the NA value remains.

# In[123]:


import pandas as pd
import numpy as np


# In[124]:


index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]

populations = [33871648, 37253956,
18976457, 19378102,
20851820, 25145561]
pop = pd.Series(populations, index=index)
pop


# With this indexing scheme, you can straightforwardly index or slice the series based on this multiple index:

# In[125]:


pop[('California', 2010):('Texas', 2000)]


# But the convenience ends there. For example, if you need to select all values from 2010, you’ll need to do some messy (and potentially slow) munging to make it happen:

# In[126]:


pop[[i for i in pop.index if i[1] == 2010]]


# This produces the desired result, but is not as clean (or as efficient for large datasets) as the slicing syntax we’ve grown to love in Pandas.

# #### The better way: Pandas MultiIndex
# Fortunately, Pandas provides a better way. Our tuple-based indexing is essentially a rudimentary multi-index, and the Pandas MultiIndex type gives us the type of operations we wish to have. We can create a multi-index from the tuples as follows:

# In[127]:


index = pd.MultiIndex.from_tuples(index)
index


# Notice that the MultiIndex contains multiple levels of indexing—in this case, the state names and the years, as well as multiple labels for each data point which encode these levels.
# 
# If we reindex our series with this MultiIndex, we see the hierarchical representation of the data:

# In[128]:


pop = pop.reindex(index)
pop


# Here the first two columns of the Series representation show the multiple index values, while the third column shows the data. Notice that some entries are missing in the first column: in this multi-index representation, any blank entry indicates the
# same value as the line above it.
# 
# Now to access all data for which the second index is 2010, we can simply use the Pandas slicing notation:

# In[129]:


pop[:, 2010]


# The result is a singly indexed array with just the keys we’re interested in. This syntax is much more convenient (and the operation is much more efficient!) than the homespun tuple-based multi-indexing solution that we started with. We’ll now further discuss this sort of indexing operation on hierarchically indexed data.
# #### MultiIndex as extra dimension
# You might notice something else here: we could easily have stored the same data using a simple DataFrame with index and column labels. In fact, Pandas is built with this equivalence in mind. The unstack() method will quickly convert a multiplyindexed Series into a conventionally indexed DataFrame:

# In[130]:


pop_df = pop.unstack()
pop_df


# Naturally, the stack() method provides the opposite operation:

# In[131]:


pop_df.stack()


# In[132]:


pop_df = pd.DataFrame({'total': pop,
                       'under18': [9267089, 9284094,
                                   4687374, 4318033,
                                   5906301, 6879014]})
pop_df


# In[133]:


f_u18 = pop_df['under18'] / pop_df['total']
f_u18.unstack()


# ### Methods of MultiIndex Creation
# The most straightforward way to construct a multiply indexed Series or DataFrame is to simply pass a list of two or more index arrays to the constructor. For example:

# In[134]:


df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['data1', 'data2'])
df


# In[135]:


data = {('California', 2000): 33871648,
        ('California', 2010): 37253956,
        ('Texas', 2000): 20851820,
        ('Texas', 2010): 25145561,
        ('New York', 2000): 18976457,
        ('New York', 2010): 19378102}
pd.Series(data)


# In[136]:


pd.Series(data).unstack()


# #### Explicit MultiIndex constructors
# For more flexibility in how the index is constructed, you can instead use the class method constructors available in the pd.MultiIndex. For example, as we did before, you can construct the MultiIndex from a simple list of arrays, giving the index values within each level:

# In[137]:


pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])


# You can construct it from a list of tuples, giving the multiple index values of each point:

# In[138]:


pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])


# You can even construct it from a Cartesian product of single indices:

# In[139]:


pd.MultiIndex.from_product([['a', 'b'], [1, 2]])


# Similarly, you can construct the MultiIndex directly using its internal encoding by passing levels (a list of lists containing available index values for each level) and labels (a list of lists that reference these labels):

# In[140]:


pd.MultiIndex(levels=[['a', 'b'], [1, 2]],
              labels=[[0, 0, 1, 1], [0, 1, 0, 1]])


# #### MultiIndex level names
# Sometimes it is convenient to name the levels of the MultiIndex. You can accomplish this by passing the names argument to any of the above MultiIndex constructors, or by setting the names attribute of the index after the fact:

# In[141]:


pop.index.names = ['state', 'year']
pop


# With more involved datasets, this can be a useful way to keep track of the meaning of various index values.
# #### MultiIndex for columns
# In a DataFrame, the rows and columns are completely symmetric, and just as the rows can have multiple levels of indices, the columns can have multiple levels as well. Consider the following, which is a mock-up of some (somewhat realistic) medical data:

# In[142]:


# hierarchical indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])

columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])
# mock some data
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37

# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data


# In[143]:


health_data['Guido']


# ### Indexing and Slicing a MultiIndex
# #### Multiply indexed Series
# Consider the multiply indexed Series of state populations we saw earlier:

# In[144]:


pop['California', 2000]


# The MultiIndex also supports _partial indexing_, or indexing just one of the levels in the index. The result is another Series, with the lower-level indices maintained:

# In[145]:


pop['California']


# In[146]:


pop.loc['California':'New York']


# With sorted indices, we can perform partial indexing on lower levels by passing an empty slice in the first index:

# In[147]:


pop[:, 2000]


# In[148]:


pop[pop > 22000000]


# Selection based on fancy indexing also works:

# In[149]:


pop[['California', 'Texas']]


# #### Multiply indexed DataFrames
# A multiply indexed DataFrame behaves in a similar manner. Consider our toy medical DataFrame from before:

# In[150]:


health_data


# In[151]:


health_data['Guido', 'HR']


# In[152]:


health_data.iloc[:2, :2]


# In[153]:


health_data.loc[:, ('Bob', 'HR')]


# Working with slices within these index tuples is not especially convenient; trying to create a slice within a tuple will lead to a syntax error:

# In[154]:


health_data.loc[(:, 1), (:, 'HR')]


# You could get around this by building the desired slice explicitly using Python’s builtin slice() function, but a better way in this context is to use an IndexSlice object, which Pandas provides for precisely this situation. 

# In[155]:


idx = pd.IndexSlice
health_data.loc[idx[:, 1], idx[:, 'HR']]


# ### Rearranging Multi-Indices
# #### Sorted and unsorted indices
# Earlier, we briefly mentioned a caveat, but we should emphasize it more here. _Many of the MultiIndex slicing operations will fail if the index is not sorted_. Let’s take a look at this here.
# We’ll start by creating some simple multiply indexed data where the indices are _not lexographically sorted:_
# 

# In[156]:


index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']
data


# If we try to take a partial slice of this index, it will result in an error:

# In[157]:


try:
    data['a':'b']
except KeyError as e:
    print(type(e))
    print(e)


# For various reasons, partial slices and other similar operations require the levels in the MultiIndex to be in sorted (i.e., lexographical) order. Pandas provides a number of convenience routines to perform this type of sorting; examples are the sort_index() and sortlevel() methods of the DataFrame. We’ll use the simplest, sort_index(), here:

# In[158]:


data = data.sort_index()
data


# With the index sorted in this way, partial slicing will work as expected:

# In[159]:


data['a':'b']


# #### Stacking and unstacking indices
# It is possible to convert a dataset from a stacked multi-index to a simple two-dimensional representation, optionally specifying the level to use:

# In[160]:


pop.unstack(level=0)


# In[161]:


pop.unstack(level=1)


# In[162]:


pop.unstack().stack()


# #### Index setting and resetting
# Another way to rearrange hierarchical data is to turn the index labels into columns; this can be accomplished with the reset_index method. Calling this on the population dictionary will result in a DataFrame with a state and year column holding the information that was formerly in the index. For clarity, we can optionally specify the name of the data for the column representation:

# In[163]:


pop_flat = pop.reset_index(name='population')
pop_flat


# Often when you are working with data in the real world, the raw input data looks like this and it’s useful to build a MultiIndex from the column values. This can be done with the set_index method of the DataFrame, which returns a multiply indexed Data Frame:

# In[164]:


pop_flat.set_index(['state', 'year'])


# ### Data Aggregations on Multi-Indices
# We’ve previously seen that Pandas has built-in data aggregation methods, such as mean(), sum(), and max(). For hierarchically indexed data, these can be passed a level parameter that controls which subset of the data the aggregate is computed on.

# In[165]:


health_data


# Perhaps we’d like to average out the measurements in the two visits each year. We can do this by naming the index level we’d like to explore, in this case the year:

# In[166]:


data_mean = health_data.mean(level='year')
data_mean


# By further making use of the axis keyword, we can take the mean among levels on the columns as well:

# In[167]:


data_mean.mean(axis=1, level='type')


# ### Combining Datasets: Concat and Append
# These operations can involve anything from very straightforward concatenation of two different datasets, to more complicated database-style joins and merges that correctly handle any overlaps between the datasets. Series and DataFrames are built with this type of operation in mind, and Pandas includes functions and methods that make this sort of data wrangling fast and straightforward.

# In[168]:


import pandas as pd
import numpy as np


# In[169]:


def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)
    
# example DataFrame
make_df('ABC', range(3))


# ### Recall: Concatenation of NumPy Arrays
# Concatenation of Series and DataFrame objects is very similar to concatenation of NumPy arrays, which can be done via the np.concatenate function. Recall that with it, you can combine the contents of two or more arrays into a single array:

# In[170]:


x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
np.concatenate([x, y, z])


# The first argument is a list or tuple of arrays to concatenate. Additionally, it takes an axis keyword that allows you to specify the axis along which the result will be concatenated:

# In[171]:


x = [[1, 2],
     [3, 4]]
np.concatenate([x, x], axis=1)


# ### Recall: Concatenation of NumPy Arrays
# Pandas has a function, pd.concat(), which has a similar syntax to np.concatenate but contains a number of options.

# In[172]:


# Signature in Pandas v0.18
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)


# pd.concat() can be used for a simple concatenation of Series or DataFrame objects, just as np.concatenate() can be used for simple concatenations of arrays:

# In[173]:


ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
pd.concat([ser1, ser2])


# It also works to concatenate higher-dimensional objects, such as DataFrames:

# In[174]:


df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
print(df1); print(df2); print(pd.concat([df1, df2]))


# By default, the concatenation takes place row-wise within the DataFrame (i.e., axis=0). Like np.concatenate, pd.concat allows specification of an axis along which concatenation will take place. Consider the following example:

# In[175]:


df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
print(df3); print(df4); print(pd.concat([df3, df4], axis='col'))


# One important difference between np.concatenate and pd.concat is that Pandas concatenation preserves indices, even if the result will have duplicate indices! Consider this simple example:

# In[176]:


x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
y.index = x.index # make duplicate indices!
print(x); print(y); print(pd.concat([x, y]))


# Notice the repeated indices in the result. While this is valid within DataFrames, the outcome is often undesirable. pd.concat() gives us a few ways to handle it
# **Catching the repeats as an error**. If you’d like to simply verify that the indices in the result of pd.concat() do not overlap, you can specify the verify_integrity flag. With this set to True, the concatenation will raise an exception if there are duplicate indices. Here is an example, where for clarity we’ll catch and print the error message:

# In[177]:


try:
    pd.concat([x, y], verify_integrity=True)
except ValueError as e:
    print("ValueError:", e)


# **Ignoring the index**. Sometimes the index itself does not matter, and you would prefer it to simply be ignored. You can specify this option using the ignore_index flag. With this set to True, the concatenation will create a new integer index for the resulting Series:

# In[178]:


print(x); print(y); print(pd.concat([x, y], ignore_index=True))


# **Adding MultiIndex keys**. Another alternative is to use the keys option to specify a label for the data sources; the result will be a hierarchically indexed series containing the data:

# In[179]:


print(x); print(y); print(pd.concat([x, y], keys=['x', 'y']))


# #### Concatenation with joins
# We just looked at, we were mainly concatenating DataFrames with shared column names. In practice, data from different sources might have different sets of column names, and pd.concat offers several options in this case. Consider the concatenation of the following two DataFrames, which have some (but not all!) columns in common:

# In[180]:


df7 = make_df('ABC', [1, 2])
df8 = make_df('BCD', [3, 4])
print(df7); print(df8);


# In[181]:


print(pd.concat([df7, df8])


# By default, the entries for which no data is available are filled with NA values. To change this, we can specify one of several options for the join and join_axes parameters of the concatenate function. By default, the join is a union of the input columns (join='outer'), but we can change this to an intersection of the columns using join='inner':

# In[182]:


print(df7); print(df8);
print(pd.concat([df7, df8], join='inner'))


# Another option is to directly specify the index of the remaining colums using the join_axes argument, which takes a list of index objects. Here we’ll specify that the returned columns should be the same as those of the first input:

# In[183]:


print(df7); print(df8);
print(pd.concat([df7, df8], join_axes=[df7.columns]))


# #### The append() method
# Because direct array concatenation is so common, Series and DataFrame objects have an append method that can accomplish the same thing in fewer keystrokes. For example, rather than calling pd.concat([df1, df2]), you can simply call df1.append(df2):

# In[184]:


print(df1); print(df2); print(df1.append(df2))


# Keep in mind that unlike the append() and extend() methods of Python lists, the append() method in Pandas does not modify the original object—instead, it creates a new object with the combined data. It also is not a very efficient method, because it involves creation of a new index and data buffer. Thus, if you plan to do multiple append operations, it is generally better to build a list of DataFrames and pass them all at once to the concat() function.

# ### Combining Datasets: Merge and Join
# One essential feature offered by Pandas is its high-performance, in-memory join and merge operations. If you have ever worked with databases, you should be familiar with this type of data interaction. The main interface for this is the pd.merge function.

# #### Relational Algebra
# The behavior implemented in pd.merge() is a subset of what is known as relational algebra, which is a formal set of rules for manipulating relational data, and forms the conceptual foundation of operations available in most databases. The strength of the relational algebra approach is that it proposes several primitive operations, which become the building blocks of more complicated operations on any dataset. With this lexicon of fundamental operations implemented efficiently in a database or other program, a wide range of fairly complicated composite operations can be performed.
# 
# Pandas implements several of these fundamental building blocks in the pd.merge() function and the related join() method of Series and DataFrames. As we will see, these let you efficiently link data from different sources.
# #### Categories of Joins
# The pd.merge() function implements a number of types of joins: the one-to-one, many-to-one, and many-to-many joins. All three types of joins are accessed via an identical call to the pd.merge() interface; the type of join performed depends on the form of the input data. Here we will show simple examples of the three types of merges, and discuss detailed options further below.
# #### One-to-one joins
# Perhaps the simplest type of merge expression is the one-to-one join, which is in many ways very similar to the column-wise concatenation.

# In[185]:


df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
print('df1', df1); print('df2', df2)


# To combine this information into a single DataFrame, we can use the pd.merge() function:

# In[186]:


df3 = pd.merge(df1, df2)
df3


# The pd.merge() function recognizes that each DataFrame has an “employee” column, and automatically joins using this column as a key. The result of the merge is a new DataFrame that combines the information from the two inputs. Notice that the order of entries in each column is not necessarily maintained: in this case, the order of the “employee” column differs between df1 and df2, and the pd.merge() function correctly accounts for this. Additionally, keep in mind that the merge in general discards the index, except in the special case of merges by index.
# #### Many-to-one joins
# Many-to-one joins are joins in which one of the two key columns contains duplicate entries. For the many-to-one case, the resulting DataFrame will preserve those duplicate entries as appropriate. Consider the following example of a many-to-one join:

# In[187]:


df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})
print(df3); print(df4); print(pd.merge(df3, df4))


# #### Many-to-many joins
# Many-to-many joins are a bit confusing conceptually, but are nevertheless well defined. If the key column in both the left and right array contains duplicates, then the result is a many-to-many merge. This will be perhaps most clear with a concrete example. Consider the following, where we have a DataFrame showing one or more skills associated with a particular group.

# In[188]:


df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
                              'Engineering', 'Engineering', 'HR', 'HR'],
                    'skills': ['math', 'spreadsheets', 'coding', 'linux',
                               'spreadsheets', 'organization']})
print(df1); print(df5); print(pd.merge(df1, df5))


# These three types of joins can be used with other Pandas tools to implement a wide array of functionality. But in practice, datasets are rarely as clean as the one we’re working with here.

# #### Specifcation of the Merge Key
# We’ve already seen the default behavior of pd.merge(): it looks for one or more matching column names between the two inputs, and uses this as the key. However, often the column names will not match so nicely, and pd.merge() provides a variety of options for handling this.
# #### The on keyword
# Most simply, you can explicitly specify the name of the key column using the on keyword, which takes a column name or a list of column names:

# In[189]:


print(df1); print(df2); print(pd.merge(df1, df2, on='employee'))


# This option works only if both the left and right DataFrames have the specified column name.

# #### The left_on and right_on keywords
# At times you may wish to merge two datasets with different column names; for example, we may have a dataset in which the employee name is labeled as “name” rather than “employee”. In this case, we can use the left_on and right_on keywords to specify the two column names:

# In[190]:


df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
              'salary': [70000, 80000, 120000, 90000]})
print(df1); print(df3);
print(pd.merge(df1, df3, left_on="employee", right_on="name"))


# The result has a redundant column that we can drop if desired—for example, by using the drop() method of DataFrames:

# In[191]:


pd.merge(df1, df3, left_on="employee", right_on="name").drop('name', axis=1)


# #### The left_index and right_index keywords
# Sometimes, rather than merging on a column, you would instead like to merge on an index. For example, your data might look like this:

# In[192]:


df1a = df1.set_index('employee')
df2a = df2.set_index('employee')
print(df1a); print(df2a)


# You can use the index as the key for merging by specifying the left_index and/or right_index flags in pd.merge():

# In[193]:


print(df1a); print(df2a);
print(pd.merge(df1a, df2a, left_index=True, right_index=True))


# For convenience, DataFrames implement the join() method, which performs a merge that defaults to joining on indices:

# In[194]:


print(df1a); print(df2a); print(df1a.join(df2a))


# If you’d like to mix indices and columns, you can combine left_index with right_on or left_on with right_index to get the desired behavior:

# In[195]:


print(df1a); print(df3);
print(pd.merge(df1a, df3, left_index=True, right_on='name'))


# ### Specifying Set Arithmetic for Joins
# In all the preceding examples we have glossed over one important consideration in performing a join: the type of set arithmetic used in the join. This comes up when a value appears in one key column but not the other. Consider this example:

# In[196]:


df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']},
                   columns=['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['wine', 'beer']},
                   columns=['name', 'drink'])
print(df6); print(df7); print(pd.merge(df6, df7))


# Here we have merged two datasets that have only a single “name” entry in common: Mary. By default, the result contains the intersection of the two sets of inputs; this is what is known as an inner join. We can specify this explicitly using the how keyword, which defaults to 'inner':

# In[197]:


pd.merge(df6, df7, how='inner')


# Other options for the how keyword are 'outer', 'left', and 'right'. An outer join returns a join over the union of the input columns, and fills in all missing values with NAs:

# In[198]:


print(df6); print(df7); print(pd.merge(df6, df7, how='outer'))


# The lef join and right join return join over the left entries and right entries, respectively. For example:

# In[199]:


print(df6); print(df7); print(pd.merge(df6, df7, how='left'))


# ### Overlapping Column Names: The sufxes Keyword
# Finally, you may end up in a case where your two input DataFrames have conflicting column names. Consider this example:`

# In[200]:


df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                     'rank': [1, 2, 3, 4]})
df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [3, 1, 4, 2]})
print(df8); print(df9); print(pd.merge(df8, df9, on="name"))


# Because the output would have two conflicting column names, the merge function automatically appends a suffix _x or _y_ to make the output columns unique. If these defaults are inappropriate, it is possible to specify a custom suffix using the suffixes keyword:

# In[201]:


print(df8); print(df9);
print(pd.merge(df8, df9, on="name", suffixes=["_L", "_R"]))


# In[202]:


pop = pd.read_csv('E:/Python_4_DS/notebooks/data/state-population.csv')
areas = pd.read_csv('E:/Python_4_DS/notebooks/data/state-areas.csv')
abbrevs = pd.read_csv('E:/Python_4_DS/notebooks/data/state-abbrevs.csv')

print(pop.head()); print(areas.head()); print(abbrevs.head())


# In[203]:


merged = pd.merge(pop, abbrevs, how='outer',
left_on='state/region', right_on='abbreviation')
merged = merged.drop('abbreviation', 1) # drop duplicate info
merged.head()


# In[204]:


merged.isnull().any()


# In[205]:


merged[merged['population'].isnull()].head()


# In[206]:


merged.loc[merged['state'].isnull(), 'state/region'].unique()


# In[207]:


merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
merged.isnull().any()


# In[208]:


final = pd.merge(merged, areas, on='state', how='left')
final.head()


# In[209]:


final.isnull().any()


# In[210]:


final['state'][final['area (sq. mi)'].isnull()].unique()


# In[211]:


final.dropna(inplace=True)
final.head()


# In[212]:


data2010 = final.query("year == 2010 & ages == 'total'")
data2010.head()


# In[213]:


data2010.set_index('state', inplace=True)
density = data2010['population'] / data2010['area (sq. mi)']


# In[214]:


density.sort_values(ascending=False, inplace=True)
density.head()


# In[215]:


density.tail()


# ### Aggregation and Grouping
# An essential piece of analysis of large data is efficient summarization: computing aggregations like sum(), mean(), median(), min(), and max(), in which a single number gives insight into the nature of a potentially large dataset. In this section, we’ll explore aggregations in Pandas, from simple operations akin to what we’ve seen on NumPy arrays, to more sophisticated operations based on the concept of a groupby.

# In[216]:


import seaborn as sns
planets = sns.load_dataset('planets')
planets.shape


# In[217]:


planets.head()


# #### Simple Aggregation in Pandas
# As with a one dimensional NumPy array, for a Pandas Series the aggregates return a single value:

# In[218]:


rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
ser


# In[219]:


ser.sum()


# In[220]:


ser.sum()


# In[221]:


df = pd.DataFrame({'A': rng.rand(5),
                   'B': rng.rand(5)})
df


# In[222]:


df.mean()


# By specifying the axis argument, you can instead aggregate within each row:

# In[223]:


df.mean(axis='columns')


# In addition, there is a convenience method describe() that computes several common aggregates for each column and returns the result. Let’s use this on the Planets data, for now drop‐
# ping rows with missing values:

# In[224]:


planets.dropna().describe()


# <img src = "C:/Users/Michael/Pictures/Pandas_aggregation.png"/>
# 
# ### GroupBy: Split, Apply, Combine
# #### Split, Apply, Combine
# - The split step involves breaking up and grouping a DataFrame depending on the value of the specified key.
# - The apply step involves computing some function, usually an aggregate, transformation, or filtering, within the individual groups.
# - The combine step merges the results of these operations into an output array.
# 
# <img src = "C:/Users/Michael/Pictures/sap.png"/>
# 
# While we could certainly do this manually using some combination of the masking, aggregation, and merging commands covered earlier, it’s important to realize that the intermediate splits do not need to be explicitly instantiated. Rather, the GroupBy can (often) do this in a single pass over the data, updating the sum, mean, count, min, or other aggregate for each group along the way. The power of the GroupBy is that it abstracts away these steps: the user need not think about how the computation is done under the hood, but rather thinks about the operation as a whole. 

# In[225]:


df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)}, columns=['key', 'data'])
df


# In[226]:


df.groupby('key')


# In[227]:


df.groupby('key').sum()


# #### The GroupBy object
# The GroupBy object is a very flexible abstraction. In many ways, you can simply treat it as if it’s a collection of DataFrames, and it does the difficult things under the hood. Let’s introduce some of the other functionality that can be used with the basic GroupBy operation.
# 
# **Column indexing.** The GroupBy object supports column indexing in the same way as the DataFrame, and returns a modified GroupBy object.

# In[228]:


planets.groupby('method')


# In[229]:


planets.groupby('method')['orbital_period']


# Here we’ve selected a particular Series group from the original DataFrame group by reference to its column name. As with the GroupBy object, no computation is done until we call some aggregate on the object:

# In[230]:


planets.groupby('method')['orbital_period'].median()


# **Iteration over groups.** The GroupBy object supports direct iteration over the groups, returning each group as a Series or DataFrame:

# In[231]:


for (method, group) in planets.groupby('method'):
    print("{0:30s} shape={1}".format(method, group.shape))


# **Dispatch methods.** Through some Python class magic, any method not explicitly implemented by the GroupBy object will be passed through and called on the groups, whether they are DataFrame or Series objects. For example, you can use the describe() method of DataFrames to perform a set of aggregations that describe each group in the data:

# In[232]:


planets.groupby('method')['year'].describe().unstack()


# #### Aggregate, flter, transform, apply
# The preceding discussion focused on aggregation for the combine operation, but there are more options available. In particular, GroupBy objects have aggregate(), filter(), transform(), and apply() methods that efficiently implement a variety of useful operations before combining the grouped data.

# In[233]:


rng = np.random.RandomState(0)
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data1': range(6),
                   'data2': rng.randint(0, 10, 6)},
                  columns = ['key', 'data1', 'data2'])
df


# **Aggregation.** We’re now familiar with GroupBy aggregations with sum(), median(), and the like, but the aggregate() method allows for even more flexibility. It can take a string, a function, or a list thereof, and compute all the aggregates at once. Here is a
# quick example combining all these:

# In[234]:


df.groupby('key').aggregate(['min', np.median, max])


# Another useful pattern is to pass a dictionary mapping column names to operations to be applied on that column:

# In[235]:


df.groupby('key').aggregate({'data1': 'min',
                             'data2': 'max'})


# Filtering. A filtering operation allows you to drop data based on the group properties. For example, we might want to keep all groups in which the standard deviation is larger than some critical value:

# In[236]:


def filter_func(x):
    return x['data2'].std() > 4
print(df); print(df.groupby('key').std());
print(df.groupby('key').filter(filter_func))


# The filter() function should return a Boolean value specifying whether the group passes the filtering. Here because group A does not have a standard deviation greater than 4, it is dropped from the result.
# 
# **Transformation.** While aggregation must return a reduced version of the data, transformation can return some transformed version of the full data to recombine. For such a transformation, the output is the same shape as the input. A common example is to center the data by subtracting the group-wise mean:

# In[237]:


df.groupby('key').transform(lambda x: x - x.mean())


# **The apply() method.** The apply() method lets you apply an arbitrary function to the group results. The function should take a DataFrame, and return either a Pandas object (e.g., DataFrame, Series) or a scalar; the combine operation will be tailored to the type of output returned.

# In[238]:


def norm_by_data2(x):
    # x is a DataFrame of group values
    x['data1'] /= x['data2'].sum()
    return x
print(df); print(df.groupby('key').apply(norm_by_data2))


# #### Specifying the split key
# In the simple examples presented before, we split the DataFrame on a single column name. This is just one of many options by which the groups can be defined, and we’ll go through some other options for group specification here.
# 
# **A list, array, series, or index providing the grouping keys.** The key can be any series or list with a length matching that of the DataFrame.

# In[239]:


L = [0, 1, 0, 1, 2, 0]
print(df); print(df.groupby(L).sum())


# Of course, this means there’s another, more verbose way of accomplishing the df.groupby('key') from before:

# In[240]:


print(df); print(df.groupby(df['key']).sum())


# **A dictionary or series mapping index to group.** Another method is to provide a dictionary that maps index values to the group keys:

# In[241]:


df2 = df.set_index('key')
mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
print(df2); print(df2.groupby(mapping).sum())


# Any Python function. Similar to mapping, you can pass any Python function that will input the index value and output the group:

# In[242]:


print(df2); print(df2.groupby(str.lower).mean())


# A list of valid keys. Further, any of the preceding key choices can be combined to group on a multi-index:

# In[243]:


df2.groupby([str.lower, mapping]).mean()


# #### Grouping example

# In[244]:


decade = 10 * (planets['year'] // 10)
decade = decade.astype(str) + 's'
decade.name = 'decade'
planets.groupby(['method', decade])['number'].sum().unstack().fillna(0)


# ### Pivot Tables
# We have seen how the GroupBy abstraction lets us explore relationships within a dataset. A pivot table is a similar operation that is commonly seen in spreadsheets and other programs that operate on tabular data. The pivot table takes simple columnwise data as input, and groups the entries into a two-dimensional table that provides a multidimensional summarization of the data. The difference between pivot tables and GroupBy can sometimes cause confusion; it helps me to think of pivot tables as essentially a multidimensional version of GroupBy aggregation. That is, you splitapply-combine, but both the split and the combine happen across not a onedimensional index, but across a two-dimensional grid.
# #### Motivating Pivot Tables

# In[245]:


import numpy as np
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')


# In[246]:


titanic.head()


# #### Pivot Tables by Hand

# In[247]:


titanic.groupby('sex')[['survived']].mean()


# This immediately gives us some insight: overall, three of every four females on board survived, while only one in five males survived! This is useful, but we might like to go one step deeper and look at survival by both sex and, say, class. Using the vocabulary of GroupBy, we might proceed using something like this: we group by class and gender, select survival, apply a mean aggregate, combine the resulting groups, and then unstack the hierarchical index to reveal the hidden multidimensionality. In code:

# In[248]:


titanic.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack()


# This gives us a better idea of how both gender and class affected survival, but the code is starting to look a bit garbled. While each step of this pipeline makes sense in light of the tools we’ve previously discussed, the long string of code is not particularly
# easy to read or use. This two-dimensional GroupBy is common enough that Pandas includes a convenience routine, pivot_table, which succinctly handles this type of multidimensional aggregation.
# #### Pivot Table Syntax
# Here is the equivalent to the preceding operation using the pivot_table method of DataFrames:

# In[249]:


titanic.pivot_table('survived', index='sex', columns='class')


# #### Multilevel pivot tables
# Just as in the GroupBy, the grouping in pivot tables can be specified with multiple levels, and via a number of options. For example, we might be interested in looking at age as a third dimension. We’ll bin the age using the pd.cut function:

# In[250]:


age = pd.cut(titanic['age'], [0, 18, 80])
titanic.pivot_table('survived', ['sex', age], 'class')


# We can apply this same strategy when working with the columns as well; let’s add info on the fare paid using pd.qcut to automatically compute quantiles:

# In[251]:


fare = pd.qcut(titanic['fare'], 2)
titanic.pivot_table('survived', ['sex', age], [fare, 'class'])


# #### Additional pivot table options
# The full call signature of the pivot_table method of DataFrames is as follows:

# In[252]:


# call signature as of Pandas 0.18
DataFrame.pivot_table(data, values=None, index=None, columns=None,
                      aggfunc='mean', fill_value=None, margins=False,
                      dropna=True, margins_name='All')


# Two of the options, fill_value and dropna, have to do with missing data and are fairly straightforward; we will not show examples of them here. The aggfunc keyword controls what type of aggregation is applied, which is a mean by default. As in the GroupBy, the aggregation specification can be a string representing one of several common choices ('sum', 'mean', 'count', 'min', 'max', etc.) or a function that implements an aggregation (np.sum(), min(), sum(), etc.). Additionally, it can be specified as a dictionary mapping a column to any of the above desired options:

# In[253]:


titanic.pivot_table(index='sex', columns='class',
                    aggfunc={'survived':sum, 'fare':'mean'})


# Notice also here that we’ve omitted the values keyword; when you’re specifying a mapping for aggfunc, this is determined automatically. At times it’s useful to compute totals along each grouping. This can be done via the margins keyword:

# In[254]:


titanic.pivot_table('survived', index='sex', columns='class', margins=True)


# Here this automatically gives us information about the class-agnostic survival rate by gender, the gender-agnostic survival rate by class, and the overall survival rate of 38%. The margin label can be specified with the margins_name keyword, which defaults to "All".

# In[255]:


E:\Python_4_DS\notebooks\data


# In[256]:


births = pd.read_csv('E:/Python_4_DS/notebooks/data/births.csv')


# In[257]:


births.head()


# In[258]:


births['decade'] = 10 * (births['year'] // 10)
births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')


# In[259]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
sns.set() # use Seaborn styles
births.pivot_table('births', index='year', columns='gender', aggfunc='sum').plot()
plt.ylabel('total births per year');


# In[260]:


quartiles = np.percentile(births['births'], [25, 50, 75])
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])


# In[261]:


births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')


# In[262]:


# set 'day' column to integer; it originally was a string due to nulls
births['day'] = births['day'].astype(int)


# In[263]:


# create a datetime index from the year, month, day
births.index = pd.to_datetime(10000 * births.year +
                              100 * births.month +
                              births.day, format='%Y%m%d')
births['dayofweek'] = births.index.dayofweek


# In[264]:


import matplotlib.pyplot as plt
import matplotlib as mpl
births.pivot_table('births', index='dayofweek',
                   columns='decade', aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mean births by day');


# In[265]:


births_by_date = births.pivot_table('births',
                                    [births.index.month, births.index.day])
births_by_date.head()


# In[266]:


births_by_date.index = [pd.datetime(2012, month, day)
                        for (month, day) in births_by_date.index]
births_by_date.head()


# In[267]:


# Plot the results
fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax);


# ### Vectorized String Operations
# One strength of Python is its relative ease in handling and manipulating string data. Pandas builds on this and provides a comprehensive set of vectorized string operations that become an essential piece of the type of munging required when one is working with (read: cleaning up) real-world data. In this section, we’ll walk through some of the Pandas string operations, and then take a look at using them to partially clean up a very messy dataset of recipes collected from the Internet.
# #### Introducing Pandas String Operations
# We saw in previous sections how tools like NumPy and Pandas generalize arithmetic operations so that we can easily and quickly perform the same operation on many array elements. For example:

# In[268]:


import numpy as np
x = np.array([2, 3, 5, 7, 11, 13])
x * 2


# This _vectorization_ of operations simplifies the syntax of operating on arrays of data: we no longer have to worry about the size or shape of the array, but just about what operation we want done. For arrays of strings, NumPy does not provide such simple access, and thus you’re stuck using a more verbose loop syntax:

# In[269]:


data = ['peter', 'Paul', 'MARY', 'gUIDO']
[s.capitalize() for s in data]


# This is perhaps sufficient to work with some data, but it will break if there are any missing values. For example:

# In[270]:


data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
[s.capitalize() for s in data]


# Pandas includes features to address both this need for vectorized string operations and for correctly handling missing data via the str attribute of Pandas Series and Index objects containing strings. So, for example, suppose we create a Pandas Series with this data:

# In[271]:


import pandas as pd
names = pd.Series(data)
names


# We can now call a single method that will capitalize all the entries, while skipping over any missing values:

# In[272]:


names.str.capitalize()


# #### Tables of Pandas String Methods
# If you have a good understanding of string manipulation in Python, most of Pandas’ string syntax is intuitive enough that it’s probably sufficient to just list a table of available methods; we will start with that here, before diving deeper into a few of the subtleties. The examples in this section use the following series of names:

# In[273]:


monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam',
                   'Eric Idle', 'Terry Jones', 'Michael Palin'])


# #### Methods similar to Python string methods
# Nearly all Python’s built-in string methods are mirrored by a Pandas vectorized string method. Here is a list of Pandas str methods that mirror Python string methods:
# 
#     len() lower() translate() islower()
#     ljust() upper() startswith() isupper()
#     rjust() find() endswith() isnumeric()
#     center() rfind() isalnum() isdecimal()
#     zfill() index() isalpha() split()
#     strip() rindex() isdigit() rsplit()
#     rstrip() capitalize() isspace() partition()
#     lstrip() swapcase() istitle() rpartition()

# In[274]:


monte.str.lower()


# In[275]:


monte.str.len()


# In[276]:


monte.str.startswith('T')


# In[277]:


monte.str.split()


# <img src = "C:/Users/Michael/Pandas_aggregation.png"/>

# #### Miscellaneous methods
# **Vectorized item access and slicing.** The get() and slice() operations, in particular, enable vectorized element access from each array. For example, we can get a slice of the first three characters of each array using str.slice(0, 3). Note that this behavior is also available through Python’s normal indexing syntax—for example, df.str.slice(0, 3) is equivalent to df.str[0:3]:

# In[278]:


monte.str[0:3]


# Indexing via df.str.get(i) and df.str[i] is similar.
# 
# These get() and slice() methods also let you access elements of arrays returned by split(). For example, to extract the last name of each entry, we can combine split() and get():

# In[279]:


monte.str.split().str.get(-1)


# **Indicator variables.** Another method that requires a bit of extra explanation is the get_dummies() method. This is useful when your data has a column containing some sort of coded indicator. For example, we might have a dataset that contains information in the form of codes, such as A=“born in America,” B=“born in the United Kingdom,” C=“likes cheese,” D=“likes spam”:

# In[280]:


full_monte = pd.DataFrame({'name': monte,
                           'info': ['B|C|D', 'B|D', 'A|C', 'B|D', 'B|C',
                                    'B|C|D']})
full_monte


# The get_dummies() routine lets you quickly split out these indicator variables into a DataFrame:

# In[281]:


full_monte['info'].str.get_dummies('|')


# ### Example: Recipe Database

# In[282]:


# !curl -O http://openrecipes.s3.amazonaws.com/recipeitems-latest.json.gz
# !gunzip recipeitems-latest.json.gz
try:
    recipes = pd.read_json('recipeitems-latest.json')
except ValueError as e:
    print("ValueError:", e)


# In[283]:


with open('E:/Python_4_DS/datasets/recipeitems-latest.json') as f:
    line = f.readline()
pd.read_json(line).shape


# In[290]:


# read the entire file into a Python array
with open('E:/Python_4_DS/datasets/recipeitems-latest.json', 'r') as f:
    # Extract each line
    data = (line.strip() for line in f)
    # Reformat so each line is the element of a list
    data_json = "[{0}]".format(','.join(data))
# read the result as a JSON
recipes = pd.read_json(data_json)


# In[286]:


recipes.shape


# ### Working with Time Series
# Pandas was developed in the context of financial modeling, so as you might expect, it contains a fairly extensive set of tools for working with dates, times, and time indexed data. Date and time data comes in a few flavors:
# - Time stamps reference particular moments in time (e.g., July 4th, 2015, at 7:00 a.m.).
# - Time intervals and periods reference a length of time between a particular beginning and end point—for example, the year 2015. Periods usually reference a special case of time intervals in which each interval is of uniform length and doesnot overlap (e.g., 24 hour-long periods constituting days).
# - Time deltas or durations reference an exact length of time (e.g., a duration of 22.56 seconds).

# ### Dates and Times in Python
# #### Native Python dates and times: datetime and dateutil
# Python’s basic objects for working with dates and times reside in the built-in date time module. Along with the third-party dateutil module, you can use it to quickly perform a host of useful functionalities on dates and times. For example, you can manually build a date using the datetime type:

# In[291]:


from datetime import datetime
datetime(year=2015, month=7, day=4)


# Or, using the dateutil module, you can parse dates from a variety of string formats:

# In[292]:


from dateutil import parser
date = parser.parse("4th of July, 2015")
date


# Once you have a datetime object, you can do things like printing the day of the week:

# In[293]:


date.strftime('%A')


# #### Typed arrays of times: NumPy’s datetime64
# The weaknesses of Python’s datetime format inspired the NumPy team to add a set of native time series data type to NumPy. The datetime64 dtype encodes dates as 64-bit integers, and thus allows arrays of dates to be represented very compactly. The date time64 requires a very specific input format:

# In[294]:


import numpy as np
date = np.array('2015-07-04', dtype=np.datetime64)
date


# Once we have this date formatted, however, we can quickly do vectorized operations on it:

# In[295]:


date + np.arange(12)


# In[296]:


np.datetime64('2015-07-04')


# In[297]:


np.datetime64('2015-07-04 12:00')


# In[298]:


np.datetime64('2015-07-04 12:59:59.50', 'ns')


# #### Dates and times in Pandas: Best of both worlds
# Pandas builds upon all the tools just discussed to provide a Timestamp object, which combines the ease of use of datetime and dateutil with the efficient storage and vectorized interface of numpy.datetime64. From a group of these Timestamp objects, Pandas can construct a DatetimeIndex that can be used to index data in a Series or DataFrame; we’ll see many examples of this below.
# For example, we can use Pandas tools to repeat the demonstration from above. We can parse a flexibly formatted string date, and use format codes to output the day of the week:

# In[299]:


import pandas as pd
date = pd.to_datetime("4th of July, 2015")
date


# In[300]:


date.strftime('%A')


# Additionally, we can do NumPy-style vectorized operations directly on this same object:

# In[301]:


date + pd.to_timedelta(np.arange(12), 'D')


# ### Pandas Time Series: Indexing by Time
# Where the Pandas time series tools really become useful is when you begin to index data by timestamps. For example, we can construct a Series object that has timeindexed data:

# In[302]:


index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                          '2015-07-04', '2015-08-04'])
data = pd.Series([0, 1, 2, 3], index=index)
data


# Now that we have this data in a Series, we can make use of any of the Series indexing patterns we discussed in previous sections, passing values that can be coerced into dates:

# In[303]:


data['2014-07-04':'2015-07-04']


# There are additional special date-only indexing operations, such as passing a year to obtain a slice of all data from that year:

# In[304]:


data['2015']


# ### Pandas Time Series Data Structures
# This section will introduce the fundamental Pandas data structures for working with time series data:
# 
# - _For time stamps_, Pandas provides the Timestamp type. As mentioned before, it is essentially a replacement for Python’s native datetime, but is based on the more efficient numpy.datetime64 data type. The associated index structure is DatetimeIndex.
# - _For time periods_, Pandas provides the Period type. This encodes a fixedfrequency interval based on numpy.datetime64. The associated index structure is PeriodIndex.
# - _For time deltas or durations_, Pandas provides the Timedelta type. Timedelta is a more efficient replacement for Python’s native datetime.timedelta type, and is based on numpy.timedelta64. The associated index structure is TimedeltaIndex.
# 
# The most fundamental of these date/time objects are the Timestamp and DatetimeIndex objects. While these class objects can be invoked directly, it is more common to use the pd.to_datetime() function, which can parse a wide variety of formats. Passing a single date to pd.to_datetime() yields a Timestamp; passing a series of dates by default yields a DatetimeIndex:

# In[306]:


dates = pd.to_datetime([datetime(2015, 7, 3), '4th of July, 2015',
                        '2015-Jul-6', '07-07-2015', '20150708'])
dates


# Any DatetimeIndex can be converted to a PeriodIndex with the to_period() function with the addition of a frequency code; here we’ll use 'D' to indicate daily frequency:

# In[307]:


dates.to_period('D')


# A TimedeltaIndex is created, for example, when one date is subtracted from another:

# In[308]:


dates - dates[0]


# #### Regular sequences: pd.date_range()
# To make the creation of regular date sequences more convenient, Pandas offers a few functions for this purpose: pd.date_range() for timestamps, pd.period_range() for periods, and pd.timedelta_range() for time deltas. We’ve seen that Python’s range() and NumPy’s np.arange() turn a startpoint, endpoint, and optional stepsize into a sequence. Similarly, pd.date_range() accepts a start date, an end date, and an optional frequency code to create a regular sequence of dates. By default, the frequency is one day:

# In[309]:


pd.date_range('2015-07-03', '2015-07-10')


# Alternatively, the date range can be specified not with a start- and endpoint, but with a startpoint and a number of periods:

# In[310]:


pd.date_range('2015-07-03', periods=8)


# You can modify the spacing by altering the freq argument, which defaults to D. For example, here we will construct a range of hourly timestamps:

# In[311]:


pd.date_range('2015-07-03', periods=8, freq='H')


# To create regular sequences of period or time delta values, the very similar pd.period_range() and pd.timedelta_range() functions are useful. Here are some monthly periods:

# In[312]:


pd.period_range('2015-07', periods=8, freq='M')


# And a sequence of durations increasing by an hour:

# In[313]:


pd.timedelta_range(0, periods=10, freq='H')


# <img src = 'C:/Users/Michael/Pictures/Frequency_offset.png'/>

# Additionally, you can change the month used to mark any quarterly or annual code by adding a three-letter month code as a suffix:
# 
# - Q-JAN, BQ-FEB, QS-MAR, BQS-APR, etc.
# - A-JAN, BA-FEB, AS-MAR, BAS-APR, etc.
# 
# In the same way, you can modify the split-point of the weekly frequency by adding a three-letter weekday code:
# 
# - W-SUN, W-MON, W-TUE, W-WED, etc.
# 
# On top of this, codes can be combined with numbers to specify other frequencies. For example, for a frequency of 2 hours 30 minutes, we can combine the hour (H) and minute (T) codes as follows:

# In[314]:


pd.timedelta_range(0, periods=9, freq="2H30T")


# All of these short codes refer to specific instances of Pandas time series offsets, which can be found in the pd.tseries.offsets module. For example, we can create a business day offset directly as follows:

# In[315]:


from pandas.tseries.offsets import BDay
pd.date_range('2015-07-01', periods=5, freq=BDay())


# In[ ]:




