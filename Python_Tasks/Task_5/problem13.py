#Problem Name:Nested Lists
#Problem Link:https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input().strip()
        score = float(input().strip())
        students.append([name, score])
    unique_scores = sorted(set(score for name, score in students))
    second_lowest_score = unique_scores[1]

    second_lowest_students = sorted(
        name for name, score in students if score == second_lowest_score
    )

    for name in second_lowest_students:
        print(name)
