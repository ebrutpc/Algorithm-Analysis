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


def Maxsubsum2(n):
    maxSum=0
    for i in range(len(n)):
        thisSum=0
        for j in range (i,len(n)):
            thisSum+= n[j]
            if(thisSum > maxSum):
                maxSum = thisSum
    return maxSum

def create_random_array(n):#n elemanlı dizi oluştur 
    import random
    arr=[]
    for i in range(n):
        arr.append(random.randint(-100,100))
        print(arr[i])
    return arr

dizi1=create_random_array(5)
dizi2=create_random_array(10)
dizi3=create_random_array(20)
dizi4=create_random_array(40)
dizi5=create_random_array(80)
dizi6=create_random_array(160)
dizi7=create_random_array(320)
dizi8=create_random_array(1000)

t1=time.time()
print(Maxsubsum(dizi8))
t2=time.time()
t2-t1


t3=time.time()
print(Maxsubsum2(dizi8))
t4=time.time()
t4-t3
