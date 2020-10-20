#!/usr/bin/env python
# coding: utf-8

# ## pandas_datareader
# 
# ### The `pandas_datareader` Module
# 
# In previous parts of this chapter, we discussed APIs.  We use APIs to interface with data on a web server and bring that data in to Python.
# 
# In this section, we make use of the `pandas_datareader` module.  This is a module that provides a set of API features to Python in such a way that the data is directly loaded in to a `pandas` DataFrame format.  The `pandas_datareader` module actually used to be part of the `pandas` module, but it was spun off in to its own separate module.

# In[1]:


import pandas_datareader.data as web


# Let's start with an example provided in the module's [documentation](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#fred).

# In[2]:


from datetime import datetime

start = datetime(2005,1,1)
end = datetime(2019,12,31)
gdp = web.DataReader('GDP', 'fred', start, end)

gdp.head()


# The above yields a data series of GDP values, listed at a quarterly frequency.  Note that the `DATE` listed in the above DataFrame is not a column of data, it contains the labels for the rows.  Remember, label names are bold-faced, so the name `2010-01-01` being in bold tells you that this is a row label, just like the name `GDP` in bold tells you that this is a column label.
# 
# Above, we accessed data from the `'fred'` data provider.  The FRED (Federal Reserve Economic Data) is an important provider of macroeconomic data, like measurement of gross domestic product.
# 
# Note that we can collect multiple data series from FRED simultaneously by requesting a list of data series in the first argument to the `DataReader()` function, as shown below.

# In[3]:


inflation = web.DataReader(['CPIAUCSL', 'CPILFESL'], 'fred', start, end)

inflation.head()


# We see two columns of data printed above, corresponding to the two data series names that were requested.  But how are these series names chosen?  The name `'CPIAUCSL'`, for instance, is not an intuitive name for "inflation."  And if `'CPIAUCSL'` and `'CPILFESL'` are both data about inflation, what makes them different?
# 
# If you search for a data series name on the [FRED website](https://fred.stlouisfed.org/), it will take you to the data series.  Thus, we can easily find that:
# - [CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL) is the consumer price index for urban consumers
# - [CPILFESL](https://fred.stlouisfed.org/series/CPILFESL) is the consumer price index for urban consumers, excluding food and energy costs
# 
# Data on FRED are organized by [category](https://fred.stlouisfed.org/categories),and [consumer price indexes](https://fred.stlouisfed.org/categories/9) are one such category.

# In[4]:


alcohol = web.DataReader('CUSR0000SAF116', 'fred', start, end)

alcohol.head()


# Price indexes are interesting, but let's focus on some financial time series.

# In[5]:


data_list = ['DGS1MO', 'DGS3MO', 'DGS6MO', 'DGS1', 'DGS2', 'DGS5', 'DGS7', 'DGS10', 'DGS30']

ts = web.DataReader(data_list, 'fred', start, end)

ts.head()


# The data returned provides the term structure of interest rates.  Interest rates on treasuries of varying maturities are collected.
# 
# It's time to treat these row labels a bit more formally.
# 
# Recall that column labels can be accessed like so.

# In[6]:


ts.columns


# The columns of a DataFrame are referred to as, quite intuitively, *columns*!
# 
# The row labels are a bit different, they are typically referred to as the *index* of the DataFrame.  The list of row labels is thus accessible via:

# In[7]:


ts.index


# It is at this point that use of `.loc` becomes interesting and useful, rather than simply an academic point about the structure of DataFrames.  For instance, to look up the term structure of interest rates on June 7, 2019, we would enter:

# In[8]:


ts.loc['2019-06-07']


# It's helpful to have an index because it lets us label the data in two dimensions at once.  The column label will tell us the name of the data series (e.g. `'DGS1'`, which is the yield on a set of 1 year constant maturity U.S. treasuries) and the row *index* will tell us the time at which that data is observed.
# 
# In earlier parts of this book, the row index was boring.  Unless explicitly given a list of row labels to use for the index, Python will assign the row index to be the row number.  For example:

# In[9]:


import pandas as pd
import numpy as np
np.random.seed(0)
df = pd.DataFrame(columns=['x'])
df['x'] = np.random.normal(0,1,10)
df.head()


# Note that the data returned from `pandas_datareader` is indexed in a very convenient way.  Along with using `ts.loc['2019-06-07']`, we can get slices of the data like so:

# In[10]:


ts.loc['2019-01-04':'2019-01-09']


# There are two important things to notice about index slicing here (*slicing* is another term for getting a subset of data).
# 
# First, the slice ends *at* the endpoint, not just before it.  This breaks from normal Python convention.  For instance, 0:10 will give you the numbers 0 through 9, not the numbers 0 through 10.  When slicing by index, the last row label you include is the last row you get.  As another example:

# In[11]:


df.loc[1:2]


# Second, the data exists for Jan. 4 and Jan. 7-9, but not for Jan. 5-6.  Why?  Because Jan. 5-6 was a weekend.
# 
# We can shift date indexes around quite easily via `.shift()`.  This will come in handy in many applications.

# In[12]:


ts.head(6)


# In[13]:


ts.shift(1).head(6)


# Note that the shifting moves data based on the dates included in the dataset.  For instance, the interest rates on Friday, if we shift the data forward by one day, are moved to Monday and not to Saturday.
# 
# Shifting is incredibly useful for calculating things like growth rates.

# In[14]:


ts['GDS30 growth'] = ts['DGS30'] / ts['DGS30'].shift(1) - 1

ts.head()


# Beyond useful slicing and shifting tricks, using indexed data like this (i.e. data where the rows have an explicit label and not simply the default row label equals row number format) is great for plotting.

# In[15]:


ts['DGS30'].plot()


# Look at the x-axis!  It's automatically labeled for us.  Thanks, Python.
# 
# Let's now plot the Treasury yield curve for '2016-06-07'.  Recall that we can access the data like so:

# In[16]:


ts.loc['2016-06-07', data_list]


# The maturity times for these securities are:

# In[17]:


mat = [1, 3, 6, 12, 24, 60, 84, 120, 360]


# We can then plot the yield curve using `seaborn`.

# In[18]:


import seaborn as sns
sns.lineplot(x=mat, y=ts.loc['2016-06-07', data_list])


# The yield curve does not always have this shape to it, though what's shown above is the "standard" appearance.  Typically, the yield curve is upward-sloping and somewhat curvy.
# 
# In contrast, the yield curve may sometimes invert.  That is, it will have places in the curve that are downward-sloping.

# In[19]:


sns.lineplot(x=mat, y=ts.loc['2007-01-02', data_list])


# The usual place where we look for this is in the 10-year Treasury minus the 2-year Treasury.

# In[20]:


ts['Slope'] = ts['DGS10'] - ts['DGS2']
ts['Slope'].plot()


# When this slope (the difference between the 10 year and 2 year) is negative, we refer to this as a yield curve inversion.
# 
# These inversion events are reasonably good predictors of recessions.
# 
# Let's test this idea.  Begin by getting a series of data about when recessions occur from [FRED](https://fred.stlouisfed.org/series/JHDUSRGDPBR).

# In[21]:


recession = web.DataReader('JHDUSRGDPBR', 'fred', start, end)

recession.head()


# The data series `'JHDUSRGDPBR'` is a list of recessions.  The value will be 1 when there is a recession and 0 when there is not a recession.
# 
# Let's now merge the recession data.  Note that the recession data is observed once per quarter.  We should convert all data to a quarterly frequency before preceeding.

# In[22]:


tsq = ts.to_period('Q')

tsq.head()


# In[23]:


recessionq = recession.to_period('Q')

recessionq.head()


# Note that the term structure data has multiple observations for a given quarter.  Suppose that we only want to use the first observation.  That is, at the start of a quarter, what does the term structure look like?  We can remove duplicate index values to get rid of the observations that do not correspond to the first observation for each quarter using `.duplicated()`.

# In[24]:


tsq = tsq[~tsq.index.duplicated(keep='first')] # <index>.duplicated(keep='first') marks all duplicates except the first as True

tsq.head()


# The observation at `'2006Q1'` is troubling.  Why is there missing data there?

# In[25]:


ts.loc['2005-12-29':'2006-01-03']


# It's unclear why the first observation for the first quarter of 2006 is missing, but we don't want to lose that quarter of data simply because one date has missing data.  Let's fill in the data.  The method we'll use to do so is `'ffill'`, which stands for forward fill.  Pandas will take the most recent data (in this case `'2005-12-30'`) and use that to fill in the missing data (at `'2006-01-02'`).

# In[26]:


ts = ts.fillna(method='ffill')

ts.loc['2005-12-29':'2006-01-03']


# With that data problem fixed, we can go back to the quarterly data.  Let's re-make the quarterly information.

# In[27]:


tsq = ts.to_period('Q')
tsq = tsq[~tsq.index.duplicated(keep='first')] # <index>.duplicated(keep='first') marks all duplicates except the first as True'

tsq.head()


# Now we can merge the two quarterly DataFrames.

# In[28]:


ts_recession = tsq.merge(recessionq, on='DATE')

ts_recession.head()


# And finally, we can try to see if recessions are more likely when the slope is negative.  In order to say that yield curve inversions might predict recessions, we need to use data from before a recession begins.  For instance, does an inversion at quarter 3 of year $t$ imply that a recession is likely to begin at quarter 4 of year $t$?  We'll use `.shift()` to make a lagged copy of the `'Slope'` column.

# In[29]:


ts_recession['Lagged Slope'] = ts_recession['Slope'].shift(1)

ts_recession.head()


# One last data-cleaning issue: `statsmodels` *hates* missing values.  It throws a fit and stops working when it sees them.  Notice that the first value of `'Lagged Slope'` is missing, because we can't observe a lag for the first data point.
# 
# To get rid of it, we use `.dropna()` to find all observations where the data is not missing.

# In[30]:


ts_recession = ts_recession.dropna()

ts_recession.head()


# Now, we can use `statsmodels` to run a logistic regression (since the y variable, `'JHDUSRGDPBR'` is only ever 0 or 1).

# In[31]:


import statsmodels.api as sm

ts_recession['constant'] = 1
model = sm.Logit(ts_recession['JHDUSRGDPBR'], ts_recession[['constant','Lagged Slope']]).fit()

print( model.summary() )


# Negative $\beta$ coefficients in a Logit model mean that the covariate (the right hand side variable) corresponding to that $\beta$ coefficient are negatively predictive of the event.  The "event" is an instance of y=1.  So, what we see here is that a higher slope is negatively predictive of a recession.
# 
# If you load a much longer dataset, you can see a similar pattern over time.
# 
# The question is, why does this work?  What's the connection between the yield curve and recessions?
# 
# Let's turn our attention to the *expectations hypothesis*, which is covered in earlier courses.  Define $y_t^{(i)}$ to be the one period interest rate at time $t$ for a Treasury security with $i$ periods to maturity.  We thus have
# 
# $$
# \Big(1+y_t^{(2)}\Big)^2 = \Big(1+y_t^{(1)}\Big)\text{E}_t\Big[\Big(1+y_{t+1}^{(1)}\Big)\Big]
# $$
# 
# That is, the cumulative return for holding a two-year Treasury to maturity should be the same return as holding a one-year Treasury to maturity and then holding another (future) one-year Treasury to maturity after that.  At year $t$, we don't know what the one-year Treasury will be at in year $t+1$.  Thus, we say that the *expected* value of it is $\text{E}_t\Big[\Big(1+y_{t+1}^{(1)}\Big)\Big]$, where $\text{E}$ stands for expected value.
# 
# Let's define the one-year forward rate as
# 
# $$
# \Big(1+f_{t}^{(1)}\Big) = \frac{\Big(1+y_t^{(2)}\Big)^2}{\Big(1+y_t^{(1)}\Big)}
# $$
# 
# The value for $f_{t}^{(1)}$ is something that we can calculate given other data at time $t$.  The Expectations Hypothesis says that this value should be a good estimate for the expected future spot rate, i.e.:
# 
# $$
# f_{t}^{(1)} = \text{E}_t\Big[1+y_{t+1}^{(1)}\Big]
# $$
# 
# Compute the forward rate below.

# In[32]:


tsq['1Y Forward'] = (1+tsq['DGS2'])**2/(1+tsq['DGS1']) - 1

tsq.head()


# Now, we shift the data ahead by 4 periods so we get a one year lag.

# In[33]:


tsq['Last Year 1Y Forward'] = tsq['1Y Forward'].shift(4)

tsq.head()


# The Expectations Hypothesis says that this one year old forward rate should be the same, on average, as what the spot rate is.  We can test this with linear regression.

# In[34]:


tsq2 = tsq.dropna().copy() # since some missinge lagged

tsq2['constant'] = 1 # note, we'll use a constant even though, theoretically, there alpha should be zero in this relationship

eh = sm.OLS(tsq2['DGS1'], tsq2[['constant','Last Year 1Y Forward']]).fit()

print(eh.summary())


# The $\beta$ coefficient is close to 1, which is expected given the predicted relationship.
# 
# What can the Expectations Hypothesis tell us?  Well, if there is a yield curve inversion, it's because the market is expecting interest rates to be lower in the future than they are today.  Why would the market expect that?  Well, during recessions, the Fed will lower rates to stimulate growth.  Thus, it's pretty natural, when you think about it, to expect an inversion to occur before a recession.  All it means is that bond traders are, on average, expecting a recession to occur.  A more pertinent question is *why* bond traders see a recession coming.  We'd need more data to answer that question.
# 
# For our final bit of work in this section, let's turn our attention to a different set of data that may be informative about future economic conditions: the [Senior Loan Office Opinion Survey ](https://www.federalreserve.gov/data/sloos.htm) published by the Federal Reserve.  We can get the data from FRED via `pandas_datareader`.

# In[35]:


first = datetime(2001,1,1)
last = datetime(2020,9,30)

credit_cards = web.DataReader('DRTSCLCC', 'fred', first, last)
credit_cards['DRTSCLCC'].plot()


# In[36]:


auto_loans = web.DataReader('STDSAUTO', 'fred', first, last)
auto_loans['STDSAUTO'].plot()


# In[37]:


loans_except_CCandAuto = web.DataReader('STDSOTHCONS', 'fred', first, last)
loans_except_CCandAuto['STDSOTHCONS'].plot()


# In[38]:


large_firms = web.DataReader('DRTSCILM', 'fred', first, last)
large_firms['DRTSCILM'].plot()


# In[39]:


small_firms = web.DataReader('DRTSCIS', 'fred', first, last)
small_firms['DRTSCIS'].plot()

