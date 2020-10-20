#!/usr/bin/env python
# coding: utf-8

# ## Homework Assignment
# 
# ### Equity Sensitivity to Recapitalization
# 
# Run the below cell to get started.  Then, respond to each question.

# In[ ]:


import numpy as np
import pandas as pd
from scipy.stats import beta, truncnorm
import seaborn as sns

np.random.seed(0)

df = pd.DataFrame(columns=['leverage', 'debt beta', 'equity beta'])
df['leverage'] = beta.rvs(1, 3, scale = 1.75,  size = 1000)/2
df['debt beta'] = truncnorm.rvs(.05, .07, size = 1000) + df['leverage']*0.0001
df['equity beta'] = np.random.normal(1, 0.25, size = 1000)
df.head()


# **Question 1:**
# 
# Print out summary statistics for the column ``'leverage'``.  Based on the output you observe, add a comment to your code block labeling the data as either left or right skewed, and explain your reasoning.

# In[ ]:


# your code here


# **Question 2:**
# 
# Print out the distribution and histogram of `leverage`.

# In[ ]:


# your code here


# **Question 3**
# 
# Use the fact that $\beta_{\text{Asset}} = \frac{\text{Equity Value}}{\text{Firm Value}} \beta_{\text{Equity}} + \frac{\text{Debt Value}}{\text{Firm Value}} \beta_{\text{Debt}}$ to compute the unlevered, asset beta of each company in the dataset.
# 
# Hint: $\frac{E}{V} = \Big(1 + \frac{E}{D}\Big)^{-1}$.

# In[ ]:


# your code here


# **Question 4**
# 
# Suppose that every firm in the database increases their leverage by 5%.  This is a relatively small increase, so you should assume that the debt beta of each firm remains the same.  Equity, in contrast, is rather sensitive to changes in firm financial policies (given that it is the residual claim on the firm's cash).  Thus, calculate a new equity beta that corresponds to the higher leverage rate.  
# 
# Hint: re-arrange the above equation to solve for $\beta_{\text{Equity}}$.

# In[ ]:


# your code here


# **Question 5**
# 
# Suppose that the market risk premium is $8\%$ and that the risk free rate is $2\%$.  Using CAPM, compute the percent increase in each firm's cost of equity associated with the leverage increase.

# In[ ]:


# your code here


# **Question 6**
# 
# Plot a line of best fit that shows the relationship between a firm's equity sensitivity (the percent change in cost of equity calculated in question five), plotted on the y-axis, and a firm's starting leverage (as summarized in question 1), plotted on the x-axis.

# In[ ]:


# your code here


# **Question 7**
# 
# Nowhere above was random noise (the $+u$ part of the line $y = \alpha + \beta x + u$ as described in the notes) added to how firm's cost of equity changes with respect to an increase in financial leverage.  In the below cell, as a comment, explain why the line plotted in response to question 6 is not a perfect fit.

# In[ ]:


# your answer here


# **Bonus**
# 
# Given that:
# 1. change in cost of equity, $\Delta(r)$, is given by $\Big(r_e^{\text{new}} - r_e^{\text{old}}\Big)\Big/\Big(r_e^{\text{old}}\Big)$ (question 7)
# 2. cost of equity, $r_e$, is a function of equity beta, $\beta_e$ (question 6)
# 3. equity beta is a function of leverage, $L$ (question 4)
# 4. an increase in leverage can be written as $L^{\text{old}}(1+x)$ (question 4)
# 
# Solve: $\partial \Delta(r) / \partial x$ and enter your answer in the below markdown cell.  Use the symbols as defined in this cell and Latex typesetting to specify your answer.

# < enter your answer here >
