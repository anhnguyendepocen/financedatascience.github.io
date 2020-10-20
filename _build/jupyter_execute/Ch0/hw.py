#!/usr/bin/env python
# coding: utf-8

# ## Homework Assignment
# 
# 
# ### Project Valuation: NPV vs. IRR
# 
# In finance, we value a stream of future cash flows by discounting these to the present period.  For example, suppose a division manager at a firm wishes to determine whether a new investment project is worth purusing.  How should the manager make this decision?  One method to do this is with net present value (NPV).  Another is with internal rate of return (IRR).  You should have heard of both of these before, and will probably remember that NPV is the preferred approach.  As your first Python exercise, you'll get to prove to/remind yourself why one should *not* use IRR.
# 
# For your convenience, both the NPV and IRR decision rules are reviewed here.
# 
# **Net Present Value**
# 
# A project with cash outflow at time $0$, future cash flows $C_1, C_2, ...$, and discount rate $r$ is undertaken if:
# 
# $$
# -C_0 + \sum_{t=1}^T \frac{CF_t}{(1+r)^t} > 0
# $$
# 
# where $T$ is the number of years that the project lasts.
# 
# **Internal Rate of Return**
#  
# A project with cash outflow at time $0$, future cash flows $C_1, C_2, ...$, and required rate of return $h$ is undertaken if:
# 
# $$
# r > h
# $$
# 
# where $r$ solves
# 
# $$
# -C_0 + \sum_{t=1}^T \frac{CF_t}{(1+r)^t} = 0.
# $$
# 
# We usually refer to $h$ as the hurdle rate.
# 
# **Homework Format**
# 
# When homework assignments are presented as Jupyter notebooks (as is the case here), you will be expected to edit some of the Python code to complete a problem.  Not all of the code requires editing.  The parts of the Python code that need to be completed by you are marked in comments blocks.
# 
# For example, suppose that you are asked to complete the following function:
# ```python
# def leverage_ratio(D,E):
#     ### start code here (~ 1 line)
#     ratio = 
#     ### end code here
#     return ratio
# ```
# 
# That is, you are asked to complete the function named `leverage_ratio()` so that when a user provides values for `D` and `E` to the function, the function returns the leverage ratio based on these values.  The code that you are expected to modify is nested within the lines `### start code here` and `### end code here`.  Do not change any code outside of these blocks.  The correct answer to this hypothetical problem would, of course, be:
# ```python
# def leverage_ratio(D,E):
#     ### start code here (~ 1 line)
#     ratio = D / (D+E)
#     ### end code here
#     return ratio
# ```

# **Tutorial: NPV and IRR with Numpy**
# 
# For your homework, you will calculate the NPV and IRR of various possible scenarios.  The exceptionally popular *numpy* module includes functions that make calculating NPV and IRR simple.
# 
# Begin by running the following block of code to import the numpy module.

# In[1]:


import numpy as np
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) # ignore this


# For a project that requires a cash outlay of $\$100$ today, and cash inflows of $\$23$ for the next five years, the npv of the project is calculated in Python by:
# ```
# np.npv(rate=0.05,values=[-100,23,23,23,23,23])
# ```
# assuming a discount rate of $5\%$.  To calculate the IRR of the project, we run:
# ```
# np.irr(values=[-100,23,23,23,23,23])
# ```
# The following block of code runs and prints these two calculations.

# In[2]:


project_npv = np.npv(rate=0.05,values=[-100,23,23,23,23,23])
project_irr = np.irr(values=[-100,23,23,23,23,23])
print(project_npv,project_irr)


# You should notice that the NPV of the stream of cash flows is negative, suggesting that this isn't a project that you'd want to take on.  Note too that the IRR is less than the discount rate, which is another sign that this is a bad project.  In the following exercises, you'll see that NPV and IRR can give you inconsistent implications about project quality.

# **Question 1 -- Delayed Investment**
# 
# Suppose that have just retired as the CEO of a successful company.  A major publisher has offered you a book deal. The publisher will pay you $\$1$ million upfront if you agree to write a book about your experiences. You estimate that it will take three years to write the book. The time you spend writing will cause you to give up speaking engagements amounting to $\$500,000$ per year. You estimate your opportunity cost to be $10\%$.
# 
# Calculate the NPV of the deal.

# In[ ]:


### start code here (~ 1 line)

### end code here


# The expected output is (check your code if the prinout does not match this number):
# ```
# -243425.99549211108
# ```
# 
# Next, calculate the IRR of the deal.

# In[ ]:


### start code here (~ 1 line)

### end code here


# The expected output is:
# ```python
# 0.23375192852825855
# ```

# **Question 2 -- Multiple IRRs**
# 
# Suppose that instead of receiving $\$1$ million up front, the publisher offers $\$550,000$ advance and $\$1$ million in four years when the book is published.
# 
# Calculate the NPV of the deal.

# In[ ]:


### start code here (~ 1 line)

### end code here


# Now calculate the IRR of the deal.

# In[ ]:


### start code here (~ 1 line)

### end code here


# You should find that the NPV is negative, but the IRR is positive.  To see what's going wrong here, recall tha the IRR is the discount rate that sets the cash flow stream to zero net present value.  In the `np.irr()` call above, Python returned an IRR to you.  But it's not the only possible IRR for this problem!  Mathematically, certain cash flow streams can have *multiple* IRRs that would set the cash flow stream to zero net present value.  To see this happen, plot the NPV for this cash flow stream over a range of possible discount rates (you'll find two that set the NPV to zero, one was the answer that `np.irr()` gave you above).  For this problem, you should include discount rates over the range $[0.01,0.51]$.
# 
# Hint: to loop over rates between $[0.01,0.51]$, one can use the `np.arange()` function with a third argument:
# ```
# for r in np.arange(0.01,0.53,0.02):
#     ... # things inside the for loop happen here
# ```
# and $r$ will take values $[0.01,0.03,0.05,...,.0.49,0.051]$. The third argument controls the *step size*, which is how much the loop increments each time (the default is to go up by $1$).  The function `range()` which we used in class cannot use decimal numbers.

# In[ ]:


# leave these four lines as is, they are needed to get the plot function working
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# define any empty lists you need here
### start code here (~ 2 lines)
rate_list =
npv_list =
### end code here

# loop over rates from 0.01 to 0.51, incrementing by 0.02 each time
### start code here (~ 3 lines)
for
    # inside the loop, calculate the NPV.  Update any lists that may need updating
    npv_list.append(  )
    rate_list.append(  )
    
### end code here

# plot the NPV for each rate you considered here
plt.plot(rate_list, npv_list)
plt.show()


# You should observe a U-shaped curve that appears to cross the line somewhere below 0.1 as well as somewhere above 0.3.  These are two valid IRRs for the question.
