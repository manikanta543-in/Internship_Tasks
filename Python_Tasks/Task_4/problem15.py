#Problem Name:Word Order
#Problem Link:https://www.hackerrank.com/challenges/word-order/problem
n = int(input())
words = []
counts = []

for _ in range(n):
    word = input().strip()
    if word in words:
        idx = words.index(word)
        counts[idx] += 1
    else:
        words.append(word)
        counts.append(1)

print(len(words))
for c in counts:
    print(c, end=" ")
