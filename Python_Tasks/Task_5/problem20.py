#Problem Name:Pilling Up!
#Problem Link:https://www.hackerrank.com/challenges/piling-up/problem
import sys
from collections import deque
def can_pile():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    num_test_cases = int(input_data[0])
    idx = 1
    for _ in range(num_test_cases):
        n = int(input_data[idx])
        idx += 1
        blocks = deque(map(int, input_data[idx : idx + n]))
        idx += n
        last_picked = float("inf")
        possible = True
        while blocks:
            if blocks[0] >= blocks[-1]:
                picked = blocks.popleft()
            else:
                picked = blocks.pop()
            if picked > last_picked:
                possible = False
                break
            last_picked = picked
        print("Yes" if possible else "No")
if __name__ == "__main__":
    can_pile()
