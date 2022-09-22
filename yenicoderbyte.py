from math import inf
maxint=inf
def maxSubArraySum(a,size):
      
    maxfar = -maxint - 1
    maxend= 0
      
    for i in range(0, size):
        maxend = maxend + a[i]
        if (maxfar < maxend):
            maxfar = maxend
 
        if maxend < 0:
            maxend = 0  
    return maxfar
  
# Driver function to check the above function
a = input()
print (maxSubArraySum(a,len(a)))