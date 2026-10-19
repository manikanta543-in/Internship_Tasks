#Problem Name:Find the Runner-Up Score!
#HackerRank Link:https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n=int(input())
arr=map(int,input().split())
l=list(set(arr))
l.sort()
print(l[-2])
