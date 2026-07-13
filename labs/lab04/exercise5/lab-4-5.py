scoreA = int(input())
scoreB = int(input())
pointsA = 0
pointsB = 0
if scoreA > scoreB:
    pointsA = pointsA + 3
else:
    if scoreB > scoreA:
        pointsB = 3
    else:
        pointsA = pointsA + 1
        pointsB = pointsB + 1
if scoreB == 0:
    pointsA = pointsA + 1
else:
    if scoreA == 0:
        pointsB = pointsB + 1
print(pointsA)
print(pointsB)
