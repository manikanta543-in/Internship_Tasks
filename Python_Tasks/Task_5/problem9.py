#Problem Name:Word Order
#Problem Link:https://www.hackerrank.com/challenges/word-order/problem
n = int(input())
counts = {}

for _ in range(n):
    word = input().strip()
    counts[word] = counts.get(word, 0) + 1

print(len(counts))
print(*counts.values())
