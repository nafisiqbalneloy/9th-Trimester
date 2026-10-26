# count = 1
# while count <=5:
#     print("hello")
#     count+=1

#print 1-100
# i=1
# while i<=100:
#     print(i)
#     i+=1


#print the multiplication table of a number n
# n = int(input("enter your num: "))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

#print the elements of the following list using a loop
# nums = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1

#search for a number x in this tuple using loop
# nums = (1,4,9,16,25,36,49,64,81,100)
# x=36

# i=0
# while i<len(nums):
#     if(nums[i]==x):
#      print("found at idx",i)
#     i+=1


#loops
# tup = (1,2,3,4,2,8)

# for i in tup:
#     print(i)

# str = "apnacollege"
# for i in str:
#     print(i)

#1
# nums = [1,4,9,16,25,36,49,64,81,100]

# for el in nums:
#     print(el)

# nums = (1,4,9,16,25,36,49,64,81,100,49)
# x = 49
# idx = 0
# for el in nums:
#     if(el==x):
#         print("number found at idx",idx)
#         idx += 1
    
#range

# for i in range(10):
#     print(i)

# for i in range(2,10): #range(start,stop)
#     print(i)

# for i in range(2,10,2): #range(start,stop,step)
#     print(i)

# for i in range(1,101,2): #ODD
#     print(i)

#100-1

# for i in range(100,0,-1):
#     print(i)

# n = int(input("enter your num: "))
# for i in range(1,11):
#     print(n*i)

#WAP to find the sum of first n numbers (using while)
n = 5
sum = 0
for i in range(1,n+1):
    sum+=i
print("total sum: ",sum)

 