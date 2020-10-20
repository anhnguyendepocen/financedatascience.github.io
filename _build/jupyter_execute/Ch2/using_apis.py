#!/usr/bin/env python
# coding: utf-8

# ## Using APIs
# 
# ### American Community Survey
# 
# The [American Community Survey](https://www.census.gov/programs-surveys/acs)(ACS) is the largest survey conducted by the U.S. Census Bureau.  It collects basic demographic information about people living across the United States.
# 
# The survey is conducted every year, and, due to processing time, releases with a lag.  For instance, the 2018 survey data is released in the latter part of 2019.  The ACS data is relased not only in one-year estimates (e.g. 2018 survey data) but also in five-year estimates (e.g. 2014-2018 survey data).  The one-year estimates are, naturally, more recent.  However, five-year estimates may be necessary in some applications.  The Census Bureau does not release survey information for small populations, due to anonymity concerns, every year.  Rather, some information is available exclusively in the five-year survey data (which averages over a five year period).
# 
# A brief overview of the data available through the ACS is available [here](https://www.census.gov/acs/www/data/data-tables-and-tools/).  Note that the ACS data includes things like age, marital status, income, employment status, and educational attainment.

# The full list of ACS data is available [here](https://api.census.gov/data/2018/acs/acs1/profile/variables/).

# Register for an API key with the U.S. Census Bureau [here](https://api.census.gov/data/key_signup.html).  This step is **required** to continue with the lecture notes!
# 
# Enter your API key as a string here:

# In[1]:


api_key = ''


# To keep my key secret, I've pickled the string that stores it, and will re-load it here.  *Do not* attempt to run the following block.

# In[2]:


import pickle
with open('census_key.p', 'rb') as f:
    api_key = pickle.load(f)


# The formula to get data from the ACS is:
# 
# ```
# 'https://api.census.gov/data/'
# + <year>
# + '/acs/acs1?get=NAME,'
# + <variable name>
# + '&for='
# + <geography>
# + ':*&key='
# + <API key>
# ```
# 
# For instance, to get median household income (which has `<variable name> = B19013_001E`) for `<year> = 2010` over the entire U.S. (`<geography> = us`), we would use the string
# 
# `'https://api.census.gov/data/' + '2010' + '/acs/acs1?get=NAME,' + 'B19013_001E' + '&for=' + 'us' + ':*&key=' + api_key`
# 
# as our URL.  An example request is shown below:

# In[3]:


import requests
r = requests.get('https://api.census.gov/data/2010/acs/acs1?get=NAME,B19013_001E&for=us:*&key='+api_key).json()
print(r)


# Likewise, to get data for *every* county in the country, we would replace `us` with `county` following the `for=` piece of the string.  This will return data on many counties.  Instead of printing them all, below, we've printed just a sample, as well as the total number of counties for which median household income data is available via ACS.

# In[4]:


r = requests.get('https://api.census.gov/data/2010/acs/acs1?get=NAME,B19013_001E&for=county:*&key='+api_key).json()
print(r[0:10])
print(len(r))


# Note that the first item in this list is:

# In[5]:


print(r[0])


# which is simply a set of headers.  That is, for each additional item in the list, the data in position 0 is the county name and the data in position 1 corresponds to the value for the variable `B19013_001E`.  The numbers in positions 2 and 3 are the county's FIPS code.  States have 2-digit FIPS codes, and counties have 3-digit FIPS codes.  If we put the state code and county code together to a 5-digit number (state code then county code), we have a unique identifier for the county.  This FIPS code is used by many different data providers.
# 
# Recall that we can remove an element from a list with the `.pop()` function.  For instance, let's remove the first element of our requested ACS data (the set of headers).

# In[6]:


headers = r.pop(0)


# Do not run the above line of code multiple times!  Python will continue popping out elements of your list.
# 
# The value for `headers` is thus:

# In[7]:


print(headers)


# as expected.  Now, the requested ACS data no longer has that element.  Rather, what is left is

# In[8]:


print(r[0:10])


# simply data.  This is useful, because we can not store all of the data we have in a DataFrame.  The command to do this is `pd.DataFrame()`.  This function takes two arguments.  First, Python expects to receive a list of lists.  This list of lists should correspond to the data that we want to store.  The list of list is a list of rows of data, where each row may be a list of multiple values (multiple columns).  The second argument is a list of column names.

# In[9]:


import pandas as pd
census = pd.DataFrame(r, columns=headers)
census.head()


# In[10]:


census['state'] = census['state'].astype(int)
census['county'] = census['county'].astype(int)


# In[11]:


census.dtypes


# In[12]:


census['B19013_001E'] = census['B19013_001E'].astype(int)


# ### Zillow Home Values
# 
# County median incomes give a sense of the economic well-being of a geographic area.  Suppose that our interest is in how home prices (for most households, the most valuable asset that the household owns), correlates with income.
# 
# Housing data is available from Zillow [here](https://www.zillow.com/research/data/).
# 
# The URL for data on all home prices in a county (single-family residential and condos) is `'http://files.zillowstatic.com/research/public_v2/zhvi/County_zhvi_uc_sfr_tier_0.33_0.67_sm_sa_mon.csv'`.  Pandas can read online csv files directly in to Python.

# In[13]:


zhvi = pd.read_csv('http://files.zillowstatic.com/research/public_v2/zhvi/County_zhvi_uc_sfr_tier_0.33_0.67_sm_sa_mon.csv')


# The `.shape` property of a Pandas DataFrame reports the numbers of rows and columns.

# In[14]:


zhvi.shape


# There are a lot of columns on this file!  Recall that the `.columns` property of a DataFrame returns a list of columns.  Recall too that we can subset a list named `x` to items `m` through `n` via `x[m:n]`.  Thus, print out only the first 20 columns of the DataFrame below (to get a sense of what's included on this DataFrame).

# In[15]:


zhvi.columns[:20]


# Likewise, the *last* `n` items of list `x` are accessible via `x[-n:]`.

# In[16]:


zhvi.columns[-20:]


# Given what we observe about the data, define a list of column names to keep.  All other columns outside of this list will be removed.

# In[17]:


keep_list = [col for col in zhvi.columns[:9]] + ['2018-12-31']
print(keep_list)


# In[18]:


zhvi = zhvi[keep_list]


# In[19]:


print(zhvi.head())


# We will combine datasets using state and county codes.  Check that the ZHVI data imported as numbers.

# In[20]:


zhvi.dtypes


# Now we can merge.  The format for merging `df1` and `df2` is to use `df1.merge(df2, left_on=, right_on=)`.  The `left_on` and `right_on` specify variables on the left (`df11)` and right (`df2`) datasets that should link the datasets together.  Note that `df1` is the left dataset because it appears before `.merge`, whereas `df2` is the right data because it appears after `.merge`.  It is also possible to use `df2.merge(df1, left_on=, right_on=)`.  In this scenario, the lists passed to `left_on` and `right_on` would flip from the earlier usage (since now `df2` is the left dataset).

# In[21]:


df = zhvi.merge(census, left_on=['StateCodeFIPS','MunicipalCodeFIPS'], right_on=['state','county'])


# In[22]:


df.head()


# This merged dataset has both county median income and an index of home values in the area.  Are income and home prices correlated?  We can quickly visualize the question with `seaborn`.

# In[23]:


import seaborn as sns


# In[24]:


sns.lmplot(x='B19013_001E', y='2018-12-31', data=df)


# There do appear to be some outliers here.  To check, try a boxplot.

# In[25]:


sns.boxplot(zhvi['2018-12-31'])


# Additionally, print out a description of the home value index data.

# In[26]:


zhvi['2018-12-31'].describe()


# One method of removing outliers is to ignore (i.e. delete) the data that is "far out" on the boxplot (i.e., well beyond the whiskers).
# 
# The `numpy` module has a `quantile()` function to retrieve the 25th and 75th percentiles, as reported above in the summary statistics.

# In[27]:


import numpy as np
quantiles = np.quantile(zhvi['2018-12-31'], q=[.25, .75])
print(quantiles)


# The interquartile range (IQR) is defined as the difference between the 75th and 25th percentiles of data.  One reasonable way to remove outliers is to eliminate observations that exceed the 75th percentile by more than 1.5\*IQR or are less than the 25th percentile by more than 1.5\*IQR.

# In[28]:


iqr = quantiles[1]-quantiles[0]
sns.lmplot(x='B19013_001E', y='2018-12-31', data=df[ (df['2018-12-31'] < quantiles[1]+1.5*iqr) &
                                                   (df['2018-12-31'] > quantiles[0]-1.5*iqr) ])

