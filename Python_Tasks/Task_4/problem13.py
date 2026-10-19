#Problem Name:Symmetric Difference
#Problem Link:https://www.hackerrank.com/challenges/symmetric-difference/problem
n=int(input())
m= set(map(int,input().split()))
o=int(input())
p=set(map(int,input().split()))
sym_set=sorted(m.symmetric_difference(p))
for i in sym_set:
    print(i)
