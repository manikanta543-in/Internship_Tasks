#Problem Name:Merge the Tools!
#Problem Link:https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub = string[i : i + k]
        print("".join(dict.fromkeys(sub)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
