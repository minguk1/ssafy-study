import random

numlist = [1,2,3,4,5,6,7,8,9]

a = random.sample(numlist, 1)

numlist.remove(a)
print(numlist)
print(a)