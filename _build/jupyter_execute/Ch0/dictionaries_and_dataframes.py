#!/usr/bin/env python
# coding: utf-8

# ## Dictionaries and DataFrames
# 
# ### Data, Three Ways
# 
# In this book, data (i.e., a collection of information) is stored as one of three variable types.  These types are:
# * list
# * dict
# * DataFrame
# 
# and we will discuss the relative advantages and disadvantages of each type here.
# 
# Recall from our earlier example the list of daily stock returns, re-created below.

# In[1]:


daily_stock_returns = [0.03, 0.01, -0.02, 0.01, -0.01]


# Lists are the easiest way to deal with data, but they're also the most limited.  For instance, what does `daily_stock_returns[2]` refer to?  We know that it has value $-0.02$, since that's the third element of the list.  But without any other reference point, the utility of this data is low.  We don't know, for instance, what date corresponds to list index value 2.  We also don't know which stock's returns are represented in this list.
# 
# Thus, lists keep track of a very limited amount of information.  They are simple and convenient, and we'll use them as appropriate.  Lists are a fundamental tool, and we'll never do away with them entirely.  However, for certain applications, better tools exist.
# 
# ### Dictionaries
# 
# Lists are quick and convenient.  No matter how advanced you get in programming, you will always make use of lists.  However, lists aren't the best tool for every job.
# 
# For example, one limitation of lists is that we have to refer to items by their position in the list.  If we type `daily_stock_returns[0]`, we'd get the stock return for the first item in the list.  But what is `0`?  Besides a relative positioning, it doesn't tell us anything.  In some cases, it would be better if we could access other information, like the date of the stock return.
# 
# In python, a `dictionary` is a tool for storing information in a *key-value* structure.  Have a look at the following dictionary, and we'll use it to clarify what is meant by "key-value."
# 
# ```python3
# finance_dict = {'debt': 'something that is owed or that one is bound to pay to or perform for another',
#                 'equity': 'the monetary value of a property or business beyond any amounts owed on it in mortgages, claims, liens, etc.'
#                 'mortgage': 'a conveyance of an interest in property as security for the repayment of money borrowed'}
# ```
# 
# These words (definitions taken from dictionary.com), make up a small dictionary variable which we've named `finance_dict`.
# 
# Each word in the dictionary (`debt`, `equity`, `mortgage`) constitutes a *key*.  We "look up" keys in dictionaries to find their *values*.  Thus, the key is a word and the value is the definition.  The command
# ```python3
# finance_dict['debt']
# ```
# would return the definition for debt.
# 
# Returning to the daily stock returns example, suppose that we want to keep track of the day on which each return occurs.  This is accomplished with a dictionary below.

# In[2]:


daily_dict = {'7/8/19':0.03,
             '7/9/19':0.01,
             '7/10/19':-0.02,
             '7/11/19':0.01,
             '7/12/19':-0.01}


# Now, given the variable `daily_dict`, we can quickly look up the stock return from $7/8/19$ by entering
# ```python3
# daily_dict['7/8/19']
# ```
# 
# This adds a bit of utility to the data, because now it includes additional information.  The keys and the values of a dictionary can each be returned individually.  Suppose we wish to know what dates are included in this data:

# In[3]:


daily_dict.keys()


# or alternatively the returns:

# In[4]:


daily_dict.values()


# Recall that, with lists, the only reference point is the index of elements in each list.  For example, to get the first element of `daily_stock_returns`, we use `daily_stock_returns[0]`.  To add to the list, we simply need to use `.append()` and Python adds to the end of the list.  To remove items from a list, we call `.pop(i)` and Python will remove the element in position `i` of the list.
# 
# Dictionaries work slightly differently, since they have more structure to them.  To add to a dictionary, we need to specify both a key (word) and a value (definition).  We do this with the `.append()` function.  The function takes as an input a dictionary of new key-value pairs that we want to add.
# 
# Thus, to add one more day of return values to `daily_dict`, we'd do:

# In[5]:


daily_dict.update( {'7/15/19':0.04} )


# while for a list we'd do

# In[6]:


daily_stock_returns.append(0.04)


# Note that either lists or dictionaries allow for multiple values to be added simultaneously.

# In[7]:


daily_dict.update( {'7/16/19':0.02, '7/17/19':-0.01} )
daily_stock_returns = daily_stock_returns + [0.02, -0.01]


# Thus, to add multiple items to a dictionary, we call `.append()` and give as an argument another dictionary of key-value pairs to add.
# 
# To add multiple items to a list, the syntax changes!  The `.append()` function takes whatever you put inside the parentheses and adds that input, as is, to the list.  We'll see later that lists are flexible and that makes them quite convenient to use.  However, in this case, the flexibility of a list is tricky.  Lists can store elements of different types, so if we used `.append( [.02, -.01] )` then Python would as a list element to the pre-existing list of numbers.  The following example clarifies.

# In[8]:


my_list = [1, 2, 3]
my_list = my_list + [4, 5]
print(my_list)


# In[9]:


my_list = [1, 2, 3]
my_list.append( [4,5] )
print(my_list)


# Deleting key-value pairs in a dictionary is straightforward.  Simply instruct Python to delete a key from the dictionary with `del`.

# In[10]:


my_dict = {'word 1': 'dfn 1', 'word 2':'dfn 2'}
del my_dict['word 1']
print(my_dict)


# ### DataFrames
# 
# Let's continue with the example of stock return data, and now suppose that we want to run a CAPM equation to estimate a firm's cost of equity.  Recall that CAPM states
# 
# $$
# r_{i,t}-r_{f,t} = \beta_i(r_{m,t} - r_{f,t})
# $$
# 
# where $r_{i,t}$ is the stock return for firm $i$ at time $t$, $r_{f,t}$ is the risk-free rate at time $t$, and $r_{m,t}$ is the market return at time $t$.  The difference $r_{m,t}-r_{f,t}$ is called the *market risk premium*.
# 
# For the sake of continuity, the daily stock return data will match that of the previous section, so that the keys in `daily_dict` correspond to $\text{Date}$ and the valeus in `daily_dict` correspond to $r_{i,t}$ in the table below.  Now let's add in information on the market return and the risk free rate.
# 
# | Date | $r_i$ | $r_m$ | $r_f$ |
# | --- | --- | --- | --- |
# | 7/8/19 | 0.03 | 0.02 | 0.01 |
# | 7/9/19 | 0.01 | 0.01 | 0.01 |
# | 7/10/19 | -0.02 | -0.03 | 0.01 |
# | 7/11/19 | 0.01 | 0.02 | 0.01 |
# | 7/12/19 | -0.01 | -0.03 | 0.01 |
# 
# The question becomes: how do we store this information in Python?
# 
# In order to estimate at a CAPM equation (which is covered in the next chapter), we will need to be able to reference $r_{i,t}$, $r_{m,t}$, and $r_{f,t}$ individually, and tell Python what to do with each of these series of returns.
# 
# If we use lists to keep track of everything then we will have the following:
# ```python3
# r_i = [0.03, 0.01, -0.02, 0.01, -0.01]
# r_m = [0.02, 0.01, -0.03, 0.02, -0.03]
# r_f = [0.01, 0.01, 0.01, 0.01, 0.01]
# t = ['7/8/19', '7/9/19', '7/10/19', '7/11/19', '7/12/19']
# ```
# 
# This is a bad practice for at least a couple of reasons.  First, one has to be extremely careful that the data line up properly so that `r_i[k]`, `r_m[k]`, and `r_f[k]` correspond to returns on the same date for every `k`.  Suppose that there is some missing data for some firm $j$ such that `r_j = [0.05, 0.02, 0.03, -0.04]`.  Without any additional information, it is impossible to track down which data point for firm $j$ is missing.  Second, it's difficult to reference returns at a particular date.  Suppose that you want to know the market return on `7/11/19`.  You would first have to determine that `t[k] = '7/11/19'` when `k = 3` and then go look up `r_m[3]` to get the market return.  Note that neither of these considerations imply that it is impossible to use lists to hold all the requisite data, it's just inconvenient for the programmer.  Remember, Python is supposed to make your life easier.
# 
# Suppose instead that we use a dictionary based approach to hold all of the data.  One way to do this is to construct a *nested dictionary*.  Nested dictionaries look like:
# ```python3
# nested_dict = {'finance':
#                 {'verb':'to supply with money or capital',
#                  'noun':'the management of revenues'},
#                'rate':
#                 {'verb':'to estimate the value or worth of',
#                  'noun':'the amount of a charge or payment with reference to some basis of calculation'}
#               }
# ```
# Here there is a dictionary with keys `'finance'` and `'rate'`.  The key `'finance'` has a value which is itself a dictionary: one key named `'verb'` which has value equal to the definition of "finance" used as a verb and another key named `'noun'` which has value equal to the definition of "finance" used as a noun.  Likewise the key `'rate'` has a value which is itself a dictionary.
# 
# If one enters `nested_dict['finance']`, Python will return the dictionary `{'verb':'to supply with money or capital', 'noun':'the management of revenues'}`.  Thus, to look up what the noun usage of "finance" is, one simply types `nested_dict['finance']['noun']`, which tells Python to look up the `noun` value to the dictionary value given by the key `'finance'`.
# 
# In the conext of the current problem, a nested dictionary might look like:
# ```python3
# daily_returns = {'r_i': {'7/8/19':0.03, '7/9/19':0.01, '7/10/19':-0.02, '7/11/19':0.01, '7/12/19':-0.01},
#                  'r_m': {'7/8/19':0.02, '7/9/19':0.01, '7/10/19':-0.03, '7/11/19':0.02, '7/12/19':-0.03},
#                  'r_f': {'7/8/19':0.01, '7/9/19':0.01, '7/10/19':0.01, '7/11/19':0.01, '7/12/19':0.01}}
# ```
# The dictionary approach adds a convenience to the problem.  Now, if one wants to look up the market return on `7/11/19` one simply has to type `daily_returns['r_m']['7/11/19']`.
# 
# Unfortunately, this approach still isn't perfect.  Remember, CAPM tells us that the excess return $r_{i,t}-r_{f,t}$ is defined by a linear function of the market risk premium $r_{m,t}-r_{f,t}$.  Therefore, what we want to do is to be able to tell Python to calculate the excess return and the market risk premium.  This is doable with a nested dictionary format, but it's a little complicated.  One would have to do something like the following (feel free to skip this code):
# ```python3
# daily_returns['r_excess'] = {}
# daily_returns['r_riskpremium'] = {}
# for t in daily_returns['r_f'].values():
#     daily_returns['r_excess'].update(t:daily_returns['r_i'][t]-daily_returns['r_f'][t])
#     daily_returns['r_riskpremium'].update(t:daily_returns['r_m'][t]-daily_returns['r_f'][t])
# ```
# This is five long lines of code.  That means lots of typing and plenty of room for typos.  Nested dictionaries are *not* the recommended way to hold and manage data.
# 
# So what *is* the recommended way to hold data in Python?  We need to use pandas.
# 
# Pandas is the standard module for working with datasets in Python, written by Wes McKinney while at AQR Capital Management.  A **module** is a collection of user-defined functions, written by one or more people, and made available for use by everyone.  The `wacc()` function from earlier in this chapter is an example of a user-defined function.  When a set of userful and related functions are created, the author(s) of these functions sometimes choose to share this set of functions with the world to make Python an even more convenient language for everyone else.
# 
# Modules that are not part of the standard Python library need to be **imported** using an import statement like:
# ```
# import pandas
# ```
# In the above, the module `pandas` is imported.  What this means is that now the functions available under `pandas` are available for you to use.  If you do not import the pandas module, the functions inside of it are unkown to Python.
# 
# To reference the functions inside of the `pandas` module, we use `pandas.<function_name>()`.  For example, `pandas` has a function called `read_csv()`, so we would use this function by typing `pandas.read_csv()`.
# 
# There are some modules, like `numpy` or `pandas` that are so frequently used in Python programming, they have unofficial ''standard'' ways of importing the module with an abbreviation for our later convience.  Two examples are given below:

# In[11]:


import pandas as pd
import numpy as np


# Basically, `import numpy as np` tells Python that we want to import `numpy`, but give it a nickname of `np` so that we can refer to the module by that nickname.
# 
# Now, instead of having to type `pandas.read_csv()` as before, we simply refer to `pandas` by its nickname and type `pd.read_csv()`.  It may not seem like a huge shortcut, but it's a very common.
# 
# We will use `pandas` for a lot of our work in this class.  Note that tutorials and recipes (example pieces of code to perform fairly common tasks) are easy to find [online](https://pandas.pydata.org/pandas-docs/stable/tutorials.html).
# 
# The stock return data that we will use is included with this handout, so we will read the data from CoCalc.  This highlights two important features of the `read_csv()` function.  First, it can pull files from a website directly (as long as the file is formatted as a csv file).  Second, it can read compressed files (note that the file name used here ends with `.gz`, a type of file compression).  File compression is an important option because of the convenience it provides.  Note that the stock data we have here would be too large to be allowed to be hosted for free on GitHub if the file were not compressed.  Moreover, other cloud-based storage solutions like Amazon S3 will charge based on the amount of storage you request, so having the ability to use compressed files means you spend less money on storage costs.
# 
# The `read_csv()` function *returns* a value.  The type of that value is not a number, string, list, or dictionary, but rather a pandas-specific variable type called a **DataFrame**.  In a moment, you'll see what one looks like.  DataFrames are essentially a nested dictionary type of structure, but with a ton of convenience features added in to make them easy to work with.  For now, use the `.read_csv()` function and then tell Python that the returned value should be set to a variable named `data`.

# In[12]:


data = pd.read_csv('https://raw.githubusercontent.com/financedatascience/data/master/stocks/all_stocks_5yr.csv.gz')


# The `data` variable is a pandas DataFrame.  Just like string variables have the `.upper()` function to translate them into all upper case, and dictionary variables have the `.keys()` function to get the keys (words) in the dictionary, DataFrame variables have some special functions specific to them.  One of these is called `.head()`, which prints out a snippet of the data file.

# In[13]:


data.head()


# In the printout, names are marked in bold font.  The csv file has column headers `['date', 'open', 'high', 'low', 'close', 'volume', 'Name', 'ret', 'Mkt', 'SMB', 'HML', 'RMW', 'CMA', 'RF']` in the first row of the file (this would be row 1 if we opened the csv file in Excel).  The pandas function `read_csv()` by default will take this first row to be the names of the columns.  This allows us to reference the column of data:

# In[14]:


data['close']


# Here, Python smartly prints out only a small subset of the `'close'` column of data.  The first five rows (row numbers 0-5) are printed, as well as the last five rows (row numbers 619035-619039).
# 
# Be careful, names are given as strings.  Python is fine with `data['close']`, but if you type `data[close]` then Python will think you're trying to use a variable `close` to store the column name.  For example if one were to type
# ```python3
# close = 'open'
# data[close]
# ```
# then Python would give back the data in column `'open'`.
# 
# Note that there are bold numbers 0-4 running down the left hand side of the `.head()` printout.  This is because the first row of data (row 2, in Excel) is read in an by default given the name `0` by Python (because Python starts counting at zero).  Hence, we could refer to a row based on this name, just like we do with a column name.  Note that if you type `data[0]`, Python will get confused.  The name inside square brackets is, according to pandas' rules for DataFrame variables, expected to be a column name and not a row name.  For the moment, let's skip over how to refer to the first row of data by using the name `0` printed on the left hand side of the printout above.
# 
# A very typical use case with DataFrames is to look up a row (or set of rows) based on a value stored in one of the columns of the DataFrame.  For example, we can select a row based on the value for `date`.  This would be achieved by entering:

# In[15]:


data[ data['date'] == '2013-02-14' ]


# At the bottom of this truncated prinout, Python informs us that there are 474 rows of data.  That is, we have 474 different stocks with return data for February 14, 2013.
# 
# Let's break down what the line of code does:
# 
# $\color{red}{\texttt{data[}}\color{blue}{\texttt{data['date']}}\color{black}{\textbf{==}\texttt{'2013-02-14'}}\color{red}{\texttt{]}}$
# 
# Work from the inside (stuff inside the red text) out.
# - $\color{blue}{\texttt{data['date']}}$: look up column of data named `date`
# - $\textbf{==}\texttt{'2013-02-14'}$: check whether each row in the column named `date` equals `'2013-02-14'`
# 
# Thus, $\color{blue}{\texttt{data['date']}}\color{black}{==\texttt{'2013-02-14'}}$ compares each row in `date` to the value `'2013-02-14'`.  Rows whether the value in `date` match this string are marked `True`, while rows that do not match this string are marked `False`.  Suppose that this list of rows looks like $\texttt{[True, False, False, True, ...]}$.
# 
# Then, $\color{red}{\texttt{data[}}\color{black}{\texttt{[True, False, False, True, ...]}}\color{red}{\texttt{]}}$ would select the rows that are marked `True` and ignore the rows marked `False`.

# As we saw in earlier, we can test for whether the date in a given row matches our day of interest with the python statement: `==`.  Recall:
# 
# ```
# x = 1
# y = 2
# ```
# if we want to test whether `x` is equal to `y`, we should *not* use
# ```
# x = y
# ```
# because Python will interpret this as setting `x` *equal to* whatever value `y` is.  We should instead use
# ```
# x == y
# ```
# which in this case will return `False`, because `x` is currently set equal to 1 and `y` is set equal to 2.
# 
# Therefore, if we issue the command:
# ```
# data['date'] == '2013-02-14'
# ```
# what Python will do is check each row for whether the `date` in that row is equal to the value `'2013-02-14'`.  Again, be careful about quotations!
# * `data['date'] == '2013-02-14'` : Python checks for whether `date` is equal to the *string* value `'2013-02-14'`
# * `data['date'] == 2013-02-14` : Python checks for whether `date` is equal to some *integer* $2013-02-14$, and ends up confused because `02` is not a number and thus not something can can be subtracted from 2013.

# In[16]:


data['date'] == '2013-02-14'


# Given this list of `True`s and `False`s, we select from `data` those marked `True`.  If we take our DataFrame $\color{red}{\texttt{data}}$ and give it a list of rows inside square brackets $\color{red}{\textbf{[}\text{ }\textbf{]}}$, Python will only use rows marked `True` and it will exclude rows marked `False`.
# 
# Properties of the DataFrame variable type will be introduced as they become necessary.  For now, return to the problem of calculating an excess return and a market risk premium.  Recall that the nested dictionary solution to this problem was tedious.  In contrast, the DataFrame solution is to simply type:

# In[17]:


data['r_excess'] = data['ret'] - data['RF']


# Short, simple, and easily readible.  To verify that the solution is correct, print the data:

# In[18]:


data.head()


# ### Selecting Pieces of DataFrames
# 
# As stated above, a very common use case with DataFrames is to select a row or subset of rows that satisfy a propery, as we did with `data[data['date'] == '2013-02-14'`.
# 
# There are two other ways to refer to a piece of a DataFrame.
# 
# **Option 1**: refer to rows and columns by their *numbering*
# 
# For example, `data.iloc[0]` gives you the 0th row:

# In[19]:


data.iloc[0]


# And likewise `data.iloc[0:2]` gives you rows 0 and 1.

# In[20]:


data.iloc[0:2]


# Here we see an example of a quirk like what we experienced with `range(k,n)` earlier.  Recall that `range(k,n)` will give you the numbers: k, k+1, k+2, ..., n-1.  For example `range(0,2)` gives you: 0, 1 (but not 2!).  Likewise, if we want to refer to a range of numbers within a list, set of rows in a dataframe, etc. we can use the `k:n` to get elements k through n-1.  For example, suppose that we have a shopping list:
# ```
# shopping_list = ['apples', 'bananas', 'peas']
# ```
# and, since everybody hates peas, we want to exclude that from our list:
# ```
# shopping_list[0:2]
# ```
# would select only the fruits.
# 
# To get refer to *column* indicies rather than row numbers, we need to use the fact that DataFrames have a *[row,column]* organization to them.  So if you want to get row 0, column 2, you would type

# In[21]:


data.iloc[0:2,5]


# Note that if we want to select *every* column of row 0, using the command
# ```
# data.iloc[0]
# ```
# works because Python understand that the 0 refers to the row number, and by default it assumes that you would want all the columns.  If instead you want to select *every* row of column 0, we need to do
# ```
# data.iloc[:,0]
# ```
# Here, in the row-specification, the statement `:` is a shortcut for saying "all the rows".  That is, if instead of writing `k:n` you instead just write `:`, Python understands this to mean that `k` should be 0 and `n` should be the biggest possible number that would make sense (i.e. the number of rows).
# 
# **Option 2**: refer to rows and columns by their *names*
# 
# Return once again to the first snapshot of this data:

# In[22]:


data.head()


# and observe that the columns have names: `date`, `open`, `high`, `low`, `close`, `volume`, and `Name`.  Note that these names are case sensitive so that the last column can be accessed by typing `ret['Name']` but not `ret['name']`.  This dataset that we loaded does not have row names, so by default Pandas will give each row a name equal to its row numer: 0, 1, 2, etc.
# 
# Whereas `ret.iloc[:,0]` gave you all the data in column 0, we could instead get all the data from column `date` with `ret.loc[:,'date']`.  The shortcut for this, since it is the usual way we slice data, is to type `ret['date']`.
# 
# The first date in the dataset can be accesed with row name `0` and column name `date` by typing:

# In[23]:


data.loc[0, 'volume']


# ### Dates
# 
# If you see the string `'2013-02-14'`, your brain automatically reads this as "February 14, 2013".  Python doesn't have a brain.  If we want Python to translate a string that represents a date into something that it can recognize as a date, we need give it some specific instructions.
# 
# What does it mean for a variable to be recognized as a date in Python?  Well, consider the date `'2013-01-31'`.  People with brains know that if we increment the date by one, the following date is `'2013-02-01'`.  Brainless Python doesn't understand something like `'2013-01-31'+1`.
# 
# Just like a `pandas` *DataFrame* special variable type is the most useful way to store data in Python, the best way to work with dates is using the `datetime` module's *datetime* special variable type.  The `datetime` module's *datetime* variable has built-in features that enable Python to do things like add on a day (e.g. add a day to $1/31/2013$ to get $2/1/2013$).
# 
# **Remember**: our goal is not to make things easy today, our goal is to be smart enough to make things easy for the rest of our lives!
# 
# Begin by importing the `datetime` module

# In[24]:


import datetime


# The `date` column in our `pandas` DataFrame is not a `datetime` variable.  We will create a new column, `dt`, that is.
# 
# The `datetime` module has a function `datetime.datetime.strptime()` that takes a date and converts it into a special `datetime` variable.  Similarly the function `datetime.datetime.timedelta(days=1)` is how we could add $1$ day to our date.

# In[25]:


x = 20110131
x_dt = datetime.datetime.strptime( str(x), '%Y%m%d' )
print(x)
print(x_dt)
print(x+1)
print(x_dt + datetime.timedelta(days=1))


# Let's break down what happens in `x_dt = datetime.datetime.strptime(str(x), '%Y%m%d')`
# 
# * `x_dt =` : define a new variable `x_dt` equal to...
# * `datetime.datetime.strptime()` : the `datetime` function capable of converting integer or string dates into `datetime` variables
# * `str(x)` : we happened to define x as an *integer*, so `str()` is the function we use to convert it to a *string*
#   * Remember, *integers* are variables where we can ask Python to do `x/2` and it understands what to do
#   * In contrast, a string like `y = 'dog'` does not have mathematical properties, and Python will freak out if you ask it to do `y/2`
#   * It just so happens that the `strptime()` function expects *string* arguments and not *integers*
# * `'%Y%m%d'` : this is how we tell the `strptime()` function what the string date is formatted like -- lookup the codes [here](http://strftime.org/)
#   * '20110131' is of type '%Y%m%d'
#   * '11Jan31' is of type '%y%b%d'
#   * '31January2011' is of type '%d%B%Y'
#   
# To add a new column to `data`, all we need to do is put `data['dt'] = ` and then tell Python what this column should be equal to.  For example:

# In[26]:


data['dt'] = 1
data.head()


# `data['dt'] = 1` creates a new column `dt` equal to all 1s.
# 
# We want to take the column `date` and use the `strptime()` function to make a column `dt`
# 
# Fortunately, `pandas` has a function `to_datetime()` that works like the `strptime()` function but it can convert and entire column all at once

# In[27]:


data['dt'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
data.head()


# To the human eye, the columns `date` and `dt` look identical.  That's because `datetime` dates still print out nicely as formatted strings.
# 
# We can use the `.dtypes` function that is built-in to `pandas` DataFrame objects to confirm that `dt` is indeed a `datetime` variable.

# In[28]:


data.dtypes


# String columns will be reported as `object` types in pandas.
