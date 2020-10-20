#!/usr/bin/env python
# coding: utf-8

# ## Basic Ingredients
# 
# Python is one of the most popular, general-purpose programming languages in the world.
# 
# It is powerful, flexible, and *easy to learn*.
# 
# ### Variables and Data
# 
# Variables store information.  Below, variable `a` is defined to store the number 5.  Next, variable `b` is defined to store 5 (the value of `a`) plus 2, which is 7.

# In[1]:


a = 5
b = a + 2
print(b)


# Variable names must start with a letter, and can contain letters, numbers, and underscores.  In general, variables should be named in a descriptive manner.  That is, if you have a variable that contains a firm's cost of capital as its information, it is better to name this something like `cost_of_capital` or `costOfCapital` rather than a non-descriptive name like `a` or `b`.
# 
# Note that you can use `#` to add comments to your code.
# 
# Python will ignore everything on a line following a `#` symbol.

# In[2]:


c = b + 7 # + 10
print(c)


# There are a handful of basic variable types.
# 
# Note that the character `#` begins a **comment**.  Python ignores the `#` character and everything that follows it.  Use this to take notes about what's happening in the code.

# In[3]:


a = 5        # a is an integer (there is no decimal point)
b = 1.5      # floating point number (in general, don't worry about integer vs. floating point)
c = False    # c is a Boolean
d = 'banana' # d is a string


# Programming is useful because variables can store *lots* of information (more than just a single number or word!).

# In[4]:


e = [1,2,3]  # e is a list
f = {'word 1':'definition 1', 'word 2':'definition 2'} # f is a dictionary


# Above, variable `e` stores information about multiple numbers.  Lists can store lots of things, not just numbers.  For example, the list `fang = ['FB', 'AMZN', 'NFLX', 'GOOG']` stores a list of string variables, where each string corresponds to one of the ticker symbols for the FANG stocks.
# 
# Above, variable `f` stores information about words and their meanings.  Like lists, dictionaries can store lots of things.  For example `FB = {'3/23/20':148.10, '3/24/20':160.98, '3/25/20':156.21, '3/26/20':163.34, '3/27/20':156.79}` records daily stock price information for Facebook, Inc. for the week of March 23, 2020.  Dictionary variables hold *keys* (e.g. a word to look up) and *values* (e.g. the definition of the word).  Here, the key is a string that records the date, and the value is a floating point number that corresponds to the stock price.
# 
# We'll return to lists and dictionaries later, including a discussion of how to modify/update data inside the list/dictionary, as well as instructions for accessing single items within a list/dictionary.  For now, we'll work with variables that hold single pieces of information for the sake of simplicity.  But note that variables can store lots of data simultaneously, and that's what makes programming truly useful for financial practioners.
# 
# Amongst the above variable types, integer and floating point numbers are a nice place to start because there are a number of straight forward operations that can be applied to these variables.  For instance, as shown above, we can add numbers together with `+`.  Subtraction, multiplication, and division work in similar ways:
# 
# Operation | Operator | Example | Result
# - | - | - | -
# Addition | `+` | `2+3` | `5`
# Subtraction | `-` | `5-3` | `2`
# Multiplication | `*` | `2*3` | `6`
# Division | `/` | `6/3` | `2`
# 
# Beyond these four basic arithmatic operations, there are two extra operations to know:
# 
# Operation | Operator | Example | Result
# - | - | - | -
# Exponentiation | `**` | `3**3` | `9`
# Modulus | `%` | `4%3` | `1`
# 
# The former, exponentiation, is key to many financial applications (e.g. time value of money).  Do not mistake `**` and `^`!  While `^` may look more familiar as an exponentiation symbol, it has an entirely different meaning in Python.
# 
# These arithmatic operators perform basic tasks with stored data.  For instance, if we have variables corresponding to debt and equity, we can calculate leverage.

# In[5]:


debt = 20
equity = 80

leverage = (debt) / (debt+equity)
print(leverage)


# Similarly, if we needed to know the holding period return of an investment of $\$500$ that earns $2\%$ per year for $3$ years, we could use these Python operators to find that out.

# In[6]:


500 * (1+.02)**3  / 500 - 1


# ### Tests of (In)Equality
# 
# We can compare the relative value of two number variables.  For example, define two variables, `debt_longterm` and `debt_shortterm`, that store information about a company's long term and short term debt, respectively.

# In[7]:


debt_longterm = 1000
debt_shortterm = 2000


# We can check for whether long term debt exceeds short term debt with the `>` character.  This test returns a *boolean* value (True or False).

# In[8]:


debt_longterm > debt_shortterm


# As you might expect, we can also use `<` and `=` characters for other tests.  For instance:

# In[9]:


debt_longterm <= debt_shortterm


# We have to be careful with tests of equality, however.  Remember, we used `=` to tell Python what information a variable should store.  For example, `x=7` tells Python that the variable `x` should store the number seven.  Thus, if we want to test for whether the information stored in `x` equals seven, we type
# ```Python3
# x == 7
# ```
# with a double `==` to denote that we're testing for equality.
# 
# Related to the `<`, `>`, and `=` characters is the word `in`.  In Python, the word `in` has a special meaning, so you can't define a variable with the name `in`.  The word `in` is used to check for whether a value appears in a list.  Use of the word `in`, like the `>` or other tests of (in)equality, results in Python returning a Boolean value.
# 
# As an example, define `tic` to be one stock ticker of interest and `tickers` to be a list of stock tickers.

# In[10]:


tic = 'AAPL'
tickers = ['AAPL','MSFT','AMD','NVDA','INTC']


# We can check for whether the value stored in `tic` appears in the list of items held in `tickers` by using the word `in`.

# In[11]:


tic in tickers


# Now that we can test for equality, we can use this information to test an important point: strings and numbers (either integers or floating points) are different.  That is, if we type

# In[12]:


2 == 1+1


# we get the value `True`, whereas if we type

# In[13]:


2 == '2'


# we get the value `False`.
# 
# ### Functions
# 
# Variables are one of the two fundamental components of any programming language.  Now that we know what variables are (they things that store data) and how to work with them, we can introduce the the other fundamental component of programming: functions.
# 
# Functions give us the ability to write some code that we reference over and over again without having to retype things.  Ultimately, programming is about making your life easier!  We work hard (say, for one semester of our lives) learning how to give a computer instructions (using Python) and then, for the rest of our lives, everything else is easier and more convenient because we can instruct a computer to do lots of the heavy lifting for us.  <u>In financial terms, we spend a little time now for a bunch of time saved later, and thus the net present value of learning to program is positive.</u>
# 
# Functions have three parts:
# 1. Function defintion (name the function and determine what *inputs* we need, if any)
# 2. Operations (execute some code)
# 3. Return statement (define what want we want to get back from the function)
# 
# As an example, let's compute the weighted average cost of capital, defined as
# 
# $$
# r_{\text{WACC}} = \frac{E}{V}\times r_E + \frac{D}{V}\times r_D\times (1-\tau_C).
# $$
# 
# That is, the weighted average cost of capital for a firm is the proportion of equity in the firm times the equity cost of capital plus the proportion of debt in the firm times the debt cost of capital.  We adjust the latter for the tax shield of debt using the corporate tax rate $\tau_C$.
# 
# **Part 1: definition**
# 
# A function defintion begins with the keyword `def` followed by the function name and then a colon.
# 
# Functions can use information passed to it via input arguments (inputs are named in the parentheses, which appear before the colon).
# 
# ```python3
# def wacc(E, D, rE, rD, tC):
# ```
# 
# Note that in this function definition, we expect `E` and `D` as inputs.  We do not require `V` to be an input to the function, since `V` is easily calculated as `V = E + D`.  This calculation is included in part 2.
# 
# **Part 2: operations**
# 
# Functions run the code written inside of the function (operations) when the function is *called*.  A function call occurs when a programmer ''uses'' the function, and we'll see an example of this shortly.
# 
# <u>NOTE</u>: indentation keeps track of whether code is ''inside'' a function
# 
# ```python3
# def wacc(E, D, rE, rD, tC):
#     V = E + D
#     cost_of_capital = E / V * rE + D / V * rD * (1 - tC)
# ```
# 
# **Part 3: return value**
# 
# Functions can be many, many lines of code.
# 
# The last line, starting with the keyword `return` specifies what value comes back when you run the function.
# 
# ```python3
# def wacc(E, D, rE, rD, tC):
#     V = E + D
#     cost_of_capital = E / V * rE + D / V * rD * (1 - tC)
#     return cost_of_capital
# ```
# 
# When a function is created, Python becomes ''aware'' of the function, but nothing else happens at that time.

# In[14]:


def wacc(E, D, rE, rD, tC):
    V = E + D
    cost_of_capital = E / V * rE + D / V * rD * (1-tC)
    return cost_of_capital


# For functions to be used, they need to be *called*.  For example:

# In[15]:


wacc(100,30,.08,.04,.35)


# tells Python to compute the weighted average cost of capital for a firm with an equity value of $100$, a debt value of $30$, an equity cost of capital of $8\%$, a debt cost of capital of $4\%$, and a tax rate of $35\%$.  The returned value of `0.0675` tells us that the firm's WACC is $6.75\%$.
# 
# In the above example, Python *assumes* the first number ($100$) should be given to the input variable `E`, it *assumes* that the second number ($30$) should be given to the input variable `D`, etc.  This is bad practice!  It's much better to use the input variable names:

# In[16]:


wacc(E=100,D=30,rE=.08,rD=.04,tC=.35)


# because then the ordering of how you enter the inputs doesn't matter.

# In[17]:


wacc(rE=.08,rD=.04,tC=.35,E=100,D=30)


# This is useful to keep in mind because, realistically, you won't remember the default ordering of inputs (the order of input variables in the `def` line of the function definition).
# 
# The `return` line is important because variables that live inside a function are stuck inside that function.
# 
# E.g. the below will throw an error because `cost_of_capital` is only *accessible* inside the function `wacc`.

# In[18]:


cost_of_capital


# ### Conditionals
# 
# Conditionals specify that a certain bit of code should run *conditional* on a statement being true or false.
# 
# Like user-written functions, the block of code that runs conditionally is indented.
# 
# In the example below, we define information about a firm's current assets and current liabilities.  Then we calculate the current ratio to see if the firm has enough current assets to cover its current liabilities.  The code incorporates a rule of thumb and tells the user that a current ratio above $1.5$ is okay, a current ratio below $1.5$ but above $1$ is risky, and a current ratio below $1$ is dangerous.

# In[19]:


current_assets = 100
current_liabilities = 60
current_ratio = current_assets / current_liabilities

print(current_ratio)
if current_ratio > 1.5:
    print('Firm is okay!')
elif current_ratio <= 1.5 and current_ratio > 1:
    print('Firm looks risky')
else:
    print('Danger!  Firm needs some cash')


# In the above example, several calls were made to the `print()` function.  The function `print()` is a built-in function that tells Python to print out the input to the user.
