#Problem Name:No Idea!
#Problem Link:https://www.hackerrank.com/challenges/no-idea/problem
import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    idx = 2
    arr = input_data[idx : idx + n]
    idx += n
    set_a = set(input_data[idx : idx + m])
    idx += m
    set_b = set(input_data[idx : idx + m])  
    happiness = sum((x in set_a) - (x in set_b) for x in arr)
    print(happiness)
if __name__ == "__main__":
    solve()
