#Problem Name:Set .add()
#Problem Link:https://www.hackerrank.com/challenges/py-set-add/problem
n=int(input())
se=set()
for i in range(n):
    se.add(input().strip())
print(len(se))
