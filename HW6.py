
# coding: utf-8

# #Homework 6

# In[1]:

#1


# In[2]:

import quandl
with open('key_quandl.txt','r') as f:
    key=f.read()


# In[3]:

data=quandl.get(['WORLDBANK/ARM_TOT','WORLDBANK/LUX_TOT'], authtoken =key, trim_start='1977-1-1', collapse='annual')
data.columns=['ARM_TOT','LUX_TOT']
data.head()


# In[4]:

import matplotlib as plt
get_ipython().magic(u'matplotlib inline')
data.plot()


# In[5]:

#2


# In[6]:

def second_largest(numbers):
    count=0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None


# In[7]:

x=second_largest(data['ARM_TOT'])
print('The secong largest value for Arm TOT is '+str(x))


# In[8]:

#3


# In[12]:

exp=quandl.get('WTO/MERCH_EXP_ARM', authtoken =key, trim_start='1992-1-1')
imp=quandl.get('WTO/MERCH_IMP_ARM', authtoken =key, trim_start='1992-1-1')
netex=exp['Value']-imp['Value']
netex.head()


# In[13]:

netex.plot()


# In[14]:

#4


# In[15]:

data=quandl.get(['NYX/XBRU_WDP','NYX/XBRU_ACKB','NYX/XAMS_WHA'],  authtoken = key, trim_start='2001-01-01',column_index=4)
data.head()


# In[16]:

data.corr()


# In[17]:

import seaborn as sns
sns.heatmap(data.corr())


# In[18]:

#5


# In[19]:

import googlemaps
from datetime import datetime
now=datetime.now()
with open('key_google.txt','r') as f:
    key=f.read()


# In[20]:

gmaps=googlemaps.Client(key=key)


# In[21]:

city1=raw_input(' Type city name ')
city2=raw_input(' Type city name ')
city3=raw_input(' Type city name ')
city4=raw_input(' Type city name ')
city5=raw_input(' Type city name ')
city6=raw_input(' Type city name ')
city7=raw_input(' Type city name ')
city8=raw_input(' Type city name ')
city9=raw_input(' Type city name ')
city10=raw_input(' Type city name ')

list_cities=[city1,city2,city3,city4,city5,city6,city7,city8,city9,city10]
print list_cities


# In[22]:

new_list=[]
for city in list_cities:
    directions=gmaps.directions(city, 'New York, NY, United States', departure_time=datetime.now())
    new_list.append(directions[0]['legs'][0]['distance'])
from pprint import pprint 
pprint (new_list)


# In[23]:

import re
km=[]
for i in new_list:
    text=i['text']
    if text[-2]=='m':
        digits=re.findall("([0-9]+.*[0-9]*)\s",text)
        subs=re.sub(",","",digits[0])
        x=int(subs)*1.60934
    else:
        digits=re.findall("([0-9]+.*[0-9]*)\s",text)
        subs=re.sub(",","",digits[0])
        x=int(subs)
    km.append(x)
print (km)


# In[26]:

final_list=[]
for i in range(0,len(km)):
    dictionary={"city":list_cities[i],'distance':str(km[i])+" km from NY"}
    final_list.append(dictionary)
pprint(final_list)


# In[ ]:



