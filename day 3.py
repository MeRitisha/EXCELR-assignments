#!/usr/bin/env python
# coding: utf-8

# # Create a List, tuple and Dictionary with 5 elements in it and how to access few elements based on the index. Try  with different examples

# In[1]:


my_list = [10, 20, 30, 40, 50]


# In[3]:


print(my_list[1])  
print(my_list[-1])  
print(my_list[:3]) 


# # Tuple Example

# In[4]:


my_tuple = ('apple', 'banana', 'cherry', 'date', 'elderberry')


# In[5]:


print(my_tuple[2])  
print(my_tuple[-2]) 


# # Dictionary Example

# In[6]:


my_dict = {
    "name": "Ritisha",
    "age": 20,
    "city": "Hyderabad",
    "country": "India",
    "language": "English"
}


# In[8]:


print(my_dict["name"])  

my_dict = {"person": {"name": "Ritisha", "age": 20}}
print(my_dict["person"]["name"]) 


# In[ ]:





# In[ ]:




