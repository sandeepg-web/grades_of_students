#from itertools import permutations as pe
# n=list(input())
# per=list(pe(n))
# x=[int(''.join(i)) for i in per]
# print(max(x))
from itertools import *
c=int(input())
n=list(input())
p=list(input())
l=[int(''.join(i)) for i in p]
print(max(l))
print(len(l))