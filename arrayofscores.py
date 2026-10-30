import sys

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
average = total / len(scores)
minimum = min(scores)
maximum = max(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)