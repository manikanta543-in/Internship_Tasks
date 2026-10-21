#Problem Name:Find the Runnerup-score
#Problem Link:https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n = int(input())
arr = sorted(set(map(int, input().split())))
print(arr[-2])
