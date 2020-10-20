#!/usr/bin/env python
# coding: utf-8

# ## Intro to APIS
# 
# ### Application Programming Interface (API)
# 
# In a later chapter, we'll cover web scraping (accessing website data).  There, our goal is to instruct Python to visit a web page and download some data.  The procedure is to have Python mimic human behavior.  That is, Python visits a URL (as a human would), read over the page (as a human would), and then acquire data (again, as a human would).  For instance, a web scraping task might be to tell Python to go to Wikipedia and look up the date Elon Musk was born.  Python would go to the relevant web page on Wikipedia, read over the HTML, and extract the data (determine Musk's birth date).
# 
# The problem with web scraping is that it is unnecessarily complicated.  While, at least for many sites, scraping is not terribly difficult, it's more than is needed.  Ultimately, the fundamental difficulty of scraping is that we're taking effort to teach Python how to be human.
# 
# An easier solution, when available, is to use an Application Programming Interface (API) to collect web data.  Not every website has an API, but many do.  Essentially, an API is a method for Python to access the data on a website without needing to be instructed in how to replicate human behavior.  This is because an API is a special interface, designed for programmers, to connect their programs to the website of interest.  You may think of an API as the way a program is intended to "read" a website (as opposed to how humans read websites).
# 
# In this part of the chapter, we'll look at two simple APIs.  Many APIs that exist will follow the structure of those presented here, but with additional features.  At the end of this chapter, we'll use an API provided by the U.S. Census to access some demographic data and combine that data with home prices.

# ### International Space Station Tracking
# 
# Our first example comes from [open-notify.org](http://open-notify.org/), a simple website designed to connect NASA data to users via a small API.  The documentation for how to use this API to track the position of the International Space Station is provided [here](http://open-notify.org/Open-Notify-API/ISS-Location-Now/).
# 
# The Open-Notify API, like all APIs, exists to serve data to programmers who know how to ask for it.  In Python, we can *request* data from the Open-Notify API with the `requests` module.

# In[1]:


import requests


# With the `requests` module, we simply have to point Python to the right webpage.  The Open-Notify documentation for ISS data tells us that the data is located at http://api.open-notify.org/iss-now.json.  Open this link in a new browser tab to get a sense of what this page looks like.  Notice that it is very sparse, there are no images, text formatting, or anything.  It's simply a line of information.  Pages designed for programs to read do not need any of the embellishments added for human eyes, because only programs are intended to read them.
# 
# The `requests` module can access the above URL with the following line of code:

# In[2]:


output = requests.get('http://api.open-notify.org/iss-now.json')


# We can see what Python got from visiting the URL by printing the output.  Note, however, that the `output` variable is a special variable constructed by the `requests` module.  Two things worth mentioning here are:
# - `output.status_code`
#   - this prints out the status code of the URL visited (e.g. 404 indicates that the page does not exist, 200 indicates that the page visit went as intended)
# - `output.json()`
#   - this returns a Python dictionary variable with all of the data collected from the URL

# In[3]:


iss = output.json()
print(iss)


# Note that the above is a nested dictionary.  The key `'iss_position'` has a value that is itself another dictionary.
# 
# Recall that values to a dicationary are accessed by using their keys.  For instance:

# In[4]:


print(iss['message'])
print(iss['iss_position'])


# To access the latitude and longitude of the International Space Station, we would thus enter:

# In[5]:


print('The latitude is:', iss['iss_position']['latitude'])
print('The longitude is:', iss['iss_position']['longitude'])


# ### DataMuse Text
# 
# As our first foray into textual analysis, we'll explore the API on [DataMuse](https://www.datamuse.com/api/).  This server provides a system for querying the meaning of words, their comman usages, synonyms, etc.
# 
# The basic structure of this API is straightforward.  Any URL is accessed in three parts:
# 1. `'https://api.datamuse.com/words?'`
#   - This is the beginning of the URL
# 2. A code that indicates the type of query we want:
#   - `'ml='` specifies that we want to find related words
#   - `'rel_rhy='` specifies that we want to find rhyming words
#   - '`rel_jjb='` specifies that we want to find adjectives used to describe a word
# 3. The word in question
# 
# Hence, suppose we wanted to write a rap song about accounts payable, and needed something to rhyme with 'payable'.  The relevant query would be:

# In[6]:


payable_rhyme = requests.get('https://api.datamuse.com/words?rel_rhy=payable').json()
print(payable_rhyme)


# It's always useful to print out some of the return value, as we did above.  Note that the structure here is a list of dictionaries, with each dictionary corresponding to a unique word that rhymes with 'payable'.
# 
# The first rhyming word we get is accessible like so:

# In[7]:


print(payable_rhyme[0])


# Note that DataMuse is helpful here: it tells us three things (i.e. there are three keys).  First, it tells us the rhyming word using the `'word'` key.  Second, it tells us a score for how "good" that word is at rhyming with the word 'payable' with the `'score'` key.  Third, it tells us how many syllables are in the rhyming word with the `numSyllables` key (useful if you need to write a sonnet!).

# In[8]:


# https://www.geeksforgeeks.org/convert-text-speech-python/
get_ipython().system('pip3 install gTTS')
from gtts import gTTS


# In[9]:


mytext = 'I have a lot of accounts payable, when I get the cash is not sayable'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("rap.mp3")


# A more practical application of the DataMuse system is to use it to observe how important jargon can be to business language.  This point was first articulated in Tim Loughran and Bill McDonald's [2011 article](https://doi.org/10.1111/j.1540-6261.2010.01625.x) in the Journal of Finance.  When performing textual analysis, as we will in a later chapter, an important task is to teach Python the meaning of English words.  There are resources online for this, and DataMuse is one such tool.  For instance, if we want to know words similar to the word 'crude', we could do:

# In[10]:


crude_words = requests.get('https://api.datamuse.com/words?ml=crude').json()
print(crude_words[0:10]) # limit output to 10 most relevant words


# This is useful because we can have a situation where one document discusses 'crude' prices, while another document discusses 'petroleum' prices.  Python doesn't innately know that 'crude' and 'petroleum' are related, so we need tools like these in order to clarify to Python that documents discussing 'crude' prices and 'petroleum' prices are likely to be related topics.
# 
# Side note: while outside the scope of what is covered in these chapters, some of you may be interested to know that, with a large body of documents, you can *teach* Python to realize that 'crude' and 'petroleum' are related words using an unsupervised machine learning tool called Latent Dirichlet Allocation (or variants thereof, e.g. SentLDA).  Various Python modules can make this seemingly complicated Bayesian task easy to implement, see `scikit-learn`, `gensim`, or `lda` for more.
# 
# Now, returning to the point about business jargon.  Consider the word 'restate'.  This is a word that sends shivers of fear down the spines of accountants.  Restating earnings is not a good thing.  Yet, what words are related to this one, according to DataMuse?

# In[11]:


restate_words = requests.get('https://api.datamuse.com/words?ml=restate').json()
print(restate_words[0:10])


# Of the top ten words related to the word 'restate', many are varients on the word 'repeat'!  That is because, in normal English, the word 'restate' is often used to describe the act of repeating a previously made statement.  In business English, however, 'restate' generally has a much more negative connotation.
# 
# We will revist this point when we get to the chapter on textual analysis.
