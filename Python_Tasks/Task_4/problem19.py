#Probelm Name:Collections.Counter()
#Problem Link:https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter
num_shoes = int(input().strip())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input().strip())
inventory = Counter(shoe_sizes)
total_earned = 0
for _ in range(num_customers):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        total_earned += price
        inventory[size] -= 1
print(total_earned)
