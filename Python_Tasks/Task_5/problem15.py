#Problem Name:Lists
#Problem Link:https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    res = [] 
    for _ in range(N):
        command, *args = input().split()
        values = list(map(int, args))
        if command == 'insert':
            res.insert(values[0], values[1])
        elif command == 'print':
            print(res)
        elif command == 'remove':
            res.remove(values[0])
        elif command == 'append':
            res.append(values[0])
        elif command == 'sort':
            res.sort()
        elif command == 'pop':
            res.pop()
        elif command == 'reverse':
            res.reverse()

