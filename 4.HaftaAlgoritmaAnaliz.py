#!/usr/bin/env python
# coding: utf-8

# # MaxSubSum O(N³)

# In[110]:


def Maxsubsum(n):
    maxSum = 0 
    for i in range(len(n)):
        for j in range(len(n)):
            thisSum=0
            for k in range(i,j+1):
                thisSum+=n[k]
            if(thisSum > maxSum):
                maxSum = thisSum
    return maxSum


# In[111]:


Maxsubsum(liste)


# # MaxSubSum2 - MaxSubSum O(N²)

# In[114]:


def Maxsubsum2(n):
    maxSum=0
    for i in range(len(n)):
        thisSum=0
        for j in range (i,len(n)):
            thisSum+= n[j]
        if(thisSum > maxSum):
            maxSum = thisSum
    return maxSum


# In[115]:


Maxsubsum2(liste)


# # MaxSubSum NLogN recursive 

# In[12]:


def maxrecsum(liste):
    n=len(liste)
    if(n==1):
        return liste[0]
    left_i=0
    left_j=n//2
    right_i=n//2
    right_j=n
    left_sum= maxrecsum(liste[left_i:left_j])
    right_sum= maxrecsum(liste[right_i:right_j])
    
    temp_left_sum=0
    t=0
    for i in range(left_j-1,left_i-1,-1):
        t+=liste[i]
        if(t>temp_left_sum):
            temp_left_sum=t
    temp_right_sum=0
    t=0
    for i in range(right_i,right_j):
        t+=liste[i]
        if(t>temp_right_sum):
            temp_right_sum=t
    center_sum=temp_left_sum+temp_right_sum
    return max_3(left_sum,right_sum,center_sum)
    


# In[13]:


def max_3(a,b,c):
    return max_2(a,max_2(b,c))
def max_2(a,b):
    if(a>b):
        return a
    else:
        return b


# In[109]:


liste=[14,-3,5,-2,-1,2,6,12,15]
maxrecsum(liste)


# # MaxSubSum Big-O(N)

# In[17]:


def MaxSubSum4(liste):
    MaxSum=0
    thissum=0
    for i in range(len(liste)):
        thissum += liste[i]
        if(thissum > MaxSum):
            MaxSum = thissum
        elif (thissum < 0):
            thissum =0
    return MaxSum


# In[18]:


liste=[14,-3,5,-2,-1,2,6,12,15]
MaxSubSum4(liste)


# # Power Loop and Recursive 

# In[101]:


rec_sayac=0
loop_counter=0


# In[102]:


def power_rec(x,n):
    global rec_sayac
    rec_sayac +=1
    if(n==0):
        return 1
    if(n==1):
        return x
    if(n%2==0):
        return pow(x*x,n/2)
    else:
        return pow(x*x,n//2)*x
    
        


# In[104]:


def power_loop(x,n):
    global loop_counter
    result=1
    for i in range(n):
        result*=x
        loop_counter+=1
    return result  


# In[106]:


m=4
for i in range(2,10):
    r_1,r_2=power_loop(m,i),power_rec(m,i)
    print("power loop :",r_1,end=" ")
    print("power recursive :",r_2)


# In[105]:


power_loop(2,3)


# In[154]:


power_rec(2,3)


# In[155]:



print(loop_counter,rec_sayac)


# In[156]:


power_loop(2,10)


# In[158]:


power_rec(2,10)


# In[159]:



print(loop_counter,rec_sayac)


# In[166]:


t=time.time()
power_loop(2,1000)
t1=time.time()
t1-t


# In[167]:


t2=time.time()
power_rec(2,1000)
t3=time.time()
t3-t2


# In[168]:


print(loop_counter,rec_sayac)


# In[116]:


import time
def create_random_array(n):#n boyutlu dizi oluştur 
    import random
    arr=[]
    for i in range(n):
        arr.append(random.randint(-100,100))
        print(arr[i])
    return arr


# In[169]:


dizi1=create_random_array(10000)
dizi2=create_random_array(100000)

dizi4=create_random_array(80000)


# In[172]:


dizi3=create_random_array(1000000)


# In[143]:


t1=time.time()
print(maxrecsum(dizi1))
t2=time.time()
t2-t1


# In[144]:


t1=time.time()
print(MaxSubSum4(dizi1))
t2=time.time()
t2-t1


# In[170]:


t1=time.time()
print(MaxSubSum4(dizi2))
t2=time.time()
t2-t1


# In[171]:


t1=time.time()
print(maxrecsum(dizi2))
t2=time.time()
t2-t1


# In[173]:


t1=time.time()
print(MaxSubSum4(dizi3))
t2=time.time()
t2-t1


# In[174]:


t1=time.time()
print(maxrecsum(dizi3))
t2=time.time()
t2-t1


# In[149]:


t1=time.time()
print(MaxSubSum4(dizi4))
t2=time.time()
t2-t1


# In[150]:


t1=time.time()
print(maxrecsum(dizi4))
t2=time.time()
t2-t1

