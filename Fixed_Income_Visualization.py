#!/usr/bin/env python
# coding: utf-8

# ## Fixed Income Data Cleaning & Visualization

# ### 1 - Initial settings

# We start by importing each one of the packages we will be using through this proyect.

# In[1]:


import pandas as pd
import numpy as np
import plotly
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import re

print('all modules are imported')


# In order to have a more insightful view of our dataset, lets configure our initial view of the dataset to show all of the columns in order to not miss any important information.

# In[2]:


pd.options.display.max_columns = None


# Next we upload our Yield Curves Rates dataset which is in CSV format.
# What **index_col=0, header=[0]** is used for is to have the first column as index.

# In[3]:


ds1 = pd.read_csv('yield-curve-rates-1990-2021.csv', error_bad_lines = False)
ds2 = pd.read_csv('dty2022.csv', error_bad_lines = False)
ds3 = pd.read_csv('dtrTYD.csv', error_bad_lines = False)


# Now lets do an initial observation of the data

# In[4]:


ds1 = ds1[::-1]
ds1


# In[5]:


ds2 = ds2[::-1]
ds2


# In[6]:


ds3 = ds3[::-1]
ds3


# In[7]:


ds = ds1.append(ds2)
ds


# In[8]:


ds = ds.append(ds3)
ds


# In[9]:


ds.shape


# In[10]:


ds.columns


# Just in case, we create a varible that lists all of the columns, if we had some coulmns that are not useful to us we could create a variable 'useless_columns' and delete them.

# In[11]:


cols = list(ds.columns)
cols


# Next we should turn the table upside down in order to have the older dates first in the table, that will allow us to have more coherent graphs when we plot the data. 

# In[12]:


ds.index.name = 'Date'


# In[13]:


ds = ds[::-1]
ds


# ### Data cleaning

# In[14]:


ds = ds.drop('4 Mo', axis = 1)
ds


# In[12]:


ds.isnull().sum()


# In[13]:


print (ds.index.name)


# In[14]:


Date = ds.index


# In[19]:


ds = ds[::-1]
ds


# ### Exploratory analysis

# #### A - Individual bond's performance through time 

# In[55]:


## Line graph
fig1 = plotly.graph_objects.Figure(
data = plotly.graph_objects.Scatter(
    x = ds['Date'],
    y = ds['1 Yr'],
    mode = 'lines',
    marker = dict(
    size = 10,
    color = ds['1 Yr'],
    showscale = True
    ),
    text = ds['1 Yr']
)
)
fig1.update_layout(title = '1 Year Treasuries Interest Rate'
                  , xaxis_title = 'Date'
                  , yaxis_title = 'Interest Rate')
fig1


# #### B - Subplots of all bonds performance

# In[21]:


fig2 = make_subplots(
    rows = 6,
    cols = 2,
    shared_xaxes = True,
    column_widths = [2, 2],
    row_heights = [2, 2, 2, 2, 2, 2]
)

fig2.add_trace(
    go.Scatter(x = ds['Date'], y = ds['1 Mo'], name = '1 Month TBills'),
    row = 1, col = 1
)
fig2.add_trace(
    go.Scatter(x = ds['Date'], y = ds['2 Mo'], name = '2 Month TBills'),
    row = 1, col = 2
)
fig2.add_trace(
    go.Scatter(x = ds['Date'], y = ds['3 Mo'], name = '3 Month TBills'),
    row = 2, col = 1
)
fig2.add_trace(
    go.Scatter(x = ds['Date'], y = ds['6 Mo'], name = '6 Month TBills'),
    row = 2, col = 2
)
fig2.add_trace(
    go.Scatter(x = ds['Date'], y = ds['1 Yr'], name = '1 Year TBills'),
    row = 3, col = 1
)
fig2.add_trace(
    go.Scatter(x = ds['Date'], y = ds['2 Yr'], name = '2 Year TBills'),
    row = 3, col = 2
)
fig2.add_trace(
    go.Scatter(x = ds['Date'], y = ds['3 Yr'], name = '3 Year TBills'),
    row = 4, col = 1
)
fig2.add_trace(
    go.Scatter(x = ds['Date'], y = ds['5 Yr'], name = '5 Year TBills'),
    row = 4, col = 2
)
fig2.add_trace(
    go.Scatter(x = ds['Date'], y = ds['7 Yr'], name = '7 Year TBills'),
    row = 5, col = 1
)
fig2.add_trace(
    go.Scatter(x = ds['Date'], y = ds['10 Yr'], name = '10 Year TBills'),
    row = 5, col = 2
)
fig2.add_trace(
    go.Scatter(x = ds['Date'], y = ds['20 Yr'], name = '20 Year TBills'),
    row = 6, col = 1
)
fig2.add_trace(
    go.Scatter(x = ds['Date'], y = ds['30 Yr'], name = '30 Year TBills'),
    row = 6, col = 2
)

fig2.update_layout(height=1000, width=1000, title_text="Subplots of all bonds performance")
fig2.show()


# #### C - Multiple bonds' performance through time in the same chart

# In[22]:


fig = px.line(ds, x='Date', y=['1 Mo','2 Mo','3 Mo', '6 Mo', '1 Yr', '2 Yr', '3 Yr', '5 Yr', '7 Yr', '10 Yr', '20 Yr', '30 Yr'], title='T-Bills Interest Rates', )
fig


# #### D - Plotting Interest Rate spread

# In[25]:


rspread = ds['3 Mo'] / ds['10 Yr']
rspread


# In[62]:


fig = px.line(ds, x='Date', y=[rspread], title='3 Mo / 10 Yr spread in %')
fig


# #### E - Bonds curve

# In[51]:


rates_curve = display(ds3.loc[0,:])


# In[ ]:




