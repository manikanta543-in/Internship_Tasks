#Problem Name:Introduction to Sets
#Problem Link:https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    s=set(arr)
    lens=len(s)
    sums=sum(s)
    avg=sums/lens
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
