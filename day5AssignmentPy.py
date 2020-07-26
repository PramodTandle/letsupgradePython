day 6
Assignment 1


#!/usr/bin/env python
# coding: utf-8

# In[2]:


list5=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
list5.sort()
x=list5.count(0)
print(list5[x:] +list5[:x])


# In[42]:


=================================================================
==================================================================
Assignment 2


def fun(list1,list2):
    i=0
    j=0
    len1=len(list1)
    len2=len(list2)
    
    list0=[]
    
    while(i<len1 and j<len2):
        if(list1[i]<list2[j]):
            list0.append(list1[i])
            i=i+1
        else:
            list0.append(list2[j])
            j=j+1
    while(i<len1):
        list0.append(list1[i])
        i=i+1
    while(j<len2):
        list0.append(list2[j])
        j=j+1
    return list0


list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
list0= fun(list1,list2)
print(list0)


# In[ ]:




