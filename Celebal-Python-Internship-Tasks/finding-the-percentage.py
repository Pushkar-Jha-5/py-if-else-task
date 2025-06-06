#Compute and print a student’s average marks.
n = int(input())
student_marks = {}
for _ in range(n):
    name, *scores = input().split()
    student_marks[name] = list(map(float, scores))

query_name = input()
print("{:.2f}".format(sum(student_marks[query_name]) / 3))
