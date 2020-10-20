#!/usr/bin/env python
# coding: utf-8

# ## Descriptive Statistics
# 
# When data contain thousands, if not millions, of observations, we need methods to summarize the data.
# 
# As a working example, consider the list of values below.

# In[1]:


x = [1, 38, 4, 3, 7, -10, 7, 2, 5]


# ### Mean and Variance
# 
# The **mean** of the data is the average value in the data. Within the sample of observations included in the data, the mean is the *expected value* of the data.  It tells us, on average, what we'd expect to observe if we picked an observation at random.  For data $x$, the mean is sometimes written $E(x)$ (the $E$ stands for expected value).

# In[2]:


import numpy as np
np.mean(x)


# Naturally, not all observations are exactly equal to the mean value.  Thus, beyond summarizing what the average value of the data is, we want some sense of how much observations deviate from the expected value.  For a list of observations, $x$, we can calculate the deviation of each of these observations from the mean by taking $x-E(x)$.

# In[3]:


x - np.mean(x)


# Now, the average deviation from the average is zero.  So simply taking the mean of these deviations isn't useful.

# In[4]:


np.mean( x - np.mean(x) )


# A trick is the square each deviation first, and then take the average of those squared deviations.

# In[5]:


np.mean( (x-np.mean(x))**2  )


# This is what's called the **variance** of the data.  Putting the above line of code into math, the variance is computed as $E\bigg( \big(x-E(x)\big)^2 \bigg)$.

# In[6]:


np.var(x)


# Now, the variance in the example above looks quite large.  Often, squaring things makes them bigger, so it makes sense that the average of squared numbers looks large.  To summare how much observations tend to deviate away from the mean, an alternative to calculating the variance is to calculate the **standard deviation**, which is just the square root of the variance.  This doesn't completely un-do the earlier squaring that is included in the variance computation, but it does tend to yield a smaller number.  The formal statement of a standard deviation is $\Bigg[E\bigg(\big( x - E(x)\big)^2 \bigg)\Bigg]^{1/2}$.

# In[7]:


np.sqrt(np.var(x))


# In[8]:


np.std(x)


# ### Median and Skewness
# 
# When we have a list of numbers, the `.sort()` command will sort that list *in place*.  Performing an operation *in place* is the alternative to *returning* a value.  For example, if we type the command `'LSU'.lower()`, Python will return a copy of the string `'LSU'` in lower case characters.  Thus if we have `s = 'LSU'` and do `s.lower()`, Python returns the value `'lsu`', but the string `s` still equals `'LSU'`.  In contrast, `x.sort()` will not return anything.  Rather, the list `x` is modified in place so that its elements get reordered from smallest to largest.  We've already seen at least one other example of an in place command: `.append()`.

# In[9]:


x.sort()
print(x)


# Sorting, at least for small lists of numbers, makes it easy to pick out the middle number.  The middle of a set of a numbers is called the **median**.

# In[10]:


import numpy as np
np.median(x)


# If the set has an even number of elements, there isn't a precise middle element.  The default is then to take the average of the two middle numbers.

# In[11]:


np.median(x[:8])


# The mean is a good bit higher than the median.  Why?
# 
# There is **skewness** in the distribution of numbers.  That means that the set of numbers has some outliers out to one side or the other.  Here, we have positive skewness, which means that there are some big outliers out to the right side.
# 
# Formally, a calculation for skewness is given in the `scipy` module.  We won't worry too much about it here.

# In[12]:


import scipy.stats


# In[13]:


scipy.stats.skew(x)


# ### Outliers, Kernel Density, and Box Plots
# 
# Means and medians tell us a little bit about the data at around the middle of the distribution.  Likewise variance and skewness tell us something about the spread of the distribution (how wide it is and how much it leans to one side or the other).
# 
# These numbers, while extraordinarily useful for a variety of applications, are still sometimes difficult to digest.  Below, we'll see the wisdom of the old adage ''a picture is worth a thousand words.''
# 
# For this analysis, we'll need more data:

# In[14]:


y = [i for i in range(100)]   # list of numbers: 0, 1, ..., 99
y.append(200)                 # add the number 200
y = y + [30, 30, 30, 30, 30]  # add the number 30 (five times)


# When operating in Jupyter notebooks, we gain access to a special module that isn't useful outside of a notebook environment (e.g. if you ran Python from your terminal/command window, this module would not work).  The module's name is `seaborn`.
# 
# Like `numpy` (usually abbreviated as `np`) and `pandas` (usually abbreviated as `pd`) the `seaborn` module has the following cononical import statement.

# In[15]:


import seaborn as sns


# The first tool to explore is the **kernel density estimate**, which plots the distribution of numbers in our data.

# In[16]:


sns.kdeplot(y)


# Note that the kernel density estimate is not good at the end points.  For mathematical reasons, a kernel density estimate is not good at  end points.  Other aspects of the plot are consistent with expectations.  The density is fairly level over 0 to 99, with a slight peak at around 30.  There is also a little bump out at 200 where we placed an outlier.

# In[17]:


np.mean(y)


# In[18]:


np.median(y)


# We again have a case of positive skewness (200 is a big outlier), and thus the mean is bigger than the median.
# 
# Knowledge about how these descriptive statics characterize the data is important in financial analytics and modeling.  For instance, consider a business looking at building a new grocery store in a county.  The expected cash flows for that project are more closely related to the median of county income, rather than the mean of county income.  Why?  Hint: county income has positive skewness.
# 
# As an alternative the the kernel density estimate, consder the **boxplot** below.

# In[19]:


sns.boxplot(y)


# The *box* (the shaded region between roughly 25 and 75) tells us where the middle 50% of the data is.  Thus, about 50% of the data falls between 25 and 75, with another 25% of the data on either side of this box.
# 
# The horizontal lines extending from either side of the box and terminating with a vertical line are called the *whiskers*.  These give a sense of where approximately the other 50% of the data falls (again, 25% on each side of the box), save for a few outliers.  Above, we see that the whiskers extend out to zero on the left and one hundered on the right.  Data that do not fall within these ranges are referred to as *outliers*, and are plotted as individual points (e.g. the number 200 on the far right).
# 
# Outlier identification is a good way to assess data quality.  We'll see an example of this in a later chapter.
